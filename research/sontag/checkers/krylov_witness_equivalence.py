import json
from pathlib import Path

import sympy as sp


def krylov(A, x):
    return sp.Matrix.hstack(x, A * x, A**2 * x)


def omega(A, x):
    return sp.expand(krylov(A, x).det())


A = sp.diag(1, 2, 3)
x = sp.Matrix([1, 1, 1])
base = omega(A, x)

S = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
similarity = omega(S * A * S.inv(), S * x)

alpha = sp.Integer(2)
beta = sp.Integer(5)
affine = omega(alpha * A + beta * sp.eye(3), x)

f = sp.Matrix([[1, 2, 3]])
feedback = omega(A + x * f, x)

A_collapse = sp.diag(-1, 1, 2)
x_collapse = sp.Matrix([1, 1, 1])
before_collapse = omega(A_collapse, x_collapse)
after_collapse = omega(A_collapse**2, x_collapse)

q_good = A
q_bad = A - 2 * sp.eye(3)

rho = sp.Integer(7)
seed_scale = sp.Integer(-1)

unsigned = [
    {"prep": "p0", "epoch": 0, "path": "a", "value": 11},
    {"prep": "p1", "epoch": 0, "path": "b", "value": 11},
]
signed = [
    {"prep": "p0", "epoch": 0, "path": "a", "value": 1},
    {"prep": "p1", "epoch": 0, "path": "b", "value": -1},
]
cartesian = [(u, s) for u in unsigned for s in signed]
pullback = [
    (u, s)
    for u in unsigned
    for s in signed
    if (u["prep"], u["epoch"], u["path"])
    == (s["prep"], s["epoch"], s["path"])
]

checks = {
    "baseline_is_nonzero": base == 2,
    "similarity_scales_by_determinant": similarity == S.det() * base,
    "seed_scaling_has_cubic_weight": omega(A, 2 * x) == 8 * base,
    "affine_operator_has_cubic_slope_weight": affine == alpha**3 * base,
    "single_input_state_feedback_preserves_omega": feedback == base,
    "nonlinear_polynomial_can_destroy_cyclicity": before_collapse != 0
    and after_collapse == 0,
    "invertible_seed_filter_scales_by_its_determinant": omega(A, q_good * x)
    == q_good.det() * base,
    "singular_seed_filter_destroys_cyclicity": omega(A, q_bad * x) == 0,
    "unreferenced_ray_representative_flips_sign": omega(A, seed_scale * x)
    == -base,
    "contragredient_reference_cancels_seed_weight": (seed_scale ** -3 * rho)
    * omega(A, seed_scale * x)
    == rho * base,
    "cartesian_join_has_spurious_pairs": len(cartesian) == 4,
    "lineage_pullback_has_only_physical_pairs": len(pullback) == 2,
}

result = {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "baseline_omega": str(base),
    "classification": {
        "cyclicity": "preserved by similarity, nonzero seed scaling, affine evolution reparameterization, state feedback, and invertible seed filtering under their stated gates",
        "signed_readout": "preserved only after the volume reference transports by the inverse determinant character",
        "witness_equivalence": "additionally requires staged-constructor and lineage preservation",
    },
    "deliberate_failure": {
        "input_spectrum": [-1, 1, 2],
        "polynomial": "p(z)=z^2",
        "before_omega": str(before_collapse),
        "after_omega": str(after_collapse),
    },
}

output = Path(__file__).parents[1] / "results" / "krylov_witness_equivalence.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

