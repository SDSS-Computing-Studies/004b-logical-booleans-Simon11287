#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer
"""


num = input("Enter a number")
num=float(num)
if num>0 or num==0:
    num=str(num)
    print( num+" is a positive integer")
elif num<0:
    num=str(num)
    print(num + " is not a positive integer")
