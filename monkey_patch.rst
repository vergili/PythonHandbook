Monkey Patch
------------


It's simply the dynamic replacement of attributes at runtime.

For instance, consider a class that has a method get_data. This method does an external lookup
(on a database or web API, for example), and various other methods in the class call it. However,
in a unit test, you don't want to depend on the external data source - so you dynamically replace
the get_data method with a stub that returns some fixed data.

Because Python classes are mutable, and methods are just attributes of the class, you can do this as
much as you like - and, in fact, you can even replace classes and functions in a module in exactly the same way.



Monkey patching is reopening the existing classes or methods in class at runtime and changing the behavior,
which should be used cautiously, or you should use it only when you really need to.

As Python is a dynamic programming language, Classes are mutable so you can reopen them and modify or even replace them.




Monkey patching can only be done in dynamic languages, of which python is a good example. Changing a method
at runtime instead of updating the object definition is one example;similarly, adding attributes
(whether methods or variables) at runtime is considered monkey patching. These are often done when
working with modules you don't have the source for, such that the object definitions can't be easily changed.

This is considered bad because it means that an object's definition does not completely or accurately
describe how it actually behaves.


**Reference
http://stackoverflow.com/questions/5626193/what-is-a-monkey-patch

***Python unit test best practice to avoid monkey patching bug
https://stackoverflow.com/questions/47041257/python-unit-test-best-practice-to-avoid-monkey-patching-bug




