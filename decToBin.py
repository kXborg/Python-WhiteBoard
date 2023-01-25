# Find number of 1s in a binary number.

def decToBin(n):
	# Convert to binary.
	dec = bin(n).replace("0b","")
	# Use comprehension to separate the integer to digits.
	x = [int(i) for i in str(dec)]
	print(x)
	# Count number of 1's in the binary number.
	count = 0
	for i in range(0, len(x)):
		if x[i] == 1:
			count += 1
	print("Number of 1's", count)

decToBin(3)