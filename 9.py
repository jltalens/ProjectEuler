import math
"""
As I have that a**2 + b**2 = c**2 I can substitute c in a + b + c = 100
and only doing two loops instead of 3 to find the numbers
"""
def pythagorean_triplet():
    for a in xrange(1,999):
        for b in xrange(1,999):
            c = math.sqrt(pow(a,2) + pow(b,2))
            res = a + b + c
            if (res == 1000 and (a < b < c)):
                return int(a*b*c)
print pythagorean_triplet()            
