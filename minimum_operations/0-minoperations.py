#!/usr/bin/python3

"""
Minimum Operations Algorithm: Given one letter H and an integer n, this
algorithm calculates the number of copy and paste operations it takes
to have n letters H.
"""


def minOperations(n):
    """A function that finds the prime factors
    of n and sums them in a variable called operations."""
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
