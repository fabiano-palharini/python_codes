import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
	tempPairs = []
	numberOfPairs = 0
	
	for i in range(n):
		try:
			tempPairs.pop(tempPairs.index(ar[i]))
			numberOfPairs += 1
		except:
			tempPairs.append(ar[i])
		
	return numberOfPairs

if __name__ == '__main__':    
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    print(sockMerchant(n, ar))