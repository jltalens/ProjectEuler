"""
If the number is divisible by 20 it will be by 5 and 4, so need to check them
If it's divisble by the [11,12,...20] it will cover [2..10] as well
"""
def evenly_divisible(n):
    for i in xrange(11,20):
        if (n % i != 0): return False
    return True
"""
As the number has to be multiple of 20 I can increase it by 20
"""
def minimum_divisible():
    i = 20
    while (not evenly_divisible(i)):
        i += 20
    return i

print minimum_divisible()
