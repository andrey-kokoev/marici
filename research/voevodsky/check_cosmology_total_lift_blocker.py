"""Total chain-level lift blocker for the relative residue cocycle.

Repeat iteration 5 tests whether the minimal objects already constructed contain
an incoming total differential whose image is the relative residue cocycle.  They
do not: the only admitted incoming generators are closed logarithmic one-forms,
and the ordered three-wall Cech nerve has no 3-simplex.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOEVODSKY_RESULTS = ROOT / "research" / "voevodsky" / "results"
OUT = VOEVODSKY_RESULTS / "cosmology_total_lift_blocker.json"


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
    relative = load("cosmology_relative_residue_cocycle.json")
    cone = load("cosmology_ordered_pair_wall_cech_residue_cone.json")
    denominator = load("cosmology_log_denominator_primitive_gate.json")

    assert relative["passed"] is True
    assert cone["passed"] is True
    assert denominator["passed"] is True
    assert relative["relative_cocycle"] == "Xi_log + minus_sigma123"
    assert relative["cocycle_residual"] == [0, 0, 0]
    assert denominator["log_complex"]["log_one_form_primitive_exists"] is False

    # Candidate source of a total lift into degree-2 generators
    # (Xi_log, minus_sigma123).  Log one-forms are closed in the denominator
    # carrier, and no Cech 3-simplex exists for three walls; hence the admitted
    # incoming matrix has two rows and zero columns.
    incoming_generators: list[str] = []
    incoming_to_degree2: list[list[int]] = [[], []]
    target_cocycle = [[1], [1]]
    augmented = [row + [target_cocycle[i][0]] for i, row in enumerate(incoming_to_degree2)]

    witnesses = {}
    for prime in (101, 103):
        coefficient_rank = rank_mod_prime(incoming_to_degree2, prime)
        augmented_rank = rank_mod_prime(augmented, prime)
        assert coefficient_rank == 0
        assert augmented_rank == 1
        witnesses[str(prime)] = {
            "incoming_generators": 0,
            "coefficient_rank": coefficient_rank,
            "augmented_rank_for_target_cocycle": augmented_rank,
            "total_lift_exists": False,
        }

    result = {
        "schema": "marici.voevodsky.cosmology-total-lift-blocker.v1",
        "status": "blocked_at_absent_total_chain_level_lift",
        "rechecked_inputs": [
            "research/voevodsky/results/cosmology_relative_residue_cocycle.json",
            "research/voevodsky/results/cosmology_ordered_pair_wall_cech_residue_cone.json",
            "research/voevodsky/results/cosmology_log_denominator_primitive_gate.json",
        ],
        "target_relative_cocycle": "Xi_log + minus_sigma123",
        "incoming_generators_available_in_minimal_total_complex": incoming_generators,
        "incoming_to_degree2_matrix_rows_Xi_minusSigma": incoming_to_degree2,
        "reason_no_incoming_generators": [
            "degree-one logarithmic denominator generators are closed and do not hit Xi_log",
            "the ordered three-wall Cech nerve has no 3-simplex whose boundary can hit sigma123",
            "no resolved/Rees exceptional generator or Cayley-Menger face generator has been sourced",
        ],
        "finite_field_witnesses": witnesses,
        "total_chain_level_lift_constructed": False,
        "logarithmic_primitive_constructed": False,
        "relative_bockstein_constructed": False,
        "ideal_dual_evaluation_applied": False,
        "ambient_division_by_p": False,
        "tautological_circuit_quotient_used": False,
        "physical_period_constructed": False,
        "stop_condition": "The five-step local denominator investigation has exhausted the minimal logarithmic, Laurent, residue, ordered-Cech, and minimal total-lift tests. Further progress requires new source data: a resolved/Rees exceptional generator, a Cech-de Rham chain map, or a Cayley-Menger face cone supplied outside the current minimal carrier.",
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
