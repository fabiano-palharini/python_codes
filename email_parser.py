import re

def is_email_valid(email):
	return (re.match('^<[a-zA-Z]\w+([.-]\w+)?\@[a-zA-Z]+\.[a-zA-Z]{1,3}>$', email)) is not None
	
	
if __name__ == '__main__':
	
	n = int(input())
	for _ in range(n):
		name, email = str(input()).split(' ')
		no_angle_brackets = email.replace('<', '').replace('>','')

		if (is_email_valid(email)):
			print(name, email)