"""
> Title: Program to Find the Factorial of a Number.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: January 31st, 2024
> Last Update: May 05th, 2024
"""

def factorial(num):
    """Function Takes 'num' as Argument and Prints Factorial of 'num'"""
    if num < 0:
        print("Factirial does not exist for negative numbers\n")
    elif num == 0:
        fact = 1
        print(f"Factorial of {num} is {fact}\n")
    elif num > 0:
        fact = 1
        for i in range(1, num+1):
            fact = fact*i
        print(f"Factorial of {num} is {fact}\n")

number = int(input("\nEnter Number: "))
factorial(number)
