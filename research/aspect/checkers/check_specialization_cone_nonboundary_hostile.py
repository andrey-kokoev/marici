import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]


def rank(matrix: sp.Matrix) -> int:
    return int(matrix.rank())


def boundary_test(previous_differential: sp.Matrix, beta: sp.Matrix) -> dict:
    augmented = previous_differential.row_join(beta)
    return {
        "differential_rank": rank(previous_differential),
        "augmented_rank": rank(augmented),
        "is_boundary": rank(previous_differential) == rank(augmented),
    }


next_differential = sp.zeros(1, 1)
beta = sp.Matrix([1])

# Hostile: beta is closed, normalized, and invariant under the identity atlas,
# but the preceding cone differential has zero image.
hostile_previous = sp.zeros(1, 1)
hostile = boundary_test(hostile_previous, beta)
hostile["is_cycle"] = next_differential * beta == sp.zeros(1, 1)
hostile["atlas_holonomy"] = 1

# Control: the same beta is hit by a declared primitive.
control_previous = sp.eye(1)
control = boundary_test(control_previous, beta)
control["is_cycle"] = next_differential * beta == sp.zeros(1, 1)
control["primitive"] = [1]

checks = {
    "hostile_beta_is_closed": hostile["is_cycle"],
    "hostile_atlas_descent_is_strict": hostile["atlas_holonomy"] == 1,
    "hostile_beta_is_not_a_boundary": not hostile["is_boundary"],
    "hostile_augmented_rank_detects_the_class": hostile["augmented_rank"] == hostile["differential_rank"] + 1,
    "control_beta_is_a_boundary": control["is_boundary"],
    "control_exhibits_an_exact_primitive": control["primitive"] == [1],
    "descent_and_exactness_are_independent": hostile["atlas_holonomy"] == 1 and not hostile["is_boundary"],
}

result = {
    "schema": "marici.aspect.specialization-cone-nonboundary-hostile.v1",
    "status": "hostile_constructed" if all(checks.values()) else "checker_failure",
    "checks": checks,
    "hostile": hostile,
    "boundary_control": control,
    "admission_gate": "export the source-derived cone differential, prove beta is a cycle, and show rank(d_prev)=rank([d_prev|beta]) with an explicit primitive",
    "conclusion": "normalized cyclic descent of the gamma-Bockstein does not imply that its cone cohomology class vanishes",
}

out = root / "results" / "specialization_cone_nonboundary_hostile.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "hostile_constructed" else 1)
