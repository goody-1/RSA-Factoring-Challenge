#!/usr/bin/python3
import sys
from math import floor as flr


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, flr(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def rsa_factors(n):
    output = []

    for i in range(2, flr(n**0.5) + 1):
        if n % i == 0:
            output = [n // i, i]
            break

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

    print(f"{line}={rsa_factors(line)[0]}*{rsa_factors(line)[1]}")
