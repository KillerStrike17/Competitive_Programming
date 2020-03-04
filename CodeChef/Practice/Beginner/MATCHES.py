# cook your dish here
def totalsum(mydict, result):
    mysum = 0
    while result!=0:
        value = result%10
        result = result//10
        mysum += mydict[value]
    
    print(mysum)

mydict = {0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
# print(mydict)

n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    result = a+b
    # print(result)
    totalsum(mydict,result)
