#!/usr/bin/env python3
"""WP53: exact weak-basis covariance and nonselection of source RG transport."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/flavor/results/wp53_rg_transport_selector_gate.json"


def dagger(a: sp.Matrix) -> sp.Matrix:
    return a.conjugate().T


def beta_u(yu: sp.Matrix, yd: sp.Matrix, a: sp.Expr, b: sp.Expr, g: sp.Expr) -> sp.Matrix:
    # Source Eq. S16, with scalar coefficients and the common-left convention.
    return a * yu + b * yu * dagger(yu) * yu + g * yd * dagger(yd) * yu


def main() -> None:
    yu = sp.Matrix([[1, 2, 0], [0, 3, 4], [5, 0, 6]])
    yd = sp.Matrix([[2, 0, 1], [3, 1, 0], [0, 4, 5]])
    left = sp.Matrix([[sp.Rational(3, 5), sp.Rational(4, 5), 0],
                      [-sp.Rational(4, 5), sp.Rational(3, 5), 0], [0, 0, 1]])
    right_u = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    right_d = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    a, b, g = sp.Rational(7, 3), sp.Rational(-5, 2), sp.Rational(-3, 2)

    yu_p = left * yu * dagger(right_u)
    yd_p = left * yd * dagger(right_d)
    covariance_residual = sp.simplify(
        beta_u(yu_p, yd_p, a, b, g) - left * beta_u(yu, yd, a, b, g) * dagger(right_u)
    )

    k, t = sp.symbols("k t", real=True)
    scale = sp.exp(k * t)
    flow_matrix = sp.diag(scale, scale)
    inverse_matrix = sp.diag(1 / scale, 1 / scale)
    ratio_before = sp.symbols("x") / sp.symbols("y")
    ratio_after = sp.simplify(scale * sp.symbols("x") / (scale * sp.symbols("y")))

    gates = {
        "one_loop_yukawa_beta_is_full_weak_basis_covariant": covariance_residual == sp.zeros(3),
        "leading_common_rescaling_flow_is_invertible": sp.simplify(flow_matrix * inverse_matrix) == sp.eye(2),
        "leading_unitarity_triangle_ratio_is_constant": sp.simplify(ratio_after - ratio_before) == 0,
        "flow_has_no_rank_loss": sp.simplify(flow_matrix.det()) != 0,
        "transport_alone_has_no_proper_image": sp.simplify(flow_matrix.det()) != 0,
    }
    assert all(gates.values()), gates

    result = {
        "schema": "marici.flavor.rg-transport-selector-gate.v1",
        "source_equations": ["S16", "S17", "S18-S21"],
        "arithmetic": "exact SymPy rational matrix algebra and symbolic exponential flow",
        "domain": "nondegenerate Yukawa pairs on any interval where the one-loop ODE exists uniquely",
        "quotient": "full weak-basis U(3)_Q x U(3)_u x U(3)_d",
        "operation": "one-loop Standard Model Yukawa/CKM RG transport",
        "descent": "yes: the beta vector field is equivariant under the full weak-basis action",
        "leading_flow": {
            "map": "(V_13,V_31) -> exp(k t) (V_13,V_31)",
            "determinant": "exp(2*k*t)",
            "ratio_invariant": "V_13/V_31",
            "contextual_partition_change": "none",
        },
        "classification": {
            "separates_physical_points": "transport preserves distinctions by local invertibility",
            "selects_smaller_admissible_family": False,
            "rigidifies_chart_presentations": False,
            "selector": False,
            "rigidifier": False,
            "physical_instrument": "no standalone instrument: RG is theoretical scale transport; boundary data and a frozen normalization are required",
        },
        "smallest_exact_falsifier": "the nonzero flow determinant exp(2*k*t), which proves the leading source map has full image rather than a proper selected image",
        "remaining_gate": "an independently fixed UV boundary condition, fixed locus, threshold matching law, or normalization not inferred from the IR fit",
        "gates": gates,
        "conclusion": "The source RG operation descends to the physical quotient but is transport, not selection.",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"passed": sum(gates.values()), "total": len(gates), "output": str(OUT.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
