l=[1,2,3,4,5,6,7,9,10]
print(list(filter(lambda x: x not in l,range(l[0],l[-1]+1)))[0])