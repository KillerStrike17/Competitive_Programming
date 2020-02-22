if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    x = list(set(arr))
    x.remove(max(x))
    print(max(x))

