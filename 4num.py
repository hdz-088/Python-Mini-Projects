# Program to find biggest number of 4 numbers

a = int(input("Enter 1st:"))
b = int(input("Enter 2nd:"))
c = int(input("Enter 3rd:"))
d = int(input("Enter 4th:"))

if (a>b and a>c and a>d):
  print("1st number is biggest")

elif(b>c and b>d):
  print("2nd number is biggest")

elif(c>d):
  print("3rd number is biggest")

else:
  print("4th number is biggest")