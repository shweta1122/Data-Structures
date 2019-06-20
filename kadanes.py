def compute(l):
    l2 = []
    for i in range(0, len(l)):
        l1 = []
        sumi = l[i]

        for j in range(i+1, len(l)):
            sumi = sumi + l[j]
            if sumi>l[i]:
                l1.append(sumi)
            else:
                return l[i]

        if l1 != []:
            l2.append(l1)
    print(max(list(map(lambda x: max(x), l2))))


l = [-1,-2,-3,-4]
print(compute(l))
