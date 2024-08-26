def binary_search(arr,target):
    left,right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid]<target:
            left = mid + 1
        else:
            right = mid -1
    return -1
arr=[1,5,3,6,7,3,5,3]
result = binary_search(arr,6)
print(result) 
