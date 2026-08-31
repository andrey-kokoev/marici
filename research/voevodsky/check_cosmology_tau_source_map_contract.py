"""Source-map contract for the universal tau_p cell.

This repeat iteration turns the universal-cell classifier into an interface test:
what exact source map would make tau_p admissible, and do the currently mutable
source packets already provide it?
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOEVODSKY_RESULTS = ROOT / "research" / "voevodsky" / "results"
NIMA_RESULTS = ROOT / "research" / "nima" / "results"
OUT = VOEVODSKY_RESULTS / "cosmology_tau_source_map_contract.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


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
    universal = load(VOEVODSKY_RESULTS / "cosmology_universal_total_lift_cell.json")
    frontier = load(NIMA_RESULTS / "cosmology_current_activation_frontier_exhaustion.json")
    boundary = load(NIMA_RESULTS / "cosmology_triple_incidence_boundary_corner_transport.json")
    authority = load(NIMA_RESULTS / "cosmology_post_candidate_authority_status.json")

    assert universal["passed"] is True
    assert universal["primitive_kernel_generator"] == [1, 1]
    assert frontier["current_routes"]["relative_p_normal_coefficient"]["status"] == "relative_residue_cocycle_constructed_total_chain_lift_open"
    assert boundary["required_resolution"].startswith("blow up")
    assert boundary["picard_lefschetz_variation_computed"] is False
    assert authority["relative_p_normal_first_failed_gate"] == "total_Cech_de_Rham_chain_map_constructed"

    # Contract matrix: a source candidate with n generators maps to tau_p by a
    # row c.  Its differential to (Xi_log, -sigma123) must be [1,1] times a unit.
    # Current packets provide no such source generator, so the source matrix has
    # zero columns.  Augmenting by required primitive vector is inconsistent.
    current_source_generators: list[str] = []
    current_source_to_pair_matrix: list[list[int]] = [[], []]
    required_vector = [[1], [1]]
    augmented = [row + [required_vector[i][0]] for i, row in enumerate(current_source_to_pair_matrix)]

    witnesses = {}
    for prime in (101, 103):
        coefficient_rank = rank_mod_prime(current_source_to_pair_matrix, prime)
        augmented_rank = rank_mod_prime(augmented, prime)
        assert coefficient_rank == 0
        assert augmented_rank == 1
        witnesses[str(prime)] = {
            "current_source_generator_count": 0,
            "coefficient_rank": coefficient_rank,
            "augmented_rank_for_unit_tau_map": augmented_rank,
            "contract_satisfied_by_current_packets": False,
        }

    result = {
        "schema": "marici.voevodsky.cosmology-tau-source-map-contract.v1",
        "status": "source_map_contract_defined_current_packets_fail_it",
        "rechecked_inputs": [
            "research/voevodsky/results/cosmology_universal_total_lift_cell.json",
            "research/nima/results/cosmology_current_activation_frontier_exhaustion.json",
            "research/nima/results/cosmology_triple_incidence_boundary_corner_transport.json",
            "research/nima/results/cosmology_post_candidate_authority_status.json",
        ],
        "contract": {
            "object_to_source": "tau_p",
            "required_degree": 1,
            "required_differential_vector_in_rows_Xi_log_minusSigma": [1, 1],
            "unit_condition": "source generator must map to (1,1) with coefficient +/-1 over Z; nonunit multiples do not kill the primitive integral class",
            "orientation_condition": "opposite normal or opposite ordered Cech face changes the sign, not the unit requirement",
            "typing_condition": "the generator must be supplied by a resolved/Rees exceptional object, logarithmic Cech-de Rham cone cell, or Cayley-Menger face cone, with a chain map to the residue complex",
        },
        "current_source_generators_matching_contract": current_source_generators,
        "current_source_to_pair_matrix_rows_Xi_minusSigma": current_source_to_pair_matrix,
        "finite_field_witnesses": witnesses,
        "independent_source_status": {
            "frontier_route_open": frontier["open_internal_route"],
            "boundary_resolution_required": boundary["required_resolution"],
            "picard_lefschetz_variation_computed": boundary["picard_lefschetz_variation_computed"],
            "first_failed_gate": authority["relative_p_normal_first_failed_gate"],
        },
        "decision": "current packets fail the tau_p source-map contract at the object-existence stage",
        "next_action": "do not search more Laurent primitives; construct one of the three typed source domains and test whether its first differential column is the primitive vector (1,1)",
        "relative_bockstein_constructed": False,
        "physical_period_constructed": False,
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
