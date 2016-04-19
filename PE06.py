r = xrange(1, 101)
a = sum(r)
print a * a - sum(i*i for i in r)
