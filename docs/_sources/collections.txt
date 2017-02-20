Collections
-----------
This module implements specialized container datatypes providing alternatives to Python’s general purpose built-in
containers, dict, list, set, and tuple.


defaultdict	dict
^^^^^^^^^^^^^^^^
subclass that calls a factory function to supply missing values

.. code:: python

    from collections import defaultdict
    d = defaultdict(int)

    >>> d
    defaultdict(<type 'int'>, {})
    >>> d[0]
    0
    >>> d[1]
    0
    >>> d['a']
    0

    s = defaultdict(str)
    >>> s[0]
    ''
    >>> s['x']
    ''


OrderedDict	dict
^^^^^^^^^^^^^^^^
subclass that remembers the order entries were added


Counter	dict
^^^^^^^^^^^^
subclass for counting hashable objects


namedtuple()
^^^^^^^^^^^^
factory function for creating tuple subclasses with named fields

deque
^^^^^

list-like container with fast appends and pops on either end




