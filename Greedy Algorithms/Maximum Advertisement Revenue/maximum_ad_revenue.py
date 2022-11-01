# python3
import sys
from itertools import permutations


def max_dot_product_naive(first_sequence, second_sequence):
    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3
    assert all(0 <= f <= 10 ** 5 for f in first_sequence)
    assert all(0 <= s <= 10 ** 5 for s in second_sequence)

    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)
    #print(max_product)
    return max_product


def max_dot_product(first_sequence, second_sequence):
    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3
    assert all(0 <= f <= 10 ** 5 for f in first_sequence)
    assert all(0 <= s <= 10 ** 5 for s in second_sequence)
    cols = len(second_sequence)
    rows = len(first_sequence)
    # out = [[0 for i in range(cols)] for j in range(rows)]
    # for x in range(len(first_sequence)):
    #     for y in range(len(second_sequence)):
    #         out[x][y] = first_sequence[x]*second_sequence[y]
    first_sequence.sort()
    second_sequence.sort()
    j = 0
    min_size = -sys.maxsize - 1
    sum = 0
    while j<len(first_sequence):
        maxInFirst = min_size
        for i in range(len(first_sequence)):
            if first_sequence[i]>maxInFirst:
                maxInFirst = first_sequence[i]
        maxInSecond = min_size
        for i in range(len(second_sequence)):
            if second_sequence[i]>maxInSecond:
                maxInSecond = second_sequence[i]
        sum = sum+(maxInFirst*maxInSecond)
        index_f = first_sequence.index(maxInFirst)
        index_s = second_sequence.index(maxInSecond)
        first_sequence.pop(index_f)
        second_sequence.pop(index_s)
    return sum








if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
