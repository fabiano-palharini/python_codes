def mutate_string(string, position, character):
	# new_value = list(string)
	# new_value[position] = character
	# return ''.join(new_value)
	return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
	s = input()
	i, c = input().split()
	s_new = mutate_string(s, int(i), c)
	print(s_new)