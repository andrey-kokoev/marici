"""Monic residue-level comparison between Xi_log and the exceptional face.

Repeat iteration 4 constructs the only comparison that is actually justified by
current data: a residue-sheaf comparison.  The Poincare residue map is monic on
the Xi_log line, and the oppositely oriented exceptional face has the same image
with the opposite sign.  This still does not construct a total Cech-de Rham lift.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOEVODSKY_RESULTS = ROOT / "research" / "voevodsky" / "results"
OUT = VOEVODSKY_RESULTS / "cosmology_residue_monic_comparison.json"


def load(name: str) -> dict:
    return json.loads((VOEVODSKY_RESULTS / name).read_text(encoding="utf-8"))


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
    pair = load("cosmology_pair_face_residue_vector.json")
    unit_gate = load("cosmology_comparison_morphism_unit_gate.json")
    blowup = load("cosmology_blowup_exceptional_cell_gate.json")

    assert pair["passed"] is True
    assert unit_gate["passed"] is True
    assert blowup["passed"] is True
    assert pair["residue_vector"] == [1, -1, 1]
    assert blowup["residue_boundary_of_exceptional_column"] == [-1, 1, -1]

    xi_residue_column = [[1], [-1], [1]]
    exceptional_boundary_column = [[-1], [1], [-1]]
    sum_column = [[xi_residue_column[i][0] + exceptional_boundary_column[i][0]] for i in range(3)]
    assert sum_column == [[0], [0], [0]]

    # On rank-one source lines, a nonzero residue column is monic over a field.
    # The two prime checks give independent witnesses for the source-local rank.
    witnesses = {}
    for prime in (101, 103):
        xi_rank = rank_mod_prime(xi_residue_column, prime)
        exceptional_rank = rank_mod_prime(exceptional_boundary_column, prime)
        combined_rank = rank_mod_prime([[1, -1], [-1, 1], [1, -1]], prime)
        canceled_rank = rank_mod_prime(sum_column, prime)
        assert (xi_rank, exceptional_rank, combined_rank, canceled_rank) == (1, 1, 1, 0)
        witnesses[str(prime)] = {
            "Xi_residue_column_rank": xi_rank,
            "exceptional_boundary_column_rank": exceptional_rank,
            "span_rank": combined_rank,
            "sum_rank_after_pairing": canceled_rank,
            "residue_map_monic_on_Xi_line": True,
            "exceptional_to_Xi_comparison_unique_after_orientation": True,
        }

    result = {
        "schema": "marici.voevodsky.cosmology-residue-monic-comparison.v1",
        "status": "residue_level_comparison_constructed_total_lift_still_absent",
        "rechecked_inputs": [
            "research/voevodsky/results/cosmology_pair_face_residue_vector.json",
            "research/voevodsky/results/cosmology_comparison_morphism_unit_gate.json",
            "research/voevodsky/results/cosmology_blowup_exceptional_cell_gate.json",
        ],
        "Xi_log_residue_column_pair_faces": [1, -1, 1],
        "opposite_exceptional_boundary_column_pair_faces": [-1, 1, -1],
        "residue_sum": [0, 0, 0],
        "comparison_type": "residue-sheaf rank-one comparison, orientation-fixed",
        "monicity_boundary": "monic only on the one-dimensional Xi_log line after applying pair-face residues; not a monomorphism of the full logarithmic denominator complex",
        "finite_field_witnesses": witnesses,
        "what_is_now_constructed": "the residue/Gysin shadow identifying the exceptional boundary with -Res(Xi_log)",
        "what_is_not_constructed": [
            "pre-residue chain map from the exceptional source to the logarithmic denominator complex",
            "Cech-de Rham total differential whose boundary is tau_p",
            "relative p-normal Bockstein",
            "physical period",
        ],
        "next_gate": "lift this monic residue comparison through the residue exact sequence; equivalently construct a preimage of the residue-level comparison in the Cech-de Rham total complex",
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
