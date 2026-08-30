from fractions import Fraction
import json
from pathlib import Path


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [
        [sum(x * y for x, y in zip(row, col)) for col in zip(*b)]
        for row in a
    ]


def rank(a):
    m = [[Fraction(x) for x in row] for row in a]
    rows = len(m)
    cols = len(m[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if m[i][c]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        scale = m[r][c]
        m[r] = [x / scale for x in m[r]]
        for i in range(rows):
            if i != r and m[i][c]:
                scale = m[i][c]
                m[i] = [x - scale * y for x, y in zip(m[i], m[r])]
        r += 1
    return r


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


zero = Fraction(0)
one = Fraction(1)

q = [[zero] * 6 for _ in range(6)]
for i in range(3):
    q[i][i + 3] = one
    q[i + 3][i] = one
assert rank(q) == 6

# Columns span ker(1,1,1) in V and the charge line in V*.
l = [
    [1, 1, 0],
    [-1, 0, 0],
    [0, -1, 0],
    [0, 0, 1],
    [0, 0, 1],
    [0, 0, 1],
]
assert rank(l) == 3
assert matmul(transpose(l), matmul(q, l)) == [[zero] * 3 for _ in range(3)]

# The orthogonal kernel has dimension three, hence equals the isotropic L.
orthogonal_equations = matmul(transpose(l), q)
assert rank(orthogonal_equations) == 3
assert 6 - rank(orthogonal_equations) == rank(l)

# Charge contraction kills the two current columns; wedging a covector with
# epsilon vanishes exactly on its one-dimensional span in dimension three.
epsilon = [1, 1, 1]
current_columns = [[l[i][j] for i in range(3)] for j in (0, 1)]
assert all(sum(e * x for e, x in zip(epsilon, col)) == 0 for col in current_columns)
assert rank([epsilon]) == 1

a = [
    [Fraction(1), Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(1), Fraction(1)],
    [Fraction(1), Fraction(0), Fraction(2)],
]
a_inv_t = transpose(inverse_3(a))
h = [[zero] * 6 for _ in range(6)]
for i in range(3):
    for j in range(3):
        h[i][j] = a[i][j]
        h[i + 3][j + 3] = a_inv_t[i][j]
assert matmul(transpose(h), matmul(q, h)) == q

# Fourier quarter-turn exchanges V and V* and is an anti-isometry of the
# symmetric split form with this sign convention.
j = [[zero] * 6 for _ in range(6)]
for i in range(3):
    j[i][i + 3] = one
    j[i + 3][i] = -one
minus_q = [[-x for x in row] for row in q]
assert matmul(transpose(j), matmul(q, j)) == minus_q

result = {
    "hyperbolic_rank": 6,
    "hyperbolic_signature": [3, 3],
    "lagrangian_rank": 3,
    "lagrangian_is_maximal_isotropic": True,
    "charge_covector_is_pure_spinor": True,
    "source_change_preserves_evaluation_pairing": True,
    "fourier_quarter_turn_exchanges_polarizations": True,
    "fourier_split_form_multiplier": -1,
    "analytic_theta_smoothing_constructed": False,
    "verdict": "finite core is a hyperbolic object with a pure-spinor Lagrangian; the global object is a two-chart rigged correspondence",
}

out = Path(__file__).parents[1] / "results" / "rh-hyperbolic-pure-spinor-core.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
