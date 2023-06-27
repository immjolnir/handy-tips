=======
handypy
=======


    Handy Tips for Python


A longer description of your project goes here...

Setup
====
.. code-block::

    $ sudo apt install tox

Build
=====

- Getting started to `tox`
.. code-block::

   $ tox -- tests/test_skeleton.py::test_fib
   $ tox list
   default environments:
   default   -> Invoke pytest to run automated tests
   
   additional environments:
   build     -> Build the package in isolation according to PEP517, see https://github.com/pypa/build
   clean     -> Remove old distribution files and temporary build artifacts (./build and ./dist)
   docs      -> Invoke sphinx-build to build the docs
   doctests  -> Invoke sphinx-build to run doctests
   linkcheck -> Check for broken links in the documentation
   publish   -> Publish the package you have been developing to a package index server. By default, it uses testpypi. If you really want to publish your package to be publicly accessible in PyPI, use the `-- --repository pypi` option.
   
   $ tox # apply the derfault, run tests
   $ tox -e build
   $ tox -e clean

- Commands
.. code-block::

    # Run all cases
    tox -e testing
    # Run a unit test file
    $ tox -- tests/test_division.py
    # Run a single case
    tox -- tests/test_unittest_lib.py::MyTestCase::test_something

