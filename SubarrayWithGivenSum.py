def output(a, s, l):
    for i in range(0, l):
        l2=[]
        l2.append(i+1)
        s2 = a[i]
        for j in range(i+1, l):
            l2.append(j+1)
            s2 = a[j]+s2
            if s2 == s:
                minimum= min(l2)
                maximum=max(l2)
                return minimum, maximum
            else:
                continue
    return -1




leng = int(input("Enter the length of array"))
sums = int(input("enter the sum"))
l = []
for i in range(0, leng):
    element = int(input("Enter the element in an array"))
    l.append(element)

print(output(l,sums, leng))
