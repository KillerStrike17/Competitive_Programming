# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
nset = set(map(int, input().split()))
x = int(input())
value = 0
for i in range(x):
    m = input().split()
    mset = set(map(int, input().split()))
    # print(nset)
    # print(mset)
    if m[0] == "intersection_update":
        # print("in block")
        nset.intersection_update(mset)
        # value += len(nset)
    elif m[0] == "update":
        nset.update(mset)
        # value += len(nset)
    elif m[0] == "symmetric_difference_update":
        nset.symmetric_difference_update(mset)
        # value += len(nset)
    elif m[0] == "difference_update":
        nset.difference_update(mset)
        # value += len(nset)
print(sum(nset))
