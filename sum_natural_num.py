"""
> Title: Program to Find the Sum of Natural Numbers.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 08th, 2024
> Last Update: May 08th, 2024.
"""

def sum_natural(limit):
    """This Function takes limitas argument and then sums all naturl number upto the limit"""
    total = 0
    for i in range(1, limit+1):
        total = total + i
    print(f"Sum of Natural numbers upto {limit} is {total}\n")

a = int(input("\nEnter Limit: "))
sum_natural(a)
