#!/usr/bin/python3
"""Mininum Operation"""


def minOperations(n):
    """Calculates the fewest number of operation needed"""
    if n <= 1:
        return 0
    i = 2
    pus = 0
    while i <= n:
        if n % i == 0:
            pus += i
            n = n / i
        else:
            i += 1
    return pus
        