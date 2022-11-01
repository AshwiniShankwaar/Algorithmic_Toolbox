# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    if ((capacity == 0) or (len(weights)==0)):
        return 0
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    ratio = [0]*len(weights)
    for i in range(0,len(weights)):
        ratio[i] = prices[i]/weights[i]



    maxratio = getmax(ratio)
    value = 0
    if weights[maxratio]<= capacity:
        capacity = capacity-weights[maxratio]
        cost = prices[maxratio]
        weights.pop(maxratio)
        prices.pop(maxratio)
        ratio.pop(maxratio)
        value = cost+maximum_loot_value(capacity,weights,prices)
    else:
        cost = ratio[maxratio]*capacity
        weights.pop(maxratio)
        prices.pop(maxratio)
        capacity = 0
        value = cost+maximum_loot_value(capacity, weights, prices)
    return value


def getmax(ratio):
    if len(ratio) == 1:
        return 0
    max = 0
    for i in range(0,len(ratio)):
        if ratio[i]>ratio[max]:
            max = i

    return max

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    #opt_value = maximum_loot_value(50, [20, 50, 30], [60, 100, 120])
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
