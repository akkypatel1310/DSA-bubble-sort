def selection_sort_try(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i],arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [1,23,43,4,67,43,2]
print(selection_sort_try(arr))