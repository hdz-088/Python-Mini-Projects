"""
> Title: Finding Areas of Different Shapes.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 05th, 2024
> Last Update: May 05th, 2024.
"""

# Defining Value of PI (constant)
PI = 3.14

def area_square(side):
    """Takes Side of Square as argument and Prints Area of Square"""
    print(f"\nSide: {side}")
    print(f"Area of Square: {pow(side, 2)}\n")

def area_rectangle(height, width):
    """Takes height and width of Rectangle as argument and Prints Area of Rectangle"""
    print(f"\nHeight:  {height}")
    print(f"Width:  {width}")
    print(f"Area of Square: {height*width}\n")

def area_triangle(base, height):
    """Takes base and height of Triangle as argument and Prints Area of Triangle"""
    print(f"\nBase: {base}")
    print(f"Height: {height}")
    print(f"Area of Square: {0.5*base*height}\n")

def area_circle(radius):
    """Takes radius of Circle as argument and Prints Area of Circle"""
    print(f"\nRadius: {radius}")
    print(f"Area of Square: {PI*pow(radius, 2)}\n")

def area_ellipse(minor, major):
    """Takes minor axis & major axis of Ellipse as argument and Prints Area of Ellipse"""
    print(f"\nMinor Axis: {minor}")
    print(f"major Axis: {major}")
    print(f"Area of Square: {PI*(0.5*minor)*(0.5*major)}\n")

def finding_area():
    """
    This function prompts the user to choose a shape and calculates its area
    The user is asked to enter a number corresponding to a shape:
        1. Square
        2. Rectangle
        3. Triangle
        4. Circle
        5. Ellipse
    Depending on the chosen shape, the function prompts for additional inputs 
    and calculates the area using respective area calculation functions.
    """
    choice = int(input("\nEnter Number: "))
    if choice == 1:
        side = int(input("\nEnter Side of Square: "))
        area_square(side)
    elif choice == 2:
        height = int(input("\nEnter height of Rectangle: "))
        width = int(input("Enter width of Rectangle: "))
        area_rectangle(height, width)
    elif choice == 3:
        base = int(input("\nEnter Base of Triangle: "))
        height = int(input("Enter Height of Triangle: "))
        area_triangle(base, height)
    elif choice == 4:
        radius = int(input("\nEnter Radius of Circle: "))
        area_circle(radius)
    elif choice == 5:
        minor = int(input("\nEnter Length of Minor Axis of Ellipse: "))
        major = int(input("Enter Length of Major Axis of Ellipse: "))
        area_ellipse(minor, major)
    else:
        print("Invalid Input. Try Again!")

def banner():
    """Prints Instructions for User and Calls finding_area Function"""
    print("Find Area of Shape")
    print("01 > Square\n02 > Rectangle\n03 > Triangle\n04 > Circle\n05 > Ellipse")
    finding_area()

banner()
