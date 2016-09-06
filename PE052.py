def multiples_have_same_digits(n):
    digit_keys = dict.fromkeys(list(str(n)))
    for x in xrange(2, 4):
        for d in list(str(x * n)):
            if not digit_keys.has_key(d): return False
        return True

 n = 0
 while True:
     n = n + 9                
     if multiples_have_same_digits(n):
         print n
         break
