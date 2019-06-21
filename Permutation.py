from itertools import permutations
s="ABC"
perm=list(map(list,permutations(s)))
print(perm)
print(" ".join(list(map(lambda x : ''.join(x), perm))))
