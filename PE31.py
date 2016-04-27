coins = (1, 2, 5, 10, 20, 50, 100, 200)

def balance(pattern): return sum(coins[x]*pattern[x] for x in xrange(0, len(pattern)))

def gen(pattern, coinnum, num):
coin = coins[coinnum]
    for p in xrange(0, num/coin + 1):
        newpat = pattern[:coinnum] + (p,)
        bal = balance(newpat)
        if bal > num: return
        elif bal == num: yield newpat
        elif coinnum < len(coins)-1:
            for pat in gen(newpat, coinnum+1, num):
                yield pat

print sum(1 for pat in gen((), 0, 200))
