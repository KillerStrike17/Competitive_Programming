import string
lower_alpha = string.ascii_lowercase

def print_rangoli(size):
    # your code goes here
    pattern = []
    width = 4*size-3
    for i in range(size):
        value = "-".join(lower_alpha[i:size])
        value = (value[::-1]+value[1::]).center(width,'-')
        pattern.append(value)
        # print(value)
    print('\n'.join(pattern[:0:-1]+pattern))
    #print(pattern[:0:-1])

if __name__ == '__main__':