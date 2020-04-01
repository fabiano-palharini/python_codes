def parser(commands):
	list = []
	for command in commands:
		cmd = command[0]
		args = command[1:]
		
		if command[0] == 'print':
			print(list)
		else:
			eval('list.' + cmd + "(" + ",".join(args) + ")")

if __name__ == '__main__':
	N = int(input())
	commands = []
	
	for i in range(N):
		commands.append(input().split())
	
	
	parser(commands)