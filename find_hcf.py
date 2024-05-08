"""
> Title: Program to Find Highest Common Factor(HCF).
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 08th, 2024
> Last Update: May 08th, 2024.
"""

def find_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i ==0) and (y % i == 0)):
            hcf = i
    return hcf

num1 = int(input("\nEnter Number-01: "))
num2 = int(input("Enter Number-02: "))

print(F"HCF: {find_hcf(num1, num2)}")
