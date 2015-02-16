def is_palindrome(n):
    decomp = [x for x in str(n)]
    first,last = 0, len(decomp)-1
    while (first < last):
        if (decomp[first] != decomp[last]):
            return False
        first += 1
        last -= 1
    return True

def largest_palindrome(x,y):
    for i in xrange(x,-1, -1):
        for j in xrange(y,-1,-1):
            num = i*j
            if (is_palindrome(num)): return num

print largest_palindrome(999,999)
