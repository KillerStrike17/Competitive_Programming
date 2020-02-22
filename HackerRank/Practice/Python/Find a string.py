def count_substring(string, sub_string):
    # print(string)
    # print(sub_string)
    count = 0
    for i in range(len(string)):
        # print(i)
        # print(string.find(sub_string,i,i+3))
        if(string.find(sub_string,i,i+len(sub_string))!=-1):
            count = count+1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)