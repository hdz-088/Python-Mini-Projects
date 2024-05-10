"""
> Title: Program to Split The Array and Add The First Part to The End.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 08th, 2024
> Last Update: May 08th, 2024.
"""

def splitting_array(arr, d):
    """Splits Array 'arr' at 'd' position and returns New Array adding First part to the end

    Args:
        arr (array): Array to be splitted
        d (int): Position at which Splitting Array

    Returns:
        array: New array having First Part at the end of Second Part 
    """
    if d <= 0 and d >= len(arr):
        return arr
    first_part = arr[:d]
    second_part = arr[d:]
    return second_part + first_part

arr = [1, 2, 3, 4, 5]
d = int(input("Enter Position To Split From: "))

print(f"Original Array: {arr}")
print(f"New Aray: {splitting_array(arr,d)}")
