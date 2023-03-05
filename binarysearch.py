import numpy as np
import time

def binarySearch(arr,x):

    lowerBound = 0
    upperBound = int(len(arr)-1)

    while lowerBound <= upperBound:
        mid= int(lowerBound+upperBound)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            lowerBound = mid + 1
        else:
            upperBound = mid - 1
    return -1
    

arr = sorted(np.random.randint(0,100,100))
print(arr)

x=int(input("Enter the number to search "))

start=(time.time()*1000)

for i in range(15000):
    index=binarySearch(arr, x)
    print(f"Element {x} found at index {index}")

end=(time.time()*1000)

print (end-start)




