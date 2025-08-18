def zero_one_knapsack(cargo):
    cargo = sorted(cargo, key=lambda x: x[0] / x[1], reverse=True)
    result = 0
    bag = 15

    for value, weight in cargo:
        if bag >= weight:
            bag -= weight
            result += value
        else:
            result += value / weight * bag
            break
    return result




cargo = [ # value, weight
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2)]
print(zero_one_knapsack(cargo))