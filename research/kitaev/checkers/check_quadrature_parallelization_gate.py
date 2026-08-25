#!/usr/bin/env python3
"""Exact distinction between common-frame and transported-sheet energy sums."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
PREVIOUS = K / "results" / "quadrature-sheet-torsor.json"
OUT = K / "results" / "quadrature-parallelization-gate.json"


def reduced_zero(matrix: sp.Matrix, c: sp.Symbol, s: sp.Symbol) -> bool:
    basis = sp.groebner([c**2 + s**2 - 1], c, s)
    return all(basis.reduce(sp.expand(entry))[1] == 0 for entry in matrix)


def main() -> None:
    c, s = sp.symbols("c s", real=True)
    I = sp.eye(2)
    Q = sp.Matrix([[c, s], [s, -c]])
    R = sp.Matrix([[-s, c], [c, s]])
    Ep, Em = I + Q, I - Q

    # Common-frame comparison: both forms act on one identified vector x.
    common_frame_sum = Ep + Em
    assert common_frame_sum == 2 * I

    # Covariant sheet comparison: the minus-sheet vector is Rx.
    transported_minus_on_source = R.T * Em * R
    assert reduced_zero(transported_minus_on_source - Ep, c, s)
    transported_sum = Ep + transported_minus_on_source
    assert reduced_zero(transported_sum - 2 * Ep, c, s)

    # Exact specialization exposes the rank distinction.
    q0 = sp.diag(1, -1)
    r0 = sp.Matrix([[0, 1], [1, 0]])
    ep0, em0 = I + q0, I - q0
    assert (ep0 + em0).rank() == 2
    assert (ep0 + r0.T * em0 * r0).rank() == 1

    # A comparison/parallelization P from minus coordinates back to plus
    # coordinates yields Ep + P^T Em P. Identity gives complementarity; the
    # sheet transport R gives duplication. Both are orthogonal, so positivity
    # alone cannot select the correct comparison.
    assert (ep0 + I.T * em0 * I) == 2 * I
    assert (ep0 + r0.T * em0 * r0) == 2 * ep0

    previous = json.loads(PREVIOUS.read_text(encoding="utf-8"))
    assert previous["sheet_energies"]["sum_rank"] == 2

    result = {
        "schema": "marici.kitaev.quadrature-parallelization-gate.v1",
        "input_sha256": hashlib.sha256(PREVIOUS.read_bytes()).hexdigest(),
        "common_frame": {
            "comparison": "E_plus(x)+E_minus(x)",
            "matrix": "(I+Q)+(I-Q)=2I",
            "theta_zero_rank": 2,
            "positive_definite": True,
        },
        "transported_frame": {
            "sheet_transport": "x_minus=R x_plus",
            "pulled_back_minus_form": "R^T(I-Q)R=I+Q",
            "comparison": "E_plus(x)+E_minus(Rx)",
            "matrix": "2(I+Q)",
            "theta_zero_rank": 1,
            "positive_definite": False,
        },
        "missing_datum": {
            "name": "cross-sheet amplitude parallelization P",
            "typed_map": "P: V_plus -> V_minus used to pull both forms to one source fiber",
            "required_test": "rank((I+Q)+P^T(I-Q)P)=2",
            "identity_parallelization_passes": True,
            "torsor_transport_parallelization_fails": True,
            "not_selected_by": ["orthogonality", "C2 equivariance", "individual sheet nonnegativity"],
        },
        "deliberate_falsifier": {
            "claim": "retaining both covariantly transported sheets automatically completes the norm",
            "counterexample": "R^T(I-Q)R=I+Q, so the sum is 2(I+Q) and retains the same null line",
        },
        "source_authority_boundary": "Fourier-Tate source data must derive the cross-sheet comparison map independently of the desired positive sum. Choosing P=I merely to obtain 2I is circular.",
        "verdict": "Opposite spin-two characters are necessary but not sufficient for rank-two positivity. The two sheet forms must also be compared in a source-derived common amplitude frame. Pullback by the very C2 transport that exchanges the sheets duplicates one rank-one form instead of complementing it.",
    }
    result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
