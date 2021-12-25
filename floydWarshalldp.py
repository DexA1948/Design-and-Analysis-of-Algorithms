""" Floyd Warshall Algorithm """
import sys


def floydWarshall(g):
    n = len(g[0])

    # shortest distance matrix
    sdm = g

    for k in range(n):
        for i in range(n):
            for j in range(n):
                sdm[i][j] = min(sdm[i][j], sdm[i][k] + sdm[k][j])

        print(f"k: {k}")
        for i in sdm:
            for j in i:
                if j == INF:
                    print("INF", end=" ")
                else:
                    print(f"  {j}", end=" ")
            print("")

    return sdm


INF = sys.maxsize

graph = [
    [INF, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

sdm = floydWarshall(graph)

print(f"The shortest distance matrix for given graph is: ")

for i in sdm:
    for j in i:
        if j == INF:
            print("INF", end=" ")
        else:
            print(f"  {j}", end=" ")
    print("")
