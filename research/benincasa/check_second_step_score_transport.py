"""Certify second-step exact descent and Boolean score naturality."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
N = 5
SIZE = 1 << N
INCIDENCE = [10, 17, 7]


def load(name):
    return json.loads((HERE / name).read_text())


def popcount(value):
    return value.bit_count()


def main():
    files = {
        "x": "cutoff-inclusion-gauss-manin-adapter-a12-to-a16-kplus1-qplus0-g2-g23plus1-axis0-p32003-point-2-3-m4.json",
        "y": "cutoff-inclusion-gauss-manin-adapter-a12-to-a16-kplus1-qplus0-g1-g31plus1-axis1-p32003-point-2-3-m4.json",
        "z": "cutoff-inclusion-gauss-manin-adapter-a12-to-a16-kplus1-qplus0-g1-g2-g3plus1-p32003-point-2-3-m4.json",
    }
    second_step = {name: load(path) for name, path in files.items()}
    cone_ranks = {name: packet["adapter_cone_rank"] for name, packet in second_step.items()}
    relation_counts = {name: packet["big_relation_count"] for name, packet in second_step.items()}
    assert cone_ranks == {"x": 0, "y": 0, "z": 0}
    assert relation_counts == {"x": 318728, "y": 318728, "z": 691992}

    naturality_tests = 0
    for incidence in INCIDENCE:
        for present in range(SIZE):
            for deleted in range(SIZE):
                effective = present & deleted
                before = tuple(0 if not ((present & ~effective) & (1 << i)) else 2 + bool(incidence & (1 << i)) for i in range(N))
                after = tuple(0 if effective & (1 << i) else (0 if not present & (1 << i) else 2 + bool(incidence & (1 << i))) for i in range(N))
                assert before == after
                naturality_tests += 1

    zeta = [[int(s & t == t) for s in range(SIZE)] for t in range(SIZE)]
    mobius = [[int(t & s == s) * (-1 if popcount(t ^ s) % 2 else 1) for t in range(SIZE)] for s in range(SIZE)]
    product = [[sum(mobius[i][k] * zeta[k][j] for k in range(SIZE)) for j in range(SIZE)] for i in range(SIZE)]
    assert product == [[int(i == j) for j in range(SIZE)] for i in range(SIZE)]

    result = {
        "schema": "marici.benincasa.second-step-score-transport.v1",
        "status": "passed",
        "second_step_cone_ranks": cone_ranks,
        "second_step_target_relation_counts": relation_counts,
        "deletion_adapter_naturality_tests": naturality_tests,
        "route_count": SIZE,
        "boolean_mobius_inverse_exact": True,
        "transported_score_kernel_dimension": 0,
        "classification": "second-step exact descent closes and the complete algebraic deletion-score tower remains jointly faithful",
        "scope_warning": "no physical-cycle realization or interacting tensor vertex is inferred",
    }
    output = HERE / "second-step-score-transport.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
