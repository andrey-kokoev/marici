#!/usr/bin/env python3
"""Construct the homotopy-coherent flat Z/3 character on the all-soft simplex."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "all-soft-flat-z3-character.json"
P = 3


def delta(vertex: tuple[int, int, int]) -> tuple[int, int, int]:
    # Oriented edges are 12,23,31.
    f1, f2, f3 = vertex
    return ((f2 - f1) % P, (f3 - f2) % P, (f1 - f3) % P)


def sub(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((x - y) % P for x, y in zip(a, b))


def add(*vectors: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(values) % P for values in zip(*vectors))


def main() -> None:
    boundary_cycle = (1, 1, 1)
    h = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    evaluations = [sum(x * y for x, y in zip(cochain, boundary_cycle)) % P for cochain in h]
    assert evaluations == [1, 1, 1]

    f01 = (0, 2, 0)
    f12 = (0, 0, 2)
    f20 = (0, 1, 1)
    assert delta(f01) == sub(h[1], h[0])
    assert delta(f12) == sub(h[2], h[1])
    assert delta(f20) == sub(h[0], h[2])
    assert add(f01, f12, f20) == (0, 0, 0)

    invariant_edge = (1, 1, 1)
    invariant_primitive = (0, 1, 2)
    assert delta(invariant_primitive) == invariant_edge

    result = {
        "status": "PASS",
        "relative_H2_mod3_generator_evaluation": 1,
        "flat_holonomy": "exp(2*pi*i/3)",
        "boundary_cycle": list(boundary_cycle),
        "cyclic_boundary_representatives": [list(x) for x in h],
        "representative_evaluations": evaluations,
        "cyclic_homotopies": {
            "f01": list(f01),
            "f12": list(f12),
            "f20": list(f20),
            "three_cycle_sum": list(add(f01, f12, f20)),
        },
        "strictly_invariant_edge_cochain": list(invariant_edge),
        "strictly_invariant_edge_cochain_is_exact": True,
        "C3_equivariance": "homotopy coherent, not strict on representatives",
        "reflection_action_on_holonomy": "complex conjugation/inversion",
        "parameter_space_character_constructed": True,
        "Cayley_Menger_relative_chain_coupling_constructed": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
