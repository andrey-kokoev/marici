import math


def hermite_coefficients(n):
    h0 = [1.0]
    if n == 0:
        return h0
    h1 = [0.0, 2.0]
    if n == 1:
        return h1
    for k in range(1, n):
        twice_t_h1 = [0.0] + [2.0 * value for value in h1]
        minus = [-2.0 * k * value for value in h0]
        size = max(len(twice_t_h1), len(minus))
        nxt = [0.0] * size
        for j in range(size):
            nxt[j] = (
                (twice_t_h1[j] if j < len(twice_t_h1) else 0.0)
                + (minus[j] if j < len(minus) else 0.0)
            )
        h0, h1 = h1, nxt
    return h1


def evaluate_polynomial(coefficients, value):
    result = 0.0
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def hermite(n, x):
    return evaluate_polynomial(
        hermite_coefficients(n), math.sqrt(2.0 * math.pi) * x
    )


def solve_3x3(matrix, rhs):
    augmented = [row[:] + [rhs[j]] for j, row in enumerate(matrix)]
    for col in range(3):
        pivot = max(range(col, 3), key=lambda row: abs(augmented[row][col]))
        augmented[col], augmented[pivot] = augmented[pivot], augmented[col]
        scale = augmented[col][col]
        for j in range(col, 4):
            augmented[col][j] /= scale
        for row in range(3):
            if row == col:
                continue
            factor = augmented[row][col]
            for j in range(col, 4):
                augmented[row][j] -= factor * augmented[col][j]
    return [augmented[j][3] for j in range(3)]


sample_points = [0.0, 1.0, 2.0]
orders = [0, 4, 8]
matrix = [[hermite(order, x) for order in orders] for x in sample_points]
rhs = [-hermite(12, x) for x in sample_points]
c0, c4, c8 = solve_3x3(matrix, rhs)


def hostile_polynomial(x):
    return (
        hermite(12, x)
        + c8 * hermite(8, x)
        + c4 * hermite(4, x)
        + c0
    )


scale = max(abs(c0), abs(c4), abs(c8), 1.0)
assert all(abs(hostile_polynomial(x)) < 1e-11 * scale for x in sample_points)
assert hostile_polynomial(1.5) < 0
assert all(hostile_polynomial(2.0 + j / 100.0) >= -1e-6 for j in range(401))


def theta_density(x):
    return (
        (4.0 * math.pi**2 * x**4 - 6.0 * math.pi * x**2)
        * math.exp(-math.pi * x**2)
    )


epsilon = 1e-12


def hostile_density(x):
    return theta_density(x) + epsilon * hostile_polynomial(x) * math.exp(
        -math.pi * x**2
    )


minimum = min(hostile_density(1.0 + j / 10000.0) for j in range(10001))
assert minimum > 0

q0 = 0.5 * math.log(2.0)
x0 = math.exp(q0)
off_seam_difference = hostile_density(x0) - theta_density(x0)
assert off_seam_difference != 0.0

print(
    {
        "status": "passed",
        "hermite_orders": [0, 4, 8, 12],
        "coefficients": [c0, c4, c8, 1.0],
        "fixed_samples": [0, 1, 2],
        "minimum_hostile_density_on_1_2_grid": minimum,
        "q0": q0,
        "off_seam_difference": off_seam_difference,
        "disposition": "finite_poisson_amplitude_action_not_canonical",
    }
)
