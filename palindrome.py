"""
Title: Program to Check Whether Given List is Palindrome or Not
Author: HDz(https://github.com/hdz-088/)
Date of Creation: January 31st, 2024
Last Update: April 23rd, 2024
"""

list = [1, 2, 3, 2, 1]

copy_list = list.copy()

copy_list.reverse()

if (copy_list == list):
    print("List is Palindrome")
else:
    print("List isn't Palindrome")
