# greet.py

def greet(name="World"):
    """Print a greeting.

    Usage examples:
    >>> greet("Pythonista")
    Hello, Pythonista!
    <BLANKLINE>
    How have you been?
    """
    print(f"Hello, {name}!")
    print()
    print("How have you been?")

# In this example, you use a raw string to write the docstring of this new version of greet(). Note the leading r in the docstring. Note that in the actual code, you double the backslash (\\) to escape it, but in the docstring you don’t need to double it.
def greet2(name="World"):
    r"""Print a greeting.

    Usage examples:
    >>> greet("Pythonista")
    /== Hello, Pythonista! ==\
    \== How have you been? ==/
    """
    print(f"/== Hello, {name}! ==\\")
    print("\\== How have you been? ==/")


# If you don’t want to use a raw string as a way to escape backslashes, then you can use regular strings that escape the backslash by doubling it.
def greet3(name="World"):
    """Print a greeting.

    Usage examples:
    >>> greet("Pythonista")
    /== Hello, Pythonista! ==\\
    \\== How have you been? ==/
    """
    print(f"/== Hello, {name}! ==\\")
    print("\\== How have you been? ==/")

