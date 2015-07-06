from manhattan import *

def computeNearestNeighbor(username, users):
	"""Creates a sorted list of users based on their distance to username"""
	distances = []
	for user in users:
		if user != username:
			distance = manhattan(users[user], users[username])
			distances.append((distance, user))

	distances.sort()

	return distances