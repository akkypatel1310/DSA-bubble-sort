import math
def jump_search(arr,target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0    
    while prev < n and arr[min(step,n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while prev < min(step,n):
        if arr[prev] == target:
            return prev
        prev += 1
    return -1
arr = [1,2,23,64,35,6,45,675,7]
target = 23
index = jump_search(arr,target)
if index != -1:
    print("index: ",index)
else:
    print("not found")