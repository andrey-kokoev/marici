#!/usr/bin/env python3
"""Exact C2 character decomposition of finite observability."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "kitaev" / "results" / "c2-observability-decomposition.json"


def obs(A: sp.Matrix, J: sp.Matrix) -> sp.Matrix:
    return sp.Matrix.vstack(*[J * A**k for k in range(A.rows)])


def main() -> None:
    # Two 2D parity blocks. One scalar row observes each block dynamically.
    block = sp.Matrix([[0, 1], [0, 0]])
    A = sp.diag(block, block)
    R = sp.diag(1, 1, -1, -1)
    J_even = sp.Matrix([[1, 0, 0, 0]])
    J_odd = sp.Matrix([[0, 0, 1, 0]])
    J_generic = J_even + J_odd
    J_orbit = sp.Matrix.vstack(J_generic, J_generic * R)
    J_characters = sp.Matrix.vstack(J_even, J_odd)

    assert A * R == R * A
    assert J_even * R == J_even
    assert J_odd * R == -J_odd
    assert obs(A, J_even).rank() == 2
    assert obs(A, J_odd).rank() == 2
    assert obs(A, sp.Matrix.vstack(J_even, J_odd)).rank() == 4

    # Pure even sheet duplication is redundant.
    assert sp.Matrix.vstack(J_even, J_even * R).rank() == 1
    assert obs(A, sp.Matrix.vstack(J_even, J_even * R)).rank() == 2

    # The orbit pair and character projections differ by an invertible 2x2
    # Hadamard row transform, hence have the same observability content.
    hadamard = sp.Matrix([[1, 1], [1, -1]])
    assert J_orbit == hadamard * J_characters
    assert hadamard.det() == -2
    assert obs(A, J_orbit).rank() == obs(A, J_characters).rank() == 4

    # PBH witnesses for the even-only output span the odd kernel of A.
    odd_eigenvector = sp.Matrix([0, 0, 1, 0])
    assert A * odd_eigenvector == sp.zeros(4, 1)
    assert J_even * odd_eigenvector == sp.zeros(1, 1)
    assert J_odd * odd_eigenvector == sp.ones(1, 1)

    result = {
        "schema": "marici.kitaev.c2-observability-decomposition.v1",
        "exact_model": {
            "state_dimension": 4,
            "parity_dimensions": {"even": 2, "odd": 2},
            "A_block": [[0, 1], [0, 0]],
            "A_commutes_with_R": True,
            "even_only_observability_rank": 2,
            "odd_only_observability_rank": 2,
            "full_character_observability_rank": 4,
        },
        "theorem_checks": {
            "even_output_kills_odd_block_at_all_Krylov_orders": True,
            "odd_output_kills_even_block_at_all_Krylov_orders": True,
            "pure_character_sheet_copy_adds_rank": False,
            "generic_output_orbit_equals_character_split_up_to_Hadamard": True,
            "Hadamard_determinant": -2,
        },
        "minimality": {
            "odd_hidden_state_dimension": 2,
            "additional_odd_output_rows": 1,
            "reason_one_row_suffices": "dynamics generates two independent odd Krylov functionals",
            "required_quantity": "rank of the restricted observability matrix, not raw row count",
        },
        "PBH_witness": {
            "eigenvalue": 0,
            "state": [0, 0, 1, 0],
            "even_output": 0,
            "odd_seam_output": 1,
        },
        "source_test": {
            "first": "verify [A_X,R_X]=0 or record its residual",
            "second": "compute character projections J_even=(J+JR)/2 and J_odd=(J-JR)/2",
            "third": "run observability/PBH separately on V_even and V_odd",
            "completion": "bound the two restricted Gramians uniformly; the full bound is their minimum when cross terms vanish",
        },
        "verdict": "For C2-equivariant dynamics, observability decomposes by sheet character. A pure even Clark output can never observe an odd invariant state, regardless of propagation time. A genuinely odd seam row can observe the whole odd block through its Krylov orbit. Two sheet-related measurements help only when their orbit contains both nonzero character projections.",
    }
    result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
