Built-in Data Types
-------------------
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


