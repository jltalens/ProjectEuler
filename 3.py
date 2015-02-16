def large_factor(a):
    b = 2
    while (b <= a/2):
        if (a % b != 0):
            b += 1
        else:
            a = a/b
            b = 2
    return a
print large_factor(600851475143)
