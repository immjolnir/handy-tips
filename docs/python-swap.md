# [Python Swap - How to Swap Two Variables the Python Way](https://blogboard.io/blog/knowledge/python-swap/)

It's simple. For any two variables `(a, b)` we can swap their values in a single assignment statement


It's simple. For any two variables a, b, we can swap their values in a single assignment statement
```
a, b = b, a
```
In fact, it works for exchanging values of multiple variables as well
```
a, b, c = c, a, b
```

### Why does this work?
This might look like a syntactic sugar for swapping variables, but in fact it's a neat application of iterable unpacking.

Simply put: iterable unpacking happens when we assign an iterable to a list or a tuple of variables in a single assignment statement. This might sound more complicated than it actually is, so here's an example.

Let's say we have an array
```
A = [1, 2, 3]
```

When we do the following assignment
```
a, b, c = A
```

what we're actually doing is equivalent to this:
```
a = A[0]
b = A[1]
c = A[2]
```
> Assigning values to multiple variables this way in Python is called `iterable unpacking`.

### So how is this related to swapping variables?

When we write `a, b = b, a` two things happen:

- Right-hand side is evaluated first, yielding a tuple with values (<value of b>, <value of a>)

- This new tuple is then assigned to the left-hand side tuple `a, b`  using `iterable unpacking` (note that a tuple is an iterable)

So in effect, we're doing the following three statements, all in a single line of code:
```
tmp = (b, a)
a = tmp[0]
b = tmp[1]
```

### Is this a standardized way to swap two variables in Python?

This is actually a perfectly fine, Pythonic way, to perform variable swap. As we explained, it's not a dirty hack, but rather a special case of using iterable unpacking syntax of Python.

### Is there a swap function in Python?
No, there's no built-in function in Python that could be used to swap values of variables. But if for any reason you need one, you can simply build it using the swap syntax - `a, b = b, a` .

- test_swap.py
