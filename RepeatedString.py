def calculate(s,n):
    s=s.lower()
    if len(s)==1:
        return n
    else:
        repeated=s*n
        finalans=''
        for i  in range(0,n):
            finalans+=repeated[i]

        count=finalans.count('a') 
        
        return count
s='abcac'
n=10
print(calculate(s,n))
