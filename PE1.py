import time
 
start = time.time()
 
s = sum([i for i in range(1000) if (i % 3 == 0 or i % 5 == 0)])
 
elapsed = time.time() - start
 
print "result %s returned in %s seconds" % (s,elapsed)
