from collections import Counter
import numpy as np
import pandas as pd


# print(df)


N = int(input())
cost = [100,75,50,25]
for i in range(N):
    
    # ml = []
    length = int(input())
    a = np.zeros(shape = (4,4))
    df = pd.DataFrame(a,columns = ('12','3','6','9'))
    print(df)
    for i in range(length):
        x = input().split()
        if x[0] == 'A':
            df.at[0,x[1]] = df.at[0,x[1]] + 1

    print(df)