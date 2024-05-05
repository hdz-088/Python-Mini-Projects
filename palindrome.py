"""Program to Check Whether Given List is Palindrome or Not."""

# Title: Program to Check Whether Given List is Palindrome or Not
# Author: HDz(https://github.com/hdz-088/)
# Date of Creation: January 31st, 2024
# Last Update: May 04th, 2024

user_list = [1, 2, 3, 2, 1]

copy_list = user_list.copy()

copy_list.reverse()

if copy_list == user_list:
    print("List is Palindrome")
else:
    print("List isn't Palindrome")
