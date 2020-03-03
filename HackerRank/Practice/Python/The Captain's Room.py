# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
num_list = list(map(int,input().split()))
mylist = Counter(num_list).most_common()[:-2:-1]
print(mylist[0][0])

