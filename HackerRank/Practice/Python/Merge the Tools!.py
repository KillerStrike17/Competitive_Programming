def merge_the_tools(string, k):
    # your code goes here
    len_string = len(string)
    N = int(len_string/k)
    value = [string[i:i+k] for i in range(0,len_string,k)]
    # print(value)

    for i in value:
        new_list = []
        for j in i:
            if not j in new_list:
                new_list.append(j)
                print(j,end="")
            else:
                continue
        print("")
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)