#!/usr/bin/python3
""" Minimum Operations
    """


def minOperations(n):
    """ Minimum Operations needed to get n H characters """
    if n <= 1:
        return 0  # If n is 1 or less, no operations are needed or possible.

    operations = 0
    factor = 2  # Start checking for factors from 2

    while n > 1:
        if n % factor == 0:  # If factor is a divisor of n
            operations += factor  # We perform a Copy and factor-1 pastes
            n //= factor  # Reduce n by this factor
        else:
            factor += 1  # Move to the next possible factor

    return operations
