"""Program to find biggest number of 4 numbers Insertd by User."""

# Title: Program to find biggest number of 4 numbers
# Author: HDz(https://github.com/hdz-088/)
# Date of Creation: January 31st, 2024
# Last Update: May 04th, 2024

num1 = int(input("Enter 1st:"))
num2 = int(input("Enter 2nd:"))
num3 = int(input("Enter 3rd:"))
num4 = int(input("Enter 4th:"))

if (num1>num2 and num1>num3 and num1>num4):
    print("1st number is biggest")
elif num2>num3 and num2>num4:
    print("2nd number is biggest")
elif num3>num4:
    print("3rd number is biggest")
else:
    print("4th number is biggest")
