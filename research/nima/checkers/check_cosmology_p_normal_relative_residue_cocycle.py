"""Independent admission of the ordered relative residue cocycle."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NIMA = ROOT / "nima"
VOE = ROOT / "voevodsky"
OUT = NIMA / "results" / "cosmology_p_normal_relative_residue_cocycle.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rank_mod_prime(matrix: list[list[int]], prime: int) -> int:
    rows = [[x % prime for x in row] for row in matrix]
    rank = 0
    columns = len(rows[0]) if rows else 0
    for column in range(columns):
        pivot = next((r for r in range(rank, len(rows)) if rows[r][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][column], -1, prime)
        rows[rank] = [(x * inv) % prime for x in rows[rank]]
        for r in range(len(rows)):
            if r == rank or not rows[r][column]:
                continue
            factor = rows[r][column]
            rows[r] = [(a - factor * b) % prime for a, b in zip(rows[r], rows[rank])]
        rank += 1
    return rank


def main() -> None:
    pair = load(VOE / "results" / "cosmology_pair_face_residue_vector.json")
    cone = load(VOE / "results" / "cosmology_ordered_pair_wall_cech_residue_cone.json")
    relative = load(VOE / "results" / "cosmology_relative_residue_cocycle.json")
    local_no_go = load(NIMA / "results" / "cosmology_p_normal_log_denominator_no_go.json")
    minimal_cech = load(NIMA / "results" / "cosmology_p_normal_marked_wall_cech_carrier.json")

    circuit = [1, -1, 1]
    opposite = [-1, 1, -1]
    assert pair["residue_vector"] == circuit
    assert cone["canceling_boundary_vector"] == opposite
    assert minimal_cech["d1_pair_to_triple"] == [circuit]
    assert local_no_go["target_double_residue"] == 1

    d_relative = [[1, -1], [-1, 1], [1, -1]]
    cocycle = [1, 1]
    residual = [sum(row[j] * cocycle[j] for j in range(2)) for row in d_relative]
    assert residual == [0, 0, 0]
    assert relative["differential_to_pair_residues_rows_q1q2_q1q3_q2q3_cols_Xi_minusSigma"] == d_relative

    witnesses = {}
    for prime in (101, 103):
        rank = rank_mod_prime(d_relative, prime)
        assert rank == 1
        assert relative["finite_field_witnesses"][str(prime)]["incoming_boundary_rank"] == 0
        witnesses[str(prime)] = {
            "relative_differential_rank": rank,
            "incoming_boundary_rank": 0,
            "cocycle_nonzero": True,
        }

    packet = {
        "schema": "marici.cosmology-p-normal-relative-residue-cocycle.v1",
        "status": "relative_residue_cocycle_constructed_total_chain_lift_missing",
        "ordered_pair_faces": ["q1_q2", "q1_q3", "q2_q3"],
        "logarithmic_residue_vector": circuit,
        "opposite_Cech_face_boundary": opposite,
        "degree_two_generators": ["Xi_log", "minus_sigma123"],
        "relative_differential": d_relative,
        "relative_cocycle_vector": cocycle,
        "relative_cocycle_residual": residual,
        "d_squared_zero_at_residue_level": True,
        "prime_witnesses": witnesses,
        "relative_residue_cocycle_constructed": True,
        "relative_residue_cocycle_nonboundary_in_minimal_residue_complex": True,
        "source_derivation": "ordered three-wall Cech face orientation plus source logarithmic pair residues",
        "tautological_circuit_quotient_used": False,
        "total_Cech_de_Rham_chain_map_constructed": False,
        "resolved_Rees_chain_lift_constructed": False,
        "p_normal_Bockstein_constructed": False,
        "ideal_dual_evaluation_applied": False,
        "physical_period_constructed": False,
        "conclusion": (
            "the opposite ordered Cech face cancels the logarithmic pair-residue vector "
            "and produces a nonzero relative cocycle at residue level; the missing datum "
            "is an actual total Cech-de Rham or resolved chain-level lift"
        ),
        "next_gate": (
            "construct a source-derived chain map lifting (Xi_log,-sigma123) from the residue "
            "complex into the logarithmic Cech-de Rham total complex and verify its full differential"
        ),
        "passed": True,
    }
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
