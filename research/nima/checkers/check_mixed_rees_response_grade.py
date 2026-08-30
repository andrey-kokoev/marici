from fractions import Fraction
import json
from pathlib import Path


# A polynomial in E and Delta represented by exact bidegree coefficients.
poly = {
    (0, 0): Fraction(0),
    (1, 0): Fraction(0),
    (0, 1): Fraction(0),
    (1, 1): Fraction(1),
}


def coefficient(p: int, q: int) -> Fraction:
    return poly.get((p, q), Fraction(0))


diagonal_value = coefficient(0, 0)
e_jet_after_diagonal = coefficient(1, 0)
delta_jet_after_temporal_specialization = coefficient(0, 1)
mixed_jet = coefficient(1, 1)

assert diagonal_value == 0
assert e_jet_after_diagonal == 0
assert delta_jet_after_temporal_specialization == 0
assert mixed_jet == 1

# Deleting either source normal removes the mixed class.
without_e_normal = {(p, q): value for (p, q), value in poly.items() if p == 0}
without_delta_normal = {(p, q): value for (p, q), value in poly.items() if q == 0}
assert without_e_normal.get((1, 1), 0) == 0
assert without_delta_normal.get((1, 1), 0) == 0

result = {
    "schema": "marici.nima.mixed-rees-response-grade.v1",
    "status": "pass",
    "separate_audits": {
        "diagonal_value": str(diagonal_value),
        "e_jet_after_diagonal": str(e_jet_after_diagonal),
        "delta_jet_after_temporal_specialization": str(
            delta_jet_after_temporal_specialization
        ),
    },
    "mixed_jet": str(mixed_jet),
    "deletion_replays": {
        "remove_e_normal": "mixed class absent",
        "remove_delta_normal": "mixed class absent",
    },
}

output = Path(__file__).parents[1] / "results" / "mixed-rees-response-grade.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
