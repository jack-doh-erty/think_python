import itertools
 
seed ='abcdefghijklmnopqrstuvwxyz'
 
com_set = itertools.combinations(seed,5)
perm_set = itertools.permutations(seed,5)

coms = 0
for i in com_set:
    coms += 1

perms = 0
for i in perm_set:
    perms += 1

print(coms, perms)