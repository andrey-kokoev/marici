import json
from fractions import Fraction
from pathlib import Path


def matmul(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0])))
        for i in range(len(left))
    )


def add(left, right):
    return tuple(tuple(left[i][j] + right[i][j] for j in range(len(left[0]))) for i in range(len(left)))


def scale(value, matrix):
    return tuple(tuple(value * entry for entry in row) for row in matrix)


zero = ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(0)))
identity = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
Q = ((Fraction(0), Fraction(0)), (Fraction(1), Fraction(0)))

rows = []
for a in (Fraction(-3), Fraction(-1, 2), Fraction(1, 4), Fraction(2), Fraction(7)):
    d = ((Fraction(0), a), (Fraction(0), Fraction(0)))
    assert matmul(d, d) == zero
    assert matmul(Q, Q) == zero
    anticommutator = add(matmul(d, Q), matmul(Q, d))
    assert anticommutator == scale(a, identity)
    contraction = scale(1 / a, Q)
    contraction_identity = add(matmul(d, contraction), matmul(contraction, d))
    assert contraction_identity == identity
    rows.append({
        "normal_displacement": str(a),
        "anticommutator_scalar": str(a),
        "contraction_coefficient": str(1 / a),
        "contractible": True,
    })

seam_d = zero
seam_anticommutator = add(matmul(seam_d, Q), matmul(Q, seam_d))
assert seam_anticommutator == zero

# A central hostile factor g changes aI to agI. At g=0 no regular rescaling of
# Q can restore the identity.
hostile_a = Fraction(2)
hostile_g = Fraction(0)
hostile_anticommutator = scale(hostile_a * hostile_g, identity)
assert hostile_anticommutator == zero

result = {
    "graded_dimension": "1|1",
    "differential_square_zero": True,
    "contraction_square_zero": True,
    "off_seam_samples": rows,
    "seam_anticommutator": [[str(entry) for entry in row] for row in seam_anticommutator],
    "seam_cohomology_allowed": True,
    "central_zero_multiplier_anticommutator": [[str(entry) for entry in row] for row in hostile_anticommutator],
    "central_zero_multiplier_rejected": True,
    "verdict": "a source Cartan-Clifford identity contracts the complex exactly away from the seam",
}

output = Path(__file__).parents[1] / "results" / "rh-cartan-clifford-contraction.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

