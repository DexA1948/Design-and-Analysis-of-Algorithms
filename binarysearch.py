def binarysearch(arr3, left, right, key):
    if left <= right:
        mid = int((left+right)/2)
        if arr3[mid] == key:
            return mid
        elif arr3[mid]>key:
            return binarysearch(arr3, left, mid-1, key)
        else:
            return binarysearch(arr3, mid+1, right, key)


""" Iterative Binary Search """
""" Binary Search """


def binary_search(arr, x):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == x: return mid

        if arr[mid] > x: end = mid - 1
        else:
            start = mid + 1

    return -1


arr = [12, 13, 15, 17, 19, 21, 23]
x = 17

result = binary_search(arr, x)

if result == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", result)
