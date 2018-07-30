MFCTool.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
===============
~~[wheel](https://gitlab.com/KOLANICH/MFCTool.py/-/jobs/artifacts/master/raw/wheels/MFCTool-0.CI-py3-none-any.whl?job=build)~~
[![PyPi Status](https://img.shields.io/pypi/v/MFCTool.svg)](https://pypi.python.org/pypi/MFCTool)
~~[![GitLab Build Status](https://gitlab.com/KOLANICH/MFCTool.py/badges/master/pipeline.svg)](https://gitlab.com/KOLANICH/MFCTool.py/pipelines/master/latest)~~
~~![GitLab Coverage](https://gitlab.com/KOLANICH/MFCTool.py/badges/master/coverage.svg)~~
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH/MFCTool.py.svg)](https://libraries.io/github/KOLANICH/MFCTool.py)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

The companion library for Android app [MifareClassicTool](https://github.com/ikarus23/MifareClassicTool)![License](https://img.shields.io/github/license/ikarus23/MifareClassicTool.svg). The app creates hex-dumps of Mifare Classic tags. This lib gives object-oriented interface to these dumps.

Features
--------
* `.contents` contains bytes of a sector.
* `.meta` contains keys and other info as they are in the dump.
* `.trailer` contains a parsed trailer, including
  * keys
  * decoded access conditions
* `.values` contains parsed and validated (`.valid`) value blocks

Usage
-----

```python
from MFCTool import *
from pathlib import Path
d = Dump()
print(d.sectors[0].contents)
print(d.sectors[0].meta)
print(d.sectors[0].trailer)
print(d.sectors[0].values)
```

Requirements
------------
* [`kaitaistruct`](https://github.com/kaitai-io/kaitai_struct_python_runtime)
  [![PyPi Status](https://img.shields.io/pypi/v/kaitaistruct.svg)](https://pypi.python.org/pypi/kaitaistruct)
  ![License](https://img.shields.io/github/license/kaitai-io/kaitai_struct_python_runtime.svg) as a runtime for Kaitai Struct-generated code. Used for decoding of values and access conditions.
