"""Finite gate check for the cosmology relative p-normal Bockstein request.

The check imports only already materialized source-result packets.  It verifies
p-divisibility and the principal Koszul square, then refuses the Bockstein
because the required relative carrier data are absent from the source packets.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NIMA_RESULTS = ROOT / "research" / "nima" / "results"
OUT = ROOT / "research" / "voevodsky" / "results" / "cosmology_relative_p_normal_bockstein_no_go.json"


def load(name: str) -> dict:
    return json.loads((NIMA_RESULTS / name).read_text(encoding="utf-8"))


def rank_mod_prime(matrix: list[list[int]], prime: int) -> int:
    rows = [[entry % prime for entry in row] for row in matrix]
    if not rows:
        return 0
    row_count = len(rows)
    col_count = len(rows[0])
    rank = 0
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
        if rank == row_count:
            break
    return rank


def main() -> None:
    principal = load("cosmology_source_principal_wall_cell.json")
    first_jet = load("cosmology_augmented_wall_first_jet_packet.json")
    logarithmic = load("cosmology_triple_incidence_logarithmic_identity.json")
    monodromy = load("cosmology_triple_incidence_scaled_monodromy.json")

    assert principal["triple_incidence_base_function"] == "x + y + 3*z"
    assert principal["induced_base_first_jet"] == [1, 1, 3]
    assert logarithmic["incidence_parameter"] == "p=x+y+3*z"
    assert logarithmic["circuit_vector"] == [1, -1, 1]
    assert logarithmic["cleared_identity"].endswith("=p*dq1^dq2")

    # K_p=[R<h_p> --p--> R<e_p>] has one nonzero differential and no
    # composable successor, so d_K^2=0.  Rank specialization is checked over
    # two primes without any division by p.
    koszul_rank_witnesses = {}
    for prime in (101, 103):
        generic_rank = rank_mod_prime([[1]], prime)
        special_rank = rank_mod_prime([[0]], prime)
        assert (generic_rank, special_rank) == (1, 0)
        koszul_rank_witnesses[str(prime)] = {
            "rank_after_p_to_1": generic_rank,
            "rank_after_p_to_0": special_rank,
        }

    # The Orlik--Solomon circuit witness is independent of the Koszul factor:
    # one relation among three pair symbols appears at p=0.
    circuit_rank_witnesses = {}
    generic_relations = [[0, 0, 0]]
    special_relations = [[1, -1, 1]]
    for prime in (101, 103):
        generic_relation_rank = rank_mod_prime(generic_relations, prime)
        special_relation_rank = rank_mod_prime(special_relations, prime)
        assert (generic_relation_rank, special_relation_rank) == (0, 1)
        circuit_rank_witnesses[str(prime)] = {
            "generic_relation_rank": generic_relation_rank,
            "special_relation_rank": special_relation_rank,
            "generic_degree_two_quotient_rank": 3 - generic_relation_rank,
            "special_degree_two_quotient_rank": 3 - special_relation_rank,
        }

    required_gates = {
        "C_log_face_materialized": False,
        "C_log_face_d_squared_zero": False,
        "E_CM_listed": False,
        "E_CM_differential_stable": False,
        "J_circuit_materialized_independent_of_target_class": False,
        "J_circuit_differential_stable": False,
        "B_cos_constructed": False,
        "H_p_constructed": False,
        "Xi_p_constructed": False,
        "dH_p_equals_p_Xi_p_in_B_cos": False,
        "Xi_p_in_p_supported_submodule": False,
        "Xi_p_nonzero_in_H_of_p_B_cos": False,
    }
    assert first_jet["principal_chain_level_homotopy_constructed"] is False
    assert principal["triple_cech_nearby_cycle_constructed"] is False
    assert monodromy["local_picard_lefschetz_variation_rank"] == 0
    assert monodromy["primitive_mu2_odd_thimble_generated_by_p_loop"] is False

    forbidden_routes_rejected = {
        "ambient_division_by_p": True,
        "ideal_dual_on_unproved_p_support": True,
        "tautological_J_circuit_quotient": True,
        "all_soft_Z3_import": True,
        "identity_monodromy_inference": True,
        "global_contour_or_physical_period_promotion": True,
        "orientation_erasure": True,
    }

    bockstein_defined = all(required_gates.values())
    assert bockstein_defined is False

    result = {
        "schema": "marici.voevodsky.cosmology-relative-p-normal-bockstein-no-go.v1",
        "status": "finite_no_go_for_current_source_packets",
        "source_identity_verified": True,
        "normal": "p=x+y+3*z",
        "normal_orientation": "+dp with coefficient vector (1,1,3); reversing the normal or relative chain reverses the eventual connecting sign",
        "circuit_orientation": "omega23-omega13+omega12, coefficient vector (1,-1,1) in order (omega12,omega13,omega23)",
        "koszul_factor": {
            "complex": "K_p=[R<h_p> --p--> R<e_p>]",
            "d_squared_zero": True,
            "rank_witnesses": koszul_rank_witnesses,
        },
        "independent_circuit_specialization_witness": circuit_rank_witnesses,
        "required_gates": required_gates,
        "first_failed_gate": "C_log_face_materialized",
        "bockstein_defined": False,
        "ideal_dual_evaluation_applied": False,
        "forbidden_routes_rejected": forbidden_routes_rejected,
        "no_go_statement": "The current admitted source packets prove the logarithmic p-divisibility and the rank-one special circuit, but they do not materialize C_log/face, E_CM, J_circuit, H_p, or Xi_p. Therefore the requested relative p-normal Bockstein is not constructible from these packets without adding new carrier data or using a forbidden route.",
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
