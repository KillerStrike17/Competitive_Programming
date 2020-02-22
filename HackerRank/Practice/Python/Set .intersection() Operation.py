# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
nset = set(map(int, input().split()))
m = int(input())
mset = set(map(int, input().split()))

print(len(nset.intersection(mset)))
