# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
a,b = input().split()
a = list(a)
a.sort()
# print(a)
value = []
for i in range(1,int(b)+1):
    # print(i)
    x = list(combinations(a,i))
    x.sort()
    # print(x)
    value.append(x)

    # print('\n'.join(list(combinations(a,i))))
# print(value)
for i in value:
    res = list(map("".join, i)) 
    print("\n".join(res))
    # for j in i:
    #     print(list(''.join(q) for q in j))
    