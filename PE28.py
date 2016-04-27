diagonal = 1
start = 1
for width in xrange(3, 1002, 2):
    increment = width - 1
    count = increment * 4
    diagonal = diagonal + start * 4 + increment * 10
    start = start + count

print diagonal
