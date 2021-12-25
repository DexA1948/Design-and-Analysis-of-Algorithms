""" Matrix Chain Multiplication Using Dynamic Programming - Memoization """
import sys


# mcm = matrix chain multiplication
# d is list of dimensions of matrix to be multiplied
def solve_mcm(d, start, end):
    memoize = [[-1 for x in range(len(d))] for y in range(len(d))]

    for x in range(len(d)):
        memoize[x][x] = 0

    return mcm_memoization(memoize, d, start, end)


def mcm_memoization(memoize, d, start, end):
    if start == end:
        return 0

    if memoize[start][end] >= 0:
        return memoize[start][end]

    # init minimum as largest possible value
    _min = sys.maxsize

    # shift parenthesis from start index to last
    for k in range(start, end):
        # calculate cost of each position for parenthesis
        cost = mcm_memoization(memoize, d, start, k) + mcm_memoization(memoize, d, k+1, end) + d[start-1] * d[k] * d[end]

        # store minimum found from each value of k i.e:position of parenthesis
        if cost < _min:
            _min = cost

    memoize[start][end] = _min

    return memoize[start][end]


dimensions = [1, 2, 3, 4, 3]
print(f"The lowest number of multiplications for given array of matrices is: {solve_mcm(dimensions, 1, len(dimensions)-1)}")

