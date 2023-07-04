# [unittest](https://docs.python.org/3/library/unittest.html)

The unittest unit testing framework was originally inspired by JUnit and has a similar flavor as major unit testing
frameworks in other languages. It supports test automation, sharing of setup and shutdown code for tests, aggregation of
tests into collections, and independence of the tests from the reporting framework.

The source code is put aside: `/usr/lib/python3.10/unittest`.

To achieve this, unittest supports some important concepts in an object-oriented way:

- test fixture

  A test fixture represents the preparation needed to perform one or more tests, and any associated cleanup actions.
  This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.

- test case

  A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs.
  unittest provides a base class, TestCase, which may be used to create new test cases.

- test suite

  A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be
  executed together.

- test runner

  A test runner is a component which orchestrates the execution of tests and provides the outcome to the user. The
  runner may use a graphical interface, a textual interface, or return a special value to indicate the results of
  executing the tests.

# 1. test case

Organizing test code

The basic building blocks of unit testing are test cases — single scenarios that must be set up and checked for
correctness. In unittest, test cases are represented by `unittest.TestCase` instances. To make your own test cases you
must write subclasses of `TestCase` or use `FunctionTestCase`.

A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. unittest
provides a base class, TestCase, which may be used to create new test cases.

- test_basic_example.py
    - A testcase is created by subclassing `unittest.TestCase`. The three individual tests are defined with methods
      whose names start with the letters `test`. This naming convention informs the test runner about which methods
      represent tests.
    - `$ python3 test_basic_example.py`
    - `unittest.main()` provides a command-line interface to the test script.
  ```
  # Passing the -v option to your test script will instruct unittest.main() to enable a higher level of verbosity, and produce the following output:
  $ python3 test_basic_example.py -v
  test_isupper (test_basic_example.TestStringMethods) ... ok
  test_split (test_basic_example.TestStringMethods) ... ok
  test_upper (test_basic_example.TestStringMethods) ... ok
  
  ----------------------------------------------------------------------
  Ran 3 tests in 0.000s
  
  OK
  ```
    - `$ python3 -m unittest -v  test_basic_example.py`

## [How To Use unittest to Write a Test Case for a Function in Python](https://www.digitalocean.com/community/tutorials/how-to-use-unittest-to-write-a-test-case-for-a-function-in-python)

The Python standard library includes the unittest module to help you write and run tests for your Python code.

Tests written using the unittest module can help you find bugs in your programs, and prevent regressions from occurring
as you change your code over time. Teams adhering to test-driven development may find unittest useful to ensure all
authored code has a corresponding set of tests.

In this tutorial, you will use Python’s unittest module to write a test for a function.

unittest.TestCase exposes a number of other methods beyond assertEqual and assertRaises that you can use.

| Method	               | Assertion        |
|-----------------------|------------------|
| assertEqual(a, b)     | 	a == b          |
| assertNotEqual(a, b)	 | a != b           |
| assertTrue(a)	        | bool(a) is True  |
| assertFalse(a)        | bool(a) is False |
| assertIsNone(a)       | 	a is None       |
| assertIsNotNone(a)	   | a is not None    |
| assertIn(a, b)	       | a in b           |
| assertNotIn(a, b)	    | a not in b       |

- test_add_fish_to_aquarium.py

- test_add_fish_to_aquarium_exception.py

- test_fish_tank.py
    - TestCase also supports a setUp method to help you create resources on a per-test basis. setUp methods can be
      helpful when you have a common set of preparation code that you want to run before each and every one of your
      tests. setUp lets you put all this preparation code in a single place, instead of repeating it over and over for
      each individual test.


- test_advanced_fish_tank.py
    - TestCase supports a counterpart to the setUp method named tearDown. tearDown is useful if, for example, we need to
      clean up connections to a database, or modifications made to a filesystem after each test completes. We’ll review
      an example that uses tearDown with filesystems:

In this tutorial, you have written TestCase classes with different assertions, used the setUp and tearDown methods, and
run your tests from the command line.

# 2. test fixture

- test_test-fixture.py

> Note The order in which the various tests will be run is determined by sorting the test method names with respect to
> the built-in ordering for strings.

If the setUp() method raises an exception while the test is running, the framework will consider the test to have
suffered an error, and the test method will not be executed.

Similarly, we can provide a tearDown() method that tidies up after the test method has been run.

If setUp() succeeded, tearDown() will be run whether the test method succeeded or not.

Such a working environment for the testing code is called a test fixture. A new TestCase instance is created as a unique
test fixture used to execute each individual test method. Thus setUp(), tearDown(), and __init__() will be called once
per test.

# 3. test suite

It is recommended that you use TestCase implementations to group tests together according to the features they test.
unittest provides a mechanism for this: the test suite, represented by unittest’s TestSuite class. In most cases,
calling unittest.main() will do the right thing and collect all the module’s test cases for you and execute them.

- test_test-suite.py

You can place the definitions of test cases and test suites in the same modules as the code they are to test (such as
widget.py), but there are several advantages to placing the test code in a separate module, such as test_widget.py:

* The test module can be run standalone from the command line.

* The test code can more easily be separated from shipped code.

* There is less temptation to change test code to fit the code it tests without a good reason.

* Test code should be modified much less frequently than the code it tests.

* Tested code can be refactored more easily.

* Tests for modules written in C must be in separate modules anyway, so why not be consistent?

* If the testing strategy changes, there is no need to change the source code.

# 4. test runner

# Skipping tests and expected failures

Unittest supports skipping individual test methods and even whole classes of tests. In addition, it supports marking a
test as an “expected failure,” a test that is broken and will fail, but shouldn’t be counted as a failure on a
TestResult.

- test_skipping-tests-and-expected-failures.py

```
$ python3 test_skipping-tests-and-expected-failures.py  -v
test_format (__main__.MyTestCase) ... skipped 'not supported in this library version'
test_maybe_skipped (__main__.MyTestCase) ... ok
test_nothing (__main__.MyTestCase) ... skipped 'demonstrating skipping'
test_windows_support (__main__.MyTestCase) ... skipped 'requires Windows'

----------------------------------------------------------------------
Ran 4 tests in 0.000s
```

The following decorators and exception implement test skipping and expected failures:

@unittest.skip(reason)
Unconditionally skip the decorated test. reason should describe why the test is being skipped.

@unittest.skipIf(condition, reason)
Skip the decorated test if condition is true.

@unittest.skipUnless(condition, reason)
Skip the decorated test unless condition is true.

@unittest.expectedFailure
Mark the test as an expected failure or error. If the test fails or errors in the test function itself (rather than in
one of the test fixture methods) then it will be considered a success. If the test passes, it will be considered a
failure.

exception unittest.SkipTest(reason)
This exception is raised to skip a test.

Usually you can use TestCase.skipTest() or one of the skipping decorators instead of raising this directly.

Skipped tests will not have setUp() or tearDown() run around them. Skipped classes will not have setUpClass() or
tearDownClass() run. Skipped modules will not have setUpModule() or tearDownModule() run.

# Distinguishing test iterations using subtests

- test_distinguishing-test-iterations-using-subtests.py

--------------------------------
# [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)

unittest.mock is a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.

unittest.mock provides a core Mock class removing the need to create a host of stubs throughout your test suite. After performing an action, you can make assertions about which methods / attributes were used and arguments they were called with. You can also specify return values and set needed attributes in the normal way.

Mock is designed for use with unittest and is based on the ‘action -> assertion’ pattern instead of ‘record -> replay’ used by many mocking frameworks.

> The standard library includes unittest.mock in Python 3.3 and later. If you’re using an older version of Python, you’ll need to install the official backport of the library. To do so, install mock from PyPI:
```
$ pip install mock
```

- test_mock-quick-guide.py

## [Getting Started with Mocking in Python](https://semaphoreci.com/community/tutorials/getting-started-with-mocking-in-python)
- test_mock-calculator.py

- test_mock-blog.py

## [Understanding the Python Mock Object Library](https://realpython.com/python-mock-library/)
When you’re writing robust code, tests are essential for verifying that your application logic is correct, reliable, and efficient. However, the value of your tests depends on how well they demonstrate these criteria. Obstacles such as complex logic and unpredictable dependencies make writing valuable tests difficult. The Python mock object library, unittest.mock, can help you overcome these obstacles.

By the end of this article, you’ll be able to:

- Create Python mock objects using Mock

- Assert you’re using objects as you intended

- Inspect usage data stored on your Python mocks

- Configure certain aspects of your Python mock objects

- Substitute your mocks for real objects using patch()

- Avoid common problems inherent in Python mocking


unittest.mock provides a class called Mock which you will use to imitate real objects in your codebase. Mock offers incredible flexibility and insightful data. This, along with its subclasses, will meet most Python mocking needs that you will face in your tests.

The library also provides a function, called patch(), which replaces the real objects in your code with Mock instances. You can use patch() as either a decorator or a context manager, giving you control over the scope in which the object will be mocked. Once the designated scope exits, patch() will clean up your code by replacing the mocked objects with their original counterparts.

Finally, unittest.mock provides solutions for some of the issues inherent in mocking objects.

Now, you have a better understanding of what mocking is and the library you’ll be using to do it. Let’s dive in and explore what features and functionalities unittest.mock offers.


## [An introduction to mocking in python](https://www.toptal.com/python/an-introduction-to-mocking-in-python)
System Calls vs. Python Mocking

To give you another example, and one that we’ll run with for the rest of the article, consider system calls. It’s not difficult to see that these are prime candidates for mocking: whether you’re writing a script to eject a CD drive, a web server which removes antiquated cache files from /tmp, or a socket server which binds to a TCP port, these calls all feature undesired side-effects in the context of your unit-tests.

The mantra to keep repeating is this:

> Mock an item where it is used, not where it came from.


- test_mock-fileystem.py

File-Removal as a Service with Python’s Mock Patch

### MOCK PATCH PITFALL: DECORATOR ORDER
When using multiple decorators on your test methods, order is important, and it’s kind of confusing. Basically, when mapping decorators to method parameters, work backwards. Consider this example:
```
    @mock.patch('mymodule.sys')
    @mock.patch('mymodule.os')
    @mock.patch('mymodule.os.path')
    def test_something(self, mock_os_path, mock_os, mock_sys):
        pass
```
Notice how our parameters are matched to the reverse order of the decorators? That’s partly because of the way that Python works. With multiple method decorators, here’s the order of execution in pseudocode:
```
patch_sys(patch_os(patch_os_path(test_something)))
```
Since the Python patch to sys is the outermost patch, it will be executed last, making it the last parameter in the actual test method arguments. Take note of this well and use a debugger when running your tests to make sure that the right parameters are being injected in the right order.

### PITFALL: THE MOCK.MOCK AND MOCK.MAGICMOCK CLASSES
The mock library also includes two important classes upon which most of the internal functionality is built upon: the Python Mock class and the Python MagicMock class. When given a choice to use a mock.Mock instance, a mock.MagicMock instance, or an auto-spec, always favor using an auto-spec, as it helps keep your tests sane for future changes. This is because mock.Mock and mock.MagicMock accept all method calls and property assignments regardless of the underlying API. Consider the following use case:

- test_mock-pitfall.py 

Re-run your test, and you’ll find that it still passes. That’s because it isn’t built against your actual API. This is why you should always use the create_autospec method and the autospec parameter with the @patch and @patch.object decorators.

### Conclusion
Python’s mock library, if a little confusing to work with, is a game-changer for unit-testing. We’ve demonstrated common use-cases for getting started using mock in unit-testing, and hopefully this article will help Python developers overcome the initial hurdles and write excellent, tested code.


- mock: Used to replace something that is used in the current scope	
- patch: Used to replace something that is imported and/or created in another scop

