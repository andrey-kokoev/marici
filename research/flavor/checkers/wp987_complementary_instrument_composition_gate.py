"""WP987: exact composition gate for WP986's complementary channels."""

import json
from fractions import Fraction
from pathlib import Path


ROWS = {
    "determinant_competition": (2, 4, -1, -5),
    "quartic_vertex": (1, 0, 0, 0),
    "scalar_pole": (0, 0, 1, 0),
    "adjoint_pole": (0, 0, 0, 1),
}

GATES = (
    "source_operation",
    "weak_basis_descent",
    "threshold_transport",
    "finite_width_completion",
    "detector_response",
    "calibrated_covariance",
    "shared_provenance",
)

SUPPORT = {
    "determinant_competition": (True, True, True, False, False, False, False),
    "quartic_vertex": (True, True, False, False, False, False, False),
    "scalar_pole": (True, True, True, False, False, False, False),
    "adjoint_pole": (True, True, True, False, False, False, False),
}


def determinant(matrix):
    a = [[Fraction(value) for value in row] for row in matrix]
    sign = 1
    det = Fraction(1)
    for col in range(len(a)):
        pivot = next((r for r in range(col, len(a)) if a[r][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            sign *= -1
        p = a[col][col]
        det *= p
        for r in range(col + 1, len(a)):
            q = a[r][col] / p
            for c in range(col, len(a)):
                a[r][c] -= q * a[col][c]
            a[r][col] = 0
    value = sign * det
    return int(value) if value.denominator == 1 else value


formal_matrix = tuple(ROWS.values())
formal_det = determinant(formal_matrix)
executable = [name for name, flags in SUPPORT.items() if all(flags)]
checks = {
    "formal_determinant_is_minus_four": formal_det == -4,
    "formal_rank_is_four": formal_det != 0,
    "seven_gates_are_declared": len(GATES) == 7,
    "no_current_row_is_executable": executable == [],
    "admitted_end_to_end_rank_is_zero": len(executable) == 0,
    "wp560_is_not_the_gamma_record": not SUPPORT["quartic_vertex"][4],
    "pole_rows_lack_detector_response": not SUPPORT["scalar_pole"][4]
    and not SUPPORT["adjoint_pole"][4],
    "shared_provenance_is_absent": all(not flags[6] for flags in SUPPORT.values()),
}

result = {
    "schema": "marici.flavor.wp987-complementary-instrument-composition-gate.v1",
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "formal_determinant": formal_det,
    "formal_rank": 4,
    "executable_rows": executable,
    "admitted_end_to_end_rank": len(executable),
    "classification": "formal constructor separator; neither selector nor admitted instrument",
    "smallest_exact_falsifier": "two source directions have identical completed nuisance-profiled detector response",
    "remaining_gate": "first construct records of the WP977 mixed vertex and its own scalar and adjoint poles; then place them in one shared-provenance likelihood with uncertainty-stable rank four",
}

out = Path(__file__).parents[1] / "results" / "wp987_complementary_instrument_composition_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
