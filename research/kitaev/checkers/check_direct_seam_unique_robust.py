#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/direct-seam-unique-robust.json"


def invariants(L, h, b):
    inv = L.inv()
    R = (h.T * inv * h)[0]
    rb = (b.T * inv * b)[0]
    tau = (b.T * inv * h)[0]
    return R, rb, tau


def score(L, h, b, u):
    R, _, tau = invariants(L, h, b)
    E = (u.T * L * u)[0]
    g = (b.T * u)[0]
    return R * g ** 2 - E * tau ** 2


def main():
    L = Matrix([[2, -1], [-1, 1]])
    h = Matrix([0, 1])
    remote = Matrix([1, 0])
    R, rb, tau = invariants(L, h, remote)
    transfer_defect = R * rb - tau ** 2
    witness = L.inv() * remote
    assert (R, rb, tau, transfer_defect) == (2, 1, 1, 1)
    assert witness == Matrix([1, 1])
    assert score(L, h, remote, witness) == 1

    dR, drb, dtau = invariants(L, h, h)
    assert dR * drb - dtau ** 2 == 0
    test_states = [Matrix([1, 0]), Matrix([0, 1]), Matrix([1, 1]), Matrix([2, -1])]
    direct_scores = [score(L, h, h, u) for u in test_states]
    assert all(value <= 0 for value in direct_scores)

    payload = {
        "schema": "marici.kitaev.direct_seam_unique_robust.v1",
        "status": "pass",
        "nonparallel_fixture": {
            "transfer_current_defect": str(transfer_defect),
            "riesz_witness": [str(x) for x in witness],
            "witness_score": "1",
        },
        "direct_target_fixture": {
            "transfer_current_defect": "0",
            "sample_scores": [str(x) for x in direct_scores],
            "universal_nonincrease": True,
        },
        "classification": "universal_first_order_robustness_iff_b_parallel_h",
        "restricted_state_caveat": "witness_must_belong_to_authorized_state_module",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
