
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    count_for_zero=0
    count_for_pilus=0
    count_for_minus=0
    for i in arr:
       
       if i>0:
            count_for_pilus+=1
            #print(count_for_pilus/n)
       elif i<0:
            count_for_minus+=1
            #print(count_for_minus/n)
       elif i==0:
            count_for_zero+=1
           # print(count_for_zero/n)
    print(count_for_pilus/n)
    print(count_for_minus/n)
    print(count_for_zero/n)
           


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
