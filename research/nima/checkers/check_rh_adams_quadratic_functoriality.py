"""Exact hostile: linear agreement does not imply quadratic Green transport."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


def transpose(a):
    return [list(row) for row in zip(*a)]


def multiply(a, b):
    bt = transpose(b)
    return [[sum((Fraction(x) * Fraction(y) for x, y in zip(row, col)), Fraction(0)) for col in bt] for row in a]


def apply(a, x):
    return [sum((Fraction(v) * Fraction(w) for v, w in zip(row, x)), Fraction(0)) for row in a]


def pullback(j, g):
    return multiply(multiply(transpose(j), g), j)


# Two incidence maps agree on the audited boundary vector e1 but differ on the
# unobserved direction. Therefore their pulled-back Green forms differ.
e1 = [Fraction(1), Fraction(0)]
j_source = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
j_hostile = [[Fraction(1), Fraction(1)], [Fraction(0), Fraction(2)]]
green = [[Fraction(2), Fraction(1)], [Fraction(1), Fraction(3)]]

assert apply(j_source, e1) == apply(j_hostile, e1)
source_form = pullback(j_source, green)
hostile_form = pullback(j_hostile, green)
assert source_form != hostile_form

# Equality on all four matrix units is equivalent to equality of a 2x2
# quadratic form. Record the coefficient-level failure exactly.
matrix_units = {
    "E11": (0, 0),
    "E12": (0, 1),
    "E21": (1, 0),
    "E22": (1, 1),
}
unit_records = []
for name, (i, j) in matrix_units.items():
    equal = source_form[i][j] == hostile_form[i][j]
    unit_records.append(
        {
            "unit": name,
            "source": str(source_form[i][j]),
            "hostile": str(hostile_form[i][j]),
            "equal": equal,
        }
    )
assert not all(record["equal"] for record in unit_records)

payload = {
    "schema": "marici.research.check.v1",
    "claim": "linear boundary-vector agreement does not imply quadratic Green-form functoriality",
    "exact_arithmetic": "fractions.Fraction",
    "audited_vector_images_equal": True,
    "source_pullback": [[str(x) for x in row] for row in source_form],
    "hostile_pullback": [[str(x) for x in row] for row in hostile_form],
    "four_matrix_unit_records": unit_records,
    "quadratic_hostile_rejected": True,
    "source_block_congruence_proved": False,
    "g1_1_closed": False,
    "verdict": "the linear relative incidence is insufficient; complete block congruence remains open",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-adams-quadratic-functoriality.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
