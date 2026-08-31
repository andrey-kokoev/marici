"""Ordered blow-up exceptional-cell gate for tau_p.

Repeat iteration 2 tests one allowed source direction from the source packets: the
oriented blow-up of the coalescing three-wall corner.  Its exceptional 2-simplex
supplies the Cech face leg with unit coefficient, but by itself has no logarithmic
Xi_log leg, so it does not satisfy the tau_p source-map contract.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOEVODSKY_RESULTS = ROOT / "research" / "voevodsky" / "results"
NIMA_RESULTS = ROOT / "research" / "nima" / "results"
OUT = VOEVODSKY_RESULTS / "cosmology_blowup_exceptional_cell_gate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


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
    contract = load(VOEVODSKY_RESULTS / "cosmology_tau_source_map_contract.json")
    cech = load(VOEVODSKY_RESULTS / "cosmology_ordered_pair_wall_cech_residue_cone.json")
    boundary = load(NIMA_RESULTS / "cosmology_triple_incidence_boundary_corner_transport.json")

    assert contract["passed"] is True
    assert contract["contract"]["required_differential_vector_in_rows_Xi_log_minusSigma"] == [1, 1]
    assert cech["passed"] is True
    assert cech["canceling_boundary_vector"] == [-1, 1, -1]
    assert boundary["required_resolution"] == "blow up the coalescing three-vertex boundary corner while retaining ordered wall and deck labels"

    # Exceptional simplex from the ordered blow-up.  Its opposite orientation
    # maps to the Cech face -sigma123 with unit coefficient.  There is no source
    # datum in this exceptional-cell-only model mapping to Xi_log.
    rows = ["Xi_log", "minus_sigma123"]
    exceptional_to_tau_rows = [[0], [1]]
    required_tau_vector = [1, 1]
    residual = [required_tau_vector[i] - exceptional_to_tau_rows[i][0] for i in range(2)]
    assert residual == [1, 0]

    # Residue differential D kills only diagonal vectors (a,a).  The exceptional
    # vector (0,1) is not closed in the residue complex without the Xi_log leg.
    d_residue = [[1, -1], [-1, 1], [1, -1]]
    exceptional_residue_boundary = mat_vec(d_residue, [0, 1])
    assert exceptional_residue_boundary == [-1, 1, -1]

    witnesses = {}
    for prime in (101, 103):
        source_rank = rank_mod_prime(exceptional_to_tau_rows, prime)
        augmented_rank_for_tau = rank_mod_prime([[0, 1], [1, 1]], prime)
        closed = all(value % prime == 0 for value in exceptional_residue_boundary)
        assert source_rank == 1
        assert augmented_rank_for_tau == 2
        assert closed is False
        witnesses[str(prime)] = {
            "exceptional_column_rank": source_rank,
            "augmented_rank_for_required_tau_vector": augmented_rank_for_tau,
            "exceptional_residue_boundary_mod_prime": [value % prime for value in exceptional_residue_boundary],
            "closed_without_Xi_leg": closed,
            "tau_contract_satisfied": False,
        }

    result = {
        "schema": "marici.voevodsky.cosmology-blowup-exceptional-cell-gate.v1",
        "status": "exceptional_cech_face_leg_constructed_Xi_log_leg_absent",
        "rechecked_inputs": [
            "research/voevodsky/results/cosmology_tau_source_map_contract.json",
            "research/voevodsky/results/cosmology_ordered_pair_wall_cech_residue_cone.json",
            "research/nima/results/cosmology_triple_incidence_boundary_corner_transport.json",
        ],
        "source_domain_tested": "oriented blow-up exceptional simplex of the ordered three-wall corner",
        "rows": rows,
        "exceptional_cell_column_rows_Xi_minusSigma": [0, 1],
        "required_tau_column_rows_Xi_minusSigma": required_tau_vector,
        "missing_component": "Xi_log unit leg",
        "residue_boundary_of_exceptional_column": exceptional_residue_boundary,
        "finite_field_witnesses": witnesses,
        "decision": "the blow-up exceptional simplex alone supplies the Cech face with unit coefficient but does not map to tau_p; it must be coupled to the logarithmic denominator class by an additional chain map",
        "next_gate": "construct the comparison morphism that pairs the exceptional face with Xi_log, or prove no such morphism is source-derived",
        "relative_bockstein_constructed": False,
        "physical_period_constructed": False,
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
