""" 0/1 Knapsack Problem using Dynamic Programming - Tabulation(Bottom-Up) """


def knapsack01_dp_tabulation(profits, weights, capacity):
    if capacity <= 0 or len(profits) == 0 or len(profits) != len(weights):
        return 0

    max_profit_table = [[0 for x in range(capacity+1)] for y in range(len(profits))]

    # for 0 capacity each index has 0 profit
    for i in range(len(profits)):
        max_profit_table[i][0] = 0

    # for first index maximum profit for any capacity is either 0 or profit of first index
    # given weight of first index is less than equal to capacity
    for c in range(capacity+1):
        if weights[0] <= c:
            max_profit_table[0][c] = profits[0]

    # remaining max profit is calculated as either including or excluding the element
    # if excluded profit = max_profit_table[i-1][c]
    # if included profit = profits[i] + max_profit_table[i-1][c-w[i]]
    for i in range(1, len(profits)):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0

            if weights[i] <= c:
                profit1 = profits[i] + max_profit_table[i-1][c-weights[i]]

            profit2 = max_profit_table[i-1][c]

            max_profit_table[i][c] = max(profit1, profit2)

    print_ks_elements(max_profit_table, weights, profits, capacity)
    return max_profit_table[len(profits)-1][capacity]


def print_ks_elements(mp, weights, profits, capacity):
    print("Selected weights are: ", end='')

    totalProfit = mp[len(profits)-1][capacity]

    for i in range(len(profits)-1, 0, -1):
        if totalProfit != mp[i-1][capacity]:
            print(str(weights[i]) + " ", end='')
            totalProfit -= profits[i]
            capacity -= weights[i]

    if totalProfit != 0:
        print(str(weights[0]) + " ", end='')


print("Total knapsack profit is: ", knapsack01_dp_tabulation([1, 6, 10, 16], [1, 2, 3, 5], 7))
print("Total knapsack profit is: ", knapsack01_dp_tabulation([1, 6, 10, 16], [1, 2, 3, 5], 6))
