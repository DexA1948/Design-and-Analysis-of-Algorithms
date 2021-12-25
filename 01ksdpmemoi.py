""" 0/1 Knapsack Problem using Dynamic Programming-Memoization """


def solve_knapsack(profits, weights, capacity):
    memoize = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    return knapsack_recursive(profits, weights, capacity, 0, memoize)


def knapsack_recursive(profits, weights, capacity, currentIndex, memoize):
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    if memoize[currentIndex][capacity] != -1:
        return memoize[currentIndex][capacity]

    profits1 = 0
    if weights[currentIndex] <= capacity:
        profits1 = profits[currentIndex] + knapsack_recursive(profits, weights, capacity-weights[currentIndex],
                                                              currentIndex+1, memoize)

    profits2 = knapsack_recursive(profits, weights, capacity, currentIndex+1, memoize)

    memoize[currentIndex][capacity] = max(profits1, profits2)

    return memoize[currentIndex][capacity]


print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
