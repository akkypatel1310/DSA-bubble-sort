def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        
        for j in range(0,n-i-1):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr

arr = [12,34,6,78,0,14,165]
print(bubble_sort(arr))
