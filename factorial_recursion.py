"""
> Title: Program to Find Factorial of Number Using Recusrion.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 08th, 2024
> Last Update: May 08th, 2024.
"""

def factorial(num):
    """Takes 'num' as Argument and return Factorial of 'num' Using Recursion"""
    if num == 1:
        return num
    return num*factorial(num-1)

n = int(input("\nEnter Number: "))

print(f"{n}! = {factorial(n)}\n")
