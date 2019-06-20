def alternate(l):
    l1 = []
    a = len(l)
    counter = 0
    for i in range(0, len(l)):
        if(i % 2 != 0):
            l1.append(l[counter])
            counter += 1
        else:
            l1.append(l[a-1])
            a = a-1

    return l1


l = sorted([1, 2, 3, 4, 5, 6])
print(alternate(l))
