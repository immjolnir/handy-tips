# queue.py

from collections import deque

class Queue:
    def __init__(self):
        self._elements = deque()

    def enqueue(self, element):
        """Add items to the right end of the queue.
        >>> numbers = Queue()
        >>> numbers
        Queue([])
        >>> for number in range(1, 4):
        ...     numbers.enqueue(number)
        >>> numbers
        Queue([1, 2, 3])
        """
        self._elements.append(element)

    def dequeue(self):
        """Remove and return an item from the left end of the queue.
        >>> numbers = Queue()
        >>> for number in range(1, 4):
        ...     numbers.enqueue(number)
        >>> numbers
        Queue([1, 2, 3])
        >>> numbers.dequeue()
        1
        >>> numbers.dequeue()
        2
        >>> numbers.dequeue()
        3
        >>> numbers
        Queue([])
        """
        return self._elements.popleft()

    # Queue also implements a .__repr__() method that provides the class’s string representation. This method will play an important role in writing and running your doctest tests, as you’ll explore in a moment.
    def __repr__(self):
        return f"{type(self).__name__}({list(self._elements)})"

# An important point to highlight in the above example is that doctest runs individual docstrings in a dedicated context or scope. Therefore, names declared in one docstring can’t be used in another docstring. So, the numbers object defined in .enqueue() isn’t accessible in .dequeue(). You need to create a new Queue instance in .dequeue() before you can test this latter method.
# You’ll dive deeper into how doctest manages the execution scope of your test cases in the Understanding the doctest Scoping Mechanism section.

