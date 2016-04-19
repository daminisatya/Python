n = 0
for a in xrange(999, 100, -1):
    for b in xrange(a, 100, -1):
        x = a * b
        if x > n:
            s = str(a * b)
            if s == s[::-1]:
                n = a * b
print n
