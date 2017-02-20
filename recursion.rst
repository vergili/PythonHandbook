Recursion
---------

Recursion is a way of programming or coding a problem, in which a function calls itself one or more times in its body.

Recursion functions are very helpfull if we want to solve a series problem


.. code:: python

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)


    print  factorial(5)
    >>> 120


.. code:: python

    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)


Recursion vs Iteration
----------------------

.. code:: python

- Recursion quite simple logic call methods
- Depend on how deeply you go in recursion you will have memory problems
- They are made for use best on tree functions or methods
- Slower than iteration

- Iteration clean logic but not simple as recursive calls sometimes
- You have better control on memory use instead of recursive methods or functions
- They are made for use on iteration on list items.

