# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
N = int(input())
data = []
for i in range(N):
    data.append(input())

value = Counter(data)
print(len(value.keys()))
for i in value.keys():
    print(value[i],end=" ")

