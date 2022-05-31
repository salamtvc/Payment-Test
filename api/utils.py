import random


def get_random_number():
	sample_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
	item = random.choice(tuple(sample_set))
	# random item from set
	print(item)