from fractions import Fraction
import json
from pathlib import Path


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    nrows = len(a)
    ncols = len(a[0])
    r = 0
    for c in range(ncols):
        pivot = next((i for i in range(r, nrows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        scale = a[r][c]
        a[r] = [x / scale for x in a[r]]
        for i in range(nrows):
            if i != r and a[i][c]:
                scale = a[i][c]
                a[i] = [x - scale * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [
        [sum(x * y for x, y in zip(row, col)) for col in zip(*b)]
        for row in a
    ]


def inverse_3(a):
    aug = [
        [Fraction(x) for x in row]
        + [Fraction(int(i == j)) for j in range(3)]
        for i, row in enumerate(a)
    ]
    for col in range(3):
        pivot = next(i for i in range(col, 3) if aug[i][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for i in range(3):
            if i != col:
                scale = aug[i][col]
                aug[i] = [x - scale * y for x, y in zip(aug[i], aug[col])]
    return [row[3:] for row in aug]


# Coordinates are (m, a, b).
d_log_mass = [1, 0, 0]
d_log_width_phi = [0, 2, 0]
d_log_width_psi = [0, 0, 2]
d_log_interference = [0, 1, 1]
d_log_matching = [-2, 1, 1]
d_relative_sign = [0, 0, 0]

base = [d_log_mass, d_log_width_phi, d_log_width_psi]
assert rank(base) == 3
assert rank(base + [d_log_interference]) == 3
assert rank(base + [d_log_matching]) == 3
assert [2 * x for x in d_log_interference] == [
    x + y for x, y in zip(d_log_width_phi, d_log_width_psi)
]
assert d_log_matching == [
    -2 * x + y + z
    for x, y, z in zip(d_log_mass, [0, 1, 0], [0, 0, 1])
]
assert rank([d_relative_sign]) == 0

zero = Fraction(0)
one = Fraction(1)
q_eval = [[zero] * 6 for _ in range(6)]
for i in range(3):
    q_eval[i][i + 3] = one
    q_eval[i + 3][i] = one

t = [
    [Fraction(1), Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(1), Fraction(1)],
    [Fraction(1), Fraction(0), Fraction(2)],
]
t_inv_t = transpose(inverse_3(t))
lift = [[zero] * 6 for _ in range(6)]
for i in range(3):
    for j in range(3):
        lift[i][j] = t[i][j]
        lift[i + 3][j + 3] = t_inv_t[i][j]
assert matmul(transpose(lift), matmul(q_eval, lift)) == q_eval

result = {
    "continuous_constructor_dimension": 3,
    "hyperbolic_double_dimension": 6,
    "basic_response_rank": 3,
    "rank_after_interference_magnitude": 3,
    "rank_after_matching_coefficient": 3,
    "relative_sign_differential_rank": 0,
    "relative_sign_type": "C2 orientation local system",
    "hyperbolic_pairing_preserved": True,
    "verdict": "Flavor contains a rank-six cotangent double plus a separately typed discrete orientation sheet",
}

out = Path(__file__).parents[1] / "results" / "flavor-hyperbolic-double-and-sign-local-system.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
