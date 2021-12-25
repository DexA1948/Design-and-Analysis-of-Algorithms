""" 0/1 Knapsack Using Recursion and Backtracking - Bruteforce """


def knapsack_recursive(profits, weights, capacity, currentIndex):
    # base cases
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + knapsack_recursive(profits, weights, capacity - weights[currentIndex],
                                                             currentIndex + 1)

    profit2 = knapsack_recursive(profits, weights, capacity, currentIndex + 1)

    return max(profit1, profit2)


print(knapsack_recursive([1, 6, 10, 16], [1, 2, 3, 5], 7, 0))
print(knapsack_recursive([1, 6, 10, 16], [1, 2, 3, 5], 6, 0))
