"""Program to Print simple Calender in CLI using calender library."""

# Title: Program to print Calendar
# Author: HDz(https://github.com/hdz-088/)
# Date of Creation: January 31st, 2024
# Last Update: May 04th, 2024

import calendar

yy = int(input("Enter Year: "))
mm = int(input("Enter Month: "))

print(calendar.month(yy, mm))
