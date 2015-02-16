"""
Using a naive approach
"""
def multiples_3_5(number):
    for x in xrange(number):
        if (x % 3 == 0 or x % 5 == 0):
            yield x
"""
Using the sum of the arithmetic series
"""
def improved_3_5(number):
    mult_of_3 = (333*1002)/2
    mult_of_5 = (199*1000)/2
    mult_of_15 = (66*1005)/2
    return mult_of_3 + mult_of_5 - mult_of_15

print sum(multiples_3_5(1000))
print improved_3_5(1000)
