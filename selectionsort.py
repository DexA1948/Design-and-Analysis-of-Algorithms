"""Selection Sort"""


def selection_sort(arr):
    step_count = 0
    for i in range(len(arr)-1):
        step_count += 1
        small = i
        for j in range(i+1, len(arr)):
            step_count += 1
            if arr[small] > arr[j]:
                small = j
        arr[i], arr[small] = arr[small], arr[i]
    print("The step count for loop is: ", step_count)


arr = [63, 57, 44, 61, 13, 27]
print("The unsorted array is: ", arr)
selection_sort(arr)
print("The sorted array is: ", arr)
