
def selectionSort(array, size):
    
    for x in range(size):
       min_index=x
       
       for j in range(x+1, size):

            if array[j] < array[min_index]:
                min_index=j
                
       (array[x], array[min_index]) = (array[min_index], array[x])

arr = [20, 2, 46, 22, 19, 6, 22, 14, 5, 48, 47, 17, 39, 5, 51, 7, 2, 22] 
size=len(arr)
selectionSort(arr, size)
print(arr)