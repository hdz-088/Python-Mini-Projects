"""
> Title: Program to Solve Quadratic Equation.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 05th, 2024
> Last Update: May 05th, 2024.
"""

# Standard Form of Quadratic Equation: ax^2 + bx + c = 0

import math

# Input Coefficients
a = float(input("\nEnter Coefficient a: "))
b = float(input("Enter Coefficient b: "))
c = float(input("Enter Coefficient c: "))

# Calculating Discriminant 
discriminat = b**2 - 4*a*c

# Checking if Discriminant is +ve, -ve or 0
if discriminat > 0:
    # Two Real Roots
    root1 = (-b + math.sqrt(discriminat)) / (2*a)
    root2 = (-b - math.sqrt(discriminat)) / (2*a)
    print(f"\nRoot-1 = {root1}")
    print(f"Root-2 = {root2}\n")
elif discriminat == 0:
    # One Real Root
    root = -b / (2*a)
    print(f"\nRoot = {root}\n")
else:
    # Complex Root
    real = -b/(2*a)
    imaginary = math.sqrt(abs(discriminat)) / (2*a)
    print(f"\nRoot-1 = {real} + {imaginary}i")
    print(f"Root-2 = {real} - {imaginary}i\n")
