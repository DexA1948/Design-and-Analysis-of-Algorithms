import math


def minmaxsearch(arr, left, right):

    if left == right:
        min_ = max_ = arr[left]
    elif left == right+1:
        if arr[left]<arr[right]:
            min_, max_ = arr[left], arr[right]
        else:
            min_, max_ = arr[right], arr[left]
    else:
        mid = math.floor((left+right)/2)
        min_, max_ = minmaxsearch(arr, left, mid)
        min1_, max1_ = minmaxsearch(arr, mid+1, right)
        if min1_ < min_:
            min_ = min1_
        if max1_ > max_:
            max_ = max1_

    return min_, max_

