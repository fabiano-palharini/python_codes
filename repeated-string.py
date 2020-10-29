import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
	repeat_s = n // len(s)
	size_last_repeat = n % len(s)
	
	a_counter_in_s = s.count('a')
	a_counter_last_s = s[0:size_last_repeat].count('a') if size_last_repeat != 0 else 0 
	
	print(a_counter_in_s * repeat_s + a_counter_last_s)
	
	
if __name__ == '__main__':
    s = input()

    n = int(input())

    result = repeatedString(s, n)
