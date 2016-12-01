Access Modifiers in Python (Public, Protected, Private)
-------------------------------------------------------
Languages like c++ or java have access modifiers to restrict connection from outside of class etc.
but in python there is no a restriction to access any function or variable. In python all function and variables have
access inside or outside of a class. The only way is just inform user about access with '_' (protected)
or '__' (private) prefixes.

Public
^^^^^^
All member variables and methods are public by default in Python. So when you want to make your member public,
you just do nothing. See the example below:


.. code:: python

    class Cup:
        def __init__(self):
            self.color = None
            self.content = None

        def fill(self, beverage):
            self.content = beverage

        def empty(self):
            self.content = None


Protected
^^^^^^^^^

Protected member is (in C++ and Java) accessible only from within the class and it’s subclasses. How to
accomplish this in Python? The answer is – by convention. By prefixing the name of your member with a single
underscore, you’re telling others “don’t touch this, unless you’re a subclass”. See the example below:


.. code:: python

    class Cup:
        def __init__(self):
            self.color = None
            self._content = None # protected variable

        def fill(self, beverage):
            self._content = beverage

        def empty(self):
            self._content = None

Same example as before, but the content of the cup is now protected. This changes virtually nothing, you’ll
still be able to access the variable from outside the class, only if you see something like this:

.. code:: python

    cup = Cup()
    cup._content = "tea"

you explain politely to the person responsible for this, that the variable is protected and he should not
access it or even worse, change it from outside the class.


Private
^^^^^^^

By declaring your data member private you mean, that nobody should be able to access it from outside the class, i.e.
strong you can’t touch this policy. Python supports a technique called name mangling. This feature turns every
member name prefixed with at least two underscores and suffixed with at most one underscore into
_<className><memberName> . So how to make your member private? Let’s have a look at the example below:

.. code:: python

    class Cup:
        def __init__(self, color):
            self._color = color    # protected variable
            self.__content = None  # private variable

        def fill(self, beverage):
            self.__content = beverage

        def empty(self):
            self.__content = None

Our cup now can be only filled and poured out by using fill() and empty() methods. Note, that if you try
accessing __content from outside, you’ll get an error. But you can still stumble upon something like this:

.. code:: python

    redCup = Cup("red")
    redCup._Cup__content = "tea"

When you see this, you should probably kick your colleague, who’s responsible for it hard in the nuts.


