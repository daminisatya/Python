from combinatorics import selections

code = tuple(int(c) for c in open('cipher1.txt').read().split(','))

def decrypt(code, password):
    l = len(password)
    return tuple(c ^ password[i % l] for i, c in enumerate(code))

def text(code): return ''.join(chr(c) for c in code)

n = 0
for password in selections(tuple((ord(c) for c in list('abcdefghijklmnopqrstuvwxyz'))), 3):
    c = decrypt(code, password)
    t = text(c)
    if t.find(' the ') > 0:
        print sum(c)
        break
