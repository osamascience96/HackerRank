#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    
    # Check first step check
    if(x1+v1 == x2+v2):
        return "YES"
    
    # Applying Constraints Check
    if(v2 >= v1):
        return "NO"
    else:
        # follow the procedure
        if((x1-x2) % (v2 - v1) == 0):
            return "YES"
        else:
            return "NO"
                


if __name__ == '__main__':
    x1 = 43
    v1 = 2
    x2 = 70
    v2 = 2
    result = kangaroo(x1, v1, x2, v2)
    print(result)
