#!/usr/bin/env python3
"""Exact finite check of the direct-dual nilpotent exchange geometry."""


def transpose(matrix):
    return tuple(zip(*matrix))


def multiply(left, right):
    columns = transpose(right)
    return tuple(tuple(sum(a * b for a, b in zip(row, col)) for col in columns) for row in left)


def add(left, right):
    return tuple(tuple(a + b for a, b in zip(x, y)) for x, y in zip(left, right))


def zero(n):
    return tuple(tuple(0 for _ in range(n)) for _ in range(n))


def main():
    n = ((0, 1), (0, 0))
    nt = transpose(n)
    k = (
        (0, 1, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, -1, 0),
    )
    j = (
        (0, 0, 1, 0),
        (0, 0, 0, 1),
        (1, 0, 0, 0),
        (0, 1, 0, 0),
    )
    assert n != ((0, 0), (0, 0)) and nt != ((0, 0), (0, 0))
    assert multiply(k, k) == zero(4)
    assert k != zero(4)
    assert add(multiply(transpose(k), j), multiply(j, k)) == zero(4)

    # J has explicit positive and negative vectors.
    positive = (1, 0, 1, 0)
    negative = (1, 0, -1, 0)
    # Evaluate directly to avoid disguising the form in helper conventions.
    assert sum(positive[i] * sum(j[i][m] * positive[m] for m in range(4)) for i in range(4)) == 2
    assert sum(negative[i] * sum(j[i][m] * negative[m] for m in range(4)) for i in range(4)) == -2

    print("doubled_incidence=nonzero_nilpotent")
    print("exchange_skew_identity=passed")
    print("exchange_metric=indefinite")
    print("positive_skew_metric=impossible")


if __name__ == "__main__":
    main()
