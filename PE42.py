def worth(word): return sum(ord(letter) - ord('A') + 1 for letter in word)

words = open('words.txt').read().replace('"', '').split(',')
triangle_numbers = dict.fromkeys(list(n*(n+1)/2 for n in xrange(1, 100)), 1)

print sum(1 for word in words if worth(word) in triangle_numbers)
