#!/usr/bin/env python3
"""Exact Choi-rank and record-transfer audit for binary Lüders reset."""

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "nima" / "results" / "toric_reset_waste_port.json"


def rank_q(a):
    a = [[Fraction(x) for x in row] for row in a]
    r = 0
    for c in range(len(a[0])):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def main():
    # Choi matrix of rho -> Pi+ rho Pi+ + Pi- rho Pi- in column ordering.
    choi_dephase = [
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1],
    ]
    # Any pure fixed-apparatus return leaves one Kraus operator; identity is
    # the relevant QND candidate and has rank-one Choi matrix.
    choi_identity = [
        [1, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 1],
    ]
    rd = rank_q(choi_dephase)
    ri = rank_q(choi_identity)
    assert rd == 2 and ri == 1

    # Classical reversible record transfer: (p,r) -> (p xor r,r).
    # For the post-measurement diagonal p=r=s states this resets p but keeps r.
    transferred = {s: (s ^ s, s) for s in (0, 1)}
    assert transferred == {0: (0, 0), 1: (0, 1)}

    result = {
        "schema": "marici.toric-reset-waste-port.v1",
        "choi_rank": {"luders_nonselective": rd, "fixed_pure_apparatus_return": ri},
        "pointer_reset_map": {str(s): list(v) for s, v in transferred.items()},
        "gates": {
            "pointer_can_be_reset_by_record_transfer": True,
            "record_is_not_erased_by_pointer_reset": True,
            "closed_pure_apparatus_return_preserves_luders_channel": False,
            "nontrivial_waste_or_record_port_required": True,
        },
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
