#!/usr/bin/env python3
"""Construct the reflection-invariant character trace on the Z/3 norm grade."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "tate-product-phase-trace-readout.json"


def trace_value(k: int) -> int:
    # zeta^k + zeta^-k with zeta^2+zeta+1=0.
    return 2 if k % 3 == 0 else -1


def main() -> None:
    rows = []
    for k in range(3):
        trace = trace_value(k)
        detector = (2 - trace) // 3
        assert trace_value((-k) % 3) == trace
        assert detector == (0 if k == 0 else 1)
        rows.append(
            {
                "class": k,
                "character_trace": trace,
                "nontriviality_detector": detector,
            }
        )

    result = {
        "status": "PASS",
        "primitive_character_count": 2,
        "reflection_action": "chi_+ <-> chi_- by complex conjugation",
        "canonical_unframed_readout": "conjugate character pair",
        "trace_table": rows,
        "trace_distinguishes_zero_from_nonzero": True,
        "trace_distinguishes_orientation": False,
        "additive_complex_period": False,
        "source_flat_character_constructed": False,
        "next_gate": "construct a source-normalized flat Z/3 differential character on the all-soft relative pair",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
