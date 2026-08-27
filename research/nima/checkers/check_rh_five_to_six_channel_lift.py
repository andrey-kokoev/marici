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


weights_five = [1, 1, 0, -2, 0]
allowed = [
    [int(weights_five[i] + weights_five[j] == 0) for j in range(5)]
    for i in range(5)
]
assert all(allowed[i][j] == 0 for i in (0, 1) for j in range(5))

zero = Fraction(0)
one = Fraction(1)
identity = [[one if i == j else zero for j in range(3)] for i in range(3)]
q_eval = [[zero] * 6 for _ in range(6)]
for i in range(3):
    q_eval[i][i + 3] = one
    q_eval[i + 3][i] = one
assert rank(q_eval) == 6

a = [
    [Fraction(2), Fraction(1), Fraction(0)],
    [Fraction(1), Fraction(1), Fraction(1)],
    [Fraction(0), Fraction(1), Fraction(3)],
]
a_inv_t = transpose(inverse_3(a))
lift = [[zero] * 6 for _ in range(6)]
for i in range(3):
    for j in range(3):
        lift[i][j] = a[i][j]
        lift[i + 3][j + 3] = a_inv_t[i][j]
assert matmul(transpose(lift), matmul(q_eval, lift)) == q_eval

result = {
    "five_channel_weights": weights_five,
    "tail_rows_forced_zero": True,
    "five_channel_nondegenerate_natural_pairing": False,
    "six_channel_carrier": "V plus V-dual",
    "six_channel_pairing_rank": rank(q_eval),
    "six_channel_signature": [3, 3],
    "rational_transfer_preserves_evaluation_pairing": True,
    "verdict": "D5 is a forgotten-type shadow; source naturality requires six channels",
}

out = Path(__file__).parents[1] / "results" / "rh-five-to-six-channel-lift.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
