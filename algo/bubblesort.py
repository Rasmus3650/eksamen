import random
def bubbleSort(arr):
    n = len(arr)
    arr=arr
    counter = 0

    for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                counter += 1
    if counter == len(arr)-1:
        print(arr)
        exit
    else:
        counter = 0
        bubbleSort(arr)
        
arr = []
for _ in range(int(input())):
    arr.append(random.randint(0,1000))

bubbleSort(arr)
