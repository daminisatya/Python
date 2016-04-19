def gcd(a,b): return b and gcd(b, a % b) or a
def lcm(a,b): return a * b / gcd(a,b)

n = 1
for i in xrange(1, 21):
    n = lcm(n, i)
print n
