from itertools import permutations
def calc(l):
    new = []
    a = list(permutations(l, 5))

    for i in a:
        new.append(list(i))
    big = eval(str(new))
    for i in range(0, len(new)):
        for j in range(0, len(a[i])):
            if new[i][j] == l[j]:
                big[i].clear()
                break
            else:
                continue
    print(big)
    count = 0
    for i in big:
        if i != []:
            count += 1

    return count
l = ['b1', 'b2', 'b3', 'b4', 'b5']
print((calc(l)))
