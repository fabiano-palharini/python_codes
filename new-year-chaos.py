import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
	original_queue = [i for i in range(1, len(q) + 1)]
	elements = {}
	
	for i in original_queue:
		elements[i] = [j for j in q if j > i]
	
	print(elements)
	
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
