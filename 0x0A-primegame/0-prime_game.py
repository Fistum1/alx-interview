#!/usr/bin/python3
""" A prime game interview question """


def get_first_prime(values):
    for i in values:
        if isPrime(i):
            return [v for v in values if v % i != 0]
    return False


def isPrime(x):
    """ It checks if number is a prime number """
    if x < 2 or x == 4:
        return False
    for i in range(2, x // 2):
        if x % i == 0:
            return False
    return True
