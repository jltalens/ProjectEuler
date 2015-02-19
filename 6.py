"""
Just intermidiate function to produce the result
"""
def calculate_square_sums(limit):
    sumSquares,squaresSum = 0,0
    for x in xrange(1,limit+1):
        squaresSum += x
        sumSquares += (x*x)
    return [squaresSum, sumSquares]
"""
Does the actual squares_of_sum - sum_of_squares calculation
"""
def squares(limit):
    factors = calculate_square_sums(limit)
    return factors[0] * factors[0] - factors[1]
print squares(100)
