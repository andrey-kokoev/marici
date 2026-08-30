#!/usr/bin/env python3
"""Exact scaling and tensor-naturality audit for the Born readout bridge."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research" / "nima" / "results" / "born-readout-variance-obstruction.json"


def main() -> None:
    x, y, a, b = sp.symbols("x y a b", real=True)
    amplitude = x + sp.I * y
    scalar = a + sp.I * b
    born = sp.expand(amplitude * sp.conjugate(amplitude))
    scaled_born = sp.expand((scalar * amplitude) * sp.conjugate(scalar * amplitude))
    quadratic_residual = sp.simplify(scaled_born - (a**2 + b**2) * born)

    # A complex-linear probability functional would obey L(iA)=iL(A), while
    # phase invariance requires L(iA)=L(A); hence (i-1)L(A)=0.
    phase_linearity_obstruction = sp.I - 1
    assert quadratic_residual == 0
    assert phase_linearity_obstruction != 0

    # Tensorial Cut compatibility: if C is the amplitude Cut map, density
    # transport is C tensor conjugate(C). Verify functorial composition on a
    # generic finite matrix packet.
    c11, c12, c21, c22 = sp.symbols("c11 c12 c21 c22", real=True)
    d11, d12, d21, d22 = sp.symbols("d11 d12 d21 d22", real=True)
    C = sp.Matrix([[c11, c12], [c21, c22]])
    D = sp.Matrix([[d11, d12], [d21, d22]])
    doubled_composite = sp.kronecker_product(D * C, D * C)
    composite_doubles = sp.kronecker_product(D, D) * sp.kronecker_product(C, C)
    tensor_naturality_residual = sp.simplify(doubled_composite - composite_doubles)
    assert tensor_naturality_residual == sp.zeros(4)

    result = {
        "schema": "marici.born-readout-variance-obstruction.v1",
        "strength": "exact algebraic typing theorem",
        "born_norm": str(born),
        "scaled_born_norm": str(scaled_born),
        "quadratic_scaling_residual": str(quadratic_residual),
        "phase_invariance_vs_complex_linearity_obstruction": str(phase_linearity_obstruction),
        "nonzero_complex_linear_phase_invariant_map_exists": False,
        "minimal_typed_domain": "A tensor conjugate(A), followed by positive evaluation and trace normalization",
        "doubled_cut_map": "C tensor conjugate(C)",
        "doubled_cut_composition_residual_rank": tensor_naturality_residual.rank(),
        "conclusion": (
            "The Born bridge cannot be a nonzero complex-linear counit on amplitudes. "
            "It requires conjugate doubling; normalization is additionally projective/rational. "
            "Strict amplitude Cut maps lift functorially to the doubled object, but positivity, "
            "physical analyzer effects, and nonzero normalization remain separate source data."
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["content_sha256"] = hashlib.sha256(canonical).hexdigest().upper()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "linear_bridge": False,
        "doubled_cut_residual_rank": tensor_naturality_residual.rank(),
        "sha256": result["content_sha256"],
    }))


if __name__ == "__main__":
    main()
