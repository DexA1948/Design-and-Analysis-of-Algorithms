""" Travelling Salesman Problem using Recursion and Backtracking - Bruteforce """


def tsp(costs, current, remaining):
    if len(remaining) == 0:
        return costs[current][0]

    print(f"Current is: {current} & Remaining is: {remaining} ")

    cost = list()

    for i in remaining:
        cost.append(costs[current][i] + tsp(costs, i, remaining-{i}))
        print(cost, end="\n\n")

    return min(cost)


cost_adj_mat = [
    [0, 10, 15, 20],
    [5, 0, 9, 10],
    [6, 13, 0, 12],
    [8, 8, 9, 0]
]

cities = {0, 1, 2, 3}

print(f"The minimum cost of travel for given travelling salesman problem is {tsp(cost_adj_mat, 0, {1, 2, 3})}")
