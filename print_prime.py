"""
> Title: Program to Print all Prime Numbers in a Range.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 05th, 2024
> Last Update: May 05th, 2024.
"""

def check(num):
    print(f"\nPrime Number from 1 to {num}")
    for digit in range(1, num+1):
        if digit > 1:
            for i in range(2, digit):
                if (digit % i) == 0:
                    break
            else:
                print(digit)
    print()

upper = int(input("Enter Range: "))
check(upper)
