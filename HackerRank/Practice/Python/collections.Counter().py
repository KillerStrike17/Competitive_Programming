# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

X = int(input())
show_size =map(int,input().split())
data = Counter(show_size)
# print(data.values())
N  = int(input())
amount = 0
for i in range(N):
    customer = list(map(int,input().split()))
    # print(customer)
    if customer[0] in data.keys():
        if data[customer[0]] > 0:
            # print(data[customer[0]])
            amount = amount + customer[1]
            data[customer[0]] = data[customer[0]] - 1
        else:
            continue
    else:
        continue

print(amount)

