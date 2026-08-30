"""Exact preregistration checker for the WP440 charged-bifurcation potential."""

import json
from pathlib import Path

import sympy as sp


I = sp.I
basis = [
    sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
    sp.diag(1, -1, 0),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),
    sp.diag(1, 1, -2),
]


def norm_squared(matrix):
    return sp.simplify(sp.trace(matrix.conjugate().T * matrix))


z = sp.symbols("z0:16", real=True)
A = sum((z[i] * basis[i] for i in range(8)), sp.zeros(3))
D = sum((z[8+i] * basis[i] for i in range(8)), sp.zeros(3))
anti = A*D + D*A
eta_term = -norm_squared(anti)

representative = {q: 0 for q in z}
representative[z[2]] = sp.sqrt(sp.Rational(1, 8))
representative[z[8]] = sp.sqrt(sp.Rational(1, 8))
charged_indices = [3, 4, 5, 6, 11, 12, 13, 14]
charged_curvature = sp.hessian(eta_term, z).subs(representative).extract(charged_indices, charged_indices)
charged_spectrum = charged_curvature.eigenvals()

# Conservative norm bounds used for a source-independent coercivity margin:
# ||[A,D]||_F^2 <= R^2/2 and ||{A,D}||_F^2 <= R^2, R=Tr(A^2)+Tr(D^2).
lam, eta, rho = sp.symbols("lambda eta rho", positive=True, real=True)
margin = rho - lam/2 - eta

checks = {
    "anticommutator_channel_is_quartic": sp.Poly(eta_term, z).total_degree() == 4,
    "wp438_representative_has_zero_anticommutator": anti.subs(representative) == sp.zeros(3),
    "wp438_representative_remains_stationary_for_new_channel": all(sp.diff(eta_term, q).subs(representative) == 0 for q in z),
    "new_channel_has_negative_charged_curvature": any(value < 0 for value in charged_spectrum),
    "charged_block_is_eight_dimensional": charged_curvature.shape == (8, 8),
    "coercivity_margin_is_strictly_positive_at_hostile_rational_point": margin.subs({rho: 1, lam: 1, eta: sp.Rational(1, 4)}) > 0,
}
checks = {key: bool(value) for key, value in checks.items()}

result = {
    "work_package": "WP440",
    "type": "preregistration",
    "potential": "-m^2 R/2 + rho R^2 - lambda ||[A,D]||_F^2 - eta ||{A,D}||_F^2",
    "coefficient_domain": ["m^2>0", "lambda>0", "eta>0", "rho>lambda/2+eta"],
    "charged_curvature_spectrum_of_unit_negative_anticommutator_channel": {str(k): int(v) for k, v in charged_spectrum.items()},
    "acceptance": [
        "identify an open coefficient region whose global minimum has gauge-mass rank eight",
        "prove the complete Hessian is nonnegative with zeros exactly equal to the gauge orbit",
        "prove boundedness and global rather than merely local preference",
        "use no measured flavor coordinate",
        "keep g_F f/v outside vacuum-shape authority",
    ],
    "falsifiers": [
        "the charged curvature never crosses zero inside the frozen coercive domain",
        "every stable global minimum retains a continuous stabilizer",
        "full breaking occurs only at an isolated or target-fitted coefficient point",
        "a nongauge Hessian zero or negative mode remains",
        "the potential is unbounded on a matrix ray",
    ],
    "outcome_boundary": "No full stationary solution, global minimum, full Hessian spectrum, gauge-mass rank, physical16 match, or instrument claim is made.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp440_charged_bifurcation_preregistration.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
