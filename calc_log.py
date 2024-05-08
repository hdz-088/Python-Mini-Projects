"""
> Title: Program to Calculate Natural Logarithm of Number.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 08th, 2024
> Last Update: May 08th, 2024.
"""

import math

num = float(input("\nEnter Number: "))

if num <= 0:
    print("Enter Posituve Number\n")
else:
    log = math.log(num)
    print(f"The Natural Log of {num} is {log}\n")
