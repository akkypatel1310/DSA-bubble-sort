def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    
    num_bucket = len(arr)
    min_value = min(arr)
    max_value = max(arr)
    buckets = [[] for _ in range(num_bucket)]
    for num in arr:
        index = int((num - min_value)/ (max_value - min_value + 1) * num_bucket)
        buckets[index].append(num)
        
    sorted_arr = []
    for bucket in buckets:
        insertion_sort(bucket)
        sorted_arr.extend(bucket)
        
    return sorted_arr

arr = [0,3,45,64,3,66,33,1,34,52]
sorted_arr = bucket_sort(arr)
print(sorted_arr)
    
    
