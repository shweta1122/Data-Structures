def compute(l):
    l2 = []
    for i in range(0, len(l)):
        l1 = []
        sumi = l[i]

        for j in range(i+1, len(l)):
            sumi = sumi + l[j]
            l1.append(sumi)

        if l1 != []:
            l2.append(l1)
    print(max(list(map(lambda x: max(x), l2))))


l = [-5, -1, 2, 10, -2, -3, -4, 5, 6, 3, -5]
compute(l)
