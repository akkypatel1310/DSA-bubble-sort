def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return quick_sort(left) + middle + quick_sort(right)
    
arr = [12,3,56,4,7,87]
print(quick_sort(arr))
        

Base Case: If the array has 0 or 1 element, it is already sorted.

Pivot Selection: Choose a pivot element. In this implementation, the middle element is chosen as the pivot.

Partitioning:

Left Subarray: Contains elements less than the pivot.
Middle Subarray: Contains elements equal to the pivot.
Right Subarray: Contains elements greater than the pivot.
Recursion: Recursively apply Quick Sort to the left and right subarrays.

Combining: Concatenate the sorted left subarray, the middle subarray, and the sorted right subarray to get the final sorted array.