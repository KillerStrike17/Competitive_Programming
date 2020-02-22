# Enter your code here. Read input from STDIN. Print output to STDOUT
m,n = input().split()
list_n = input().split()
A = set(input().split())
B = set(input().split())
happy = 0
#print(m,n,list_n,list_m,A,B)
# for i in list_n:
#     if (i in A):
#         happy = happy + 1
#         continue
#     elif (i in B):
#         happy = happy - 1

# print(happy)
x = [(i in A)-(i in B) for i in list_n]
print(sum(x))
