MFCTool.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
===============
~~[wheel](https://gitlab.com/KOLANICH/MFCTool.py/-/jobs/artifacts/master/raw/wheels/MFCTool-0.CI-py3-none-any.whl?job=build)~~
[![PyPi Status](https://img.shields.io/pypi/v/MFCTool.svg)](https://pypi.python.org/pypi/MFCTool)
~~[![GitLab Build Status](https://gitlab.com/KOLANICH/MFCTool.py/badges/master/pipeline.svg)](https://gitlab.com/KOLANICH/MFCTool.py/pipelines/master/latest)~~
~~![GitLab Coverage](https://gitlab.com/KOLANICH/MFCTool.py/badges/master/coverage.svg)~~
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH/MFCTool.py.svg)](https://libraries.io/github/KOLANICH/MFCTool.py)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

**We have moved to https://codeberg.org/KFmts/MFCTool.py (the namespace has changed to `KFmts`, which groups packages related to parsing or serialization), grab new versions there.**

Under the disguise of "better security" Micro$oft-owned GitHub has [discriminated users of 1FA passwords](https://github.blog/2023-03-09-raising-the-bar-for-software-security-github-2fa-begins-march-13/) while having commercial interest in success and wide adoption of [FIDO 1FA specifications](https://fidoalliance.org/specifications/download/) and [Windows Hello implementation](https://support.microsoft.com/en-us/windows/passkeys-in-windows-301c8944-5ea2-452b-9886-97e4d2ef4422) which [it promotes as a replacement for passwords](https://github.blog/2023-07-12-introducing-passwordless-authentication-on-github-com/). It will result in dire consequencies and is competely inacceptable, [read why](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

If you don't want to participate in harming yourself, it is recommended to follow the lead and migrate somewhere away of GitHub and Micro$oft. Here is [the list of alternatives and rationales to do it](https://github.com/orgs/community/discussions/49869). If they delete the discussion, there are certain well-known places where you can get a copy of it. [Read why you should also leave GitHub](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

---

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
