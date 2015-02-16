"""
The only way I arrived to the solution is:
1) Multipling the two largest numbers with 3 digits (999*999)
2) Counting down till I find the first palindrome
3) Finding two factors (if any) less or equal than 999
"""

"""
Returns if a number is palindrome by checking 
head and tail of an array created with that number
"""
def is_palindrome(n):
    decomp = [x for x in str(n)]
    first,last = 0, len(decomp)-1
    while (first < last):
        if (decomp[first] != decomp[last]):
            return False
        first += 1
        last -= 1
    return True

"""
Finds entire divisors of a numbers. The divisors have to be
less or equal to the given arguments
"""
def find_divisors_less_than(x, lessThan):
    for i in xrange(lessThan,-1,-1):
        if (x % i == 0):
            x = x/i
            if (x > lessThan): return False
            return True
    return False

"""
Core function generate numbers backwards and check if its 
a palindrome and find the divisors (if any)
"""
def largest_palindrome(x,y):
    for num in xrange(x*y, -1, -1):
        if (is_palindrome(num) and find_divisors_less_than(num,x)):
            return num
    return False    
print largest_palindrome(999,999)
