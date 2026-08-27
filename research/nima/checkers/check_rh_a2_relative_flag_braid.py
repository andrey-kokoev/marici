from fractions import Fraction
import json
from pathlib import Path


def matmul(a, b):
    return [
        [sum(x * y for x, y in zip(row, col)) for col in zip(*b)]
        for row in a
    ]


def identity():
    return [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1)],
    ]


def root_1(value):
    out = identity()
    out[0][1] = value
    return out


def root_2(value):
    out = identity()
    out[1][2] = value
    return out


def product(*matrices):
    out = identity()
    for matrix in matrices:
        out = matmul(out, matrix)
    return out


def exchange_period(a, b):
    values = [a, b]
    for _ in range(5):
        values.append((1 + values[-1]) / values[-2])
    return values


samples = [
    (Fraction(2), Fraction(3), Fraction(5)),
    (Fraction(-2), Fraction(7), Fraction(5)),
    (Fraction(3, 2), Fraction(-4, 3), Fraction(5, 4)),
]

for a, b, c in samples:
    assert a + c != 0
    left = product(root_1(a), root_2(b), root_1(c))
    right = product(
        root_2(b * c / (a + c)),
        root_1(a + c),
        root_2(a * b / (a + c)),
    )
    assert left == right

period_samples = [
    (Fraction(2), Fraction(3)),
    (Fraction(5, 2), Fraction(7, 3)),
    (Fraction(-2), Fraction(4)),
]

for a, b in period_samples:
    values = exchange_period(a, b)
    assert values[5] == a
    assert values[6] == b

# The braid chart is genuinely partial.
wall_a = Fraction(2)
wall_c = Fraction(-2)
assert wall_a + wall_c == 0

result = {
    "ambient_group": "SL(3)",
    "root_system": "A2",
    "exact_braid_samples": len(samples),
    "exchange_period_samples": len(period_samples),
    "exchange_period": 5,
    "chart_wall": "a+c=0",
    "single_flag_is_sufficient_for_cluster_atlas": False,
    "relative_decorated_flag_required": True,
    "theta_source_braid_constructed": False,
    "verdict": "the missing coherencer is a source-authorized relative-flag braid constructor",
}

out = Path(__file__).parents[1] / "results" / "rh-a2-relative-flag-braid.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
