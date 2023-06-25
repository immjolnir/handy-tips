# Tips for C++


## [How can I declare and define multiple variables in one line using C++?](https://stackoverflow.com/questions/6838408/how-can-i-declare-and-define-multiple-variables-in-one-line-using-c)

With the following declaration, only the last variable (index) is set to 0:
```
int column, row, index = 0;
```

Instead, the following sets all variables to 0:
```
int column, row, index;
column = index = row = 0;
```

But personally, I find the following methods much more readable:
```
int column = 0, row = 0, index = 0;
int column = 0;
int row = 0;
int index = 0;
```

As of C++17, you can use [Structured Bindings](https://en.cppreference.com/w/cpp/language/structured_binding):
```
#include <iostream>
#include <tuple>

int main () 
{
    auto [hello, world] = std::make_tuple("Hello ", "world!");
    std::cout << hello << world << std::endl;
    return 0;
}
```

## Throwing Exceptions in C++
When C++ code is executed, various types of errors can occur in the program - coding errors made by programmers, errors due to incorrect input or other unforeseen errors.

When an error occurs, C++ usually stops the program execution and generates an error message. In most scenarios, the preferred way to report and handle both logic and runtime errors is to use exceptions. Exceptions provide a formal and well-defined way for detecting errors and to pass the information up the call stack.

#### Why Use Exceptions in C++?
Exceptions provide a way to react to exceptional circumstances in programs by transferring control to special functions called handlers.

Throwing exceptions are preferred in modern C++ over traditional error handling for the following reasons:

- C++ exceptions force the calling code to identify error conditions and handle them. This prevents them from stopping program execution.

- C++ destroys all objects in scope after an exception occurs, thereby reducing resource usage.

- An exception provides a clean separation between the code that identifies an error and the code that throws and handles the C++ error.

- C++ error types can be grouped together, which allows creating a hierarchy of exception objects, grouping them in namespaces or classes and categorizing them according to type.


#### C++ try catch and throw
Exception handling in C++ is done using three keywords: `try`, `catch` and `throw`.

To catch exceptions, a portion of code is placed under exception inspection. This is done by enclosing this portion of code in a try block. When an exception occurs within the try block, control is transferred to the exception handler. If no exception is thrown, the code continues normally and the handlers are ignored.

An exception in C++ is thrown by using the `throw` keyword from inside the try block. The `throw` keyword allows the programmer to define custom exceptions.

Exception handlers in C++ are declared with the catch keyword, which is placed immediately after the try block. Multiple handlers (catch expressions) can be chained - each one with a different exception type. Only the handler whose argument type matches the exception type in the throw statement is executed.

C++ does not require a `finally` block to make sure resources are released if an exception occurs.

#### Examples
- exception-throw-exception.cpp

#### Track, Analyze and Manage C++ Errors With Rollbar
Managing errors and throwing exceptions in your code is challenging. It can make deploying production code an unnerving experience. Being able to track, analyze, and manage errors in real-time can help you to proceed with more confidence. Rollbar automates error monitoring and triaging, making fixing C++ errors easier than ever.


## Tilde Expansion
- wordexp.c
- exception-throw-exception-from-ctor.cpp