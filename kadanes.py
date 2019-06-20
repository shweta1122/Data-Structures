def compute(l):
    l2 = []
    for i in range(0, len(l)):
        l1 = []
        sumi = 0

        for j in range(i, len(l)):
            sumi = sumi + l[j]
            l1.append(sumi)

        if l1 != []:
            l2.append(l1)
    print(max(list(map(lambda x: max(x), l2))))


l = [-1,-2,-3,-4]
compute(l)
