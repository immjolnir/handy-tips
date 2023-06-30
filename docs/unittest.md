

# Simple Smalltalk Testing: With Patterns

YOU CAN'T ARGUE with inspiration (or deadlines). I started to write the final column in the sequence about using patterns for design, but what came out was this. It describes some work I have been doing with a framework that takes the tedium out of writing tests. I'll get back to the pattern stuff in the next issue.

Smalltalk has suffered because it lacks a testing culture. This column describes a simple testing strategy and a framework to support it. The testing strategy and framework are not intended to be complete solutions, but, rather, are intended to be starting points from which industrial strength tools and procedures can be constructed.

The article is divided into four sections:

- Philosophy. Describes the philosophy of writing and running tests embodied by the framework. Read this section for general background.

- Framework. A literate program version of the testing framework. Read this for in-depth knowledge of how the framework operates.

- Example. An example of using the testing framework to test part of the methods in Set.

- Cookbook. A simple cookbook for writing your own tests.

# JUnit: unit testing and coiling in tandem

## Implementations

* [unittest](https://docs.python.org/3/library/unittest.html): The unittest unit testing framework was originally inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.
