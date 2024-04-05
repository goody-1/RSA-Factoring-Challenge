#!/usr/bin/python3
import sys
from math import floor as flr


def get_factors(n):
    output = [n, 1]

    if n % 2 == 0:
        output = [n // 2, 2]
    if n == 2:
        output = [2, 1]
    else:
        for i in range(3, flr(n**0.5) + 1):
            if n % i == 0:
                output = [n // i, i]
                break

    return output


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    return [line.strip() for line in lines]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    lines = read_file(filename)

    for line in lines:
        n = int(line)
        try:
            print(f"{line}={get_factors(n)[0]}*{get_factors(n)[1]}")
        except TypeError:
            print(f"{line} returns a type error.")
        except IndexError:
            print(f"{line} is prime.")
