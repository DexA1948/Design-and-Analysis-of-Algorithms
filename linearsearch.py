""" Linear Search """


def search(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1


arr = [11, 123, 456, 10, 223, 123]
x = 10

result = search(arr, len(arr), x)

if result == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", result)
