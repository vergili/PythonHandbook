
Rotate an array
^^^^^^^^^^^^^^^
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
How many different ways do you know to solve this problem?

.. code:: python

    def rotate(a, k):

        return a[len(a)-k:] + a[:len(a)-k]



Reverse a String
^^^^^^^^^^^^^^^^
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

.. code:: python

    def reverse(s):

        l = s.split(' ')
        l.reverse()
        return l


Evaluate Reverse Polish Notation (Stack)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /.
Each operand may be an integer or another expression. For example:

["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

.. code:: python



Isomorphic Strings
^^^^^^^^^^^^^^^^^^
Given two strings s and t, determine if they are isomorphic. Two strings are isomorphic if the characters
in s can be replaced to get t.

For example,"egg" and "add" are isomorphic, "foo" and "bar" are not.

Analysis

We can define a map which tracks the char-char mappings. If a value is already mapped, it can not be mapped again.

.. code:: python



Word Ladder
^^^^^^^^^^^
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start
to end, such that only one letter can be changed at a time and each intermediate word must exist in the dictionary.
For example, given:

start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]

One shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", the program should return its length 5.

.. code:: python

