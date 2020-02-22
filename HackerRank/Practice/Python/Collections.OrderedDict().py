# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N = int(input())
mydict = OrderedDict()
for i in range(N):
    # print(i)
    name,price= input().rsplit(' ',1)

    # print(data)
    if name not in mydict.keys():
        mydict[name] = int(price)
        # print("my dict",mydict)
    else:
        value = mydict[name]
        mydict[name] = int(value) + int(price)
    
for key in mydict.keys():
    print(key,mydict[key])
