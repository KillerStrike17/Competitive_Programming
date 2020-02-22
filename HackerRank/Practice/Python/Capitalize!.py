#!/bin/python3

import math
import os
import random
import re
import sys
import string
# Complete the solve function below.
def solve(s):
    #print(s)
    # x=""
    value = s.split()
    # for i in value:
    #     i = i.capitalize()
    #     # print(i)
    #     x = x + i + " "
    # print(s[0])
    return string.capwords(s,' ')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
