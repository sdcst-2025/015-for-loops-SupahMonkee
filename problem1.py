#!python3
"""
###### Problem 1
Ask the user to enter in the width and height of a box.
This should be an integer value less than 10
Draw a box filled with "*" symbols that matches the
width and height.
You will need 2 nested loops to draw the contents of
1 row and the number of rows.

inputs:
int number

outputs:


example:
enter a number:4
****
****
****
****

"""
import os
l = 11
h = 11
while l > 10 and h > 10: 
    l = int(input('Enter length value: '))
    h = int(input('Enter height value: '))
    if l > 10 or h > 10:
        os.system('cls')
        print("Length and height values must be less than 10.")

for i in range(h):
    print('')
    for i in range(l):
        print("*", end='')

#done