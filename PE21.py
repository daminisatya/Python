def divisors(n): return list(i for i in xrange(1, n/2+1) if n % i == 0)
pair = dict( ((n, sum(divisors(n))) for n in xrange(1, 10000)) )
print sum(n for n in xrange(1, 10000) if pair.get(pair[n], 0) == n and pair[n] != n)
