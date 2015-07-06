from computeNearestNeighbor import *

def recommend(username, users):
	"""Recommends bands that have not been rated by username"""
	
	nearest = computeNearestNeighbor(username,users)[0][1]

	recommendations = []

	# Find bands that neighbor rated but user did not
	neighborRatings = users[nearest]
	userRatings = users[username]

	for artist in neighborRatings:
		if not artist in userRatings:
			recommendations.append((artist, neighborRatings[artist]))

	# Here, author uses the sorted function to demonstrate different ways to sort in python
	return sorted(recommendations, key = lambda artistTuple: artistTuple[1], reverse=True)

