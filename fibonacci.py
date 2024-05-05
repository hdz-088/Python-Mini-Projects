"""
> Title: Program to Print the Fibonacci sequence Upto Num Terms.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: January 31st, 2024
> Last Update: May 05th, 2024
"""

def fibonacci(num):
    """Prints Fibonacci Sequence Upto 'num' Terms"""
    count = 0
    n1 = 0
    n2 = 1
    if num <= 0:
        print("Enter Positive Integer")
    elif num == 1:
        print("Fibonacci sequence for 1:")
        print(n1)
    elif num > 1:
        print(f"Fibonacci sequence upto {num}: ")
        while count < num:
            print(n1)
            n3 = n1 + n2
            n1, n2 = n2, n3
            count += 1

num = int(input("Enter Number: "))
fibonacci(num)
