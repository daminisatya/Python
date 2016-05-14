MAX = 100000
triangle = [ n * (  n + 1) / 2 for n in xrange(0, MAX) ]
pentagon = [ n * (3*n - 1) / 2 for n in xrange(0, MAX) ]
hexagon  = [ n * (2*n - 1)     for n in xrange(0, MAX) ]
pentagon_dict = dict.fromkeys(pentagon, 1)
hexagon_dict  = dict.fromkeys(hexagon, 1)

for t in xrange(286, MAX):
	v = triangle[t]
	if pentagon_dict.has_key(v) and hexagon_dict.has_key(v):
		print v
		break