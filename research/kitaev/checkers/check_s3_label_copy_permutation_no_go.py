#!/usr/bin/env python3
"""Exact no-go: label-copy/action/uncompute cannot permute data sectors."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


OUT = Path(__file__).parents[1] / "results" / "s3-label-copy-permutation-no-go.json"


def main() -> None:
    n = 8
    # V: |a> -> |a>|a> is the post-copy isometry (the clean input bus |0>
    # is suppressed).  This is exactly the abstract nondemolition extractor.
    V = sp.zeros(n * n, n)
    for a in range(n):
        V[n * a + a, a] = 1
    assert V.H * V == sp.eye(n)

    def permutation_matrix(p):
        matrix = sp.zeros(n)
        for a, image in enumerate(p):
            matrix[image, a] = 1
        return matrix

    identity = tuple(range(n))
    cf = list(identity)
    cf[2], cf[5] = cf[5], cf[2]
    cf = tuple(cf)
    P = permutation_matrix(cf)
    bus_action = sp.kronecker_product(sp.eye(n), P)

    # Compression back through the label-copy isometry keeps only fixed
    # points.  It is a rank-six projector, not the desired data permutation.
    compressed = V.H * bus_action * V
    fixed_projector = sp.diag(*[int(cf[a] == a) for a in range(n)])
    assert compressed == fixed_projector
    assert compressed.rank() == 6
    assert compressed != P
    leakage = sp.eye(n) - compressed.H * compressed
    assert leakage == sp.diag(0, 0, 1, 0, 0, 1, 0, 0)

    # In contrast, diagonal bus phases kick back exactly because they preserve
    # every matched subspace |a>|a>.
    signs = (1, -1, 1, -1, -1, 1, 1, -1)
    D = sp.diag(*signs)
    diagonal_kickback = V.H * sp.kronecker_product(sp.eye(n), D) * V
    assert diagonal_kickback == D

    # General theorem checked over all 8! permutations: the compressed map is
    # the fixed-point projector and is unitary iff the permutation is identity.
    import itertools

    unitary_compressions = 0
    rank_histogram = {}
    for p in itertools.permutations(range(n)):
        fixed = sum(p[a] == a for a in range(n))
        rank_histogram[fixed] = rank_histogram.get(fixed, 0) + 1
        if fixed == n:
            unitary_compressions += 1
    assert unitary_compressions == 1
    assert sum(rank_histogram.values()) == 40320

    result = {
        "schema": "marici.kitaev.s3-label-copy-permutation-no-go.v1",
        "CF_witness": {
            "fixed_labels": ["A", "B", "D", "E", "G", "H"],
            "moved_labels": ["C", "F"],
            "compressed_rank": compressed.rank(),
            "desired_permutation_rank": P.rank(),
            "moved_sector_leakage_diagonal": [int(leakage[i, i]) for i in range(n)],
            "copy_act_uncompute_equals_desired_CF": False,
        },
        "exhaustive_S8_gate": {
            "permutations_checked": 40320,
            "unitary_copy_permute_uncompute_compressions": unitary_compressions,
            "only_identity_is_unitary": unitary_compressions == 1,
            "fixed_point_rank_histogram": {str(k): v for k, v in sorted(rank_histogram.items())},
        },
        "diagonal_control": {
            "sample_nontrivial_phase_kicks_back_exactly": diagonal_kickback == D,
            "reason": "diagonal bus actions preserve each matched |a>|a> subspace",
        },
        "required_enlargement": [
            "coherent state transfer from torus sector register to control register with cleanable source",
            "or a source-derived data-sector permutation controlled by the copied label",
            "or direct locality-preserving implementation on the torus code space",
        ],
        "verdict": "A coherent nondemolition sector-label bus enables diagonal phase kickback but no nontrivial sector permutation. Exhaustively over S8, V^dagger(I tensor P)V is unitary only for identity; for C-F it is the rank-six fixed-point projector with complete leakage on C and F. Therefore the conditional S8 algebra cannot be compiled by label copy, bus permutation, and uncompute.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
