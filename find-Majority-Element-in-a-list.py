# A majority element appears more than half the time. Find majority element from the list below.
# l1 = [1,3,3,5,5,7,8,3,6,7,9,3,3,2,10]

def findMajority(l):
	counter = 0
	value = 0
	for i in range(0, len(l)):
		x = l.count(l[i])
		if x > counter:
			counter = x
			value = l[i]
		else:
			pass
	print("Majority element is", str(value), "occuring ", counter, " times.")
	

l1 = [1,3,3,5,5,7,8,3,6,7,9,3,3,2,10]
findMajority(l1)