"""Exact nonradial port-alignment RG closure audit for WP494."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp484 = load("wp484_gauged_connector_frame_lift.json")
wp493 = load("wp493_radial_quartic_rg_closure.json")

L = [
    sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]]),
    sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]]),
]

# Exact SO(3) vector-generator completeness tensor.
completeness_checks = []
for i in range(3):
    for j in range(3):
        for k in range(3):
            for ell in range(3):
                lhs = sum(generator[i, j] * generator[k, ell] for generator in L)
                rhs = int(i == k) * int(j == ell) - int(i == ell) * int(j == k)
                completeness_checks.append(lhs == rhs)

s = sp.Matrix(sp.symbols("s0:3", real=True))
x = sp.Matrix(sp.symbols("x0:3", real=True))
gauge_contraction = sp.expand(sum((s.T * generator * x)[0] ** 2 for generator in L))
radial_minus_alignment = sp.expand((s.dot(s)) * (x.dot(x)) - (s.dot(x)) ** 2)

# Same radial norms, different relative port alignment.
parallel = {s[0]: 1, s[1]: 0, s[2]: 0, x[0]: 1, x[1]: 0, x[2]: 0}
orthogonal = {s[0]: 1, s[1]: 0, s[2]: 0, x[0]: 0, x[1]: 1, x[2]: 0}
radial_invariant = sp.expand((s.dot(s)) * (x.dot(x)))
alignment_invariant = sp.expand((s.dot(x)) ** 2)

# Evaluate the full matrix invariants at the isotropic WP484 vacuum.
s_scale, mu = sp.symbols("s mu", positive=True)
gram_s = s_scale**2 * sp.eye(3)
gram_x = 2 * mu**2 * sp.eye(3)
i_radial_vacuum = sp.factor(sp.trace(gram_s) * sp.trace(gram_x))
i_alignment_vacuum = sp.factor(sp.trace(gram_s * gram_x))
i_gauge_vacuum = sp.factor(i_radial_vacuum - i_alignment_vacuum)

checks = {
    "wp484_dependency_passed": wp484["passed"],
    "wp493_dependency_passed": wp493["passed"],
    "so3_generator_completeness_holds_in_all_components": all(completeness_checks),
    "gauge_contraction_reduces_to_radial_minus_alignment": sp.simplify(gauge_contraction - radial_minus_alignment) == 0,
    "hostile_pair_has_equal_radial_invariant": radial_invariant.subs(parallel) == radial_invariant.subs(orthogonal) == 1,
    "hostile_pair_has_distinct_alignment_invariant": alignment_invariant.subs(parallel) == 1 and alignment_invariant.subs(orthogonal) == 0,
    "gauge_loop_distinguishes_hostile_pair": gauge_contraction.subs(parallel) == 0 and gauge_contraction.subs(orthogonal) == 1,
    "isotropic_vacuum_radial_value_is_eighteen": i_radial_vacuum == 18 * s_scale**2 * mu**2,
    "isotropic_vacuum_alignment_value_is_six": i_alignment_vacuum == 6 * s_scale**2 * mu**2,
    "isotropic_vacuum_gauge_combination_is_twelve": i_gauge_vacuum == 12 * s_scale**2 * mu**2,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP494",
    "domain": "WP484 connector S and adjoint triplet X as SO(3)_P vectors, with the WP493 radial quartic basis",
    "exact_gauge_contraction": {
        "component_form": "sum_a (s^T L_a x)^2=|s|^2|x|^2-(s dot x)^2",
        "matrix_form": "Tr(G_S) Tr(G_X)-Tr(G_S G_X)",
        "G_S": "S^T S",
        "G_X": "G_X_ij=Tr(X_i X_j)",
    },
    "new_compulsory_invariant": "I_align=Tr((S^T S) G_X)",
    "hostile_pair": {
        "parallel": {"I_rad": "1", "I_align": "1", "gauge_contraction": "0"},
        "orthogonal": {"I_rad": "1", "I_align": "0", "gauge_contraction": "1"},
        "meaning": "radial data alone do not determine the port-gauge counterterm",
    },
    "isotropic_vacuum_values": {
        "I_rad": str(i_radial_vacuum),
        "I_align": str(i_alignment_vacuum),
        "I_rad_minus_I_align": str(i_gauge_vacuum),
    },
    "classification": "WP493's radial completion remains nonradially incomplete; SO(3)_P gauge support requires an independent connector-flavon alignment quartic.",
    "selector": False,
    "rigidifier": False,
    "instrument": None,
    "smallest_exact_falsifier": "Parallel and orthogonal unit port vectors have identical radial norms but gauge contractions zero and one, respectively.",
    "remaining_gate": "Add the alignment coupling as an independent running coordinate, enumerate the remaining SU(3)_F adjoint and cyclic-row quartic invariants, and recompute the WP489 vacuum and width cone after RG completion.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp494_port_alignment_rg_closure.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
