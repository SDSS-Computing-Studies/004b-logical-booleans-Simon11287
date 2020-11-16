#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and a perfect cube.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.
"""
import math
a=input("Enter a number")
a=float(a)
b=math.pow(a,1/3)
b=round(b)
c=math.pow(b,3)
d=math.pow(a,1/2)
d=round(d)
e=math.pow(d,2)
if c==a and e==a:
    a=str(a)
    print(a+" is both a perfect square and a perfect cube.")
elif e==a:
    a=str(a)
    print(a+" is only a perfect square.")
elif c==a:
    a=str(a)
    print(a+" is only a perfect cube.")
