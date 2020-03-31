def count_substring(string, sub_string):
	input = list(string)
	input_sub = list(sub_string)	
	#count = 0	
	# for i in range(0, len(input) -1):
		# if input[i:i+len(sub_string)] == input_sub[0:len(sub_string)]:
			# count += 1			
	return sum ([1 for i in range(0, len(input) -1) if input[i:i+len(sub_string)] == input_sub[0:len(sub_string)]])
	

if __name__ == '__main__':
	string = input().strip()
	sub_string = input().strip()

	count = count_substring(string, sub_string)
	print(count)