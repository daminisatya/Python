def worth(name): return sum(ord(letter) - ord('A') + 1 for letter in name)

names = open('names.txt').read().replace('"', '').split(',')
names.sort()

print sum((i+1) * worth(names[i]) for i in xrange(0, len(names)))
