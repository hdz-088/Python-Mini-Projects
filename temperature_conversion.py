"""
> Title: Program to Convert Temperature from C to F or-to K and Vice-Versa
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 05th, 2024
> Last Update: May 05th, 2024.
"""

def celc_fahr():
    """Converts From Celcius To Fahrenheit"""
    celc = int(input("Enter Temperature in Celcius: "))
    fahr = (celc*(9/5))+32
    print(f"{celc} °C in Fahrenheit is {fahr} °F")

def fahr_celc():
    """Converts From Fahrenheit To Celcius"""
    fahr = int(input("Enter Temperature in Fahrenheit: "))
    celc = (fahr-32)*(5/9)
    print(f"{fahr} °F in Celcius is {celc} °C")

def celc_kelvin():
    """Converts From Celcius To Kelvin"""
    celc = int(input("Enter Temperature in Celcius: "))
    kelvin = celc + 273.15
    print(f"{celc} °C in Kelvin is {kelvin} K")

def fahr_kelvin():
    """Converts From Fahrenheit To kelvin"""
    fahr = int(input("Enter Temperature in Fahrenheit: "))
    kelvin = ((fahr-32)*(5/9)) + 273.15
    print(f"{fahr} °F in Kelvin is {kelvin} K")

def banner():
    """This Function Calls Other Functions Based on User Input"""
    print("Welcome to temperature Convertor")
    print("1 > Celcius to Fahrenheit")
    print("2 > Fahrenheit to Calcius")
    print("3 > Celcius to Kelvin")
    print("4 > Fahrenheit to Kelvin")
    choice = int(input("\nEnter Your Chooice: "))
    if choice == 1:
        celc_fahr()
    elif choice == 2:
        fahr_celc()
    elif choice == 3:
        celc_kelvin()
    elif choice == 4:
        fahr_kelvin()
    else:
        print("Invalid Input. Try Again!")

banner()
