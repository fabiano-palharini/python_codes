import re

def is_color_valid(color):
	return (re.match('^#[a-fA-F0-9]{3,6}', color)) is not None
	
	
if __name__ == '__main__':
	final_colors = []
	n = int(input())
	for _ in range(n):
		colors = input()		
		colors = re.sub('[{}]','',colors)
		colors = colors.replace('#',' #').split()
		
		if len(colors) > 1:
			for color in colors:
				color = re.sub('[^#a-zA-Z0-9]','',color)				
				if is_color_valid(color):
					final_colors.append(color)
	
	for color in final_colors:
		print(color)