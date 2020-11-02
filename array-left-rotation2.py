import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def array_left_rotation(a, n, k):
	print(a[k:])
	print(a[:k])
	return a[k:]+a[:k]

if __name__ == '__main__':
	n, k = map(int, input().strip().split(' '))
	print(n)
	print(k)
	a = list(map(int, input().strip().split(' ')))
	answer = array_left_rotation(a, n, k);
	print(*answer, sep=' ')