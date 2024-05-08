"""
> Title: Program to Find the Largest Element of Array.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 08th, 2024
> Last Update: May 08th, 2024.
"""

def largest_element(array):
    """Function Finds Largest Element of Provided Array"""
    if array == 0:
        return "Array is Empty\n"
    largest = arr[0]
    for element in arr:
        if element > largest:
            largest = element
    return largest

arr = [11, 22, 33, 99, 44, 55]

print(f"\nThe Largest Element of Array {arr} is: {largest_element(arr)}\n")
