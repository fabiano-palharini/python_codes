import textwrap

def wrap(string, max_width):
	result = ''
	for s in textwrap.wrap(string, max_width):
		result += s + '\n'
	return  result

if __name__ == '__main__':
	string, max_width = input(), int(input())
	result = wrap(string, max_width)
	print(result)

