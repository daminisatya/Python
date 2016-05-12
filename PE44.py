MAX = 2000
pent = [ n * (3*n - 1) / 2 for n in xrange(1, 2*MAX) ]
pdic = dict.fromkeys(pent)

def main2():
    for j in xrange(0, MAX):
        for k in xrange(j+1, 2*MAX-1):
            p_j = pent[j]
            p_k = pent[k]
            p_sum = p_j + p_k
            p_diff = p_k - p_j
            if pdic.has_key(p_sum) and pdic.has_key(p_diff):
                return p_diff
print main2()
