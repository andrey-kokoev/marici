import json
import math
from pathlib import Path


F = ((2, 7), (3, 7))
det_f = F[0][0] * F[1][1] - F[0][1] * F[1][0]


def v(g):
    return (2 * g + 7, 3 * g + 7)


def fixed_grade_smith_nonzero(g):
    x, y = v(g)
    return math.gcd(x, y)


physical_grade = 3
bounded = [
    {
        "g": g,
        "v_g": list(v(g)),
        "fixed_grade_nonzero_smith_factor": fixed_grade_smith_nonzero(g),
        "has_seven_factor": fixed_grade_smith_nonzero(g) % 7 == 0,
    }
    for g in range(2, 43)
]

seven_locus_correct = all(
    item["has_seven_factor"] == (item["g"] % 7 == 0) for item in bounded
)
even_seven_locus = [
    item["g"] for item in bounded if item["g"] % 2 == 0 and item["has_seven_factor"]
]

gates = [
    abs(det_f) == 7,
    v(physical_grade) == (13, 16),
    fixed_grade_smith_nonzero(physical_grade) == 1,
    seven_locus_correct,
    even_seven_locus == [14, 28, 42],
]

result = {
    "schema": "marici.strominger.cross_grade_affine_vs_fixed_charge.v1",
    "affine_frame": [list(row) for row in F],
    "affine_cross_grade_discriminant": abs(det_f),
    "affine_domain_axes": ["symbolic_grade", "constant_offset"],
    "physical_grade": physical_grade,
    "physical_grade_vector": list(v(physical_grade)),
    "physical_fixed_grade_smith_factor": fixed_grade_smith_nonzero(physical_grade),
    "physical_fixed_grade_has_index_seven": False,
    "bounded_fixed_grade_audit": bounded,
    "even_grade_seven_locus": even_seven_locus,
    "grade_changing_physical_constructor_established": False,
    "failure_code": "cross_grade_parameter_lattice_mistyped_as_fixed_grade_charge_lattice",
    "gates_passed": sum(gates),
    "gates_total": len(gates),
    "all_passed": all(gates),
}

output = (
    Path(__file__).parents[1]
    / "results"
    / "cross_grade_affine_vs_fixed_charge_checks.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(gates) else 1)
