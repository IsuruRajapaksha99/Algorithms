def bucketSort(array, Nbuckets):

    #finding maximum value
    maxVal = max(array)

    #list for buckets
    buckets = [[] for _ in range(Nbuckets)]
    
    for i in array:
        bucket_index = i * Nbuckets//(maxVal+1)
        buckets[bucket_index].append(i)

    #Sorting the bucket
    for i in range(Nbuckets):
        buckets[i] = sorted(buckets[i])

    #Concatenate the sorted buckets into a single output array
    output_arr = [i for bucket in buckets for i in bucket ]

    return output_arr

arr=[20, 2, 46, 22, 19, 6, 22, 14, 5, 48, 47, 17, 39, 5, 51, 7, 2, 22] 

print(bucketSort(arr, 6))

