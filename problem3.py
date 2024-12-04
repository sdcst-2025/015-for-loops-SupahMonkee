#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""

import os, math

n = 10

while n > 9 or n <= 0:
    try: 
        n = int(input('Enter an integer that is smaller than 10: '))
        if n < 10:
            break
        else:
            os.system('cls')
            print('Integer must be less than 10 and positive')
    except:
        os.system('cls')
        print('Number must be an integer')

for i in range(n):
    