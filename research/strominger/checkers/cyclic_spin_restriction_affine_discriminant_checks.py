import cmath
import json
import math
from pathlib import Path


def record(s):
    l = 2 * s - 1
    n = 2 * l + 1
    weights = list(range(-l, l + 1))
    residues = [m % n for m in weights]
    frame = ((2, n), (3, n))
    determinant = frame[0][0] * frame[1][1] - frame[0][1] * frame[1][0]

    def ell(vector):
        x, y = vector
        return (3 * x - 2 * y) % n

    columns = ((2, 3), (n, n))
    phases = [cmath.exp(2j * cmath.pi * m / n) for m in weights]
    phase_count = len({(round(z.real, 12), round(z.imag, 12)) for z in phases})
    all_smaller_collide = all(
        len({m % order for m in weights}) < n for order in range(1, n)
    )
    return {
        "s": s,
        "l": l,
        "n": n,
        "weights": weights,
        "residues": residues,
        "residues_are_complete": sorted(residues) == list(range(n)),
        "phase_count": phase_count,
        "restriction_is_regular": phase_count == n,
        "all_smaller_cyclic_orders_collide": all_smaller_collide,
        "frame": [list(row) for row in frame],
        "absolute_determinant": abs(determinant),
        "smith_factors": [1, abs(determinant)],
        "ell_on_columns": [ell(column) for column in columns],
        "ell_surjective_witness": ell((1, 1)),
        "affine_cokernel_matches_weight_quotient": (
            abs(determinant) == n
            and all(ell(column) == 0 for column in columns)
            and ell((1, 1)) == 1
        ),
    }


records = [record(s) for s in range(1, 21)]
spin_two = record(2)

gates = [
    all(item["residues_are_complete"] for item in records),
    all(item["restriction_is_regular"] for item in records),
    all(item["all_smaller_cyclic_orders_collide"] for item in records),
    all(item["smith_factors"] == [1, item["n"]] for item in records),
    all(item["affine_cokernel_matches_weight_quotient"] for item in records),
    spin_two["n"] == 7,
    spin_two["weights"] == [-3, -2, -1, 0, 1, 2, 3],
    spin_two["residues"] == [4, 5, 6, 0, 1, 2, 3],
]

result = {
    "schema": "marici.strominger.cyclic_spin_restriction_affine_discriminant.v1",
    "theorem": "H_(2s-1)|C_(4s-1) is regular and coker(F_s) is its character-label group",
    "comparison_map": "[x,y] -> 3x-2y mod (4s-1)",
    "independently_quantized_charge_lattice": "X*(SO(2))=Z",
    "bounded_scope": {"s": [1, 20], "cases": len(records)},
    "spin_two": spin_two,
    "axis_mark_required": True,
    "full_radiative_amplitudes_remain_continuous": True,
    "physical_comparison_index_seven": True,
    "executable_rotation_intervention_verified": False,
    "gates_passed": sum(gates),
    "gates_total": len(gates),
    "all_passed": all(gates),
}

output = (
    Path(__file__).parents[1]
    / "results"
    / "cyclic_spin_restriction_affine_discriminant_checks.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(gates) else 1)
