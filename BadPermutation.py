import itertools
from itertools import permutations
flatten_iter = itertools.chain.from_iterable
def factors(n):
    a= set(flatten_iter((i, n//i) 
                for i in range(1, int(n**0.5)+1) if n % i == 0))
    a=sorted(list(a))
    b=list(permutations(a))
    print("len"+str(len(b)))
    f=[]
    f.extend(b)
    print(f)      
    for i in range(0,len(a)-1):
        c=a[i]
        d=a[i+1]
        for j in f:
            try:
                for k in range(0,len(j)-1):
                    if j[k]==c and j[k+1]==d:
                        
                        b.remove((j))
            except:
                continue

    return len(b),a,b
print(factors(6))