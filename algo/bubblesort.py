import random
import numpy as np

arr = np.random.randint(1, 1000, size=int(input()))

def bubbleSort(arr):
    n = len(arr)
    arr=arr
    counter = 0

    while True:
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                counter += 1
        if counter == len(arr)-1:
            return arr
        else:
            counter = 0

print(bubbleSort(arr))
