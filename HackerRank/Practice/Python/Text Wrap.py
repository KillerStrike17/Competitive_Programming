import textwrap

def wrap(string, max_width):
    word_list = ""
    wrapper = textwrap.TextWrapper(width=max_width)
    for i in wrapper.wrap(string):
        word_list = word_list + i + "\n"
    return word_list

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)