"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is frue.
"""

#! python3

import math
a=input("Enter a number")
a=int(a)
b=a/6
c=a/8
d=math.floor(b)
e=math.floor(c)
if b==d and c==e:
    a=str(a)
    print(a+" is not frue.")
elif b==d:
    a=str(a)
    print(a+" is frue.")
else:
    a=str(a)
    print(a+" is not frue.")
