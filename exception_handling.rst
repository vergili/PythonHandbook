Exception Handling
------------------

Exception is an unforeseen error that occurs when a program is running.



Built-in Exceptions
^^^^^^^^^^^^^^^^^^^

https://docs.python.org/2.7/library/exceptions.html#ZeroDivisionError



try except finally else
^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    import sys

    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise



.. code:: python

    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
        except IOError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()

