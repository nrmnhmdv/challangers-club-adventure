import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    #n=int(input())
    k=2*n-2
    for i in range(n,0):   
        for j in range(k,0):
            print(end="")
       
        k=k-2
        for j in range(i+1,0):
            print("#",end="")
    
        print("\r")

if __name__ == '__main__':
    n = int(input())

    staircase(n)
