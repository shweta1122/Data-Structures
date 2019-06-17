from itertools import permutations
l = [1, 5, 3, 2]
perm = permutations(l, 2)
perm = list(map(sorted, perm))
perm = list(map(str, perm))
perm.sort()
perm = list(map(eval, perm))
perm = perm[::2]
print(len(list(filter(lambda x: sum(x) in l, perm))))
