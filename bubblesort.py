array = [28, 4, 53, 1, 0, 45, 8, 32]
print(f"This is the unsorted array:  {array}")
length = array.__len__()


def bubblesort(arr, length):
    if length == 1:
        return "Array is of length one so its already sorted."
    else:
        for i in range(length - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        bubblesort(arr, length - 1)

    return arr


print(f"The sorted array is: {bubblesort(array, length)}")


"""Bubble Sort - Iterative"""
array = [28, 4, 53, 1, 0, 45, 8, 32]
print(f"This is the unsorted array:  {array}")


def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


bubble_sort(array)
print(f"The sorted array is: {array}")
