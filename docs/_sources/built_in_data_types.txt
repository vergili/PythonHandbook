Built-in Types
--------------
Python is dynamically typed, this means that you don't need to state the types of
variables when you declare them or anything like that. You can do things like x=111
and then x="I'm a string" without error.

In python values have type there is no type for variables like other dynamically typed languages.


Numeric Types
^^^^^^^^^^^^^

- int: Integers; equivalent to C longs in Python 2.x, non-limited length in Python 3.x
- long: Long integers of non-limited length; exists only in Python 2.x
- float: Floating-Point numbers, equivalent to C doubles
- complex: Complex Numbers


Iterator Types
^^^^^^^^^^^^^^

Python supports a concept of iteration over containers. This is implemented using two distinct methods;
these are used to allow user-defined classes to support iteration. Sequences, described below in more detail,
always support the iteration methods.

One method needs to be defined for container objects to provide iteration support:

container.__iter__()

Return an iterator object. The object is required to support the iterator protocol described below.
If a container supports different types of iteration, additional methods can be provided to specifically
request iterators for those iteration types. (An example of an object supporting multiple forms of iteration
would be a tree structure which supports both breadth-first and depth-first traversal.) This method corresponds
to the tp_iter slot of the type structure for Python objects in the Python/C API.

The iterator objects themselves are required to support the following two methods, which together form the iterator protocol:

iterator.__iter__()

Return the iterator object itself. This is required to allow both containers and iterators to be used with
the for and in statements. This method corresponds to the tp_iter slot of the type structure for Python objects in the Python/C API.

iterator.__next__()

Return the next item from the container. If there are no further items, raise the StopIteration exception.
This method corresponds to the tp_iternext slot of the type structure for Python objects in the Python/C API.

Python defines several iterator objects to support iteration over general and specific sequence types, dictionaries, a
nd other more specialized forms. The specific types are not important beyond their implementation of the iterator protocol.

Once an iterator’s __next__() method raises StopIteration, it must continue to do so on subsequent calls.
Implementations that do not obey this property are deemed broken.

.. code:: python

    my_list = [4, 7, 0, 3, 6, 7, 8, 4]

    my_iter = iter(my_list)

    print(next(my_iter))
    print(next(my_iter))

    print(my_iter.next())
    print(my_iter.next())

    next(my_iter)


Sequences
^^^^^^^^^

- str: String; represented as a sequence of 8-bit characters in Python 2.x, but as a sequence of Unicode characters (in the range of U+0000 - U+10FFFF) in Python 3.x
- bytes: a sequence of integers in the range of 0-255; only available in Python 3.x
- byte array: like bytes, but mutable (see below); only available in Python 3.x
- list
- tuple


Debugging is also something which once mastered can greatly enhance your
bug hunting skills. Most of the newcomers neglect the importance of the
Python debugger (``pdb``). In this section I am going to tell you only a
few important commands. You can learn more about it from the official
documentation.

**Running from commandline**

You can run a script from the commandline using the Python debugger.
Here is an example:

.. code:: python

    $ python -m pdb my_script.py

It would cause the debugger to stop the execution on the first statement
it finds. This is helpful if your script is short. You can then inspect
the variables and continue execution line-by-line.

**Running from inside a script**

You can set break points in the script itself so that you can inspect
the variables and stuff at particular points. This is possible using the
``pdb.set_trace()`` method. Here is an example:

.. code:: python

    import pdb

    def make_bread():
        pdb.set_trace()
        return "I don't have time"

    print(make_bread())

Try running the above script after saving it. You would enter the
debugger as soon as you run it. Now it's time to learn some of the
commands of the debugger.

**Commands:**


