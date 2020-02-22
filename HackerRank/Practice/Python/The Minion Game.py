def minion_game(string):
    vowels = 'AEIOU'

    counterA = 0
    counterB = 0
    for i in range(len(string)):
        if s[i] in vowels:
            counterA += (len(string)-i)
        else:
            counterB += (len(string)-i)

    #print(counterA)
    #print(counterB)
    if counterA > counterB:
        print("Kevin {}".format(counterA))
    elif counterB > counterA:
        print("Stuart {}".format(counterB))
    else:
        print("Draw")


    

if __name__ == '__main__':
    s = input()
    minion_game(s)