if __name__ == '__main__':
	n = int(input())
	arr = sorted(list(map(int, input().split())), reverse=True)
		
	top = None
	for i in arr:		
		if top is None or top == i:
			top = i
		else:
			print(i)
			break