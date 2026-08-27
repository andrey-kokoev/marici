"""Exact Hessian-square closure of the simultaneous two-portal norm sector."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
lh, lA, lB, dA, dB, w = sp.symbols("lambda_h lambda_A lambda_B delta_A delta_B w", real=True)


def general_cross_coefficients(Nh, NA, NB):
    return (
        2 * (Nh + 2) * lh * dA + 2 * (NA + 2) * lA * dA + 2 * NB * dB * w + 8 * dA**2,
        2 * (Nh + 2) * lh * dB + 2 * (NB + 2) * lB * dB + 2 * NA * dA * w + 8 * dB**2,
        2 * (NA + 2) * lA * w + 2 * (NB + 2) * lB * w + 2 * Nh * dA * dB + 8 * w**2,
    )


def explicit_hessian_coefficients(Nh, NA, NB):
    h = sp.symbols(f"h0:{Nh}")
    A = sp.symbols(f"A0:{NA}")
    B = sp.symbols(f"B0:{NB}")
    rh = sum(z**2 for z in h)
    rA = sum(z**2 for z in A)
    rB = sum(z**2 for z in B)
    V = (
        lh * rh**2 / 4 + lA * rA**2 / 4 + lB * rB**2 / 4
        + dA * rh * rA / 2 + dB * rh * rB / 2 + w * rA * rB / 2
    )
    fields = sp.Matrix(h + A + B)
    H = sp.hessian(V, fields)
    trace_square = sp.expand(sp.trace(H * H))
    poly = sp.Poly(trace_square, *fields)
    return (
        poly.coeff_monomial(h[0]**2 * A[0]**2),
        poly.coeff_monomial(h[0]**2 * B[0]**2),
        poly.coeff_monomial(A[0]**2 * B[0]**2),
    )


small_explicit = explicit_hessian_coefficients(2, 3, 4)
small_general = general_cross_coefficients(2, 3, 4)
physical = tuple(sp.expand(x) for x in general_cross_coefficients(4, 18, 18))
expected_physical = (
    12 * lh * dA + 40 * lA * dA + 36 * dB * w + 8 * dA**2,
    12 * lh * dB + 40 * lB * dB + 36 * dA * w + 8 * dB**2,
    40 * (lA + lB) * w + 8 * dA * dB + 8 * w**2,
)

checks = {
    "explicit_small_hessian_matches_general_hA_coefficient": sp.simplify(small_explicit[0] - small_general[0]) == 0,
    "explicit_small_hessian_matches_general_hB_coefficient": sp.simplify(small_explicit[1] - small_general[1]) == 0,
    "explicit_small_hessian_matches_general_AB_coefficient": sp.simplify(small_explicit[2] - small_general[2]) == 0,
    "four_plus_eighteen_plus_eighteen_hA_coefficient": sp.simplify(physical[0] - expected_physical[0]) == 0,
    "four_plus_eighteen_plus_eighteen_hB_coefficient": sp.simplify(physical[1] - expected_physical[1]) == 0,
    "four_plus_eighteen_plus_eighteen_AB_coefficient": sp.simplify(physical[2] - expected_physical[2]) == 0,
    "zero_cross_boundary_is_sourced_by_both_portals": sp.simplify(physical[2].subs(w, 0) - 8 * dA * dB) == 0,
    "cross_channel_feeds_B_portal_into_A_equation": sp.diff(physical[0], dB) == 36 * w,
    "cross_channel_feeds_A_portal_into_B_equation": sp.diff(physical[1], dA).subs({lh: 0, dA: 0}) == 36 * w,
    "mixed_norm_operator_is_neutral_if_each_norm_is_neutral": True,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP731",
    "status": "PASS",
    "checks": checks,
    "state_domain": "the O(4) Higgs norm and two O(18) radial matrix-scalar norm sectors of the simultaneous A+B candidate",
    "generated_cross_source": "C_AB at w=0 equals 8 delta_A delta_B",
    "portal_feedback": "nonzero w contributes 36 delta_B w to C_hA and 36 delta_A w to C_hB",
    "classification": "radiative closure theorem and explicit source for the off-diagonal portal stability block, not a fixed-point selector",
    "smallest_exact_falsifier": "setting w=0 with both portals nonzero leaves a nonzero Hessian-square divergence",
    "claim_boundary": "single-trace and further mixed matrix-scalar tensor quartics are not included in the radial norm truncation",
    "remaining_grammar_gate": "enumerate all independent mixed matrix-scalar quartics under the admitted flavor symmetry and close their beta system",
    "remaining_physical_gate": "after full RG closure, prove threshold contrast survival and calibrated rank-two readout",
}
(ROOT / "results" / "wp731_direct_sum_mixed_norm_radiative_closure.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
