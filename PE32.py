from combinatorics import permutations

def num(l):
    s = 0
    for n in l: s = s * 10 + n
    return s

product = {}
for perm in permutations(range(1,10)):
    for cross in range(1,4):            
        for eq in range(cross+1, 6):    
            a = num(perm[0:cross])
            b = num(perm[cross:eq])
            c = num(perm[eq:9])
            if a * b == c: product[c] = 1

print sum(p for p in product)
