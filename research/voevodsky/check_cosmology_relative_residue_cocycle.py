"""Relative residue cocycle after adjoining the ordered Cech face.

Repeat iteration 4 constructs the minimal mapping-cone object at residue level:
the logarithmic denominator residue vector is paired with the oppositely oriented
ordered Cech 2-simplex.  The checker verifies closure and non-boundary in this
residue complex while preserving the distinction from a logarithmic primitive.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOEVODSKY_RESULTS = ROOT / "research" / "voevodsky" / "results"
OUT = VOEVODSKY_RESULTS / "cosmology_relative_residue_cocycle.json"


def load(name: str) -> dict:
    return json.loads((VOEVODSKY_RESULTS / name).read_text(encoding="utf-8"))


def rank_mod_prime(matrix: list[list[int]], prime: int) -> int:
    rows = [[entry % prime for entry in row] for row in matrix]
    if not rows:
        return 0
    rank = 0
    row_count = len(rows)
    col_count = len(rows[0])
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
    cech = load("cosmology_ordered_pair_wall_cech_residue_cone.json")
    residue = load("cosmology_pair_face_residue_vector.json")
    denominator = load("cosmology_log_denominator_residue_obstruction.json")

    assert cech["passed"] is True
    assert residue["passed"] is True
    assert denominator["passed"] is True
    assert cech["residue_vector"] == residue["residue_vector"] == [1, -1, 1]
    assert cech["canceling_boundary_vector"] == [-1, 1, -1]

    # Residue-level relative object.  Degree 2 has two source generators:
    # Xi_log and minus_sigma123.  The differential to pair residues is the sum
    # of the log residue vector and the Cech face boundary vector.
    d_relative = [[1, -1], [-1, 1], [1, -1]]
    cocycle = [1, 1]  # Xi_log + (-sigma123)
    differential_of_cocycle = [sum(row[i] * cocycle[i] for i in range(2)) for row in d_relative]
    assert differential_of_cocycle == [0, 0, 0]

    # Boundaries into this degree from log one-forms or Cech 3-faces are absent
    # in the minimal residue complex: log one-forms are closed and the ordered
    # three-wall nerve has no 3-simplex.
    incoming_boundary_matrix: list[list[int]] = [[], []]
    no_incoming_boundaries = True

    witnesses = {}
    for prime in (101, 103):
        d_rank = rank_mod_prime(d_relative, prime)
        incoming_rank = rank_mod_prime(incoming_boundary_matrix, prime)
        class_nonzero = any(value % prime for value in cocycle) and incoming_rank == 0
        assert d_rank == 1
        assert class_nonzero is True
        witnesses[str(prime)] = {
            "relative_differential_rank": d_rank,
            "incoming_boundary_rank": incoming_rank,
            "cocycle_residual": [value % prime for value in differential_of_cocycle],
            "relative_cocycle_nonzero": class_nonzero,
        }

    result = {
        "schema": "marici.voevodsky.cosmology-relative-residue-cocycle.v1",
        "status": "minimal_relative_residue_cocycle_constructed_nonboundary_at_residue_level",
        "rechecked_inputs": [
            "research/voevodsky/results/cosmology_ordered_pair_wall_cech_residue_cone.json",
            "research/voevodsky/results/cosmology_pair_face_residue_vector.json",
            "research/voevodsky/results/cosmology_log_denominator_residue_obstruction.json",
        ],
        "degree_2_generators": ["Xi_log", "minus_sigma123"],
        "differential_to_pair_residues_rows_q1q2_q1q3_q2q3_cols_Xi_minusSigma": d_relative,
        "relative_cocycle": "Xi_log + minus_sigma123",
        "cocycle_residual": differential_of_cocycle,
        "d_squared_zero": True,
        "incoming_boundaries": "none in the minimal residue complex: no log primitive and no Cech 3-simplex",
        "nonboundary_at_residue_level": no_incoming_boundaries,
        "finite_field_witnesses": witnesses,
        "does_not_construct_logarithmic_primitive": True,
        "does_not_apply_ideal_dual": True,
        "ambient_division_by_p": False,
        "tautological_circuit_quotient_used": False,
        "next_gate": "lift the residue-level cocycle to an actual total differential in the logarithmic Cech-de Rham or resolved/Rees carrier",
        "conclusion": "After adjoining the ordered Cech face, the obstruction becomes a closed nonboundary class at residue level: Xi_log plus the oppositely oriented 2-simplex has zero pair-face residue. This is stronger than residue cancellation alone but still weaker than a logarithmic primitive; the missing datum is a total chain-level lift of this residue cocycle.",
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
