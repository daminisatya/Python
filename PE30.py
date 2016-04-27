def power_of_digits(n, p):
    s = 0
    while n > 0:
        d = n % 10
        n = n / 10
        s = s + pow(d, p)
    return s
print sum(n for n in xrange(2, 200000) if power_of_digits(n, 5) == n)
