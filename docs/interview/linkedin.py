"""
Given:
  A method getRandom01() that generates a random integer in [0, 1], where 0 and 1 is generated with probability 0.5

Implement:
  A method getRandom06Uniform() that generates a random integer in [0, 6] with uniform probability


Answer:   2^2 + 2^1 + 2^0
          1     1     1
          4     2     1   =  7

"""

from random import randint
import math


def generator():

    rand_num1 = randint(0, 1)
    rand_num2 = randint(0, 1)
    rand_num3 = randint(0, 1)

    while True:
        res = math.pow(2, 2) * rand_num1 + \
              math.pow(2, 1) * rand_num2 + \
              math.pow(2, 0) * rand_num3

        if res != 7:
            return res

        else:
            rand_num1 = randint(0,1)
            rand_num2 = randint(0,1)
            rand_num3 = randint(0,1)


print generator()

