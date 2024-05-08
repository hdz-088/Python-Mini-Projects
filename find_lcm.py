"""
> Title: Program to Find Least Common multiple (LCM).
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 08th, 2024
> Last Update: May 08th, 2024.
"""

def find_lcm(x, y):
    """Function Takes 2 numbers as Arguments and Finds LCM for them."""
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

num1 = int(input("\nEnter Number-01: "))
num2 = int(input("Enter Number-02: "))

print(f"LCM: {find_lcm(num1, num2)}\n")
