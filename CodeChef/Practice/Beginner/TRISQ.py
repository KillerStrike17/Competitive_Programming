# cook your dish here
def triangle(x):
    x = int((x -2)/2)
    return int(x*(x+1)/2)
    
n = int(input())
for i in range(n):
    x = int(input())
    print(triangle(x))
    
    
