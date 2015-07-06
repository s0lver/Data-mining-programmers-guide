def manhattan(rating1,rating2):
	"""Computes the Manhattan distance"""

	distance =  0
	for key in rating1:
		if key in rating2:
			distance += abs( rating1[key] - rating2[key])

	return distance