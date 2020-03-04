# cook your dish here
def check(a,b):
    sim = esim = esim2 = esim3 = dsim = 0
    for i in range(len(a)):
        if a[i]==b[i] and a[i]!='?':
            sim += 1
        elif a[i]!=b[i] and b[i]=='?':
            esim += 1
        elif a[i]!=b[i] and a[i]=='?':
            esim2 += 1
        elif a[i]==b[i] and a[i]=='?':
            esim3 += 1
        elif a[i]!=b[i]:
            dsim +=1
    
    total = esim+esim2+esim3
    print(dsim,dsim + total)
    # print(sim,esim,esim2,esim3)
    

x = int(input())
for i in range(x):
    a = input()
    b = input()
    check(a,b)
