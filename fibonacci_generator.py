def new_number(nitems):
	a = 0
	b = 1
	count = 0
	current = None
	while count <= nitems:
		if count > 2:
			current = int(b + a)
			yield current
			a = b
			b = current
			
		elif count == 1:
			yield b
		elif count == 0:
			yield a
			
		count += 1

if __name__ == "__main__":
	fibonacci_items = []
	nitems = int(input('How many items?'))
	nth_element = None
	
	for x in new_number(nitems):
		nth_element = x
		
	print(x)