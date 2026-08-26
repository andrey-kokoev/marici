import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
dependency = json.loads((root / "results" / "wp468_common_dilaton_hessian.json").read_text(encoding="utf-8"))

R = sp.Matrix(
    [
        [100, 0, -100 * sp.sqrt(3)],
        [0, 4, -4 * sp.sqrt(2)],
        [-100 * sp.sqrt(3), -4 * sp.sqrt(2), 308],
    ]
)
d = sp.Matrix([sp.sqrt(3), sp.sqrt(2), 1])
norm2 = sp.simplify((d.T * d)[0])
lift = sp.simplify(2 * d * d.T)
R_lifted = sp.simplify(R + lift)

old_spectrum = R.eigenvals()
new_spectrum = R_lifted.eigenvals()
old_massive = {value: multiplicity for value, multiplicity in old_spectrum.items() if value != 0}
new_without_lift = {value: multiplicity for value, multiplicity in new_spectrum.items() if value != 2 * norm2}
projector = sp.simplify(d * d.T / norm2)

checks = {
    "wp468_dependency_passed": dependency["passed"],
    "old_hessian_annihilates_dilation": R * d == sp.zeros(3, 1),
    "dilation_norm_squared_is_six": norm2 == 6,
    "lift_is_rank_one": lift.rank() == 1,
    "lifted_pole_mass_squared_is_twelve": new_spectrum.get(12) == 1,
    "old_massive_spectrum_is_unchanged": new_without_lift == old_massive,
    "lift_projector_is_idempotent": sp.simplify(projector * projector - projector) == sp.zeros(3),
    "lift_projector_residues_are_half_third_sixth": [sp.simplify(projector[i, i]) for i in range(3)]
    == [sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 6)],
    "full_physical_nullity_is_removed": dependency["hessian_nullity"] - 1 == 11,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP469",
    "source_lift": "kappa*(Q-D*w^2)^2",
    "benchmark": {"kappa": 1, "w": 1},
    "dilation_vector": [str(value) for value in d],
    "dilation_norm_squared": str(norm2),
    "radial_hessian_update": [[str(value) for value in row] for row in lift.tolist()],
    "updated_radial_spectrum": {str(value): int(multiplicity) for value, multiplicity in new_spectrum.items()},
    "lifted_pole": {
        "mass_squared": "12",
        "diagonal_residues": [str(sp.simplify(projector[i, i])) for i in range(3)],
    },
    "updated_full_hessian_nullity": dependency["hessian_nullity"] - 1,
    "classification": "source-derived rank-one lifting of the physical dilation pole with exact preservation of orthogonal massive residues",
    "instrument": None,
    "remaining_gate": "derive mass-eigenstate vertices and all-open-channel widths before calibrated detector composition",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp469_source_radial_lift.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)

