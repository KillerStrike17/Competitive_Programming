N = int(input())
for i in range(N):
	a,b = map(int, input().split())
	if a>b:
		print(">")
	elif b>a:
		print("<")
	elif a==b:
		print("=")