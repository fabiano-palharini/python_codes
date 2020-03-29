#data = []


data = [
	{'user':'tom', 'consumption': 1},
	{'user':'john', 'consumption': 5},
	{'user':'rachel', 'consumption': 2},
]


def user_with_highest_consumption():
	if len(data) > 0:
		print(sorted(data, key = lambda i : i['consumption'], reverse=True)[0])
	
user_with_highest_consumption()
