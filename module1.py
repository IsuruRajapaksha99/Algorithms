import numpy as np



def LinearSearch(arr,n,sk):
  for i in range (0,n):
    if (arr[i]==sk):
      return i
  return -1




arr=np.random.randint(0,100,100)
print(arr)
sk=input("Enter a search key")
n=len(arr)

result=LinearSearch(arr,n,sk)
print(result)