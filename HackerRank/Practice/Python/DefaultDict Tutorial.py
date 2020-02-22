# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
N = list(map(int,input().split()))
A = defaultdict(list)
B = []
for i in range(1,N[0]+1):
    A[input()].append(i)
# print(A)
for i in range(N[1]):
    B.append(input())

for i in B:
    if i in A.keys():
        print(" ".join(map(str,A[i])))
    else:
        print("-1")
