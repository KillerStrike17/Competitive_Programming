# Enter your code here. Read input from STDIN. Print output to STDOUT

n=input()
s=set()
for i in range(int(n)):
    # print(i)
    # print(s)
    s.add(input())

print(len(s))
