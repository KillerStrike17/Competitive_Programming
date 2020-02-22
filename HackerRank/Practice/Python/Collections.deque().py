# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
N = int(input())
for i in range(N):
    command = input()
    if "appendleft" in command:
        b = command.split()
        # print(b)
        d.appendleft(b[1])
    elif "append" in command:
        
        b = command.split()
        # print(b)
        d.append(b[1])
    elif "popleft" in command:
        d.popleft()
    elif "pop" in command:
        d.pop()

print(' '.join(d))
