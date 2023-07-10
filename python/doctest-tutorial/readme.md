
# [doctest](https://docs.python.org/3/library/doctest.html)

```
$ python example.py  -v

- or
```
$ python -m doctest -v example.py
```
This will import example.py as a standalone module and run `testmod()` on it. 
> Note that this may not work correctly if the file is part of a package and imports other submodules from that package.

# [Python's doctest: Document and Test Your Code at Once](https://realpython.com/python-doctest/)

Are you interested in writing usage examples for your code that work as documentation and test cases simultaneously? If your answer is yes, then Python’s doctest module is for you. This module provides a testing framework that doesn’t have too steep a learning curve. It’ll allow you to use code examples for two purposes: documenting and testing your code.

Apart from allowing you to use your code’s documentation for testing the code itself, doctest will help you keep your code and its documentation in perfect sync at any moment.

In this tutorial, you’ll:

- Write doctest tests in your code’s documentation and docstrings
- Understand how doctest works internally
- Explore the limitations and security implications of doctest
- Use doctest for test-driven development
- Run your doctest tests using different strategies and tools


Almost all experienced programmers will tell you that documenting your code is a best practice. Some will say that code and its documentation are equally important and necessary. Others will tell you that documentation is even more important than the code itself.

In Python, you’ll find many ways to document a project, app, or even modules and scripts. Larger projects generally require dedicated external documentation. But in small projects, using explicit `names`, `comments`, and `docstrings` might be sufficient:

Comments have a couple of drawbacks:

    They’re ignored by the interpreter or compiler, which makes them unreachable at runtime.
    They often get outdated when the code evolves and the comments remain untouched.

Documentation strings, or simply docstrings, are a neat Python feature that can help you document your code as you go. The advantage of docstrings compared to comments is that the interpreter doesn’t ignore them. They’re a living part of your code.

Because docstrings are active parts of your code, you can access them at runtime. To do this, you can use the .__doc__ special attributes on your packages, modules, classes, methods, and functions.

Tools like MkDocs and Sphinx can take advantage of docstrings for generating project documentation automatically.

Embedding REPL-like code examples in your code helps you:

    Keep the documentation in sync with the current state of your code
    Express your code’s intended usage
    Test your code as you write it

Those benefits sound neat! Now, how can you run the code examples that you’ve embedded in your documentation and docstrings? You can use Python’s doctest module from the standard library.


## What doctest Is and How It Works

The doctest module is a lightweight testing framework that provides quick and straightforward test automation. It can read the test cases from your project’s documentation and your code’s docstrings. This framework is shipped with the Python interpreter and adheres to the batteries-included philosophy.

You can use doctest from either your code or your command line. To find and run your test cases, doctest follows a few steps:

    Searches for text that looks like Python interactive sessions in your documentation and docstrings
    Parses those pieces of text to distinguish between executable code and expected results
    Runs the executable code like regular Python code
    Compares the execution result with the expected result

The doctest framework searches for test cases in your documentation and the docstrings of packages, modules, functions, classes, and methods. It doesn’t search for test cases in any objects that you import.

In general, doctest interprets as executable Python code all those lines of text that start with the primary (>>>) or secondary (...) REPL prompts. The lines immediately after either prompt are understood as the code’s expected output or result.


- calculations.py

- printed_output.py 


Testing what a function prints on the screen is pretty straightforward using doctest. With other testing frameworks, doing this kind of test may be a bit more complicated. You would need to deal with the standard output stream, which may require advanced Python knowledge.

## Writing doctest Tests for Catching Exceptions

Besides testing for successful return values, you’ll often need to test code that’s expected to raise exceptions in response to errors or other issues.

The doctest module follows mostly the same rules when catching return values and exceptions. It searches for text that looks like a Python exception report or traceback and checks it against any exception that your code raises.

For example, say that you’ve added the following divide() function to your calculations.py file:

- calculations.py: divide

The first highlighted line holds a header that’s common to all exception tracebacks. The second highlighted line contains the actual exception and its specific message. These two lines are the only requirement for doctest to successfully check for expected exceptions.

When dealing with exception tracebacks, doctest completely ignores the traceback body because it can change unexpectedly. In practice, doctest is only concerned about the first line, which reads Traceback (most recent call last):, and the last line. As you already know, the first line is common to all exception tracebacks, while the last line shows information about the raised exception.

Because doctest completely ignores the traceback body, you can do whatever you want with it in your docstrings. Typically, you’ll only include the traceback body if it adds significant value to your documentation. In terms of your options, you can:

    Completely remove the traceback body
    Replace parts of the traceback body with an ellipsis (...)
    Completely replace the traceback body with an ellipsis
    Replace the traceback body with any custom text or explanation
    Include the complete traceback body

In any case, the traceback body only has meaning for humans reading your documentation. The second, fourth, and last options in this list will be useful only if the traceback adds value to your code’s documentation.


## Building More Elaborate doctest Tests

Often, you need to test functionality that depends on other objects in your code. For example, you may need to test the methods of a given class. To do this, you’ll need to instantiate the class first.

- queue.py

## Dealing With Whitespaces and Other Characters

Regarding characters such as whitespaces and backslashes, the rules are a bit complex. Expected outputs can’t consist of blank lines or lines containing only whitespace characters. Such lines are interpreted as the end of the expected output.

If your expected output includes blank lines, then you must use the <BLANKLINE> placeholder tag to replace them:

- greet.py

## Summarizing the doctest Test Syntax

As you already know, doctest recognizes tests by looking for pieces of text that mimic Python interactive sessions. According to this rule, lines starting with the >>> prompt are interpreted as simple statements, compound statement headers, or expressions. Similarly, lines beginning with the ... prompt are interpreted as continuation lines in compound statements.

Any lines that don’t start with >>> or ..., up to the next >>> prompt or blank line, represent the output that you expect from the code. The output must appear as it would in a Python interactive session, including both return values and printed outputs. Blank lines and the >>> prompt work as test separators or terminators.

If you don’t have any output lines between lines that start with >>> or ..., then doctest assumes that the statement is expected to have no output, which is the case when you call functions that return None or when you have assignment statements.

The doctest module ignores anything that doesn’t follow the doctest test syntax. This behavior allows you to include explanatory text, diagrams, or whatever you need in between your tests. 

```
import doctest

doctest.testfile("test_calculations.txt", verbose=True)
or 
doctest.testmod(verbose=True)
```

## Running doctest Tests With unittest and pytest

The doctest module provides an incredibly convenient way to add test cases to a project’s documentation. However, doctest isn’t a substitute for a full-fledged testing framework, like the standard-library unittest or the third-party pytest. This is especially true in large projects with an extensive and complex codebase. For this kind of project, doctest may not be sufficient.


Using unittest to Run doctest Tests

If you ever want to run doctest tests with unittest, then you can use the doctest API. The API allows you to convert doctest tests into unittest test suites. To do this, you’ll have two main functions:
Function 	Description
DocFileSuite() 	Converts doctest tests from one or more text files into a unittest test suite
DocTestSuite() 	Converts doctest tests from a module into a unittest test suite

To integrate your doctest tests with the unittest discovery mechanism, you must add a load_tests() function to your unittest boilerplate code. As an example, get back to your test_calculations.txt file:

## Using pytest to Run doctest Tests

If you decide to use the pytest third-party library to automate your project’s tests, then you can also integrate your doctest tests. In this case, you can use pytest’s --doctest-glob command-line option like in the example below:

$ pytest --doctest-glob="test_calculations.txt"

When you run this command, you get output like the following:

===================== test session starts =====================
platform darwin -- Python 3.10.3, pytest-7.1.1, pluggy-1.0.0
rootdir: .../python-doctest/examples
collected 1 item

test_calculations.txt .                                  [100%]

===================== 1 passed in 0.02s =======================

Just like unittest, pytest interprets your dedicated test file as a single test. The --doctest-glob option accepts and matches patterns that’ll allow you to run multiple files. A helpful pattern could be "test*.txt".

You can also execute doctest tests directly from your code’s docstrings. To do this, you can use the --doctest-modules command-line option. This command-line option will scan all the modules under your working directory, loading and running any doctest tests it finds.

If you want to make this integration permanent, then you can add the following parameter to pytest’s configuration file in your project’s root directory:

; pytest.ini

[pytest]
addopts = --doctest-modules

From now on, whenever you run pytest on your project’s directory, all the doctest tests will be found and executed.


# TODO: integrate the doctest with sphix or mkdoc
