import sys
def rev(l,b):
    c=b
    orgi=[]
    for i in range(0,len(l),b):
        temp=[]
        for j in range(i,c):
            temp.append(l[j])
        orgi.extend(temp[::-1])
        c=c+c
        if c <=len(l):
            continue
            
        else:
            c=len(l)

    return orgi

testcase=int(input())
for i in range(testcase):
    a,b = map(int,sys.stdin.readline().split())
    l= [int(x) for x in input().split()]
    print(rev(l,b))