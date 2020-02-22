n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    value = input()
    if "pop" in value:
        s.pop()
    else:
        value = value.split()
        if "remove" in value[0]:
            s.remove(int(value[1]))
        elif "discard" in value[0]:
            s.discard(int(value[1]))

print(sum(s))
