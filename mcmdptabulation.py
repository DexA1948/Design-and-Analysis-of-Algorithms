""" Matrix Chain Multiplication Using Dynamic Programming - Tabulation """
import sys


def mcm(d):
    cost = [[-1 for x in range(len(d))] for y in range(len(d))]

    for x in range(1, len(d)):
        cost[x][x] = 0

    print("Initial cost matrix is: ")
    for x in cost:
        print(x)

    # cost = [
    #         [-1,| -1, -1, -1, -1],
    #         ----|---------------
    #         [-1,|  0, -1, -1, -1],
    #         [-1,| -1,  0, -1, -1],
    #         [-1,| -1, -1,  0, -1],
    #         [-1,| -1, -1, -1,  0]
    # ]

    # loop to generate required fill up positions
    for x in range(1, len(d)-1):
        for y in range(1, len(d)-x):
            print(f"\nThe selected cell from cost matrix to calculate is: {y}, {y+x}")
            cost[y][y+x] = sys.maxsize

            for k in range(y, y+x):
                cost[y][y+x] = min(cost[y][y+x], cost[y][k] + cost[k+1][y+x] + d[y-1]*d[k]*d[y+x])

            print(f"Cost Matrix After Calculating 'cost[{y}][{y+x}]': ")
            for i in cost:
                print(i)

    return cost[1][len(d)-1]


dimensions = [1, 2, 3, 4, 3]
print(f"\nThe lowest number of multiplications for given array of matrices is: {mcm(dimensions)}")
