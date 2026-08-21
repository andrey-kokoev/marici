#!/usr/bin/env python3
"""Exact audit that the unpolarized Cut projector has two helicity lifts."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research" / "nima" / "results" / "helicity-cut-two-lift-ambiguity.json"


def main() -> None:
    I2 = sp.eye(2)
    swap = sp.Matrix([[0, 1], [1, 0]])
    p_plus = sp.Matrix([[1, 0], [0, 0]])
    p_minus = sp.Matrix([[0, 0], [0, 1]])
    total = p_plus + p_minus

    preserve = {"plus": p_plus, "minus": p_minus}
    exchange = {
        "plus": sp.simplify(swap * p_plus * swap),
        "minus": sp.simplify(swap * p_minus * swap),
    }
    preserve_total = preserve["plus"] + preserve["minus"]
    exchange_total = exchange["plus"] + exchange["minus"]

    assert preserve_total == total == I2
    assert exchange_total == total
    assert exchange["plus"] == p_minus
    assert exchange["minus"] == p_plus
    assert preserve["plus"] != exchange["plus"]

    r, s = sp.symbols("r s", real=True)
    even_state = sp.Matrix([r, 0, 0, s])
    crossed_state = sp.kronecker_product(I2, swap) * even_state
    assert crossed_state == sp.Matrix([0, r, s, 0])
    norm_residual = sp.simplify((crossed_state.T * crossed_state)[0] - (even_state.T * even_state)[0])
    assert norm_residual == 0

    result = {
        "schema": "marici.helicity-cut-two-lift-ambiguity.v1",
        "strength": "exact finite lifting obstruction",
        "all_outgoing_cut_input": "Q(-k)=Q(k), established for the summed physical projector",
        "trace_projector": str(total),
        "preserving_lift": {k: str(v) for k, v in preserve.items()},
        "exchanging_lift": {k: str(v) for k, v in exchange.items()},
        "both_forget_to_same_trace_projector": preserve_total == exchange_total == total,
        "lifts_are_distinct": preserve["plus"] != exchange["plus"],
        "example_preserving_state": str(even_state),
        "example_exchanged_state": str(crossed_state),
        "norm_residual": str(norm_residual),
        "lift_fiber": "Z/2: preserve helicity or exchange helicity at the opposite occurrence",
        "missing_selector": "source-defined oriented crossing/Hodge-star convention on the two Cut occurrences",
        "conclusion": (
            "Trace-strict physical Cut does not determine helicity-resolved Cut. Both lifts have "
            "the same metric projector and norm but act differently on the Bell state. A source "
            "crossing/orientation datum is required before forming the doubled Bell square."
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["content_sha256"] = hashlib.sha256(canonical).hexdigest().upper()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "same_trace": result["both_forget_to_same_trace_projector"],
        "distinct_lifts": result["lifts_are_distinct"],
        "sha256": result["content_sha256"],
    }))


if __name__ == "__main__":
    main()
