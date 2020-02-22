if __name__ == '__main__':
    scores = []
    names = []
    final_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        names.append(name)
    y = scores.copy()
    # print(min(scores))
    scores = set(scores)
    scores.remove(min(scores))
    value = min(scores)
    for i in range(len(names)):
        if value == y[i]:
            final_list.append(names[i])
    
    final_list.sort()
    for i in final_list:
        print(i)
