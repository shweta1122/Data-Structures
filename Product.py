def product(l):
    b=func(l)
    return b
def func(l):
    pro=1
    a=[]
    for i in range(0,len(l)):
        index=i
        pro=1
        while (index>0):
                 pro*=l[index-1]
                 index=index-1
        for j in range(i,len(l)):
            
            if j<len(l)-1:
                pro*=l[j+1]
                
        a.append(pro)        
    return a
print(product(l=[3,2,1]))