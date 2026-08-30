"""Exact 210 fixed-point obstruction for the minimal WP736 parent."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
a1, aA, aB, a3, ak, ay = sp.symbols(
    "alpha_1 alpha_A alpha_B alpha_3 alpha_kappa alpha_y", nonnegative=True
)

kappa_nullcline = sp.factor(
    (sp.Rational(15, 2) * a1 + 9 * aA + sp.Rational(9, 2) * aB) / 15
)
P1 = (
    sp.Rational(137, 6) + sp.Rational(1063, 18) * a1
    + sp.Rational(44, 3) * a3 + 39 * aA + sp.Rational(75, 2) * aB
    - 15 * ak
)
PA = 1 + 13 * a1 + 12 * a3 + 57 * aA + 12 * aB - 6 * ak
P1_reduced = sp.factor(P1.subs(ak, kappa_nullcline))
PA_reduced = sp.factor(PA.subs(ak, kappa_nullcline))
expected_P1 = (
    sp.Rational(137, 6) + sp.Rational(464, 9) * a1
    + sp.Rational(44, 3) * a3 + 30 * aA + 33 * aB
)
expected_PA = (
    1 + 10 * a1 + 12 * a3 + sp.Rational(267, 5) * aA
    + sp.Rational(51, 5) * aB
)

poly_P1 = sp.Poly(P1_reduced, a1, aA, aB, a3)
poly_PA = sp.Poly(PA_reduced, a1, aA, aB, a3)

# If the parent flavor Yukawa enters beta_kappa with E_ky >= 0, then
# alpha_kappa=(gauge-E_ky alpha_y)/15 <= kappa_nullcline. Since both gauge
# brackets contain -D alpha_kappa, this can only increase them.
Eky = sp.symbols("E_kappa_y", nonnegative=True)
kappa_with_y = kappa_nullcline - Eky * ay / 15
P1_with_y_shift = sp.factor(P1.subs(ak, kappa_with_y) - P1_reduced)
PA_with_y_shift = sp.factor(PA.subs(ak, kappa_with_y) - PA_reduced)
hostile_residual = PA_reduced.subs({a1: 0, aA: 0, aB: 0, a3: 0})

checks = {
    "parent_kappa_nullcline_is_exact": sp.simplify(
        kappa_nullcline - (a1 / 2 + 3 * aA / 5 + 3 * aB / 10)
    ) == 0,
    "hypercharge_reduced_bracket_is_exact": sp.simplify(P1_reduced - expected_P1) == 0,
    "SU2A_reduced_bracket_is_exact": sp.simplify(PA_reduced - expected_PA) == 0,
    "hypercharge_coefficients_are_strictly_positive": all(c > 0 for c in poly_P1.coeffs()),
    "SU2A_coefficients_are_strictly_positive": all(c > 0 for c in poly_PA.coeffs()),
    "hypercharge_bracket_has_positive_constant": poly_P1.TC() == sp.Rational(137, 6),
    "SU2A_bracket_has_unit_positive_constant": poly_PA.TC() == 1,
    "parent_flavor_yukawa_increases_hypercharge_bracket": P1_with_y_shift == Eky * ay,
    "parent_flavor_yukawa_increases_SU2A_bracket": PA_with_y_shift == sp.Rational(2, 5) * Eky * ay,
    "no_positive_hypercharge_interacting_zero": all(c > 0 for c in poly_P1.coeffs()),
    "no_positive_SU2A_interacting_zero": all(c > 0 for c in poly_PA.coeffs()),
    "deliberate_failure_residual_is_one": hostile_residual == 1 and hostile_residual != 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP737",
    "status": "PASS",
    "checks": checks,
    "state_domain": "nonnegative rescaled squared parent couplings in the 210 gauge-Yukawa truncation",
    "one_loop_gauge_coefficients": {
        "U1Y": "137/6",
        "SU2A": "1",
        "SU2B": "-17/6",
        "SU3c": "-7",
    },
    "kappa_nullcline": "alpha_kappa = alpha_1/2 + 3 alpha_A/5 + 3 alpha_B/10",
    "exact_obstruction": {
        "P1": "137/6 + 464 alpha_1/9 + 44 alpha_3/3 + 30 alpha_A + 33 alpha_B > 0",
        "PA": "1 + 10 alpha_1 + 12 alpha_3 + 267 alpha_A/5 + 51 alpha_B/5 > 0",
    },
    "classification": "the minimal product parent fixes the matching sign and ratio but has no perturbative interacting magnitude selector or full RG basin",
    "smallest_exact_falsifier": "the reduced SU2A bracket is at least one throughout the nonnegative orthant",
    "deliberate_failure_residual": {"Gaussian_boundary_value_of_PA": str(hostile_residual)},
    "robustness": "any nonnegative parent flavor Yukawa lowers alpha_kappa and increases both obstructing gauge brackets",
    "remaining_source_gate": "derive additional anomaly-free Yukawa-active matter independently and reverse the bracket sign without losing perturbative control or Clebsch matching",
    "remaining_threshold_gate": "not reached because the minimal parent has no selected source fixed point",
    "remaining_physical_gate": "not reached; labelled independently calibrated singlet-triplet readout remains required",
    "external_reproduction": {
        "tool": "PyR@TE 3",
        "repository": "https://github.com/LSartore/pyrate",
        "revision": "04b219c2016f3fc4f2371d72607edc26a7e06364",
    },
}
(ROOT / "results" / "wp737_minimal_product_parent_fixed_point_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
