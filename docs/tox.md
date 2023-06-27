# [tox](https://github.com/tox-dev/tox): Command line driven CI frontend and development task automation tool.

tox aims to automate and standardize testing in Python. It is part of a larger vision of easing the packaging, testing and release process of Python software (alongside pytest and devpi).


tox is a generic virtualenv management and test command line tool.

It is very similiar to Makefile but more powerful.

- No need to create virtual environment at the beginning.
  - virtualenv-based automation of test activities


## [Guidance to tox](https://tox.wiki/en/latest/user_guide.html#user-guide)
* test runners(such as pytest)
* linters(e.g. flake8)
* formatters(for example black or isort)
* documentation generators(e.g., Sphinx)
* build and publishing tools(build with twine)
* ...

## [General tips and tricks](https://tox.wiki/en/3.1.1/example/general.html)
- Interactively passing positional arguments: `tox -- -x tests/test_something.py:cls::case`

- Selecting one or more environments to run tests against: `tox -e docs`

## [Why You Should Use tox](https://christophergs.com/python/2020/04/12/python-tox-why-use-it-and-tutorial/)


