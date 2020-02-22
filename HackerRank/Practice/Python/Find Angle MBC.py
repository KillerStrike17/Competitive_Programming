# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
a = int(input())
b = int(input())
degree =  math.atan(a/b)
print(str(round(math.degrees(degree)))+"°")
