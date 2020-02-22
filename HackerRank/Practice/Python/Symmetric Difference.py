# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
mset = set(map(int,input().split()))
n = int(input())
nset = set(map(int,input().split()))
value = list(mset.difference(nset).union(nset.difference(mset)))
for i in sorted(value):
    print(i)
# print(value)
