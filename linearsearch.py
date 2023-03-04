import numpy as np

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

# perform linear search
index = linear_search(arr, sk)

print(f"Element {sk} found at index {index}")
