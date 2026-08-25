#!/usr/bin/env python3
"""Conditional closure of affine three-bit controls plus the C-F duality."""

from __future__ import annotations

import itertools
import json
from collections import deque
from pathlib import Path


OUT = Path(__file__).parents[1] / "results" / "s3-duality-affine-hybrid-closure.json"


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[i]] for i in range(8))


def affine_permutation(matrix: tuple[int, ...], shift: int) -> tuple[int, ...]:
    out = []
    for x in range(8):
        y = shift
        for row in range(3):
            bit = ((matrix[row] & x).bit_count() & 1)
            y ^= bit << (2 - row)
        out.append(y)
    return tuple(out)


def rank3(rows: tuple[int, ...]) -> bool:
    span = {0}
    for row in rows:
        span |= {x ^ row for x in tuple(span)}
    return len(span) == 8


def closure(generators: list[tuple[int, ...]]) -> set[tuple[int, ...]]:
    identity = tuple(range(8))
    seen = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for generator in generators:
            candidate = compose(generator, current)
            if candidate not in seen:
                seen.add(candidate)
                queue.append(candidate)
    return seen


def main() -> None:
    matrices = [rows for rows in itertools.product(range(8), repeat=3) if rank3(rows)]
    affine = {affine_permutation(matrix, shift) for matrix in matrices for shift in range(8)}
    assert len(matrices) == 168
    assert len(affine) == 1344

    # C=2 (010), F=5 (101) in the frozen A,...,H encoding.
    cf = list(range(8))
    cf[2], cf[5] = cf[5], cf[2]
    cf = tuple(cf)
    assert cf not in affine

    # A compact generating set for AGL(3,2): three translations, two adjacent
    # bit swaps, and one shear.  Adjoin the protected C-F transposition.
    def xor_translation(mask: int) -> tuple[int, ...]:
        return tuple(x ^ mask for x in range(8))

    swap01 = affine_permutation((0b010, 0b100, 0b001), 0)
    swap12 = affine_permutation((0b100, 0b001, 0b010), 0)
    shear01 = affine_permutation((0b110, 0b010, 0b001), 0)
    affine_generators = [xor_translation(4), xor_translation(2), xor_translation(1), swap01, swap12, shear01]
    affine_generated = closure(affine_generators)
    assert affine_generated == affine

    hybrid = closure(affine_generators + [cf])
    assert len(hybrid) == 40320
    all_permutations = set(itertools.permutations(range(8)))
    assert hybrid == all_permutations

    # The mechanism is sharp: AGL(3,2) is 2-transitive, so conjugates of one
    # transposition supply all 28 pair transpositions.
    conjugates = set()
    for a in affine:
        inverse = [0] * 8
        for i, value in enumerate(a):
            inverse[value] = i
        conjugates.add(compose(compose(a, cf), tuple(inverse)))
    assert len(conjugates) == 28

    result = {
        "schema": "marici.kitaev.s3-duality-affine-hybrid-closure.v1",
        "exact_counts": {
            "GL_3_2": len(matrices),
            "AGL_3_2": len(affine),
            "CF_conjugate_transpositions": len(conjugates),
            "hybrid_closure": len(hybrid),
            "S8": len(all_permutations),
        },
        "gates": {
            "affine_generators_generate_AGL_3_2": affine_generated == affine,
            "CF_is_not_affine": cf not in affine,
            "AGL_is_two_transitive_on_eight_labels": len(conjugates) == 28,
            "affine_plus_CF_generates_S8": hybrid == all_permutations,
        },
        "typing_boundary": {
            "theorem_strength": "conditional finite algebraic closure",
            "condition": "the protected C-F torus-basis action and affine Clifford controls act on one physically intertwined eight-state register",
            "missing_map": "a source-derived intertwiner between the torus sector basis and the frozen three-bit control/record register",
            "not_claimed": "locality-preserving or fault-tolerant execution of all S8 permutations",
        },
        "verdict": "Conditionally on a common physical eight-state register, the protected C-F transposition plus affine three-bit Clifford controls generates every classical sector permutation S8. The closure is exact, but executable hybrid composition remains blocked by the missing source-derived torus-to-record intertwiner.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
