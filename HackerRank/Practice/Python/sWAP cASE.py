def swap_case(s):
    x=""
    for i in s:
        if i.islower():
            x = x+ i.upper()
        else:
            x = x +i.lower()
    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)