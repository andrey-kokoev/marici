#!/usr/bin/env python3
"""Independent exact audit of the native Clark common-frame bulk identity."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
G = ROOT / "research" / "grothendieck"
SWAP = G / "theta-clark-sheet-swap-natively-reverses-spin-two.md"
BULK = G / "theta-clark-sheet-bulks-sum-to-an-exact-faithful-gram-trace.md"
OUT = ROOT / "research" / "kitaev" / "results" / "clark-bulk-common-frame-audit.json"


def quadratic_matrix(expr: sp.Expr, variables: list[sp.Symbol]) -> sp.Matrix:
    return sp.hessian(sp.expand(expr), variables) / 2


def main() -> None:
    xr, xi, zr, zi, a = sp.symbols("x_r x_i z_r z_i a", real=True)
    variables = [xr, xi, zr, zi]
    # X=G+f and Y=a*d_z G. Multiplication by i sends (yr,yi) to (-yi,yr).
    e_plus = (xr - a * zi) ** 2 + (xi + a * zr) ** 2
    e_minus = (xr + a * zi) ** 2 + (xi - a * zr) ** 2
    trace = xr**2 + xi**2 + a**2 * (zr**2 + zi**2)
    spin = 2 * a * (xi * zr - xr * zi)

    assert sp.expand(e_plus - (trace + spin)) == 0
    assert sp.expand(e_minus - (trace - spin)) == 0
    assert sp.expand(e_plus + e_minus - 2 * trace) == 0

    h_plus = quadratic_matrix(e_plus, variables)
    h_minus = quadratic_matrix(e_minus, variables)
    h_sum = sp.simplify(h_plus + h_minus)
    expected = sp.diag(2, 2, 2 * a**2, 2 * a**2)
    assert h_sum == expected
    assert sp.factor(h_sum.det()) == 16 * a**4
    assert h_sum.subs(a, 1).rank() == 4
    assert h_sum.subs(a, 0).rank() == 2
    assert h_plus.subs(a, 1).rank() == h_minus.subs(a, 1).rank() == 2

    # Direct sums preserve the identity labelwise at every finite cutoff N.
    cutoff_ranks = {}
    for n in range(1, 5):
        block = sp.diag(*([h_sum.subs(a, 1)] * n))
        assert block.rank() == 4 * n
        cutoff_ranks[str(n)] = block.rank()

    result = {
        "schema": "marici.kitaev.clark-bulk-common-frame-audit.v1",
        "source_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (SWAP, BULK)
        },
        "common_frame": {
            "coordinates": ["Re(G+f)", "Im(G+f)", "Re(d_z G)", "Im(d_z G)"],
            "formed_before_sheet_comparison": True,
            "E_plus": "T+S",
            "E_minus": "T-S",
            "sum": "2T",
        },
        "representation_audit": {
            "trace": "|G+f|^2+a^2|d_z G|^2",
            "odd_component": "2a Im((G+f) conjugate(d_z G))",
            "third_quadratic_component": False,
            "equal_sheet_coefficients": True,
        },
        "gram_matrix": {
            "sum_matrix": [[2, 0, 0, 0], [0, 2, 0, 0], [0, 0, "2a^2", 0], [0, 0, 0, "2a^2"]],
            "determinant": "16a^4",
            "rank_for_nonzero_a": 4,
            "rank_at_a_zero": 2,
            "faithful_on_feature_packet_for_nonzero_a": True,
        },
        "finite_cutoffs": {
            "checked_label_counts": [1, 2, 3, 4],
            "ranks_at_a_one": cutoff_ranks,
            "identity_is_labelwise": True,
        },
        "typing_boundary": {
            "feature_packet": "(G+f,a d_z G)",
            "gram_faithfulness_proves_state_faithfulness": False,
            "additional_required_map": "J_X: admissible boundary states -> feature packet",
            "additional_required_condition": "ker J_X=0, uniformly through completion",
            "unresolved_simultaneous_vanishing": ["G+f=0 almost everywhere", "d_z G=0 almost everywhere"],
        },
        "completion_boundary": {
            "finite_bulk_coefficients_closed": True,
            "defect_channels_closed": False,
            "uniform_lower_bound_proved": False,
        },
        "deliberate_falsifiers": {
            "a_zero": "determinant vanishes and rank drops from four to two",
            "state_feature_kernel": "a nonzero admissible state mapped to G+f=0 and d_z G=0 is invisible to the Gram trace",
        },
        "verdict": "The native Clark positive bulk resolves the common-frame, equal-coefficient, and representation-completeness gates exactly. Its Gram matrix is faithful on the four-real-dimensional feature packet for a nonzero Clark parameter and at every finite labelled direct sum. Faithfulness on admissible boundary states and completion stability remain separate injectivity and uniform-bound theorems.",
    }
    result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
