def prime_numbers(n):
	for a in range(2, n):
		if a > 1:
			for b in range(2, n):
				if a % b == 0:
					break
				else:
					print(a)
prime_numbers(10)