"""
> Title: Program to Print Fibonacci Sequenc Using Recursion.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 08th, 2024
> Last Update: May 08th, 2024.
"""

def fibonacci(num):
    """Function takes 'num' as argument and return fibonacci"""
    if num <= 1:
        return num
    return fibonacci(num-1) + fibonacci(num-2)

limit = int(input("\nEnter Number of Terms: "))

if limit < 0:
    print("Please Enter Positive Number\n")
else:
    print("Fibonacci Sequence: ")
    for i in range(limit):
        print(fibonacci(i))
    print()
