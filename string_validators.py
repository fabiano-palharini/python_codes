if __name__ == '__main__':
	s = input()	
	print(str(True if s.isalnum() else False))
	print(str(True if s.isalpha() else False))
	print(str(True if s.isdigit() else False))
	print(str(True if s.islower() else False))
	print(str(True if s.isupper() else False))
