def decToBin(n):
	if n >= 1:
		decToBin(n // 2)
	dec = n%2
	print(dec)

decToBin(3)