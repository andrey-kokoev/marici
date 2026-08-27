import json
import math
from fractions import Fraction
from pathlib import Path


def rising(value, count):
    return math.prod(value + offset for offset in range(count))


def endpoint_record(s, g):
    affine_constant = 4 * s - 1
    minus_content = rising(2 * s, g)
    minus_pair = (
        -(2 * g + affine_constant) * minus_content,
        -(3 * g + affine_constant) * minus_content,
    )

    a_max = g + 4 * s
    c1_over_c0 = Fraction(g * (g + 2 * s), 2 * g + affine_constant)
    plus_ratio = 2 * c1_over_c0 + 1 - g
    expected_ratio = Fraction(3 * g + affine_constant, 2 * g + affine_constant)

    frame = ((2, affine_constant), (3, affine_constant))
    determinant = frame[0][0] * frame[1][1] - frame[0][1] * frame[1][0]
    harmonic_degree = 2 * s - 1
    harmonic_dimension = 2 * harmonic_degree + 1
    return {
        "s": s,
        "g": g,
        "q": 2 * g + 4 * s,
        "a_max": a_max,
        "minus_pair": list(minus_pair),
        "plus_ratio": [plus_ratio.numerator, plus_ratio.denominator],
        "expected_ratio": [expected_ratio.numerator, expected_ratio.denominator],
        "ratio_matches": plus_ratio == expected_ratio,
        "frame": [list(row) for row in frame],
        "absolute_discriminant": abs(determinant),
        "harmonic_degree": harmonic_degree,
        "harmonic_dimension": harmonic_dimension,
        "dimension_matches_discriminant": harmonic_dimension == abs(determinant),
    }


records = [endpoint_record(s, g) for s in range(1, 9) for g in range(2, 21)]
spin_two = endpoint_record(2, 3)
alternative_generalization_rejected = all(
    (4 * s - 1) != (2 * s + 3) for s in range(1, 9) if s != 2
)

gates = [
    all(item["ratio_matches"] for item in records),
    all(item["dimension_matches_discriminant"] for item in records),
    spin_two["frame"] == [[2, 7], [3, 7]],
    spin_two["harmonic_degree"] == 3,
    spin_two["harmonic_dimension"] == 7,
    alternative_generalization_rejected,
]

result = {
    "schema": "marici.strominger.general_spin_affine_discriminant_dimension.v1",
    "general_frame": "F_s=[[2,4s-1],[3,4s-1]]",
    "general_discriminant": "abs(det F_s)=4s-1",
    "representation_identity": "4s-1=dim H_(2s-1)",
    "spin_two_record": spin_two,
    "bounded_scope": {"s": [1, 8], "g": [2, 20], "cases": len(records)},
    "all_endpoint_ratios_match": all(item["ratio_matches"] for item in records),
    "all_dimensions_match": all(item["dimension_matches_discriminant"] for item in records),
    "alternative_2s_plus_3_rejected_away_from_s2": alternative_generalization_rejected,
    "physical_cyclic_charge_attachment_established": False,
    "next_missing_constructor": "representation_dimension_to_affine_cyclic_residue_morphism",
    "gates_passed": sum(gates),
    "gates_total": len(gates),
    "all_passed": all(gates),
}

output = (
    Path(__file__).parents[1]
    / "results"
    / "general_spin_affine_discriminant_dimension_checks.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(gates) else 1)
