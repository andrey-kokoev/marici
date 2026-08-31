"""Admission gate for the relative p-normal Bockstein candidate.

The checker constructs the auxiliary principal-normal Koszul factor and verifies
that the source logarithmic identity has the required p-divisibility.  It then
refuses to define a Bockstein because the current source packets do not yet
materialize the relative Cayley--Menger Cech/bulk-face carrier, a stable generic
relation subcomplex, or a lift dH=p*Xi in that quotient.
"""

from __future__ import annotations

import json
from pathlib import Path

NIMA = Path(__file__).resolve().parents[1]
OUT = NIMA / "results" / "cosmology_relative_p_normal_bockstein_candidate.json"


def load(name: str) -> dict:
    return json.loads((NIMA / "results" / name).read_text(encoding="utf-8"))


def rank_mod_prime(columns: list[list[int]], prime: int) -> int:
    """Small exact column-rank routine used only for the declared K_p factor."""
    if not columns:
        return 0
    rows = [list(row) for row in zip(*columns)]
    rank = 0
    for column in range(len(columns)):
        pivot = next((r for r in range(rank, len(rows)) if rows[r][column] % prime), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column] % prime, -1, prime)
        rows[rank] = [(value * inverse) % prime for value in rows[rank]]
        for row in range(len(rows)):
            if row == rank:
                continue
            factor = rows[row][column] % prime
            if factor:
                rows[row] = [
                    (value - factor * pivot_value) % prime
                    for value, pivot_value in zip(rows[row], rows[rank])
                ]
        rank += 1
        if rank == len(rows):
            break
    return rank


def main() -> None:
    principal = load("cosmology_source_principal_wall_cell.json")
    logarithmic = load("cosmology_triple_incidence_logarithmic_identity.json")
    first_jet = load("cosmology_augmented_wall_first_jet_packet.json")
    monodromy = load("cosmology_triple_incidence_scaled_monodromy.json")
    cm_support = load("cosmology_p_normal_cayley_menger_support.json")
    cech = load("cosmology_p_normal_marked_wall_cech_carrier.json")
    denominator = load("cosmology_p_normal_log_denominator_no_go.json")
    relative_residue = load("cosmology_p_normal_relative_residue_cocycle.json")
    total_lift = load("cosmology_p_normal_total_lift_exhaustion.json")

    assert principal["triple_incidence_base_function"] == "x + y + 3*z"
    assert principal["wall_relation_coefficients"] == [-1, -1, 1]
    assert logarithmic["circuit_vector"] == [1, -1, 1]
    assert logarithmic["transverse_normalized_coefficient"] == 1
    assert "=p*dq1^dq2" in logarithmic["cleared_identity"]

    # K_p=[R<h_p> --p--> R<e_p>].  Its only nonzero differential has no
    # composable successor, hence d_K^2=0.  Generic and special ranks are
    # independently checked over two finite fields without dividing by p.
    koszul = {
        "coefficient_ring": "R=Z[x,y,z]",
        "normal": "p=x+y+3*z",
        "degrees": {"1": ["h_p"], "0": ["e_p"]},
        "differential": "d(h_p)=p*e_p; d(e_p)=0",
        "d_squared_zero": True,
        "normal_orientation": "+dp represented by ordered coefficients (1,1,3)",
    }
    rank_tests = {}
    for prime in (101, 103):
        generic_rank = rank_mod_prime([[1]], prime)  # specialize p -> 1
        special_rank = rank_mod_prime([[0]], prime)  # specialize p -> 0
        assert (generic_rank, special_rank) == (1, 0)
        rank_tests[str(prime)] = {"p_to_1_rank": generic_rank, "p_to_0_rank": special_rank}

    carrier_gates = {
        "source_p_and_divisibility_identity": True,
        "auxiliary_K_p_constructed": True,
        "C_log_face_differential_materialized": cech["minimal_relative_carrier_constructed"],
        "Cayley_Menger_endpoint_face_subcomplex_listed": cm_support["E_CM_constructed"],
        "Cayley_Menger_endpoint_face_subcomplex_is_zero": cm_support["E_CM_is_zero"],
        "endpoint_face_subcomplex_differential_stable": cm_support["E_CM_differential_stable"],
        "generic_circuit_relation_subcomplex_materialized": True,
        "generic_relation_subcomplex_differential_stable": cech["J_circuit"]["differential_stable"],
        "minimal_relative_carrier_B_cos_constructed": cech["minimal_relative_carrier_constructed"],
        "bulk_face_augmented_carrier_constructed": cech["bulk_face_augmentation_constructed"],
        "relative_residue_cocycle_constructed": relative_residue["relative_residue_cocycle_constructed"],
        "relative_residue_cocycle_nonboundary": relative_residue["relative_residue_cocycle_nonboundary_in_minimal_residue_complex"],
        "total_Cech_de_Rham_chain_map_constructed": relative_residue["total_Cech_de_Rham_chain_map_constructed"],
        "lift_H_p_with_dH_equals_p_Xi_in_B_cos": False,
        "Xi_cycle_in_I_times_B_cos": False,
        "Xi_survival_rank_test_executed_on_minimal_carrier": True,
        "Xi_survival_rank_test": cech["Xi_survives_minimal_carrier"],
        "ordinary_logarithmic_primitive_exists": denominator["ordinary_logarithmic_primitive_exists"],
        "ordinary_Laurent_primitive_exists": denominator["ordinary_Laurent_primitive_exists"],
        "unbounded_double_residue_obstruction": denominator["unbounded_exponent_local_obstruction"],
        "source_normalized_relative_test_chain": False,
        "mu2_odd_pairing": False,
    }
    assert first_jet["principal_chain_level_homotopy_constructed"] is False
    assert principal["triple_cech_nearby_cycle_constructed"] is False
    assert monodromy["local_picard_lefschetz_variation_rank"] == 0
    assert monodromy["primitive_mu2_odd_thimble_generated_by_p_loop"] is False

    bockstein_defined = all(
        carrier_gates[key]
        for key in (
            "bulk_face_augmented_carrier_constructed",
            "lift_H_p_with_dH_equals_p_Xi_in_B_cos",
            "Xi_cycle_in_I_times_B_cos",
            "Xi_survival_rank_test",
        )
    )
    assert not bockstein_defined

    packet = {
        "schema": "marici.cosmology-relative-p-normal-bockstein-candidate.v1",
        "status": "current_source_p_normal_branch_exhausted_tau_p_classified_not_sourced",
        "source_normal": "p=x+y+3*z",
        "circuit_identity": logarithmic["cleared_identity"],
        "koszul_factor": koszul,
        "koszul_specialization_rank_tests": rank_tests,
        "carrier_target": "B_cos=(C_log/face/E_CM)/J_circuit",
        "carrier_gates": carrier_gates,
        "bockstein_defined": False,
        "ideal_dual_evaluation_applied": False,
        "ambient_division_by_p": False,
        "all_soft_Z3_used_as_coefficient": False,
        "inferred_from_monodromy": False,
        "global_contour_constructed": False,
        "physical_period_covector_constructed": False,
        "currently_open_internal_constructor": (
            "supply new source data mapping a resolved/Rees, Cech-de Rham cone, "
            "or Cayley-Menger face generator to tau_p with unit coefficient"
        ),
        "first_failed_gate": "source_derived_unit_map_to_tau_p",
        "currently_open_internal_route": total_lift["currently_open_internal_route"],
        "requires_new_source_data": total_lift["requires_new_source_data"],
        "next_falsifier": "supply a source-derived unit map to tau_p and rerun the full total differential",
        "passed": True,
    }
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
