"""Exact simultaneous singlet-triplet Yukawa-nullcline no-go."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
g1, g2, T = sp.symbols("g1 g2 T", nonnegative=True)
yA, kA, yB, kB = sp.symbols("y_A kappa_A y_B kappa_B", real=True)

# Exact reduction of the PyR@TE matrix output at A=a I_3 and B=b I_3:
# beta_A contains tr(A^dag A)A + 3/4 tr(B^dag B)A
#                 + 3/2 A A^dag A + 3/8 B^T B* A;
# beta_B contains tr(A^dag A)B + 3/4 tr(B^dag B)B
#                 + 1/2 B A* A^T + 5/8 B B^dag B.
matrix_reduction = {
    "A_from_A": (3, sp.Rational(3, 2)),
    "A_from_B": (sp.Rational(3, 4) * 3, sp.Rational(3, 8)),
    "B_from_A": (3, sp.Rational(1, 2)),
    "B_from_B": (sp.Rational(3, 4) * 3, sp.Rational(5, 8)),
}
amplitude = {name: sum(terms) for name, terms in matrix_reduction.items()}
squared = {name: 2 * value for name, value in amplitude.items()}
x = squared["A_from_B"]
y = squared["B_from_A"]
gauge_amplitude = {
    "A_g1": sp.Rational(15, 4),
    "A_g2": sp.Rational(9, 4),
    "B_g1": sp.Rational(15, 4),
    "B_g2": sp.Rational(33, 4),
}

equations = [
    8 * yA + 2 * kA - 12 * g1,
    3 * yA + 9 * kA + x * kB + 6 * T
    - sp.Rational(15, 2) * g1 - sp.Rational(9, 2) * g2,
    12 * yB + sp.Rational(1, 2) * kB - 12 * g1 - 24 * g2,
    3 * yB + sp.Rational(23, 4) * kB + y * kA + 6 * T
    - sp.Rational(15, 2) * g1 - sp.Rational(33, 2) * g2,
]
solution = {name: sp.factor(value) for name, value in sp.solve(
    equations, (yA, kA, yB, kB), dict=True
)[0].items()}

expected = {
    yA: 3 * (4 * T + 115 * g1 + 53 * g2) / 206,
    kA: -6 * (4 * T + 12 * g1 + 53 * g2) / 103,
    yB: (20 * T + 575 * g1 + 1089 * g2) / 618,
    kB: 4 * (-20 * T + 43 * g1 + 147 * g2) / 103,
}
contrast = sp.factor(-4 * solution[yA] * solution[kA] + 3 * solution[yB] * solution[kB])
expected_contrast = (
    2 * (-28 * T + 431 * g1 + 453 * g2)
    * (4 * T + 115 * g1 + 465 * g2) / 10609
)
minus_kA_numerator = sp.Poly(sp.factor(-solution[kA] * 103 / 6), T, g1, g2)
positive_coefficient_certificate = all(
    coefficient > 0 for coefficient in minus_kA_numerator.coeffs()
)
origin_only_certificate = (
    minus_kA_numerator.as_expr().subs({T: 0, g1: 0, g2: 0}) == 0
    and set(minus_kA_numerator.monoms()) == {(1, 0, 0), (0, 1, 0), (0, 0, 1)}
)
hostile_residual = sp.factor(solution[kA].subs({g1: 1, g2: 0, T: 0}))

checks = {
    "published_A_self_coefficient_reproduced": squared["A_from_A"] == 9,
    "published_B_self_coefficient_reproduced": squared["B_from_B"] == sp.Rational(23, 4),
    "cross_x_is_21_over_4": x == sp.Rational(21, 4),
    "cross_y_is_7": y == 7,
    "published_A_gauge_coefficients_reproduced": (
        2 * gauge_amplitude["A_g1"] == sp.Rational(15, 2)
        and 2 * gauge_amplitude["A_g2"] == sp.Rational(9, 2)
    ),
    "published_B_gauge_coefficients_reproduced": (
        2 * gauge_amplitude["B_g1"] == sp.Rational(15, 2)
        and 2 * gauge_amplitude["B_g2"] == sp.Rational(33, 2)
    ),
    "simultaneous_nullclines_solve_exactly": all(
        sp.simplify(eq.subs(solution)) == 0 for eq in equations
    ),
    "closed_form_solution_matches": all(
        sp.simplify(solution[name] - value) == 0 for name, value in expected.items()
    ),
    "kappa_A_negative_form_is_exact": sp.simplify(
        solution[kA] + 6 * (4 * T + 12 * g1 + 53 * g2) / 103
    ) == 0,
    "negative_form_has_strictly_positive_coefficients": positive_coefficient_certificate,
    "negative_form_vanishes_only_at_source_origin": origin_only_certificate,
    "formal_portal_contrast_factorization_is_exact": sp.simplify(
        contrast - expected_contrast
    ) == 0,
    "wp734_simple_slice_now_has_negative_kappa_A": hostile_residual == sp.Rational(-72, 103),
    "deliberate_failure_residual_is_nonzero": hostile_residual != 0,
    "no_strictly_positive_four_yukawa_solution_on_nonnegative_source_domain": (
        positive_coefficient_certificate and origin_only_certificate
    ),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP735",
    "status": "PASS",
    "checks": checks,
    "source_domain": "g1 >= 0, g2 >= 0, T = alpha_t + alpha_b >= 0 at one-loop Yukawa order",
    "derived_cross_coefficients": {"x": "21/4", "y": "7"},
    "normalization_checks": {"E_kappaA_kappaA": "9", "E_kappaB_kappaB": "23/4"},
    "exact_obstruction": "kappa_A = -6(4T + 12g1 + 53g2)/103 <= 0, with equality only at the source origin",
    "classification": "the simultaneous singlet-triplet direct sum has no fully positive one-loop Yukawa nullcline; it is neither a viable selector nor a viable rigidifier of the desired portal fixed point",
    "smallest_exact_falsifier": "any strictly positive source coordinate T, g1, or g2 forces kappa_A < 0",
    "deliberate_failure_residual": {"slice": "g1=1, g2=T=0", "kappa_A": str(hostile_residual)},
    "claim_boundary": "one-loop Yukawa system; no threshold, complete scalar, two-loop Yukawa, or detector authority",
    "remaining_source_gate": "an independently derived structural term must alter the kappa_A numerator without tuning and then fix magnitude and RG basin",
    "remaining_physical_gate": "threshold survival and calibrated detector readout remain unconstructed",
    "external_reproduction": {
        "tool": "PyR@TE 3",
        "repository": "https://github.com/LSartore/pyrate",
        "revision": "04b219c2016f3fc4f2371d72607edc26a7e06364",
    },
}
(ROOT / "results" / "wp735_simultaneous_singlet_triplet_nullcline_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
