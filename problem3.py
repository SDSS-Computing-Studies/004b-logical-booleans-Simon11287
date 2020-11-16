#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""

import math
a=input("Enter integer 1")
b=input("Enter integer 2")
c=input("Enter integer 3")
a=float(a)
b=float(b)
c=float(c)

if a>(b and c):
    x=math.pow(c,2)
    y=math.pow(b,2)
    z=math.pow(a,2)
elif b>(a and c):
    x=math.pow(a,2)
    y=math.pow(c,2)
    z=math.pow(b,2)
elif c>(a and b):
    x=math.pow(a,2)
    y=math.pow(b,2)
    z=math.pow(c,2)

if z==(y+x):
    z=math.pow(z,1/2)
    z=int(z)
    z=str(z)
    y=math.pow(y,1/2)
    y=int(y)
    y=str(y)
    x=math.pow(x,1/2)
    x=int(x)
    x=str(x)
    print( x +','+y+','+z +" form a Pythagorean triple")
elif z<(y+z) or z>(y+x):
    print(" do not form a Pythagorean triple")
