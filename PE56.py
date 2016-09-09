maxNum = 0
for a in xrange(0, 100):
    for b in xrange(0, 100):
        ds = sum(int(digit) for digit in str(a**b))
        if ds > maxNum: maxNum = ds
print maxNum
