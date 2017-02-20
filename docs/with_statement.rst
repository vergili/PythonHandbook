With Statement
--------------

```with``` statement introduced with Python 2.5




.. code:: python

    class File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()


    files = []
    for _ in range(10000):
        with File('foo.txt', 'w') as infile:
            infile.write('foo')
            files.append(infile)



.. code:: python

    from contextlib import contextmanager

    @contextmanager
    def open_file(path, mode):
        the_file = open(path, mode)
        yield the_file
        the_file.close()

    files = []

    for x in range(100000):
        with open_file('foo.txt', 'w') as infile:
            files.append(infile)

    for f in files:
        if not f.closed:
            print('not closed')



.. code:: python

    from contextlib import contextmanager

    @contextmanager
    def tag(name):
        print("<%s>" % name)
        yield
        print("</%s>" % name)

    >>> with tag("h1"):
    ...    print("foo")
    ...
    <h1>
    foo
    </h1>


.. code:: python

    from contextlib import ContextDecorator

    class makeparagraph(ContextDecorator):
        def __enter__(self):
            print('<p>')
            return self

        def __exit__(self, *exc):
            print('</p>')
            return False

    @makeparagraph()
    def emit_html():
        print('Here is some non-HTML')

    emit_html()