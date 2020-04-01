def custom_reverse(list):
	list.reverse()

def custom_pop(list):
	list.pop()
	
def custom_sort(list):
	list.sort()
	
def custom_append(list, element):
	list.append(int(element))

def custom_remove(list, element):
	list.remove(int(element))

def custom_insert(list, position, element):
	list.insert(int(position), int(element))	

def custom_print(list):
	print(list)

def parser(commands):
	list = []
	for command in commands:		
		if command[0] == 'print':
			custom_print(list)
		elif command[0] == 'insert':
			custom_insert(list, command[1], command[2])
		elif command[0] == 'remove':
			custom_remove(list, command[1])
		elif command[0] == 'append':
			custom_append(list, command[1])
		elif command[0] == 'sort':
			custom_sort(list)
		elif command[0] == 'pop':
			custom_pop(list)
		elif command[0] == 'reverse':
			custom_reverse(list)
			

if __name__ == '__main__':
	N = int(input())
	commands = []
	
	for i in range(N):
		commands.append(input().split())
	
	
	parser(commands)