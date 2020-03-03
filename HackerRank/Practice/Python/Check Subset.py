# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    a = int(input())
    seta = set(input().split())
    b = int(input())
    setb = set(input().split())
    # print(seta,setb)
    print(seta.issubset(setb))
