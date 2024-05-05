"""
> Title: Program to Swap Two Variables.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 05th, 2024
> Last Update: May 05th, 2024.

> There are 3 Methods in Python to Swap Two Variables

Swapping Variabels Using Tuple Unpacking Method
num1, num2 = num2, num1

Swapping Variabels Using Temp Variable
temp = num1
num1 = num2
num2 = temp

Swapping Variabels Using Arithmetic Operations
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
"""

# Taking User Input
num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))

# Printing Before Swap
print("\nBefore Swapping")
print(f"Num1 = {num1}")
print(f"Num2 = {num2}")

# Swapping Variabels Using Tuple Unpacking Method
num1, num2 = num2, num1

# Printing After Swap
print("\nAfter Swapping")
print(f"Num1 = {num1}")
print(f"Num2 = {num2}")
