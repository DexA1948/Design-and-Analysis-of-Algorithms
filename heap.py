# # Max-Heap data structure in Python
#
# def heapify(arr, n, i):
#     largest = i
#     l = 2 * i + 1
#     r = 2 * i + 2
#
#     if l < n and arr[l] > arr[largest]:
#         largest = l
#
#     if r < n and arr[r] > arr[largest]:
#         largest = r
#
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         if i-1 >= 0:
#             heapify(arr, n, (i-1)//2)
#
#
# def insert(array, newNum):
#     size = len(array)
#     if size == 0:
#         array.append(newNum)
#     else:
#         array.append(newNum);
#         size = len(array)
#         heapify(array, size, (size//2)-1)
#
#
# def deleteNode(array, num):
#     size = len(array)
#     i = 0
#     for i in range(0, size):
#         if num == array[i]:
#             break
#
#     array[i], array[size - 1] = array[size - 1], array[i]
#
#     array.remove(num)
#
#     for i in range((len(array) // 2) - 1, -1, -1):
#         heapify(array, len(array), i)
#
#
# arr = []
#
# insert(arr, 100)
# print("Max-Heap array: " + str(arr))
# insert(arr, 1)
# print("Max-Heap array: " + str(arr))
# insert(arr, 3)
# print("Max-Heap array: " + str(arr))
# insert(arr, 4)
# print("Max-Heap array: " + str(arr))
# insert(arr, 90)
# print("Max-Heap array: " + str(arr))
# insert(arr, 5)
# print("Max-Heap array: " + str(arr))
# insert(arr, 2)
# print("Max-Heap array: " + str(arr))
# insert(arr, 10)
# print("Max-Heap array: " + str(arr))
# insert(arr, 110)
# print("Max-Heap array: " + str(arr))
# insert(arr, 8)
# print("Max-Heap array: " + str(arr))
# insert(arr, 200)
# print("Max-Heap array: " + str(arr))
# insert(arr, 77)
# print("Max-Heap array: " + str(arr))
#
# deleteNode(arr, 4)
# print("After deleting an element: " + str(arr))

# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


# The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        print(arr)
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


# Driver code
arr = [80, 100, 500, 10, 600, 700, 55, 1, 555]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i]),
# This code is contributed by Mohit Kumra
