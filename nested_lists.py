if __name__ == '__main__':
	students = []
	scores = []
	
	#read all inputs and store in both lists: students and scores
	for _ in range(int(input())):
		name = input()
		score = float(input())
			
		students.append({'name': name, 'score': score})
		scores.append(score)
	
	#remove the lowest score
	scores = sorted(scores)	
	scores_without_lowest_one = list(filter(lambda a: a != min(scores), scores))
	
	#get the second lowest
	second_lowest = scores_without_lowest_one[0]
	
	#print in alphabetical order the names of the students with the second lowest score
	for i in sorted(students, key = lambda i : i['name']):
		if i['score'] == second_lowest:
			print(i['name'])		