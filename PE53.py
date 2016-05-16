fact_c = { 0: 1, 1: 1 }
def fact(n): return fact_c.has_key(n) and fact_c[n] or fact_c.setdefault(n, n * fact(n-1))

count = 0
for n in xrange(1, 101):
    for r in xrange(0, n):
        ncr = fact(n) / fact(r) / fact(n-r)
        if ncr > 1000000: count += 1
print count