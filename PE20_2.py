import time
 
def factorial(n):
    if n == 0: return 1
    else: return n * factorial(n - 1)
 
def sum_digits(n):
    return sum([int(i) for i in str(n)])
 
start = time.time()
 
sumfac = sum_digits(factorial(100))
 
elapsed = time.time() - start
 
print("%s found in %s seconds") % (sumfac,elapsed)
