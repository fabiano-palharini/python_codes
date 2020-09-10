def my_decorator(func):
	def wrapper(a):
		print('something is happening before')
		func(a)
		print('something is happening after')
		
	return wrapper
	
@my_decorator
def say_whee(text):
	print(f'Wheeeeeeeeeeeee {text}')
	
