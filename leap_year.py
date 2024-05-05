"""
> Title: Program to Check For Leap Year.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 05th, 2024
> Last Update: May 05th, 2024.
"""

year = int(input("Enter Year: "))

# Divided by 100 means century year (ending with 00)
# Century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year")
# Not divided by 100 means not a century year
# Year divided by 4 is a leap year
elif (year % 4 == 0) and (year % 100 != 0):
    print(f"{year} is a leap year")
# If not divided by both 400 (century year) and 4 (not century year)
# Year is not leap year
else:
    print(f"{year} is not a leap year")
