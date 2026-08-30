import json
from fractions import Fraction
from pathlib import Path


def matmul(left, right):
    return tuple(tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def scale(value, matrix):
    return tuple(tuple(value * entry for entry in row) for row in matrix)


identity = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
rows = []
for a, forcing in ((Fraction(-2), Fraction(3)), (Fraction(-1, 2), Fraction(-7)), (Fraction(1, 4), Fraction(5)), (Fraction(3), Fraction(11))):
    forward = ((a, forcing), (Fraction(0), Fraction(1)))
    reverse = ((Fraction(1), -forcing), (Fraction(0), a))
    qd = matmul(reverse, forward)
    dq = matmul(forward, reverse)
    assert qd == scale(a, identity)
    assert dq == scale(a, identity)
    rows.append({
        "a": str(a),
        "forcing": str(forcing),
        "QD": [[str(entry) for entry in row] for row in qd],
        "DQ": [[str(entry) for entry in row] for row in dq],
    })

mixed_a = Fraction(1)
mixed_residual = Fraction(-1)
mixed_forcing = Fraction(4)
mixed_diagonal = mixed_a + mixed_residual
mixed_forward = ((mixed_diagonal, mixed_forcing), (Fraction(0), Fraction(1)))
mixed_reverse = ((Fraction(1), -mixed_forcing), (Fraction(0), mixed_diagonal))
mixed_composite = matmul(mixed_reverse, mixed_forward)
assert mixed_composite == scale(Fraction(0), identity)

result = {
    "triangular_source_samples": rows,
    "off_diagonal_forcing_cancels_operatorially": True,
    "both_ordered_composites_checked": True,
    "mixed_diagonal_hostile": {
        "a": str(mixed_a),
        "tangential_residual": str(mixed_residual),
        "forcing": str(mixed_forcing),
        "composite_scalar": str(mixed_diagonal),
        "normal_cartan_identity_survives": False,
    },
    "verdict": "ordered tail incidence supplies nilpotence; the source reverse arrow and pure normal composite remain decisive",
}

output = Path(__file__).parents[1] / "results" / "rh-tail-incidence-cartan.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

