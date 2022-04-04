#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    
    total_apples_falls = 0;
    total_oranges_falls = 0;
    
    applies_units = []
    oranges_units = []

    for apple in apples:
        applies_units.append(apple + a)
    
    for orange in oranges:
        oranges_units.append(orange + b)
    

    for apple_distance in applies_units:
        if(apple_distance >= s and apple_distance <= t):
            total_apples_falls +=1
    
    for orange_distance in oranges_units:
        if(orange_distance >= s and orange_distance <= t):
            total_oranges_falls +=1
    
    print(total_apples_falls)
    print(total_oranges_falls)


if __name__ == '__main__':
    s = 7
    t = 11
    a = 5
    b = 15
    apples = [-2,2,1]
    oranges = [5,-6]

    countApplesAndOranges(s, t, a, b, apples, oranges)
