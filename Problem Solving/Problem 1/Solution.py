#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    
    #frist element is always the number of students
    numStd = grades[0];

    resultGrades = []

    for i in range(1, (numStd + 1)):
        originalGrade = grades[i]

        NextMult = int(math.floor(originalGrade/5) * 5) + 5
        Difference = NextMult - originalGrade

        if (Difference < 3 and NextMult >= 40):
            resultGrades.append(NextMult)
        else:
            resultGrades.append(grades[i])
    
    return resultGrades

if __name__ == '__main__':

    grades = [4,73,67,38,33]

    result = gradingStudents(grades)

    print(result);
