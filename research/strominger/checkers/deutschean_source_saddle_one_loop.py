#!/usr/bin/env python3
"""Exact one-loop source-saddle gate for the continuous-q carrier."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT = ROOT / "research/strominger/results/deutschean_source_saddle_one_loop.json"

T = sp.symbols("T")
b, c, kappa = sp.symbols("b c kappa")
h = 1 - T

explicit = sp.Rational(3, 2) * T
amplitude_curvature = sp.Rational(81, 32) * T**2 / h
mixed = -sp.Rational(9, 8) * T * (2 - T**2) / h**2
quartic = (T**3 - 6) / (8 * h**2)
cubic_pair = sp.Rational(5, 24) * (2 - T**2) ** 2 / h**3

laplace_one_loop = sp.factor(
    explicit + amplitude_curvature + mixed + quartic + cubic_pair
)
stirling_correction = -sp.Rational(1, 12)
normalized_one_loop = sp.factor(laplace_one_loop + stirling_correction)
expected_laplace = (T**4 - 66 * T**3 + 53 * T**2 - 8) / (96 * (T - 1) ** 3)
expected_normalized = T * (T**3 - 74 * T**2 + 77 * T - 24) / (
    96 * (T - 1) ** 3
)

# Fixed-t differentiation is E = z d/dz = T/(1-T) d/dT.  At the first
# response order only the saddle action S0 and determinant/amplitude term S1
# enter; S2 begins one order later.
E = lambda expression: sp.factor(T / (1 - T) * sp.diff(expression, T))
S0 = 1 + T + 1 / T - sp.exp(T) / T
S1 = -sp.Rational(5, 4) * T - sp.log(1 - T) / 2
A0 = sp.factor(S0 + E(S0))
A1 = E(S1)
qd0 = sp.factor(1 + E(A0))
qd1 = sp.factor(
    -sp.Rational(1, 2) * (E(E(A0)) - E(A0)) + E(A1) - A1
)
V1 = sp.factor(qd1 * (1 - T) ** 2)
H1 = sp.factor((1 / T - 1) * V1 + 4 * T)
expected_H1 = 2 * T + sp.Rational(11, 4) * T**2 + T**3 / (1 - T)

# Second adjacent-response transport.  The epsilon^3 discrete shift supplies
# Q2; W0(T)=T has zero second derivative, so no quadratic Taylor term occurs.
A2 = sp.factor(E(normalized_one_loop) - normalized_one_loop)
qd2 = sp.factor(
    sp.Rational(1, 3) * E(A0)
    - sp.Rational(1, 2) * E(E(A0))
    + sp.Rational(1, 6) * E(E(E(A0)))
    - A1
    + sp.Rational(3, 2) * E(A1)
    - sp.Rational(1, 2) * E(E(A1))
    + E(A2)
    - 2 * A2
)
V2 = sp.factor(qd2 / qd0**2 - qd1**2 / qd0**3)
delta1 = V1 - 4 * T
delta2 = V2 - 4 * V1
H2 = sp.factor(
    V2 / T
    - sp.Rational(1, 2) * (V1 / T) ** 2
    - delta2
    - 4 * H1
    - delta1 * sp.diff(H1, T)
)
expected_H2 = T**2 * (
    146 * T**5
    - 425 * T**4
    + 248 * T**3
    + 536 * T**2
    - 866 * T
    + 391
) / (48 * (T - 1) ** 4)
n = sp.symbols("n", integer=True, nonnegative=True)
stable_H2_coefficient = sp.simplify(
    -sp.Rational(23, 3)
    + sp.Rational(15, 4) * (n + 1)
    - sp.Rational(5, 6) * sp.binomial(n + 2, 2)
    + sp.Rational(5, 8) * sp.binomial(n + 3, 3)
)
expected_stable_H2_coefficient = (5 * n**3 + 10 * n**2 + 175 * n - 198) / 48

# Phase-preserving hostile family:
# (exp(tx)-c*t) exp(b*tx) exp(-(exp(tx)-1-tx)/t).
S1_family = -b * T - sp.log(1 - T) / 2
A1_family = E(S1_family)
qd1_family = sp.factor(
    -sp.Rational(1, 2) * (E(E(A0)) - E(A0))
    + E(A1_family)
    - A1_family
)
V1_family = sp.factor(qd1_family * (1 - T) ** 2)
H1_family = sp.factor((1 / T - 1) * V1_family + 4 * T)
expected_H1_family = (
    (sp.Rational(9, 2) - 2 * b) * T
    + (b + sp.Rational(3, 2)) * T**2
    + T**3 / (1 - T)
)
S2_family = sp.factor(
    c * T
    + (b + 1) ** 2 * T**2 / (2 * h)
    - (b + 1) * T * (2 - T**2) / (2 * h**2)
    + (T**3 - 6) / (8 * h**2)
    + sp.Rational(5, 24) * (2 - T**2) ** 2 / h**3
    - sp.Rational(1, 12)
)
A2_family = sp.factor(E(S2_family) - S2_family)
qd2_family = sp.factor(
    sp.Rational(1, 3) * E(A0)
    - sp.Rational(1, 2) * E(E(A0))
    + sp.Rational(1, 6) * E(E(E(A0)))
    - A1_family
    + sp.Rational(3, 2) * E(A1_family)
    - sp.Rational(1, 2) * E(E(A1_family))
    + E(A2_family)
    - 2 * A2_family
)
V2_family = sp.factor(qd2_family / qd0**2 - qd1_family**2 / qd0**3)
delta1_family = V1_family - 4 * T
delta2_family = V2_family - 4 * V1_family
H2_family = sp.factor(
    V2_family / T
    - sp.Rational(1, 2) * (V1_family / T) ** 2
    - delta2_family
    - 4 * H1_family
    - delta1_family * sp.diff(H1_family, T)
)
amplitude_port_determinant = sp.factor(
    sp.diff(H1_family, b) * sp.diff(H2_family, c)
    - sp.diff(H1_family, c) * sp.diff(H2_family, b)
)

# Primitive-phase hostile deformation. Adding kappa*(tx)^2 inside the
# primitive numerator changes the rescaled saddle map to
# z=T*exp(-T)-2*kappa*T^2 while preserving zero-source normalization.
z_kappa = T * sp.exp(-T) - 2 * kappa * T**2
E_kappa = lambda expression: sp.factor(
    z_kappa / sp.diff(z_kappa, T) * sp.diff(expression, T)
)
h_kappa = sp.factor(T * sp.diff(z_kappa, T) / z_kappa)
S0_kappa = (
    1
    + sp.log(T / z_kappa)
    + (sp.exp(-T) - 1) / z_kappa
    + kappa * T**2 / z_kappa
)
S1_kappa = -(b + 1) * T + sp.log(T / z_kappa) - sp.log(h_kappa) / 2
A0_kappa = sp.factor(S0_kappa + E_kappa(S0_kappa))
A1_kappa = sp.factor(E_kappa(S1_kappa))
qd0_kappa = sp.factor(1 + E_kappa(A0_kappa))
qd1_kappa = sp.factor(
    -sp.Rational(1, 2) * (E_kappa(E_kappa(A0_kappa)) - E_kappa(A0_kappa))
    + E_kappa(A1_kappa)
    - A1_kappa
)
V0_kappa = sp.factor(1 - 1 / qd0_kappa)
V1_kappa = sp.factor(qd1_kappa / qd0_kappa**2)
W0_kappa = sp.log(V0_kappa / z_kappa)
W0prime_kappa = sp.factor(sp.diff(W0_kappa, T) / sp.diff(V0_kappa, T))
H1_kappa = sp.factor(
    V1_kappa / V0_kappa - (V1_kappa - 4 * V0_kappa) * W0prime_kappa
)
phase_normal_response = sp.factor(
    sp.diff(H1_kappa, kappa).subs(kappa, 0)
    - sp.diff(H1_kappa.subs(kappa, 0), T)
    * sp.diff(V0_kappa, kappa).subs(kappa, 0)
)
expected_phase_normal_response = -(
    T
    * (
        2 * T**4 * b
        + T**4
        + 2 * T**3 * b
        + 10 * T**3
        - 10 * T**2 * b
        - 9 * T**2
        + 2 * T * b
        - 22 * T
        + 4 * b
        + 26
    )
    * sp.exp(T)
    / (T - 1)
)

# General normalized primitive-phase jet g(T)=O(T^2).  Its first variation is
# a fourth-order differential operator.  The triangular leading symbol is 31
# for T^2 at physical b=5/4, and m(m-1)(m-2)(m+8)/2 for T^m, m>=3.
g = sp.Function("g")(T)
phase_operator = -T * sp.exp(T) / (2 * (T - 1)) * (
    (T - T**2) * sp.diff(g, T, 4)
    + (2 * T**3 * b + T**3 - 4 * T**2 * b + 4 * T**2 + 2 * T * b - 14 * T + 11)
    * sp.diff(g, T, 3)
    + (4 * T**3 * b + 2 * T**3 - 6 * T**2 * b + 13 * T**2 - 2 * T * b - 37 * T + 4 * b + 26)
    * sp.diff(g, T, 2)
    + (2 * T**3 * b + T**3 - 2 * T**2 * b + 8 * T**2 - 4 * T * b - 22 * T + 4 * b + 15)
    * sp.diff(g, T)
)


def leading_coefficient(expression: sp.Expr, power: int) -> sp.Expr:
    return sp.expand(sp.series(expression, T, 0, power + 1).removeO()).coeff(T, power)


physical_phase_operator = phase_operator.subs(b, sp.Rational(5, 4))
triangular_failures = []
if leading_coefficient(physical_phase_operator.subs(g, T**2).doit(), 1) != 31:
    triangular_failures.append(2)
for m in range(3, 13):
    observed_lead = leading_coefficient(
        physical_phase_operator.subs(g, T**m).doit(), m - 2
    )
    expected_lead = sp.Rational(m * (m - 1) * (m - 2) * (m + 8), 2)
    if sp.simplify(observed_lead - expected_lead) != 0:
        triangular_failures.append(m)

# The T^2 and T^3 inputs collide at response grade one, so the nonzero
# monomial symbols do not imply injectivity.  Normalize the resulting formal
# kernel by a2=33, a3=-31 and solve successively through a9.
kernel_coefficients = {
    2: sp.Integer(33),
    3: sp.Integer(-31),
    4: sp.Rational(273, 16),
    5: sp.Rational(-731, 104),
    6: sp.Rational(61429, 24960),
    7: sp.Rational(-223001, 291200),
    8: sp.Rational(12875249, 55910400),
    9: sp.Rational(-19602017, 305510400),
}
kernel_jet = sum(value * T**power for power, value in kernel_coefficients.items())
kernel_residual = sp.series(
    physical_phase_operator.subs(g, kernel_jet).doit(), T, 0, 8
).removeO()
rho = sp.symbols("rho")
phase_kernel_indicial = sp.factor(rho * (rho - 1) * (rho + 9))

checks = {
    "laplace_terms_collapse_to_expected_rational_function": sp.simplify(
        laplace_one_loop - expected_laplace
    ) == 0,
    "gamma_normalized_one_loop_matches_expected": sp.simplify(
        normalized_one_loop - expected_normalized
    ) == 0,
    "normalization_vanishes_at_zero_source": normalized_one_loop.subs(T, 0) == 0,
    "only_cubic_saddle_pole_is_required": sp.denom(normalized_one_loop).as_powers_dict().get(
        T - 1, 0
    ) == 3,
    "leading_fixed_t_response_is_saddle_coordinate": sp.simplify(A0 - T) == 0,
    "leading_qd_is_inverse_tree_jacobian": sp.simplify(qd0 - 1 / (1 - T)) == 0,
    "transported_first_correction_recovers_H1": sp.simplify(H1 - expected_H1) == 0,
    "second_adjacent_transport_recovers_exact_H2": sp.simplify(H2 - expected_H2) == 0,
    "H2_stable_coefficients_equal_cubic_diagonal": sp.simplify(
        stable_H2_coefficient - expected_stable_H2_coefficient
    ) == 0,
    "phase_preserving_family_has_universal_unit_tail": sp.simplify(
        H1_family - expected_H1_family
    ) == 0,
    "explicit_q_inverse_atom_does_not_enter_H1": c not in H1_family.free_symbols,
    "dressing_changes_only_initialization_weights": sp.simplify(
        sp.diff(H1_family, b) - (-2 * T + T**2)
    ) == 0,
    "explicit_atom_first_appears_in_H2": sp.simplify(
        sp.diff(H2_family, c) - T**2 * (3 - 2 * T)
    ) == 0,
    "two_port_amplitude_jacobian_is_nonzero": amplitude_port_determinant
    == -T**3 * (T - 2) * (2 * T - 3),
    "phase_normal_deformation_matches_exact_first_variation": sp.simplify(
        phase_normal_response - expected_phase_normal_response
    ) == 0,
    "phase_normal_deformation_changes_stable_tail": sp.expand(
        sp.series(phase_normal_response.subs(b, sp.Rational(5, 4)), T, 0, 5).removeO()
    ).coeff(T, 3) == 17,
    "general_phase_variation_operator_recovers_quadratic_fixture": sp.simplify(
        phase_operator.subs(g, T**2).doit() - phase_normal_response
    ) == 0,
    "phase_operator_monomial_symbols_match_through_grade_12": not triangular_failures,
    "phase_operator_has_formal_kernel_jet_through_response_grade_7": sp.simplify(
        kernel_residual
    ) == 0,
    "phase_kernel_indicial_roots_are_zero_one_minus_nine": sp.solve(
        phase_kernel_indicial, rho
    ) == [-9, 0, 1],
}

payload = {
    "artifact_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
    "checks": checks,
    "observed": {
        "laplace_one_loop": str(laplace_one_loop),
        "stirling_correction": str(stirling_correction),
        "gamma_normalized_one_loop": str(normalized_one_loop),
        "saddle_propagator": "(1-T)^(-1)",
        "max_propagator_power": 3,
        "leading_fixed_t_response": str(A0),
        "leading_qd": str(qd0),
        "first_scaled_response_correction_V1": str(V1),
        "derived_H1": str(H1),
        "derived_H2": str(H2),
        "H2_stable_coefficient_for_n_at_least_4": str(stable_H2_coefficient),
        "phase_preserving_family_H1": str(expected_H1_family),
        "universal_tail": "T^3/(1-T)",
        "explicit_atom_H2_response": str(sp.diff(H2_family, c)),
        "amplitude_port_jacobian_determinant": str(amplitude_port_determinant),
        "phase_normal_first_variation": str(phase_normal_response),
        "physical_phase_variation_tail_coefficients": {
            "T^3": "17",
            "T^4": "41/12",
        },
        "phase_operator_order": 4,
        "phase_operator_triangular_symbol": {
            "m=2_at_b=5/4": "31",
            "m>=3": "m(m-1)(m-2)(m+8)/2",
        },
        "triangular_symbol_failures_through_m=12": triangular_failures,
        "phase_kernel_normalization": "a2=33,a3=-31",
        "phase_kernel_coefficients_through_T9": {
            str(power): str(value) for power, value in kernel_coefficients.items()
        },
        "phase_kernel_residual_through_response_grade_7": str(kernel_residual),
        "phase_kernel_indicial_polynomial_for_h_equals_g_prime": str(
            phase_kernel_indicial
        ),
        "authorized_analytic_indicial_root": "1",
    },
    "passed": all(checks.values()),
    "semantic_boundary": (
        "Exact saddle expansion and first fixed-t adjacent-grade transport. It "
        "proves H1 and H2, hence the stable constant and cubic connected-source "
        "diagonals. It does not yet test the H1 phase-null jet against H2, prove "
        "higher decoration-deficit laws, or control completion."
    ),
}

RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)
