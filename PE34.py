fact = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)

def sum_of_digits_factorial(n):
    s = 0
    while n > 0:
        d = n % 10
        s = s + fact[d]
        n = n / 10
    return s

print sum(n for n in xrange(10, 100000) if n == sum_of_digits_factorial(n))
