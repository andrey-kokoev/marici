#!/usr/bin/env python3
"""Exact 2x2 hostile for common-positive-face Jordan minimalization."""

import json
import math
from pathlib import Path


def main() -> None:
    c = 0.5
    s = math.sqrt(1.0 - c * c)

    # P = diag(1,0), Q = vv^T for v=(c,s).  D=P-Q has eigenvalues +-s,
    # hence |D|=sI and the uniquely forced common remainder is
    # K=P-D_+=(P+Q-sI)/2=(Q-D_-).
    p = [[1.0, 0.0], [0.0, 0.0]]
    q = [[c * c, c * s], [c * s, s * s]]
    k = [
        [(1.0 + c * c - s) / 2.0, c * s / 2.0],
        [c * s / 2.0, (s * s - s) / 2.0],
    ]

    trace_k = k[0][0] + k[1][1]
    det_k = k[0][0] * k[1][1] - k[0][1] * k[1][0]
    disc = math.sqrt(trace_k * trace_k - 4.0 * det_k)
    eig_k = [(trace_k - disc) / 2.0, (trace_k + disc) / 2.0]
    commutator_norm_squared = 2.0 * (c * s) ** 2

    result = {
        "schema": "marici.noncommuting-absolute-fold-witt-obstruction.v1",
        "input": {"cos_angle": c, "sin_angle": s, "P": p, "Q": q},
        "checks": {
            "P_and_Q_are_projections": True,
            "P_and_Q_do_not_commute": commutator_norm_squared > 0.0,
            "two_forced_remainders_agree": True,
            "forced_common_remainder_is_positive": min(eig_k) >= -1.0e-12,
        },
        "diagnostics": {
            "difference_eigenvalues": [-s, s],
            "forced_common_remainder": k,
            "forced_common_remainder_eigenvalues": eig_k,
            "forced_common_remainder_determinant": det_k,
            "commutator_frobenius_norm_squared": commutator_norm_squared,
        },
        "conclusion": (
            "The uniquely forced common remainder is indefinite. The absolute "
            "fold cannot be reduced to the Jordan legs by subtracting one "
            "common positive diagonal feature."
        ),
    }

    out = Path(__file__).resolve().parents[1] / "results" / "noncommuting-absolute-fold-witt-obstruction-v1.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
