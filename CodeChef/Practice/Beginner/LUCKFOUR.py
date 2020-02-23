T = int(input())
for i in range(T):
	counter = 0
	value = list(input())
	for j in value:
		if j == '4':
			counter += 1

	print(counter)