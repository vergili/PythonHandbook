Decorators
----------

Basically decorator is a function which takes another function and modify behaviour of the function.
Decorators are very helpfull to reduce size of code and make it easy and understandable.

For instance as most of python developers know  @staticmethod and @property are very useful and famous decorators
to make our methods static or a property.

Before a decorator example we need to understand functions as an argument, returning function and nested functions.

Functions can be Argument
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    def func()
        return 'Hello World'


    def anyfunction(arg_func):
        print('This function argument is a function')
        print(arg_func())

    anyfunction(func)
    >>> This function argument is a function
    >>> Hello world


Functions can return Function & Nested Function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Functions can be defined under another function and they can be returned.

.. code:: python

    def main_func():

        def sub_func():
            return 'this is sub function'

        return sub_func

    a = sub_func()
    print a
    >>> this is sub function


A Decorator Example
^^^^^^^^^^^^^^^^^^^

.. code:: python

    def spamrun(fn):

        def sayspam(*args):
            print "spam, spam, spam"

        return sayspam

    @spamrun
    def useful(a, b):
        print a**2 + b**2

    useful(3,4)
    spam, spam, spam





**References**

https://docs.python.org/3/library/functions.html

https://docs.python.org/3/library/functools.html

https://github.com/lord63/awesome-python-decorator
