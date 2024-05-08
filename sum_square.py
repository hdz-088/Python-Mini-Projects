"""
> Title: Program to Calculate Square Sum of n Natural Numbers.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 08th, 2024
> Last Update: May 08th, 2024.
"""

def cube_sum(n):
    """Function Takes limit as input and returns Square Sum upto limit"""
    total = 0
    if n <= 0:
        return 0
    for i in range(1, n+1):
        total += i**2
    return total

num = int(input("\nEnter Limit: "))

print(f"The Square sum of First {num} Number: {cube_sum(num)}\n")
