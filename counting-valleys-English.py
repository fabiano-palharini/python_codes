import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
	level = 0
	previous_level = 0
	valleys = 0
	
	for step in path:
		previous_level = level
		level += int(1 if step =='U' else -1)
		if previous_level < 0 and level == 0:
			valleys += 1
		
	return valleys

if __name__ == '__main__':
    steps = int(input().strip())

    path = input()

    print(countingValleys(steps, path))