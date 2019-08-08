import math
a = [10, 20, 20, 10, 10, 30, 50, 10, 20]
myDict = dict.fromkeys(a, 0)
for i in a:
    myDict[i]+=1
socks = list(myDict.values())
print(socks)
for i in range(0,len(socks)):
    socks[i]=math.floor((socks[i]/2))

print(sum((socks)))
    

