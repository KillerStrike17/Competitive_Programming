# Enter your code here. Read input from STDIN. Print output to STDOUT
N,M = map(int,input().split())
#print(N)
# print(M)
pattern = [(".|."*(2*i+1)).center(M,"-")for i in range(int(N/2))]
# print(pattern)
# print()
# print(pattern[::-1])
print("\n".join(pattern + ["WELCOME".center(M,"-")] + pattern[::-1]))
