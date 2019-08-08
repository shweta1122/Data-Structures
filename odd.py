def c(x):
    s =[list(map(int, (l))) for l in x]
    print(s)
    odd=[]
    even=[]
    for i in range(0,len(s)):
        if i%2==0:
            odd.append(s[i][0])
        else:
            even.append(s[i][0])


    return (sum(odd)-sum(even))



l=input()
print(c(l))
