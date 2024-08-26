def binary_search(arr,left,right,target):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr,target):
    if arr[0] == target:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    return binary_search(arr, i//2,min(i,len(arr)-1),target)

arr = [1,3,5,7,9,11,14,16,17,34,45,56,67,89,123,455,567]
target = 56

index = exponential_search(arr,target)

if index != -1:
    print(f"element {target} found as {index}")
else:
    print("not found")
        
        
        
