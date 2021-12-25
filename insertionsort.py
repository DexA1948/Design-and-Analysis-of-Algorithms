"""Insertion Sort"""


def insertion_sort(arr):
    while_loop_count = 0
    for i in range(1, len(arr)):
        value = arr[i]
        hole = i
        while (value < arr[hole - 1]) & (hole > 0):
            arr[hole] = arr[hole - 1]
            hole -= 1
            while_loop_count += 1
        arr[hole] = value

    print("The sorted array is: ", arr)
    print("The total number of steps taken is:",  3 + 1 + len(arr) * 4 + while_loop_count*4 + 2)


arr = [3, 2, 1, 69, 100, 0, 123]
print("The unsorted array is: ", arr)
insertion_sort(arr)
