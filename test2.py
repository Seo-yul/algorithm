import itertools
# permutations

a = [1,2,3,4]
b = [9,8]
c = itertools.permutations((a,b),2)
for i in c:
    print(i)