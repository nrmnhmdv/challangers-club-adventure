import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    answer = []
    alice, bob = 0, 0
    for alice_s, bob_s in zip(a, b):
        if alice_s > bob_s:
            alice += 1
        if alice_s < bob_s:
            bob += 1
    answer.append(alice)
    answer.append(bob)
    return answer

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
