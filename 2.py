"""
Naive aproach (using iterations)
"""
def fibonacci(number):
    a,b = 1,2
    while a < number:
        if ( a % 2 == 0 ): yield a
        a,b = b, a+b

"""
The even numbers 2, 8, 34, 144, 610 ... follow a serie as well
F(n) = 4 * F(n-1) + F(n-2)

"""
def improved_fibonacci(number):
    a,b = 2,8
    while a < number:
        yield a
        a,b = b, b*4+a

print sum(fibonacci(4000000))
print sum(improved_fibonacci(4000000))
