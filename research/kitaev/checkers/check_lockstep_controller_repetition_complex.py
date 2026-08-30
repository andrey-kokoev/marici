#!/usr/bin/env python3
"""Exact repetition-code complex for lockstep controller redundancy."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
FINITE = K / "results" / "s3-lockstep-controller-redundancy.json"
OUT = K / "results" / "lockstep-controller-repetition-complex.json"


def rank_mod2(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    a = [row[:] for row in matrix]
    rank = 0
    for column in range(len(a[0])):
        pivot = next((r for r in range(rank, len(a)) if a[r][column]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for r in range(len(a)):
            if r != rank and a[r][column]:
                a[r] = [x ^ y for x, y in zip(a[r], a[rank])]
        rank += 1
    return rank


def syndrome(word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(word[j] ^ word[j+1] for j in range(len(word)-1))


def hamming(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(x != y for x, y in zip(left, right))


def main() -> None:
    census = {}
    for n in range(1, 8):
        ones = (1,) * n
        zero = (0,) * n
        code = {zero, ones}
        parity_check = [[int(column in (row, row+1)) for column in range(n)]
                        for row in range(n-1)]
        kernel = {word for word in itertools.product((0, 1), repeat=n)
                  if syndrome(word) == (0,) * (n-1)}
        assert kernel == code
        assert rank_mod2(parity_check) == n-1
        assert syndrome(ones) == (0,) * (n-1)
        distance = hamming(zero, ones)
        assert distance == n

        detection = {}
        correction = {}
        for s in range(n+1):
            all_nonzero_errors_detected = all(
                syndrome(error) != (0,) * (n-1)
                for error in itertools.product((0, 1), repeat=n)
                if 1 <= sum(error) <= s
            )
            detection[str(s)] = all_nonzero_errors_detected
            assert all_nonzero_errors_detected == (s < n)
        for t in range(n+1):
            ball0 = {word for word in itertools.product((0, 1), repeat=n)
                     if hamming(word, zero) <= t}
            ball1 = {word for word in itertools.product((0, 1), repeat=n)
                     if hamming(word, ones) <= t}
            unique = ball0.isdisjoint(ball1)
            correction[str(t)] = unique
            assert unique == (2*t < n)
        census[str(n)] = {
            "rank_H": rank_mod2(parity_check),
            "kernel_size": len(kernel),
            "minimum_distance": distance,
            "detects_up_to_s": detection,
            "corrects_up_to_t": correction,
        }

    finite = json.loads(FINITE.read_text(encoding="utf-8"))
    assert finite["minimality"]["minimum_copies_for_detection"] == 2
    assert finite["minimality"]["minimum_copies_for_correction"] == 3
    result = {
        "schema": "marici.kitaev.lockstep-controller-repetition-complex.v1",
        "inputs_sha256": {
            str(FINITE.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(FINITE.read_bytes()).hexdigest()
        },
        "exact_complex": {
            "sequence": "0 -> F2 --E_n--> F2^n --H_n--> F2^(n-1) -> 0",
            "encoding": "E_n(b)=b*1_n",
            "parity_check": "H_n(x)_j=x_j+x_(j+1)",
            "boundary_squared_zero": "H_n E_n=0",
            "exactness": "ker H_n=im E_n=span{1_n}; rank H_n=n-1",
        },
        "coding_theorem": {
            "code": "binary repetition [n,1,n]",
            "minimum_distance": "d=n",
            "detect_s_errors_iff": "n >= s+1",
            "correct_t_errors_iff": "n >= 2t+1",
            "common_mode_error": "1_n is the nonzero codeword, has zero syndrome, and acts as logical X",
        },
        "fanout": {
            "map": "F:F2 -> F2^4, F(b)=b*1_4",
            "controller_pipeline": "command -> E_n -> syndrome/decode -> F -> four actuators",
            "common_mode_image": "logical X before F becomes simultaneous four-actuator command inversion",
        },
        "exhaustive_census_n_1_through_7": census,
        "lens_separation": {
            "shared_Carrier_geometry": [
                "repetition complex", "syndrome quotient", "distance", "fanout incidence map"
            ],
            "quantum_coefficient_lens_required_for": [
                "mapping actuator-command inversion to encoded Pauli/CPTP faults",
                "recovery and exRec semantics", "T-equivalent interface cost"
            ],
        },
        "verdict": "Controller redundancy is the exact binary repetition complex. Two-copy detection and three-copy correction are the n=2 and n=3 cases of d=n: n>=s+1 detects s errors and n>=2t+1 corrects t errors. The all-replica common mode is not a syndrome defect but the logical X codeword, whose four-port fanout inverts every actuator command. This algebra is shared Carrier geometry; its physical quantum meaning requires the coefficient lens.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
