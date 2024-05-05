"""
> Title: Program to Find Armstrong Number in a Range.
> Author: HDz(https://hdz-088.github.io/hdzala/)
> Date of Creation: May 05th, 2024
> Last Update: May 05th, 2024.
"""
def checking(upper):
    print(f"Armstrong Numbers From 1-{upper}")
    for i in range(1, upper+1):
        sum_num = 0
        num_str = str(i)
        len_num = len(num_str)
        for j in range(1, len_num+1):
            temp = int(num_str[j-1])**len_num
            sum_num = sum_num + temp
        if sum_num == i:
            print(i)

upper = int(input("Enter Number: "))
checking(upper)
