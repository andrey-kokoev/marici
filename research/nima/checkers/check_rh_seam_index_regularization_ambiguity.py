import json
from fractions import Fraction
from pathlib import Path


rows = []
for n in (2, 3, 5, 10, 100):
    inside_root = 1 - Fraction(1, n)
    outside_root = 1 + Fraction(1, n)
    assert abs(inside_root) < 1
    assert abs(outside_root) > 1
    rows.append({
        "n": n,
        "inside_regularization_root": str(inside_root),
        "outside_regularization_root": str(outside_root),
        "inside_winding": 1,
        "outside_winding": 0,
        "coefficient_distance_to_boundary_symbol": str(Fraction(1, n)),
    })

half_plane_rows = []
for t in (Fraction(-2), Fraction(-1, 2), Fraction(0), Fraction(3, 2), Fraction(4)):
    epsilon = Fraction(1, 3)
    common_modulus_squared = t * t + epsilon * epsilon
    half_plane_rows.append({
        "t": str(t),
        "epsilon": str(epsilon),
        "upper_and_lower_modulus_squared": str(common_modulus_squared),
        "zeros_assigned_to_opposite_sectors": True,
    })

result = {
    "boundary_symbol": "z-1",
    "boundary_symbol_fredholm": False,
    "circle_regularizations": rows,
    "regularization_index_difference": 1,
    "half_plane_equal_modulus_samples": half_plane_rows,
    "boundary_data_choose_sector_charge": False,
    "verdict": "seam zeros require a source-derived relative index and boundary incidence",
}

output = Path(__file__).parents[1] / "results" / "rh-seam-index-regularization-ambiguity.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

