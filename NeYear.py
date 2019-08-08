import math


def calc(l, o):
    temp = []
    for i in range(0, len(o)):
        temp.append(abs(l[i]-o[i]))
    s = sum(temp)//2
    if s < len(o):
        print(s+1)
    else:
        print('Too chaotic')


l = [2,1,5,3,4]
o = [1, 2, 3,4,5]
calc(l,o)
