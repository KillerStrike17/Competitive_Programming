# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
a,b = input().split()
a =list(a)
a.sort()
c = list(combinations_with_replacement(a,int(b)))

for i in c:
    # print(i)
    for j in i:
        print(j,end="")
    print("")

