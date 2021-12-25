""" Matrix Chain Multiplication Using Recursion and Backtracking - Bruteforce """
import sys


# mcm = matrix chain multiplication
# d is list of dimensions of matrix to be multiplied
def mcm(d, start, end):
    if start == end:
        return 0

    # init minimum as largest possible value
    min_ = sys.maxsize

    # shift parenthesis from start index to last
    for k in range(start, end):
        # calculate cost of each position for parenthesis
        cost = mcm(d, start, k) + mcm(d, k+1, end) + d[start-1] * d[k] * d[end]

        # store minimum found from each value of k i.e:position of parenthesis
        if cost < min_:
            min_ = cost

    return min_


dimensions = [1, 2, 3, 4, 3]
print(f"The lowest number of multiplications for given array of matrices is: {mcm(dimensions, 1, len(dimensions)-1)}")

