terms = {}
count = 0
for a in xrange(2,101):
    for b in xrange(2,101):
        c = pow(a,b)
        if not terms.get(c, 0):
            terms[c] = 1
            count = count + 1

print count
