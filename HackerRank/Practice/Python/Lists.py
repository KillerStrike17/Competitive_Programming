if __name__ == '__main__':
    N = int(input())
    list_1= []
    for i in range(N):
        value = input()
        if "pop" in value:
            list_1.pop()
        elif "print" in value:
            print(list_1)
        elif "reverse" in value:
            list_1.reverse()
        elif "sort" in value:
            list_1.sort()
        else:
            value_1 = value.split()
            if "insert" in value_1[0]:
                list_1.insert(int(value_1[1]),int(value_1[2]))
            elif "append" in value_1[0]:
                list_1.append(int(value_1[1]))
            elif "remove" in value_1[0]:
                list_1.remove(int(value_1[1]))
