# CPython vs Cython

Let us now see the differences −

- CPython: 

- [Cython](https://cython.org/): C-Extensions for Python
  - Cython is an optimising static compiler for both the Python programming language and the extended Cython programming language (based on Pyrex). It makes writing C extensions for Python as easy as Python itself.

- Jython is written in Java and ends up producing Java byte code. The Java byte code runs on Java Runtime Environment, which is an implementation of Java Virtual Machine (JVM). 
- 
- IronPython (written in C# language) compiles down your Python code to Common Language Runtime (CLR), which is a similar technology as compared to JVM, developed by Microsoft.


```
>>> def f(x, y):
...    print("Hello")
...    if x:
...       y += x
...    print(x, y)
...    return x+y
...
>>> import dis
>>> dis.dis(f)
  2           0 LOAD_GLOBAL              0 (print)
              2 LOAD_CONST               1 ('Hello')
              4 CALL_FUNCTION            1
              6 POP_TOP

  3           8 LOAD_FAST                0 (x)
             10 POP_JUMP_IF_FALSE       20

  4          12 LOAD_FAST                1 (y)
             14 LOAD_FAST                0 (x)
             16 INPLACE_ADD
             18 STORE_FAST               1 (y)

  5     >>   20 LOAD_GLOBAL              0 (print)
             22 LOAD_FAST                0 (x)
             24 LOAD_FAST                1 (y)
             26 CALL_FUNCTION            2
             28 POP_TOP

  6          30 LOAD_FAST                0 (x)
             32 LOAD_FAST                1 (y)
             34 BINARY_ADD
             36 RETURN_VALUE
```


- CPython

CPython is the implementation of the language called “Python” in C. Python is an interpreted programming language. Hence, Python programmers need interpreters to convert Python code into machine code. Whereas Cython is a compiled programming language. The Cython programs can be executed directly by the CPU of the underlying computer without using any interpreter.

- Cython

Cython is designed as a C-extension for Python. The developers can use Cython to speed up Python code execution. But they can still write and run Python programs without using Cython. But the programmers have to install both Python and C-compiler as a pre-requisite to run Cython programs.

## Libraries in CPython
- [unittest](https://github.com/python/cpython/tree/main/Lib/unittest)
  - Python unit testing framework, based on Erich Gamma's JUnit and Kent Beck's Smalltalk testing framework (used with permission).
