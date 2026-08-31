"""Residue-functor nonfaithfulness gate for the tau_p source problem.

Repeat iteration 5 checks the logical gap left by the monic residue comparison:
equality after the residue functor does not construct a pre-residue morphism.
The checker models the residue functor with an explicit kernel direction, so the
fiber over the residue column is non-singleton.  A source lift needs an extra
chain-level choice or theorem, not another residue-rank calculation.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOEVODSKY_RESULTS = ROOT / "research" / "voevodsky" / "results"
OUT = VOEVODSKY_RESULTS / "cosmology_residue_functor_nonfaithfulness_gate.json"


def load(name: str) -> dict:
    return json.loads((VOEVODSKY_RESULTS / name).read_text(encoding="utf-8"))


def mat_vec(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(row[i] * vector[i] for i in range(len(vector))) for row in matrix]


def rank_mod_prime(matrix: list[list[int]], prime: int) -> int:
    rows = [[entry % prime for entry in row] for row in matrix]
    if not rows:
        return 0
    rank = 0
    row_count = len(rows)
    col_count = len(rows[0]) if rows else 0
    for col in range(col_count):
        pivot = next((r for r in range(rank, row_count) if rows[r][col] % prime), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][col], -1, prime)
        rows[rank] = [(value * inv) % prime for value in rows[rank]]
        for r in range(row_count):
            if r == rank:
                continue
            factor = rows[r][col] % prime
            if factor:
                rows[r] = [(a - factor * b) % prime for a, b in zip(rows[r], rows[rank])]
        rank += 1
    return rank


def main() -> None:
    monic = load("cosmology_residue_monic_comparison.json")
    unit_gate = load("cosmology_comparison_morphism_unit_gate.json")
    contract = load("cosmology_tau_source_map_contract.json")

    assert monic["passed"] is True
    assert unit_gate["passed"] is True
    assert contract["passed"] is True
    assert monic["Xi_log_residue_column_pair_faces"] == [1, -1, 1]
    assert monic["opposite_exceptional_boundary_column_pair_faces"] == [-1, 1, -1]

    # A minimal pre-residue model separates a residue-visible Xi coordinate from
    # one residue-invisible kernel coordinate k.  The residue functor sends
    # (xi,k) to xi*(1,-1,1).  Both (1,0) and (1,1) have the same residue, so
    # residue comparison alone cannot choose a pre-residue morphism.
    residue_functor_matrix = [[1, 0], [-1, 0], [1, 0]]
    lift_a = [1, 0]
    lift_b = [1, 1]
    residue_a = mat_vec(residue_functor_matrix, lift_a)
    residue_b = mat_vec(residue_functor_matrix, lift_b)
    assert residue_a == residue_b == [1, -1, 1]
    kernel_vector = [0, 1]
    assert mat_vec(residue_functor_matrix, kernel_vector) == [0, 0, 0]

    witnesses = {}
    for prime in (101, 103):
        functor_rank = rank_mod_prime(residue_functor_matrix, prime)
        kernel_rank = 2 - functor_rank
        assert functor_rank == 1
        assert kernel_rank == 1
        witnesses[str(prime)] = {
            "pre_residue_rank": 2,
            "residue_image_rank": functor_rank,
            "kernel_rank": kernel_rank,
            "two_distinct_lifts_same_residue": True,
            "residue_equality_implies_source_morphism": False,
        }

    result = {
        "schema": "marici.voevodsky.cosmology-residue-functor-nonfaithfulness-gate.v1",
        "status": "residue_comparison_cannot_be_inverted_source_lift_required",
        "rechecked_inputs": [
            "research/voevodsky/results/cosmology_residue_monic_comparison.json",
            "research/voevodsky/results/cosmology_comparison_morphism_unit_gate.json",
            "research/voevodsky/results/cosmology_tau_source_map_contract.json",
        ],
        "minimal_pre_residue_model": {
            "basis": ["Xi_log_visible", "kernel_invisible"],
            "residue_functor_matrix_rows_pair_faces_cols_visible_kernel": residue_functor_matrix,
            "kernel_vector": kernel_vector,
            "same_residue_lifts": [lift_a, lift_b],
        },
        "finite_field_witnesses": witnesses,
        "interpretation": "The residue/Gysin shadow is necessary and fixes the visible coefficient, but the residue functor has a kernel. Equality after residue therefore does not construct a pre-residue chain map from the exceptional source to Xi_log.",
        "remaining_required_datum": "a source-derived lift through the residue exact sequence that specifies the kernel component and proves compatibility with the total differential",
        "exhausted_local_tests": [
            "ordinary Laurent primitive search",
            "double-residue obstruction",
            "pair-face residue vector",
            "ordered Cech residue cone",
            "relative residue cocycle",
            "universal tau_p classifier",
            "exceptional Cech leg",
            "conditional unit forcing",
            "residue-level monic comparison",
            "nonfaithfulness of residue as a reverse construction",
        ],
        "next_source_only_tasks": [
            "construct the logarithmic Cech-de Rham residue exact sequence and a section on this class",
            "construct a resolved/Rees exceptional generator with its pre-residue kernel component",
            "construct a Cayley-Menger face cone that supplies the missing kernel datum",
        ],
        "relative_bockstein_constructed": False,
        "physical_period_constructed": False,
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
