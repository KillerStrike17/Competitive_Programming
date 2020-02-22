# Enter your code here. Read input from STDIN. Print output to STDOUT
value = list(map(int,input().split()))
sum_value = 0
for i in range(value[0]):
    # print(i)
    value2 = list(map(int,input().split()))
    # print(max(value2[1:]))
    sum_value += (max(value2[1:])**2)
print(sum_value)
print(sum_value%value[1])
