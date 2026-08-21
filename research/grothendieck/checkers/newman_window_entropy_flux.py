"""Exact checks of the forced finite-window Newman entropy identity."""

from fractions import Fraction


def normalized_derivative(xs: list[Fraction], bs: list[Fraction]) -> Fraction:
    n = len(xs)
    radius = sum(x * x for x in xs)
    p = Fraction(n * (n - 1), 2)
    c = p / radius
    a = [
        sum((Fraction(1, 1) / (xs[i] - xs[j]) for j in range(n) if j != i), Fraction(0))
        for i in range(n)
    ]
    velocity = [2 * a[i] + bs[i] for i in range(n)]

    direct_delta = sum(
        2 * (velocity[i] - velocity[j]) / (xs[i] - xs[j])
        for i in range(n)
        for j in range(i + 1, n)
    )
    radius_prime = 2 * sum(xs[i] * velocity[i] for i in range(n))
    direct_normalized = direct_delta - p * radius_prime / radius

    q = [a[i] - c * xs[i] for i in range(n)]
    flux_form = 4 * sum(v * v for v in q) + 2 * sum(bs[i] * q[i] for i in range(n))
    assert direct_normalized == flux_form
    print(f"rank={n} normalized_derivative={direct_normalized} flux_form={flux_form}")
    return direct_normalized


normalized_derivative([Fraction(-2), Fraction(-1), Fraction(3)], [Fraction(1), Fraction(-2), Fraction(1)])
normalized_derivative([Fraction(-5), Fraction(-1), Fraction(2), Fraction(4)], [Fraction(2), Fraction(0), Fraction(-3), Fraction(1)])
normalized_derivative([Fraction(-7), Fraction(-3), Fraction(-1), Fraction(4), Fraction(7)], [Fraction(-2), Fraction(3), Fraction(1), Fraction(-1), Fraction(-1)])

# For any non-Hermite configuration q != 0, b = -M q reverses production
# when M > 2, while b = +M q reinforces it.
hostile_xs = [Fraction(-2), Fraction(-1), Fraction(3)]
n = len(hostile_xs)
radius = sum(x * x for x in hostile_xs)
c = Fraction(n * (n - 1), 2) / radius
a = [
    sum((Fraction(1) / (hostile_xs[i] - hostile_xs[j]) for j in range(n) if j != i), Fraction(0))
    for i in range(n)
]
q = [a[i] - c * hostile_xs[i] for i in range(n)]
negative = normalized_derivative(hostile_xs, [-3 * value for value in q])
positive = normalized_derivative(hostile_xs, [3 * value for value in q])
assert negative < 0 < positive
print("forced_window_identity=True")
print(f"hostile_derivative={negative}")
print(f"reinforcing_derivative={positive}")
print("exterior_force_can_reverse_sign=True")
