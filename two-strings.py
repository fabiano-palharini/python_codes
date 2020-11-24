#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the twoStrings function below.
def twoStrings(s1, s2):
	string1 = Counter(s1)
	string2 = Counter(s2)
	
	return ('YES' if string1 & string2 != {} else 'NO')

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

    print(result)
