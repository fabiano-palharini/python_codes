# Return the character with the "longest consecutive run" of an input character sequence
# abbbc -> b
# bbbaaaabbccd -> a
# abcdeffg -> f
# abbbcccc -> c
test_cases = ['abbbc', 'bbbaaaabbccd', 'abcdeffg', 'abbbcccc']
# test_cases = ['abbbc']



for input in test_cases:
	max_char = None
	max_counter = 0
	current_char = None
	current_counter = 0

	for char in input:
		if current_char != char or current_char is None:			
			current_char = char
			current_counter = 1					
		else:
			current_counter += 1
			
		if current_counter > max_counter:
			max_counter = current_counter
			max_char = current_char
			
	
	print(f'{input} - {max_char}: {max_counter}')