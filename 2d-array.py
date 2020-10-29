import math
import os
import random
import re
import sys

def sum_elements(i, j, arr):
	return arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]

# Complete the hourglassSum function below.
def hourglassSum(arr):
	highest_value = None
	
	for i in range(1, 5	):
		for j in range(1, 5):
			sum_hourly = sum_elements(i, j, arr)
			if highest_value is None or highest_value < sum_hourly:
				highest_value = sum_hourly
		
	return(highest_value)
	
if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)