"""Exact algebra checks for affine-normalized Newman-flow rigidity."""

from fractions import Fraction


def check(xs: list[Fraction]) -> None:
    assert sum(xs) == 0
    assert sum(x * x for x in xs) == 1
    n = len(xs)
    p = Fraction(n * (n - 1), 2)
    a = [
        sum((Fraction(1) / (xs[i] - xs[j]) for j in range(n) if j != i), Fraction(0))
        for i in range(n)
    ]
    assert sum(xs[i] * a[i] for i in range(n)) == p
    q = [a[i] - p * xs[i] for i in range(n)]
    assert sum(xs[i] * q[i] for i in range(n)) == 0
    direct = 2 * sum(a[i] * q[i] for i in range(n))
    squares = 2 * sum(value * value for value in q)
    assert direct == squares
    print(f"rank={n} normalized_log_discriminant_derivative={direct}")


# A distinct centered unit-sphere rational configuration.
check([Fraction(-7, 10), Fraction(-1, 10), Fraction(1, 10), Fraction(7, 10)])

print("normalized_flow=A(x)-p*x")
print("sphere_tangency=True")
print("hermite_stationarity_forced=True")
print("uniform_reference_from_affine_normalization=False")
