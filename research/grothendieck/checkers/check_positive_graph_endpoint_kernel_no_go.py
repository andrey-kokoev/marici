from fractions import Fraction
from math import comb


def identity(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def multiply(a, b):
    return [
        [sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0))
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def inverse(a):
    n = len(a)
    aug = [a[i][:] + identity(n)[i] for i in range(n)]
    for col in range(n):
        pivot = next(row for row in range(col, n) if aug[row][col] != 0)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [value / scale for value in aug[col]]
        for row in range(n):
            if row != col:
                factor = aug[row][col]
                aug[row] = [
                    aug[row][j] - factor * aug[col][j]
                    for j in range(2 * n)
                ]
    return [row[n:] for row in aug]


def determinant(a):
    n = len(a)
    work = [row[:] for row in a]
    value = Fraction(1)
    for col in range(n):
        pivot = next((row for row in range(col, n) if work[row][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            value = -value
        pivot_value = work[col][col]
        value *= pivot_value
        for row in range(col + 1, n):
            factor = work[row][col] / pivot_value
            for j in range(col, n):
                work[row][j] -= factor * work[col][j]
    return value


def quadratic(h, x):
    column = [[value] for value in x]
    return multiply(multiply([x], h), column)[0][0]


def pascal(n, shift, scalar):
    return [
        [scalar * comb(i, j) * shift ** (i - j) if j <= i else Fraction(0)
         for j in range(n)]
        for i in range(n)
    ]


def main():
    checks = {}
    for n in range(2, 7):
        # Uniform measure on [0,1]: an exact positive Hilbert moment matrix.
        h = [[Fraction(1, i + j + 1) for j in range(n)] for i in range(n)]
        checks[f"hankel_positive_order_{n}"] = all(
            determinant([row[:k] for row in h[:k]]) > 0
            for k in range(1, n + 1)
        )

        a = pascal(n, Fraction(-2, 3), Fraction(3, 5))
        a_inverse = inverse(a)
        moved = multiply(multiply(transpose(a_inverse), h), a_inverse)
        checks[f"moved_graph_positive_order_{n}"] = all(
            determinant([row[:k] for row in moved[:k]]) > 0
            for k in range(1, n + 1)
        )

        # Nonzero state with zero zeroth-moment endpoint coordinate.
        x = [Fraction(0), Fraction(1)] + [Fraction(0)] * (n - 2)
        checks[f"endpoint_kernel_contains_positive_state_order_{n}"] = (
            x[0] == 0 and quadratic(h, x) > 0
        )

    for name, passed in checks.items():
        print(f"{name}: {'PASS' if passed else 'FAIL'}")
    print(f"summary: {sum(checks.values())}/{len(checks)} checks passed")
    raise SystemExit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
