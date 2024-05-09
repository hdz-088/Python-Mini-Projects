"""
> Title: Program For Array Rotation.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 08th, 2024
> Last Update: May 08th, 2024.
"""

def array_rotate(arr, d):
    """Function Returns Rotated Array For Given Position 'd'"""
    n = len(arr)
    if d<0 or d>=n:
        return "Invalid Rotation Value"
    # Rotated Array
    rotated_arr = [0]*n
    # Rotation
    for i in range(n):
        rotated_arr[i] = arr[(i+d)%n]
    return rotated_arr

arr = [1, 2, 3, 4, 5]

print(arr)
d = int(input("Enter Number of Position to Rotate: "))

print(f"\nOriginal Array: {arr}")
print(f"Rotated Array: {array_rotate(arr, d)}\n")