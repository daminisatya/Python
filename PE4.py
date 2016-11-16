import time
 
def is_palindrome1(num):
    reversed = 0
    original = num
 
    if num < 10: return True
    if num % 10 == 0: return False
 
    while num >= 1:
        reversed = (reversed * 10) + (num % 10)
        num = num/10
 
    if original == reversed: return True
    else: return False
 
def is_palindrome2(num):
    if str(num)==str(num)[::-1]: return True
    else: return False
 
start = time.time()
for i in range(1000,1000000): a = is_palindrome1(i)
elapsed = (time.time() - start)
 
print "first function took %s seconds" % elapsed
 
start = time.time()
for i in range(1000,1000000): a = is_palindrome2(i)
elapsed = (time.time() - start)
 
print "second function took %s seconds" % elapsed
