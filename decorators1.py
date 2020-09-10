def my_decorator(func):
	def wrapper():
		print('something before the function')
		func()
		print('something after the function')
	
	return wrapper
	
def say_whee():
	print('Wheeeeee!!!')
	
say_whee = my_decorator(say_whee)