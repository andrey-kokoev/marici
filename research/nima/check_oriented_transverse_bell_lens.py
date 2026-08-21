#!/usr/bin/env python3
"""Exact two-dimensional real-form construction of helicity and analyzer effects."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research" / "nima" / "results" / "oriented-transverse-bell-lens.json"


def zero(matrix: sp.Matrix) -> bool:
    return matrix.applyfunc(sp.simplify) == sp.zeros(*matrix.shape)


def main() -> None:
    I2 = sp.eye(2)
    J = sp.Matrix([[0, -1], [1, 0]])
    p_plus = (I2 - sp.I * J) / 2
    p_minus = (I2 + sp.I * J) / 2

    helicity_checks = {
        "J_squared_plus_identity": zero(J * J + I2),
        "P_plus_idempotent": zero(p_plus * p_plus - p_plus),
        "P_minus_idempotent": zero(p_minus * p_minus - p_minus),
        "P_sum_identity": zero(p_plus + p_minus - I2),
        "P_product_zero": zero(p_plus * p_minus),
        "P_plus_hermitian": zero(p_plus.conjugate().T - p_plus),
        "P_minus_hermitian": zero(p_minus.conjugate().T - p_minus),
        "conjugation_swaps_helicity": zero(p_plus.conjugate() - p_minus),
    }
    assert all(helicity_checks.values())

    phi = sp.symbols("phi", real=True)
    analyzer = sp.Matrix([[0, sp.exp(-sp.I * phi)], [sp.exp(sp.I * phi), 0]])
    e_plus = (I2 + analyzer) / 2
    e_minus = (I2 - analyzer) / 2
    analyzer_checks = {
        "observable_hermitian": zero(analyzer.conjugate().T - analyzer),
        "observable_binary": zero(analyzer * analyzer - I2),
        "effects_exhaust_identity": zero(e_plus + e_minus - I2),
        "effects_orthogonal": zero(e_plus * e_minus),
        "effect_plus_projector": zero(e_plus * e_plus - e_plus),
        "effect_minus_projector": zero(e_minus * e_minus - e_minus),
    }
    assert all(analyzer_checks.values())

    # Reversing transverse orientation sends J -> -J and swaps helicity, while
    # leaving the unordered two-outcome measurement complete.
    reversed_plus = (I2 - sp.I * (-J)) / 2
    orientation_check = zero(reversed_plus - p_minus)
    assert orientation_check

    result = {
        "schema": "marici.oriented-transverse-bell-lens.v1",
        "strength": "exact local coefficient construction",
        "input": "oriented real metric transverse plane (V,g,J), J^2=-1",
        "helicity_projectors": {
            "plus": str(p_plus),
            "minus": str(p_minus),
        },
        "helicity_checks": helicity_checks,
        "analyzer_observable": str(analyzer),
        "analyzer_checks": analyzer_checks,
        "orientation_reversal_swaps_helicity": orientation_check,
        "derived_structures": [
            "complex conjugation exchanging helicities",
            "orthogonal exhaustive helicity effects",
            "a continuous family of Hermitian binary analyzer effects",
        ],
        "not_derived": [
            "the transverse orientation/complex structure on the admitted Ward quotient",
            "the physical detector angles",
            "the Born pairing and accepted-event normalization",
        ],
        "conclusion": (
            "Once an oriented transverse real form is supplied, conjugation and local binary "
            "analyzer effects require no new carrier divisor. The current Ward packet supplies "
            "the quotient and metric trace but does not serialize the orientation/Hodge operator J."
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["content_sha256"] = hashlib.sha256(canonical).hexdigest().upper()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "helicity_checks": all(helicity_checks.values()),
        "analyzer_checks": all(analyzer_checks.values()),
        "sha256": result["content_sha256"],
    }))


if __name__ == "__main__":
    main()
