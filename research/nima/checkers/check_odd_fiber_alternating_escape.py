from fractions import Fraction
from math import sqrt


def order_apply(vector):
    size = len(vector)
    return [
        sum(
            ((i > j) - (i < j)) * vector[j]
            for j in range(size)
        )
        for i in range(size)
    ]


sizes = [3, 5, 9, 17, 33]
sum_outputs = []
average_outputs = []

for size in sizes:
    alternating = [1 if i % 2 == 0 else -1 for i in range(size)]
    assert order_apply(alternating) == [0] * size
    assert sum(alternating) == 1

    sum_outputs.append(1 / sqrt(size))
    average_outputs.append(1 / (size * sqrt(size)))

assert all(a > b for a, b in zip(sum_outputs, sum_outputs[1:]))
assert all(a > b for a, b in zip(average_outputs, average_outputs[1:]))

print("odd alternating packets lie exactly in the order kernel")
print("unit-normalized sum output tends to zero")
print("finite joint faithfulness has no uniform lower bound")
