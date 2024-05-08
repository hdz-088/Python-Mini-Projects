"""
> Title: Program to Calculate Body Mass Index.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 08th, 2024
> Last Update: May 08th, 2024.
"""

def calc_bmi(height, weight):
    """Function Calculates BMI using Height and Weight"""
    return round(weight/(height**2), 2)

def remarks(bmi):
    """BMI score Remarks"""
    if bmi <= 18.5:
        return "You are Underweight\n"
    elif 18.5 < bmi <= 24.9:
        return "Your weight is Normal\n"
    elif 25 < bmi <= 29.29:
        return "You are Overweight\n"
    else:
        return "You are Obese"

h = float(input("\nEnter Your Height(in Meter): "))
w = float(input("Enter Your Weight(in kg): "))

bmi = calc_bmi(h, w)

print(f"\nYour BMI is {bmi}, and {remarks(bmi)}")
