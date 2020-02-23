N = list(map(int,input().split()))
M = list(map(int, input().split()))
# print(N)
# print(M)
max_sum = 0
list_max_sum = []
for i in range(N[1]-1,-1,-1):
    # print(i)
    local_sum = 0
    list_local_sum =[]
    for j in range(i,-1,-1):
        # print(j)
        temp = local_sum + M[j]
        if temp == N[0]:
            local_sum = temp
            list_local_sum.append(j)
            break
        elif temp > N[0]:
            continue
        elif temp < N[0]:
            local_sum = temp
            list_local_sum.append(j)
            continue
    if max_sum < local_sum:
        max_sum = local_sum
        list_max_sum = list_local_sum
print(max_sum)
list_max_sum.sort()
print(' '.join([str(i) for i in list_max_sum]))