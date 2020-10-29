import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
	jumps = 0
	i = 0
	while i < len(c) - 1:		
		if (i+2 < len(c)) and c[i+2] == 0:
			i+=2			
		else:
			i+=1
		jumps += 1
		
		print('i = ' + str(i))
		print('jumps = ' + str(jumps))
	
	return jumps
			

if __name__ == '__main__':
    
    c = list(map(int, input().rstrip().split()))

    print(jumpingOnClouds(c))