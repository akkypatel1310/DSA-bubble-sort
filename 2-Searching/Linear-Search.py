def linear_search(arr,target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

arr = [1,2,34,5,3,45,78]
target = 4
result = linear_search(arr,target)
if result != -1:
    print("Position at:",result)
else:
    print("Not Found")
