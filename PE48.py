s = 0
mod = pow(10, 10)
for x in xrange(1, 1001):
	s = s + pow(x, x)

print s % mod