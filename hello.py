def recursive(n):
	if not isinstance(n, int):
		raise AttributeError("Wrong argument")
	n -= 1
	print(n)
	if n <= 0:
		return
	recursive(n)

recursive(10)