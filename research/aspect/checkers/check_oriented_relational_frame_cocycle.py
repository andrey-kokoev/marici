#!/usr/bin/env python3
"""Check the reflection kernel, Bargmann separator, and robust rank gates."""
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASPECT = HERE.parent
CONTRACT = ASPECT / "contracts" / "oriented-relational-frame-cocycle.v1.json"
RESULT = ASPECT / "results" / "oriented_relational_frame_cocycle.json"


def inner(a, b):
    return sum(x.conjugate() * y for x, y in zip(a, b))


def fidelity(a, b):
    return abs(inner(a, b)) ** 2


def bloch_state(x, y, z):
    return (
        math.sqrt((1 + z) / 2) + 0j,
        cmath.exp(1j * math.atan2(y, x)) * math.sqrt((1 - z) / 2)
    )


def fidelity_gram(states):
    return [[2 * fidelity(a, b) for b in states] for a in states]


def bargmann(a, b, c):
    return inner(a, b) * inner(b, c) * inner(c, a)


def apply_unitary(u, state):
    return tuple(sum(u[i][j] * state[j] for j in range(2)) for i in range(2))


def close_matrix(a, b, tol=1e-12):
    return all(abs(a[i][j] - b[i][j]) < tol for i in range(len(a)) for j in range(len(a)))


def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    q = 1 / math.sqrt(3)
    signs = ([1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1])
    tetra = [bloch_state(x*q, y*q, z*q) for x, y, z in signs]
    mirror = [tuple(x.conjugate() for x in state) for state in tetra]

    original_gram = fidelity_gram(tetra)
    mirror_gram = fidelity_gram(mirror)
    original_b = bargmann(tetra[0], tetra[1], tetra[2])
    mirror_b = bargmann(mirror[0], mirror[1], mirror[2])

    theta, phi = 0.31, -0.52
    u = (
        (math.cos(theta), -cmath.exp(1j*phi)*math.sin(theta)),
        (cmath.exp(-1j*phi)*math.sin(theta), math.cos(theta))
    )
    transported = [apply_unitary(u, state) for state in tetra]
    transported_b = bargmann(transported[0], transported[1], transported[2])

    rephased = [
        tuple(cmath.exp(1j * phase) * x for x in state)
        for state, phase in zip(tetra, (0.2, -0.7, 1.1, -0.4))
    ]
    rephased_b = bargmann(rephased[0], rephased[1], rephased[2])

    delta = contract["uncertainty"]["overlap_entry_threshold_delta"]
    tetra_min, tetra_max = 4/3, 4
    selector_min, selector_max = (5-math.sqrt(13))/2, (5+math.sqrt(13))/2
    tetra_bound = math.sqrt((tetra_max + 8*delta) / (tetra_min - 8*delta))
    selector_bound = math.sqrt((selector_max + 8*delta) / (selector_min - 8*delta))

    checks = {
        "pairwise_fidelities_miss_mirror": close_matrix(original_gram, mirror_gram),
        "tetrahedral_triple_has_nonzero_orientation": abs(original_b.imag) > 1e-12,
        "mirror_flips_oriented_cocycle": abs(mirror_b - original_b.conjugate()) < 1e-12,
        "common_unitary_preserves_cocycle": abs(transported_b - original_b) < 1e-12,
        "independent_rephasing_preserves_cocycle": abs(rephased_b - original_b) < 1e-12,
        "tetrahedral_uncertainty_gate_open": delta < contract["uncertainty"]["tetrahedral_full_rank_threshold"],
        "selector_uncertainty_gate_open": delta < contract["uncertainty"]["selector_full_rank_threshold"],
        "robust_condition_bounds_finite": math.isfinite(tetra_bound) and math.isfinite(selector_bound),
        "claim_boundary_preserved": not any(contract["claim_boundary"].values())
    }
    passed = all(checks.values())
    out = {
        "schema": "marici.aspect.oriented-relational-frame-cocycle-result.v1",
        "passed": passed,
        "bargmann_original": [original_b.real, original_b.imag],
        "bargmann_mirror": [mirror_b.real, mirror_b.imag],
        "tetrahedral_condition_upper_bound_at_delta": tetra_bound,
        "selector_condition_upper_bound_at_delta": selector_bound,
        "checks": checks,
        "physical_status": "not_run",
        "conclusion": "pairwise_metric_needs_one_oriented_triple_cocycle_to_remove_reflection_kernel"
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
