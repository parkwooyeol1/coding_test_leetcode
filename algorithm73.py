def zero_one_knapsack(cargo):
    bag = 15
    dp = [[0]*(bag + 1)for i in range(len(cargo)+1)]

    for i in range(1, len(cargo)+1):
        vaule, weight = cargo[i-1]
        for j in range(bag+1):
            if weight <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + vaule)
            else:
                dp[i][j] = dp[i-1][j]

    return dp[len(cargo)][bag]

cargo = [ # value, weight
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2)]
print(zero_one_knapsack(cargo))