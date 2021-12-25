"""Merge Sort"""


def merge_sort(arr, start, end):
    if len(arr) > 1:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)
    return


def merge(arr, start, mid, end):
    #calculate number of elements on divided arrays
    nl = mid - start + 1
    nr = end - mid

    #copy the items from each section
    left_arr = []
    right_arr = []

    for i in range(nl):
        left_arr.append(arr[start+i])

    for i in range(nr):
        right_arr.append(arr[mid+1+i])

    k = start
    i = j =0

    while()