data = [
	{'user':'tom', 'consumption': 1},
	{'user':'john', 'consumption': 5},
	{'user':'rachel', 'consumption': 2},
]

highest_consumption = {}

def user_with_highest_consumption():

	for rec in data:	
		
		if len(highest_consumption)  == 0 or highest_consumption[0]['consumption'] < rec['consumption']:
			highest_consumption[0] = rec
		
	print('No records found' if len(highest_consumption) == 0 else  highest_consumption[0])

	
user_with_highest_consumption()