import math
phi = (1 + pow(5, 0.5)) / 2
c = math.log10(5) / 2
logphi = math.log10(phi)
n = 1
while True:
    if n * logphi - c >= 999:
        print n
        break
    n = n + 1
