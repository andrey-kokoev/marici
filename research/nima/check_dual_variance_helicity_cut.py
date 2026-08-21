#!/usr/bin/env python3
"""Exact invariance of the polarization Cut coevaluation under paired frames."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research" / "nima" / "results" / "dual-variance-helicity-cut.json"


def main() -> None:
    a, b, c, d = sp.symbols("a b c d")
    U = sp.Matrix([[a, b], [c, d]])
    determinant = sp.det(U)
    U_dual = sp.simplify(U.inv().T)
    omega = sp.Matrix([1, 0, 0, 1])  # e_+ tensor e^+ + e_- tensor e^-
    paired = sp.simplify(sp.kronecker_product(U, U_dual) * omega)
    paired_residual = paired.applyfunc(lambda x: sp.factor(x)) - omega
    assert paired_residual.applyfunc(sp.simplify) == sp.zeros(4, 1)

    swap = sp.Matrix([[0, 1], [1, 0]])
    one_sided_swap = sp.kronecker_product(sp.eye(2), swap) * omega
    paired_swap = sp.kronecker_product(swap, swap.inv().T) * omega
    assert one_sided_swap != omega
    assert paired_swap == omega

    result = {
        "schema": "marici.dual-variance-helicity-cut.v1",
        "strength": "exact mixed-variance lifting theorem",
        "cut_tensor": "omega=e_+ tensor e^+ + e_- tensor e^- in V tensor V*",
        "generic_frame": str(U),
        "generic_frame_determinant": str(determinant),
        "dual_frame": str(U_dual),
        "paired_frame_residual": [str(sp.simplify(x)) for x in paired_residual],
        "one_sided_helicity_swap_changes_tensor": one_sided_swap != omega,
        "paired_helicity_swap_preserves_tensor": paired_swap == omega,
        "conclusion": (
            "The Z/2 alternatives of the ket-ket presentation are not distinct physical Cut "
            "maps once the second occurrence is correctly typed as dual. Any GL(2) frame "
            "change, including helicity swap, is canceled by contragredient transport. "
            "External detector frames remain physical inputs and are not fixed by this theorem."
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["content_sha256"] = hashlib.sha256(canonical).hexdigest().upper()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "generic_residual_zero": all(x == "0" for x in result["paired_frame_residual"]),
        "paired_swap_invariant": result["paired_helicity_swap_preserves_tensor"],
        "sha256": result["content_sha256"],
    }))


if __name__ == "__main__":
    main()
