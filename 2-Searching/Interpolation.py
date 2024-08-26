def interpolation(arr, target):
    low = 0
    high = len(arr)-1
    
    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        pos = low + ((high - low) // (arr[high]- arr[low]) * (target - arr[low]))
        if arr[pos] == target:
            return pos
        
        if arr[pos]<target:
            low = pos + 1
            
        else:
            high = pos - 1
    return -1

arr = [12,34,56,78,90,9,65,44]
target = 9

index = interpolation(arr,target)
if index != -1:
    print(f'Element {target} found at index {index}')
else:
    print('Not found')







