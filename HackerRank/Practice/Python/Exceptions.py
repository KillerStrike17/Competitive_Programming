# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
for i in range(N):
    
    
    try:
        a = list(map(int,input().split()))
        print(int(a[0]//a[1]))
    except Exception as e:
        print("Error Code:",e)
