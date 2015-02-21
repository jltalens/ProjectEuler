"""
Determines the primality of a number
"""
def is_prime(a):
   b = 2
   while (b <= a/2):
       if ( a % b == 0 ):
           return False
       b += 1
   return True    
"""
Generates prime numbers. On each prime we sum one to the index
"""
def prime_generator(n):
    p = 1
    prev = 2
    for x in xrange(1,n):
        prev += 1
        while (not is_prime(prev)):
            prev += 1
    return prev

print prime_generator(10001)
