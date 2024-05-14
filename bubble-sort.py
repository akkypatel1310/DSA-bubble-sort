#create an array
arr = [12,24,36,3,23,43]
def bubble_sort_check(arr):
    n = len(arr)
    #create a loop to iterate for n no. of times (Count of Elements in Array)
    for i in range(n):
        for j in range(0,n-i-1):
            #compare if the j is bigger than the next value then swap them
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr)
bubble_sort_check(arr)
print(arr)