"""
> Title: Program to Print all Non Prime Numbers in a Range.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 05th, 2024
> Last Update: May 05th, 2024.
"""

def check(num):
    print(f"\nNot Prime Number from 1 to {num}")
    print("1")
    for digit in range(1, num+1):
        if digit > 1:
            for i in range(2, digit):
                if (digit % i) == 0:
                    print(digit)
                    break
    print()

upper = int(input("Enter Range: "))
check(upper)
