"""Exact WP617 no-go for a renormalizable single SU(3)_F adjoint selector."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

x = sp.Matrix([sp.Rational(4, 3), sp.Rational(1, 3), sp.Rational(-5, 3)])
tangent = sp.Matrix([2, -3, 1])

m1 = sp.simplify(sum(x))
m2 = sp.simplify(sum(value**2 for value in x))
m3 = sp.simplify(sum(value**3 for value in x))
dm1 = sp.simplify(sum(tangent))
dm2 = sp.simplify(2 * x.dot(tangent))
dm3 = sp.simplify(
    3 * sum(x[index] ** 2 * tangent[index] for index in range(3))
)

vandermonde = sp.simplify(
    (x[0] - x[1]) * (x[1] - x[2]) * (x[0] - x[2])
)

# The most general eigenvalue-dependent renormalizable potential for one
# traceless Hermitian SU(3) adjoint is a*m2+b*m2^2+k*m3 plus a constant.
a, b, k = sp.symbols("a b k", real=True)
potential_tangent_derivative = sp.simplify(
    (a + 2 * b * m2) * dm2 + k * dm3
)

# A repeated-eigenvalue stationary branch at the same quadratic norm.
r = sp.sqrt(7) / 3
repeated = sp.Matrix([r, r, -2 * r])
repeated_m1 = sp.simplify(sum(repeated))
repeated_m2 = sp.simplify(sum(value**2 for value in repeated))
repeated_m3 = sp.simplify(sum(value**3 for value in repeated))

target_gaps = sorted(
    [abs(x[0] - x[1]), abs(x[1] - x[2]), abs(x[0] - x[2])]
)
target_mass_squares = [sp.simplify(gap**2) for gap in target_gaps]
repeated_gaps = sorted(
    [
        abs(repeated[0] - repeated[1]),
        abs(repeated[1] - repeated[2]),
        abs(repeated[0] - repeated[2]),
    ]
)
repeated_mass_squares_normalized = [
    sp.simplify(gap**2 / (9 * r**2)) for gap in repeated_gaps
]

checks = {
    "centered_target_is_traceless": m1 == 0,
    "target_centered_second_moment": m2 == sp.Rational(14, 3),
    "target_centered_cubic": m3 == sp.Rational(-20, 9),
    "declared_direction_preserves_trace": dm1 == 0,
    "declared_direction_is_tangent_to_fixed_m2": dm2 == 0,
    "cubic_has_nonzero_tangent_response": dm3 == 18,
    "general_potential_moves_target_when_cubic_present":
        potential_tangent_derivative == 18 * k,
    "target_has_three_distinct_eigenvalues": vandermonde != 0,
    "repeated_branch_has_same_m2": repeated_m1 == 0 and repeated_m2 == m2,
    "repeated_branch_has_different_m3": repeated_m3 != m3,
    "target_gauge_mass_square_pattern_is_1_4_9":
        target_mass_squares == [1, 4, 9],
    "repeated_branch_mass_square_pattern_is_0_1_1":
        repeated_mass_squares_normalized == [0, 1, 1],
}

if not all(checks.values()):
    raise SystemExit(f"WP617 check failed: {checks}")

result = {
    "work_package": "WP617",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "one traceless Hermitian SU(3)_F adjoint with a source-free renormalizable conjugation-invariant potential",
    "complete_renormalizable_invariant_family": "constant plus a Tr(Phi^2) plus b Tr(Phi^2)^2 plus k Tr(Phi^3); Cayley-Hamilton removes an independent Tr(Phi^4)",
    "centered_target": ["4/3", "1/3", "-5/3"],
    "target_moments": {"m1": "0", "m2": "14/3", "m3": "-20/9"},
    "hostile_tangent": [2, -3, 1],
    "tangent_residuals": {"dm1": "0", "dm2": "0", "dm3": "18"},
    "stationary_locus_theorem": "for nonzero cubic coefficient, the eigenvalue stationarity equation is quadratic and therefore admits at most two distinct eigenvalues; for zero cubic coefficient the orientation is flat at fixed quadratic norm",
    "classification": "the cubic Casimir is a valid signed observer but a single-adjoint renormalizable action is neither a selector of the target charge geometry nor a compatible target stationary source",
    "smallest_exact_falsifier": "along tangent (2,-3,1), the target preserves trace and Tr(Phi^2) but changes Tr(Phi^3) by 18, so every nonzero cubic coefficient moves it",
    "physical_probe": "off-diagonal SU(3)_F gauge-boson mass squares are proportional to eigenvalue-gap squares",
    "target_mass_square_pattern": [1, 4, 9],
    "single_adjoint_stationary_pattern": [0, 1, 1],
    "instrument_gate": "resolve the three family-root vector channels in a common calibrated line shape and show that no additional Higgs representation contributes to their masses",
    "remaining_source_gate": "add an independently motivated second noncommuting flavon or higher-degree source rule, then prove the complete invariant family selects rather than merely reads the signed cubic",
}

out = ROOT / "results" / "wp617_single_adjoint_cubic_casimir_no_go.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
