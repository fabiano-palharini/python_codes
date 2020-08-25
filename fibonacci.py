if __name__ == '__main__':
	fibonacci_items = []
	nitems = int(input('How many items?'))
	n0, n1 = 0, 1
	current_item = None
	# print(n0)
	# print(n1)
	# fibonacci_items.append(n0)
	# fibonacci_items.append(n1)
	count = 2
	while count < nitems:
		current_item = n1 + n0
		n0 = n1
		n1 = current_item
		count += 1
		# print(current_item)
		# fibonacci_items.append(current_item)
		
	print(current_item)