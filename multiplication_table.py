"""
> Title: Program to Display the multiplication Table.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: January 31st, 2024
> Last Update: May 05th, 2024
"""

def multi_table(num):
    """Function Takes num as Argument of Which It will Make Multiplication Table Using For Loop"""
    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")

n = int(input("\nEnter Number: "))
multi_table(n)
