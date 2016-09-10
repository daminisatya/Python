def is_lychrel(n):
    n = str(n)
    for count in xrange(0, 50):
        n = str(int(n) + int(n[::-1]))
        if n == n[::-1]: return False
    return True

print sum(1 for n in xrange(0, 10000) if is_lychrel(n))

