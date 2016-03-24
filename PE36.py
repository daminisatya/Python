def ispalindrome(n, base):
    digits = []
    reverse = []
    while n > 0:
        d = str(n % base)
        digits.append(d)
        reverse.insert(0, d)
        n = n / base
    return digits == reverse
print sum(n for n in xrange(1, 1000000) if ispalindrome(n, 10) and ispalindrome(n, 2))
