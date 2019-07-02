#code
from itertools import combinations
l=[]
test=int(input())
for i in range(test):
    pkt=int(input())
    a=[int(x) for x in input().split()]
    std=int(input())
    a=list(combinations(a,std))
    for x in a:
        b=max(x)-min(x)
        l.append(b)
    print(min(l))
