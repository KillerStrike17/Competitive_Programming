# cook your dish here
N = int(input())
for i in range(N):
    l = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    sum_v =0
    for i in range(l):
        sum_v += min(a[i],b[i])
    print(sum_v)
