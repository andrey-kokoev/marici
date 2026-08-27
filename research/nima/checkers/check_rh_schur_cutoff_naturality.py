from fractions import Fraction
import json
from pathlib import Path


def inv2(a, b, d):
    det = a * d - b * b
    return ((d / det, -b / det), (-b / det, a / det))


def quad(matrix, vector):
    return sum(vector[i] * matrix[i][j] * vector[j] for i in range(2) for j in range(2))


# The old cutoff has A=1, B=1, and C(z)=z+1, hence S_X(z)=z.
old_feedback = Fraction(1)

# The enlarged cutoff restricts to the same old A and B blocks, but the new
# internal state couples to the old one through A_Y.
A_inv = inv2(Fraction(1), Fraction(1, 2), Fraction(1))
B = (Fraction(1), Fraction(0))
new_feedback = quad(A_inv, B)

assert old_feedback == 1
assert new_feedback == Fraction(4, 3)
assert new_feedback - old_feedback == Fraction(1, 3)

result = {
    "schema": "marici.rh-schur-cutoff-naturality.v1",
    "old_blocks": {"A": "1", "B": "1", "C": "z+1", "S": "z"},
    "new_blocks": {
        "A": "[[1,1/2],[1/2,1]]",
        "B": "[1,0]",
        "C": "z+1",
        "S": "z-1/3",
    },
    "block_restriction_holds": True,
    "schur_naturality_holds": False,
    "relative_feedback_increment": "1/3",
    "required_extra_datum": "source_derived_relative_schur_connection",
    "finite_falsifier": "old zero z=0 moves to z=1/3",
}

out = Path(__file__).parents[1] / "results" / "rh-schur-cutoff-naturality.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
