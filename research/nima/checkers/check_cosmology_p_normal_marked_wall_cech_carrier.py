"""Exact minimal marked-wall Cech carrier at the p-normal corner.

The three ordered walls give the simplicial Cech differential

  C0=R^3 --d0--> C1=R^3 --d1--> C2=R/(p),

with pair order (12,13,23), d0 the edge-incidence matrix, and
d1=(1,-1,1).  The checker proves d1*d0=0 and shows that at p=0 the
relevant special complex is exact: the triple Cech term kills the rank-one
nearby quotient.  Hence the minimal Cech carrier has no surviving Xi class;
a Bockstein would require a separately source-derived bulk/face augmentation.
"""

from __future__ import annotations

import json
from pathlib import Path

NIMA = Path(__file__).resolve().parents[1]
OUT = NIMA / "results" / "cosmology_p_normal_marked_wall_cech_carrier.json"


def load(name: str) -> dict:
    return json.loads((NIMA / "results" / name).read_text(encoding="utf-8"))


def matmul(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def rank_mod_prime(matrix: list[list[int]], prime: int) -> int:
    rows = [[entry % prime for entry in row] for row in matrix]
    rank = 0
    columns = len(rows[0]) if rows else 0
    for column in range(columns):
        pivot = next((row for row in range(rank, len(rows)) if rows[row][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, prime)
        rows[rank] = [(entry * inverse) % prime for entry in rows[rank]]
        for row in range(len(rows)):
            if row == rank or not rows[row][column]:
                continue
            factor = rows[row][column]
            rows[row] = [(a - factor * b) % prime for a, b in zip(rows[row], rows[rank])]
        rank += 1
    return rank


def main() -> None:
    principal = load("cosmology_source_principal_wall_cell.json")
    logarithmic = load("cosmology_triple_incidence_logarithmic_identity.json")
    first_jet = load("cosmology_augmented_wall_first_jet_packet.json")
    cm_support = load("cosmology_p_normal_cayley_menger_support.json")

    assert principal["wall_order"] == ["q_g1", "q_g2", "q_g3"]
    assert principal["triple_incidence_base_function"] == "x + y + 3*z"
    assert logarithmic["oriented_pair_order"] == ["omega12", "omega13", "omega23"]
    assert logarithmic["circuit_vector"] == [1, -1, 1]
    assert first_jet["physical_localization_boundary_cech_closed"] is True
    assert first_jet["first_derivative_pairwise_cech_closed"] is True
    assert cm_support["E_CM_is_zero"] is True

    # Rows are ordered pairs (12,13,23); columns are walls (1,2,3).
    d0 = [[-1, 1, 0], [-1, 0, 1], [0, -1, 1]]
    d1 = [[1, -1, 1]]
    assert matmul(d1, d0) == [[0, 0, 0]]

    prime_tests = {}
    for prime in (101, 103):
        rank_d0 = rank_mod_prime(d0, prime)
        rank_d1 = rank_mod_prime(d1, prime)
        special_h1 = 3 - rank_d0 - rank_d1
        special_h2 = 1 - rank_d1
        generic_nearby_quotient = 3 - rank_d0  # no triple term for p != 0
        assert (rank_d0, rank_d1) == (2, 1)
        assert generic_nearby_quotient == 1
        assert special_h1 == special_h2 == 0
        prime_tests[str(prime)] = {
            "rank_d0": rank_d0,
            "rank_d1_at_p0": rank_d1,
            "generic_pair_quotient_rank_without_triple_term": generic_nearby_quotient,
            "special_H1_rank": special_h1,
            "special_H2_rank": special_h2,
        }

    # J_sew=im(d0) is a differential-stable subcomplex because d1*d0=0.
    # C1/J_sew is rank one, and d1 induces a unit map to the special triple
    # term.  Thus adjoining a proposed Xi column cannot raise special rank.
    j_circuit = {
        "name": "J_sew=im(d0)",
        "generators": ["-omega12-omega13", "omega12-omega23", "omega13+omega23"],
        "rank": 2,
        "differential_stable": True,
        "not_defined_by_forcing_p_eta_to_zero": True,
    }

    packet = {
        "schema": "marici.cosmology-p-normal-marked-wall-cech-carrier.v1",
        "coefficient_ring": "R localized at K_CM with triple term R/(p)",
        "degrees": {"0": ["wall1", "wall2", "wall3"], "1": ["pair12", "pair13", "pair23"], "2": ["triple123_on_p0"]},
        "d0_wall_to_pair": d0,
        "d1_pair_to_triple": d1,
        "d_squared_zero": True,
        "E_CM": "zero complex on the K_CM-invertible stratum",
        "J_circuit": j_circuit,
        "minimal_relative_carrier_constructed": True,
        "prime_tests": prime_tests,
        "generic_nearby_pair_quotient_rank": 1,
        "special_sewn_H1_rank": 0,
        "special_sewn_H2_rank": 0,
        "Xi_survives_minimal_carrier": False,
        "minimal_Cech_p_normal_Bockstein_nonzero": False,
        "principal_ideal_dual_applied": False,
        "bulk_face_augmentation_constructed": False,
        "physical_period_covector_constructed": False,
        "conclusion": (
            "the source-ordered minimal marked-wall Cech complex is exact in the "
            "special pair/triple degrees, so its rank-one generic nearby quotient is "
            "killed by the triple term and cannot support a nonzero p-normal Bockstein"
        ),
        "next_gate": (
            "construct a separately source-derived bulk/face augmentation with a new degree-one "
            "lift H_p, then rerun d^2, quotient stability, and two-prime Xi survival"
        ),
        "passed": True,
    }
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
