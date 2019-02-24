[![codecov](https://codecov.io/gh/sagersmith8/journal/branch/master/graph/badge.svg)](https://codecov.io/gh/sagersmith8/journal)
[![Build Status](https://travis-ci.org/sagersmith8/journal.png)](https://travis-ci.com/sagersmith8/journal)

# journal
---

Engineering notebook designed for agile based software engineering

- [installation](#installation)
- [dependencies](#dependencies)
- [dev-dependencies](#dev-dependencies)
- [usage](#usage)
- [versions](#versions)
  - [0.0.1](#0.0.1)
- [license](#licence)

## installation
---

```bash
pip install journal
``` 

## dependencies
---
[python 2.7](https://www.python.org/download/releases/2.7/)
[colorama](https://pypi.org/project/colorama/)
[GitPython](https://pypi.org/project/GitPython/)


## dev-dependencies
--
[codecov](https://pypi.org/project/codecov/)
[flake8](https://pypi.org/project/flake8/)
[mock](https://pypi.org/project/mock/)
[nose](https://pypi.org/project/nose/)

## usage
---
```bash
$ journal -h
usage: journal [-h] [-t] [-d] [-n] [-c] [-s] [-j] [-b BEFORE] [-a AFTER]
               [entry]

        journal makes commits to repos in the following locations:
        	journal location: /Users/sagesmith/.journal
        	notes location: /Users/sagesmith/.journal/.notes
        	ticket location: /Users/sagesmith/.journal/.ticket
        	todo location: /Users/sagesmith/.journal/.todo

positional arguments:
  entry                 entry to enter in journal

optional arguments:
  -h, --help            show this help message and exit
  -t, --ticket          specifies ticket journal
  -d, --do              specifies todo journal
  -n, --note            specifies note journal
  -s, --standup         prints stand up
  -j, --journal         specifies entire journal
  -b BEFORE, --before BEFORE
                        specifies to grab standup logs before entered date
  -a AFTER, --after AFTER
                        specifies to grab standup logs after entered date

made by sage smith
```

## versions
---

#### 0.0.1
Initial release. Includes `journal` and `standup` commands

## license
---
[Apache Commons 2.0](https://www.apache.org/licenses/LICENSE-2.0)
