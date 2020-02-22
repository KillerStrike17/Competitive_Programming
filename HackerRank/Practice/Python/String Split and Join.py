def split_and_join(line):
    # write your code here
    text = line.split(" ")
    text = '-'.join(text)
    return text

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)