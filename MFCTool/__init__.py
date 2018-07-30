__author__ = "KOLANICH"
__license__ = "Unlicense"
__copyright__ = """
This is free and unencumbered software released into the public domain.
Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.
In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
For more information, please refer to <https://unlicense.org/>
"""


import binascii
import os, re, sys
from codecs import decode
from collections import OrderedDict, defaultdict
from pathlib import Path

from _io import BytesIO, _IOBase

from .mifare_classic import KaitaiStream, MifareClassic

sectorRx = re.compile("\\+Sector:\\s(\\d+)")

META_SIZE = 16


class Sector:
	def __init__(self, contents, meta):
		self.contents = contents
		self.meta = meta
		self._trailer = None
		self._values = None

	def __repr__(self):
		return self.__class__.__name__ + "(" + repr(self.contents) + ", " + repr(self.meta) + ")"

	@property
	def trailer(self):
		if not self._trailer:
			self._trailer = MifareClassic.Trailer(KaitaiStream(BytesIO(decode(self.meta.replace("-", "0"), "hex"))), _root=MifareClassic)
		return self._trailer

	@property
	def values(self):
		vs = MifareClassic.Sector.Values(KaitaiStream(BytesIO(self.contents)), _root=MifareClassic)
		if not self._values:
			self._values = vs.values
		return self._values


class DumpParser:
	def __init__(self, dump):
		self.dump = dump
		self.contents = bytearray()
		self.onNewSector(None)

	def onNewSector(self, sectorNo):
		if self.contents:
			if not self.meta:
				(self.contents, self.meta) = (self.contents[:-META_SIZE], self.contents[-META_SIZE:])
			self.dump.sectors[self.sectorNo] = Sector(self.contents, self.meta)
		self.sectorNo = sectorNo
		self.contents = bytearray()
		self.meta = ""

	def processLine(self, line):
		line = line.strip()
		m = sectorRx.search(line)
		# print(line, m)
		if m:
			self.onNewSector(int(m.group(1)))
		else:
			try:
				self.contents += decode(line, "hex")
			except binascii.Error as e:
				self.meta = line

	def finish(self):
		self.onNewSector(None)

	def __enter__(self):
		pass

	def __exit__(self, *args, **kwargs):
		self.finish()


class Dump:
	def __init__(self, data):
		if isinstance(data, _IOBase):
			self.read(data)

		elif isinstance(data, str):
			try:
				data = Path(data)
			except BaseException:
				self.read(data.splitlines())
				return
			self.__class__.__init__(self, data)
		elif isinstance(data, Path):
			with data.open("rt", encoding="utf-8") as f:
				self.__class__.__init__(self, f)

	def read(self, lines):
		self.sectors = {}
		p = DumpParser(self)
		for line in lines:
			p.processLine(line)
		p.finish()
		del p
