# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
x, y  = input().split()
x = ''.join(sorted(x))
# print(x)
z = list(permutations(x,int(y)))
for i in z:
    for j in range(int(y)):
        print(i[j],end="")
    print("")
