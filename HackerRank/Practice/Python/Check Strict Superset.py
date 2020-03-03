# Enter your code here. Read input from STDIN. Print output to STDOUT
seta = set(input().split())
n = int(input())
counter = 0
for i in range(n):
    b = set(input().split())
    check = b.issubset(seta)
    # print(check)
    if check == False:
        counter = -1

if counter == -1:
    print(False)
else:
    print(True)
