#!/usr/bin/env python3
"""Check projector-loop and cyclic-shift compilers for one Bargmann cocycle."""
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASPECT = HERE.parent
CONTRACT = ASPECT / "contracts" / "bargmann-cocycle-two-compiler-gate.v1.json"
RESULT = ASPECT / "results" / "bargmann_cocycle_two_compiler_gate.json"


def inner(a, b):
    return sum(x.conjugate() * y for x, y in zip(a, b))


def projector(state):
    return [[state[i] * state[j].conjugate() for j in range(2)] for i in range(2)]


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def kron3(a, b, c):
    out = [[0j for _ in range(8)] for _ in range(8)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                row = 4*i + 2*j + k
                for p in range(2):
                    for q in range(2):
                        for r in range(2):
                            col = 4*p + 2*q + r
                            out[row][col] = a[i][p] * b[j][q] * c[k][r]
    return out


def cyclic_shift(left=True):
    v = [[0j for _ in range(8)] for _ in range(8)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                source = 4*i + 2*j + k
                target = 4*j + 2*k + i if left else 4*k + 2*i + j
                v[target][source] = 1 + 0j
    return v


def bloch_state(x, y, z):
    return (
        math.sqrt((1 + z) / 2) + 0j,
        cmath.exp(1j * math.atan2(y, x)) * math.sqrt((1 - z) / 2)
    )


def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    q = 1 / math.sqrt(3)
    states = [
        bloch_state(q, q, q),
        bloch_state(q, -q, -q),
        bloch_state(-q, q, -q)
    ]
    p = [projector(state) for state in states]
    projector_loop = trace(mm(mm(p[0], p[1]), p[2]))
    projector_reverse = trace(mm(mm(p[0], p[2]), p[1]))

    product = kron3(p[0], p[1], p[2])
    cyclic = trace(mm(cyclic_shift(True), product))
    reverse_cyclic = trace(mm(cyclic_shift(False), product))

    pairwise_product = (
        abs(inner(states[0], states[1]))**2
        * abs(inner(states[1], states[2]))**2
        * abs(inner(states[2], states[0]))**2
    )
    expected_b = inner(states[0], states[1]) * inner(states[1], states[2]) * inner(states[2], states[0])

    checks = {
        "projector_loop_equals_Bargmann_cocycle": abs(projector_loop - expected_b) < 1e-12,
        "three_copy_cycle_equals_projector_loop": abs(cyclic - projector_loop) < 1e-12,
        "projector_reversal_conjugates": abs(projector_reverse - projector_loop.conjugate()) < 1e-12,
        "cycle_reversal_conjugates": abs(reverse_cyclic - cyclic.conjugate()) < 1e-12,
        "pairwise_product_is_only_squared_magnitude": abs(pairwise_product - abs(expected_b)**2) < 1e-12,
        "pairwise_product_loses_nonzero_orientation": pairwise_product > 0 and abs(expected_b.imag) > 1e-12,
        "three_cycle_needs_two_transpositions": contract["compiler_two"]["minimum_whole_copy_transpositions"] == 2,
        "claim_boundary_preserved": not any(contract["claim_boundary"].values())
    }
    passed = all(checks.values())
    out = {
        "schema": "marici.aspect.bargmann-cocycle-two-compiler-gate-result.v1",
        "passed": passed,
        "projector_loop": [projector_loop.real, projector_loop.imag],
        "three_copy_cycle": [cyclic.real, cyclic.imag],
        "reverse_cycle": [reverse_cyclic.real, reverse_cyclic.imag],
        "pairwise_product": pairwise_product,
        "checks": checks,
        "physical_status": "not_run",
        "conclusion": "two_exact_compilers_agree_pairwise_overlap_product_is_orientation_blind"
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
