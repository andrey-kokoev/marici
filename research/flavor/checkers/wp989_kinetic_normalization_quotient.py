"""WP989: exact kinetic-normalization quotient of the WP986 lift packet."""

import json
from fractions import Fraction as F
from pathlib import Path


r0 = (F(2), F(4), F(-1), F(-5))
r1 = (F(0), F(2), F(0), F(-1))
n_s = (F(-1, 2), F(0), F(-1), F(0))
n_A = (F(-3, 2), F(-1, 2), F(0), F(-1))
coordinate_rows = {
    "e_Gamma": (F(1), F(0), F(0), F(0)),
    "e_B": (F(0), F(0), F(1), F(0)),
    "e_C": (F(0), F(0), F(0), F(1)),
}


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def rank(rows):
    a = [list(row) for row in rows]
    pivots = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(pivots, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivots], a[pivot] = a[pivot], a[pivots]
        p = a[pivots][col]
        a[pivots] = [x / p for x in a[pivots]]
        for i in range(len(a)):
            if i != pivots and a[i][col]:
                q = a[i][col]
                a[i] = [x - q * y for x, y in zip(a[i], a[pivots])]
        pivots += 1
        if pivots == len(a):
            break
    return pivots


checks = {
    "normalization_orbit_rank_two": rank((n_s, n_A)) == 2,
    "physical_quotient_dimension_two": 4 - rank((n_s, n_A)) == 2,
    "determinant_response_descends": dot(r0, n_s) == dot(r0, n_A) == 0,
    "second_ratio_descends": dot(r1, n_s) == dot(r1, n_A) == 0,
    "two_invariant_rows_are_independent": rank((r0, r1)) == 2,
    "wp986_coordinate_rows_fail_descent": all(
        dot(row, n_s) != 0 or dot(row, n_A) != 0
        for row in coordinate_rows.values()
    ),
    "one_complementary_invariant_is_minimal": rank((r0,)) == 1
    and rank((r0, r1)) == 2,
}

result = {
    "schema": "marici.flavor.wp989-kinetic-normalization-quotient.v1",
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "normalization_generators": {
        "scalar": [str(x) for x in n_s],
        "adjoint": [str(x) for x in n_A],
    },
    "labelled_dimension": 4,
    "normalization_orbit_dimension": 2,
    "physical_quotient_dimension": 2,
    "invariant_rows": {
        "determinant_response": [str(x) for x in r0],
        "complementary_ratio": [str(x) for x in r1],
    },
    "minimal_additional_invariant_channels": 1,
    "classification": "faithful quotient correction; neither selector nor rigidifier",
    "smallest_exact_falsifier": "a source-authorized kinetic term that makes either normalization generator physically observable",
    "remaining_instrument_gate": "a calibrated weak-basis-invariant response to A^2/C or another independent annihilator row",
}

out = Path(__file__).parents[1] / "results" / "wp989_kinetic_normalization_quotient.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
