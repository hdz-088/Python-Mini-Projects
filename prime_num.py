"""
> Title: Program To Check For Prime Number.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 05th, 2024
> Last Update: May 05th, 2024.
"""

def check(num):
    """This Function takes num as argument and checks whether num is Prime or Not"""
    flag = True
    if num == 1:
        print(f"{num} is NOT a Prime Number")
    elif num > 1:
        for i in range(2, num):
            if num%i == 0:
                flag = False
                break
        if flag:
            print(f"{num} is a Prime Number\n")
        else:
            print(f"{num} is NOT a Prime Number\n")

number = int(input("\nEnter Number: "))
check(number)
