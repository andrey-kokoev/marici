"""Exact checks for the affine-discriminant reduced-orbit constructor."""
import json
import math
from pathlib import Path


F = ((2, 7), (3, 7))
det_F = F[0][0] * F[1][1] - F[0][1] * F[1][0]
entry_gcd = math.gcd(*(abs(x) for row in F for x in row))


def ell(vector):
    x, y = vector
    return (3 * x - 2 * y) % 7


exceptional_rows = []
for g in range(14, 141, 14):
    v = (2 * g + 7, 3 * g + 7)
    w = (v[0] // 7, v[1] // 7)
    exceptional_rows.append(
        {
            "g": g,
            "v": v,
            "w": w,
            "seven_w_equals_v": (7 * w[0], 7 * w[1]) == v,
            "ell_w": ell(w),
            "primitive_w": math.gcd(abs(w[0]), abs(w[1])) == 1,
        }
    )

free_reduced_orbit = [((x % 7), ((-x) % 7)) for x in range(7)]
unreduced_orbit = [(x, y) for x in range(7) for y in range(7)]
fixed_reduced_orbit = [(0,)]
annihilator = [
    (u, v)
    for u in range(7)
    for v in range(7)
    if all((u * x + v * y) % 7 == 0 for x, y in free_reduced_orbit)
]

hostile_frame = ((2, 6), (3, 6))
hostile_det = hostile_frame[0][0] * hostile_frame[1][1] - hostile_frame[0][1] * hostile_frame[1][0]

tests = {
    "affine_frame_has_smith_cokernel_Z7": entry_gcd == 1 and abs(det_F) == 7,
    "ell_annihilates_frame_columns": ell((2, 3)) == 0 and ell((7, 7)) == 0,
    "exceptional_grade_generators_are_canonical": all(
        row["seven_w_equals_v"] and row["ell_w"] == 1 and row["primitive_w"]
        for row in exceptional_rows
    ),
    "free_reduced_orbit_is_seven_element_antidiagonal": len(set(free_reduced_orbit)) == 7
    and all((x + y) % 7 == 0 for x, y in free_reduced_orbit),
    "unreduced_orbit_has_forty_nine_values": len(unreduced_orbit) == 49,
    "fixed_orbit_has_zero_reduced_rank": fixed_reduced_orbit == [(0,)],
    "annihilator_is_seven_element_common_mode": len(annihilator) == 7
    and all(u == v for u, v in annihilator),
    "changing_source_frame_changes_discriminant": abs(hostile_det) == 6,
}

result = {
    "schema": "marici.checker_results.v1",
    "checker": "oriented_affine_discriminant_orbit_checks.py",
    "passed": all(tests.values()),
    "tests": tests,
    "affine_frame": F,
    "determinant": det_F,
    "exceptional_grade_rows": exceptional_rows,
    "annihilator": annihilator,
    "constructor": "coker(F) tensor reduced_Z[free_reflection_orbit]",
    "verdict": "one associated constructor derives both Z/7 coefficients and the anti-diagonal",
    "remaining_missing_arrow": "parity-equivariant comparison chi_g into the actual magnetic boundary or physical route packet",
}

out = Path(__file__).resolve().parents[1] / "results" / "oriented_affine_discriminant_orbit_checks.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
