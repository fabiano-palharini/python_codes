import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
	for i in range(d):
		item = a.pop(0)
		a.append(item)
		print(a)
	
	return a

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)