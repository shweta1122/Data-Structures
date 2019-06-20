l1 = list(map(int,input().split(' ')))
l2 = list(map(int,input().split(' ')))
print(len(([[i, j] for i in l1 for j in l2 if i**j > j**i])))
