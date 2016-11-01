import time
 
def fib_sum(n):
    fib = [1,2]
    n1,n2 = 1,2
    while n1+n2 &lt; n:
        fib.append(n1+n2)
        n1,n2 = n2,n1+n2
    return sum(fib[1::3])
 
start = time.time()
for i in range(1000000): fibsum = fib_sum(4000000)
elapsed = (time.time() - start)
 
print "result %s returned after %s seconds (1 million iterations)." % (fibsum, elapsed)
