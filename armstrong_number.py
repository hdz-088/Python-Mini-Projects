"""
> Title: Program to Check Armstrong Number.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 05th, 2024
> Last Update: May 05th, 2024.
"""

num = int(input("Enter Number: "))

num_str = str(num)
len_num = len(num_str)

sum_power = 0

for i in range(1, len_num+1):
    temp = int(num_str[i-1])**len_num
    sum_power = sum_power + temp

if sum_power == num:
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is NOT an Armstrong Number")
