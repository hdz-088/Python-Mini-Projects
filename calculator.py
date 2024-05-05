"""
> Title: Creating Simple Calculator Using Arithmetic Operators.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 05th, 2024
> Last Update: May 05th, 2024.
"""

# Calculation Functions
# ------------------------------
def addition(num1, num2):
    """This Function Takes num1, num2 as Arguments and adds them."""
    print(f"{num1} + {num2} = {num1 + num2}")

def subtraction(num1,num2):
    """This Function Takes num1, num2 as Arguments and substracts them."""
    print(f"{num1} - {num2} = {num1 - num2}")

def multiply(num1, num2):
    """This Function Takes num1, num2 as Arguments and multiplies them."""
    print(f"{num1} * {num2} = {num1 * num2}")

def division(num1, num2):
    """This Function Takes num1, num2 as Arguments and divides them."""
    print(f"{num1} / {num2} = {num1 / num2}")

def modulo(num1, num2):
    """This Function Takes num1, num2 as Arguments and gives modulus."""
    print(f"{num1} % {num2} = {num1 % num2}")

def power(num1, num2):
    """This Function Takes num1, num2 as Arguments and it works as num1^num2."""
    print(f"{num1} ^ {num2} = {pow(num1, num2)}")
#--------------------------------

# Initialising Function
#--------------------------------
def calculation():
    """
    This Fuction takes num1, Operator and num2 from User-Input
    and checks operator with conditional statements 
    to execut appropriate operation on the provided number.
    """
    num1 = int(input("Enter 1st Number: "))
    operator = input("Enter Operator (+,-,*,/,%,^): ")
    num2 = int(input("Enter 2nd Number: "))
    if operator == "+":
        addition(num1, num2)
    elif operator == "-":
        subtraction(num1,num2)
    elif operator == "*":
        multiply(num1,num2)
    elif operator == "/":
        division(num1,num2)
    elif operator == "%":
        modulo(num1,num2)
    elif operator == "^":
        power(num1,num2)

calculation()
