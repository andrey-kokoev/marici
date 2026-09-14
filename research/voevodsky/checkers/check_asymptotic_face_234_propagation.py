#!/usr/bin/env python3
"""Check combinatorial and exponent-level propagation of the H_234 remainder.

This verifies only the rapid-decay bookkeeping used by the seventh edgewise
subdivision. It does not prove Connes's analytic remainder estimate or
positivity.
"""
from fractions import Fraction
import json
from pathlib import Path


def propagated_order(alpha: Fraction, requested_order: int) -> int:
    """Choose source decay order M so alpha*M >= requested_order."""
    return (requested_order * alpha.denominator + alpha.numerator - 1) // alpha.numerator


def main() -> None:
    # Seven positive cutoff scales; deliberately nonuniform.
    alphas = tuple(Fraction(i, 7) for i in range(1, 8))
    cells = []
    target_orders = (1, 2, 5, 10, 25)

    for i in range(7):
        for j in range(7):
            for k in range(7):
                # A translated cell may meet three independently rescaled rows.
                # Products/composites are controlled by the weakest exponent.
                alpha = min(alphas[i], alphas[j], alphas[k])
                witnesses = {}
                for n in target_orders:
                    m = propagated_order(alpha, n)
                    assert alpha * m >= n
                    witnesses[str(n)] = m
                cells.append({
                    "index": [i, j, k],
                    "minimum_cutoff_exponent": str(alpha),
                    "source_orders_for_target_orders": witnesses,
                })

    assert len(cells) == 7 ** 3 == 343
    assert min(alphas) > 0

    result = {
        "schema": "marici.voevodsky.asymptotic-face-234-propagation.v1",
        "subdivision_order": 7,
        "elementary_tetrahedra": len(cells),
        "cutoff_exponents": [str(a) for a in alphas],
        "minimum_exponent": str(min(alphas)),
        "orders_tested": list(target_orders),
        "all_cells_preserve_rapid_decay": True,
        "reason": (
            "For alpha>0 and every requested n, choose M with alpha*M>=n; "
            "then O((Lambda^alpha)^(-M)) is O(Lambda^(-n))."
        ),
        "claim_boundary": (
            "Finite combinatorial/exponent check only; assumes the source "
            "O(Lambda^-N) estimate and bounded-packet continuity."
        ),
        "cells": cells,
    }

    out = Path(__file__).parents[1] / "results" / "asymptotic_face_234_propagation.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "cells"}, indent=2))


if __name__ == "__main__":
    main()
