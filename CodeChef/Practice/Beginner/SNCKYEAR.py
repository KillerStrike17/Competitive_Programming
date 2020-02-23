# cook your dish here
T = int(input())
a = [2010,2015,2016,2017,2019]

for i in range(T):
    N = int(input())
    
    if N in a:
    	print("HOSTED")
    else:
    	print("NOT HOSTED")
