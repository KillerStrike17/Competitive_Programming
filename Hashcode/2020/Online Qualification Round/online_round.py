books, libraries,days= list(map(int,input().split()))
scores = list(map(int,input().split()))
my_lib={}
my_book = {}
for i in range(libraries):
	my_lib[i] = list(map(int, input().split()))
	my_book[i] = list(map(int, input().split()))

print(my_lib)
print(my_book)

x = {k: v for k, v in sorted(my_lib.items(), key=lambda item: item[1][1],reverse = True)}
counter = signup = 0
for i in range(days):
	if signup == 0:
		key_value = list(x.keys())
		my_data = my_lib[key_value[counter]]
		signup = my_data[1]
