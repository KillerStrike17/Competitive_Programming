# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
x = str(input())
groups = []
# uniquekeys = []
for k,g in groupby(x):
    groups.append(list(g))      
    # uniquekeys.append(k)
# print(groups)
for i in groups:
    value = len(i)
    print(tuple((value,int(i[0]))),end =" ")