import json
from pathlib import Path

import sympy as sp


I = sp.I
sqrt2 = sp.sqrt(2)
J1 = sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) / sqrt2
J2 = sp.Matrix([[0, -I, 0], [I, 0, -I], [0, I, 0]]) / sqrt2
J3 = sp.diag(1, 0, -1)
J = (J1, J2, J3)

epsilon = sp.LeviCivita
commutator_residuals = []
for i in range(3):
    for j in range(i + 1, 3):
        rhs = sp.zeros(3)
        for k in range(3):
            rhs += I * epsilon(i, j, k) * J[k]
        commutator_residuals.append(sp.simplify(J[i] * J[j] - J[j] * J[i] - rhs))

casimir_trace = sp.simplify(sum(sp.trace(x * x) for x in J))
assert all(r == sp.zeros(3) for r in commutator_residuals)
assert casimir_trace == 6

g, y, a, sigma, scale = sp.symbols("g y a sigma scale", positive=True)
f2 = sp.simplify(6 * y**2 * sigma**2)
v2 = sp.simplify(2 * a * sigma**2)
target = sp.simplify(g * sp.sqrt(f2 / v2))
dilated_target = sp.simplify(target.subs(sigma, scale * sigma))

hostile_a1 = sp.simplify(target.subs({y: 1, a: 1}))
hostile_a3 = sp.simplify(target.subs({y: 1, a: 3}))

assert target == sp.sqrt(3) * g * y / sp.sqrt(a)
assert sp.simplify(dilated_target - target) == 0
assert hostile_a1 == sp.sqrt(3) * g
assert hostile_a3 == g
assert sp.simplify(hostile_a1 - hostile_a3) != 0

result = {
    "work_package": "WP467",
    "source_action": "positive renormalizable common-dilaton sum of squares",
    "spin_one_checks": {
        "commutator_residual_count": sum(int(r != sp.zeros(3)) for r in commutator_residuals),
        "quadratic_trace_casimir": str(casimir_trace),
    },
    "vacuum_relations": {
        "f_squared": str(f2),
        "v_squared": str(v2),
        "g_f_over_v": str(target),
    },
    "common_dilation_target_change": str(sp.simplify(dilated_target - target)),
    "coefficient_hostile_pair": {
        "y_1_a_1": str(hostile_a1),
        "y_1_a_3": str(hostile_a3),
    },
    "classification": "proper relational ratio selector conditional on dimensionless source coefficients; not yet a numerical selector or instrument",
    "scale_kernel_repaired": sp.simplify(dilated_target - target) == 0,
    "numerical_selector_admitted": sp.simplify(hostile_a1 - hostile_a3) == 0,
}

out = Path(__file__).parents[1] / "results" / "wp467_common_dilaton_clock_portal.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

