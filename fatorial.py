# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(1500)
import sys
import cProfile

def fatorial(n):
	if n == 1 or n == 0:
		return 1
	else:
		return n * fatorial(n-1)
	
if __name__ == '__main__':
	sys.setrecursionlimit(2000)
	x = int(input('Calcule o fatorial de: '))
	print(sys.getsizeof(fatorial(x)))
	print(fatorial(x))
	cProfile.run('fatorial(x)')