def get_pandigital(n):
    pandigital = ''
    for x in xrange(1, 10):
        pandigital += str(x * n)
        if len(pandigital) >= 9: break
    if len(pandigital) == 9 and sorted(dict.fromkeys(list(pandigital)).keys()) == list("123456789"): return pandigital
    else: return ''

max = 0
for n in xrange(1, 10000):
    p = get_pandigital(n)
    if p and p > max: max = p

print max
