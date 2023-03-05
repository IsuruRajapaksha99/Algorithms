import numpy as np
import time

def linear_search(arr, sk):
    for i in range(len(arr)):
        if arr[i] == sk:
            return i
    return -1

# generate a random input array
arr =np.random.randint(0,100,100)
print(arr)
 

# search for a random element in the array
sk = int(input("Enter the number you need to search"))

start=(time.time()*1000)
# perform linear search

for i in range(50000):
    index = linear_search(arr, sk)
    print(f"Element {sk} found at index {index}")
end=(time.time()*1000)

print (end-start)