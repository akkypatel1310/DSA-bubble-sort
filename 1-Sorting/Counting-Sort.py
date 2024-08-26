def counting_sort(arr):
    if not arr:
        return arr
    max_value = max(arr)
    min_value = min(arr)
    
    count = [0] * (max_value-min_value + 1)
    
    for num in arr:
        count[num - min_value] += 1
        
    for i in range(1,len(count)):
        count[i] += count[i-1]
        
    output = [0] * len(arr)
    for num in reversed(arr):
        output[count[num - min_value] -1 ] = num
        count[num-min_value] -= 1
    
    for i in range(len(arr)):
        arr[i] = output[i]
        
    return arr

arr = [4,3,5,34,6,2,1]
print(counting_sort(arr))
    
