import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    
    max_score=scores[0]
    min_score=scores[0]
    count_of_max=0
    count_of_min=0
    for val in scores:
        if val>max_score:
            max_score=val
            count_of_max+=1
        if val<min_score:
            min_score=val
            count_of_min+=1
    
    return count_of_max,count_of_min
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
