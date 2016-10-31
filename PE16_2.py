import time
 
def pow2sum(exp):
    pow = list(str(2**1000))
    return sum([int(i) for i in pow])
 
start = time.time()
n = pow2sum(1000)
elapsed = (time.time() - start)
print "%s found in %s seconds" % (n,elapsed)
