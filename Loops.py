if __name__ == '__main__':
	n = int(input())
	
	[print(i**2) for i in range(n)]
	
	#print(*[n**2 for n in range(n)], sep='\n')
	
	# i = 0
	# while (i < n):
		# print(i**2)
		# i += 1