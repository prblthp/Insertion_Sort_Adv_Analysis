# Enter your code here. Read input from STDIN. Print output to STDOUT
# !/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort function below.


cnt = 0


def binarySearch(arr, l, r, x):
    global cnt
    while l <= r:

        mid = l + (r - l) // 2

        k = 1

        if arr[mid] == x:
            j1 = len(arr) - 1

            while mid + k <= j1 and arr[mid + k] == x:
                k += 1

            j2 = mid + k
            arr.insert(j2, x)
            cnt += i - j2
            return arr

        if arr[mid] < x:
            l = mid + 1

        else:
            r = mid - 1

    cnt += i - l
    arr.insert(l, x)
    return arr


def insertionSort(arr):
    if (len(set(arr)) == 1):
        return 0

    arr2 = []
    arr2.append(arr[0])
    global i
    for i in range(1, len(arr)):
        binarySearch(arr2, 0, len(arr2) - 1, arr[i])
    return (cnt)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    if t < 1 & t > 15:
        sys.exit()

    for t_itr in range(t):

        n = int(input())
        if n > 100000:
            sys.exit()

        arr = list(map(int, input().rstrip().split()))
        if all(i >= 1 and i <= 10000000 for i in arr) == False:
            sys.exit()
        # print(arr)
        result = insertionSort(arr)
        cnt = 0
        fptr.write(str(result) + '\n')

    fptr.close()

