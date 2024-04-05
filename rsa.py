#!/usr/bin/python3

import sys
from math import isqrt


def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def rsa_factors(n):
    """
    Find the prime factors of a number using RSA factoring algorithm.

    Args:
        n (int): The number to factorize.

    Returns:
        list: A list of prime factors of the number.
    """
    output = []

    while n % 2 == 0:
        output.append(2)
        n //= 2

    for i in range(3, isqrt(n) + 1, 2):
        while n % i == 0:
            output.append(i)
            n //= i

    if n > 2:
        output.append(n)

    return output


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    lines = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    line = int(lines[0].strip())
    factors = rsa_factors(line)

    print(f"{line}={factors[0]}*{factors[1]}")
