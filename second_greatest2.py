if __name__ == '__main__':
	n = int(input())
	arr = list(map(int, input().split()))
	
	#remove all max values from the array
	new_list = list(filter(lambda a: a != max(arr), arr))
	
	#order the array on descending order and print the first element
	print(sorted(new_list, reverse=True)[0])