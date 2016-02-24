maxp, maxsol = 0, 0
for p in xrange(12, 1001, 2):
    solutions = 0
    for a in xrange(1, p/3):
        a2 = a*a
        for b in xrange(a, (p-a)/2):
            c = p - a - b
            if a2 + b*b == c*c: solutions = solutions + 1
    if solutions > maxsol: maxp, maxsol = p, solutions
print maxp
