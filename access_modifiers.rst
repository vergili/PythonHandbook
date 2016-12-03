Access Modifiers in Python (Public, Protected, Private)
-------------------------------------------------------
Languages like c++ or java have access modifiers to restrict connection from outside of class etc.
but in python there is no restriction to access any function or variable. In python all function and variables have
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

Private
^^^^^^^

In python a private variable or method started with at least two underscores and suffixed with at most one underscore

Example Naming rule:
``__my_variable`` or ``___my_variable``  or  ``__my_variable_``

``__my_method()`` or ``___my_variable()``  or  ``__my_variable_()``

Python support to reach private members from outside of the class but it is mandatory to add ``_ClassName`` prefix

To reach a private member of class we have to call like this:

``_ClassName__my_variable``


.. code:: python

    class Pet:
        def __init__(self):
            self.__species = None  # private variable

        def fill(self, species):
            self.__species = species

        def empty(self):
            self.__species = None

        def show(self):
            print self.__species


This method will work but not suggested since __species is a private variable
.. code:: python

    pet = Pet()
    pet._Pet__species = "van"
    pet.show()


This is the suggested way to fill species
.. code:: python

    pet = Pet()
    pet.fill('van')
    pet.show()


Protected
^^^^^^^^^

Protected member is (in C++ and Java) accessible only from within the class and it’s subclasses. How to
accomplish this in Python? The answer is – by convention. By prefixing the name of your member with a single
underscore, you’re telling others “don’t touch this, unless you’re a subclass”. See the example below:

.. Note::  protected prefix (_) is just to inform user there is no any restriction like private modifiers (__) in python.


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




**References:**
https://docs.python.org/3/tutorial/classes.html#private-variables

