def insertion_sort_try(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1 
        while j>=0 and arr[j]>key:
            pass
            arr[j+1] = arr[j]
            j-=1
            arr[j+1] = key
    return arr

arr = [12,32,4,5,35,65]
print(insertion_sort_try(arr))

