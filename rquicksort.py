import random


def partition(arr, start, end):
    pivot = arr[end]
    pindex = start

    for i in range(start, end):
        if arr[i] <= pivot:
            arr[pindex], arr[i] = arr[i], arr[pindex]
            pindex = pindex+1

    arr[pindex], arr[end] = arr[end], arr[pindex]
    return pindex


def rpartition(arr, start, end):
    r = random.randrange(start, end)
    arr[r], arr[end] = arr[end], arr[r]
    return partition(arr, start, end)


def quicksort(arr, start, end):
    if start >= end:
        return

    pindex = rpartition(arr, start, end)
    quicksort(arr, start, pindex-1)
    quicksort(arr, pindex+1, end)
