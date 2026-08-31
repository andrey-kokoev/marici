"""Minimal local log/face carrier census for the triple-incidence divisor.

The checker deliberately constructs only the source-local logarithmic wall
carrier supplied by q3=q1+q2+p and the known generic Cayley--Menger nonsingularity.
It tests whether this minimal carrier already supplies the missing p-normal
Bockstein data.  It does not add a bulk-face differential or a hidden primitive.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NIMA_RESULTS = ROOT / "research" / "nima" / "results"
OUT = ROOT / "research" / "voevodsky" / "results" / "cosmology_minimal_log_face_carrier_census.json"


def load(name: str) -> dict:
    return json.loads((NIMA_RESULTS / name).read_text(encoding="utf-8"))


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


def matmul(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    if not left or not right:
        return []
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def zero_matrix(rows: int, cols: int) -> list[list[int]]:
    return [[0 for _ in range(cols)] for _ in range(rows)]


def main() -> None:
    source = load("cosmology_source_principal_wall_cell.json")
    boundary = load("cosmology_triple_incidence_boundary_corner_transport.json")
    log_identity = load("cosmology_triple_incidence_logarithmic_identity.json")
    coefficient = load("cosmology_triple_incidence_physical_coefficient.json")

    assert source["triple_incidence_base_function"] == "x + y + 3*z"
    assert boundary["local_coordinates"] == {"u": "q1", "v": "q2", "q3": "u+v+p"}
    assert log_identity["circuit_vector"] == [1, -1, 1]
    assert log_identity["cleared_identity"].endswith("=p*dq1^dq2")
    assert coefficient["algebraic_coefficient_generically_nonzero"] is True

    # Minimal logarithmic wall carrier.  In the dlog algebra the generators are
    # closed; no bulk-face primitive is inserted.
    bases = {
        "degree_0": ["1"],
        "degree_1": ["alpha1=dlog(q1)", "alpha2=dlog(q2)", "alpha3=dlog(q3)"],
        "degree_2": ["omega12", "omega13", "omega23"],
    }
    d0 = zero_matrix(3, 1)
    d1 = zero_matrix(3, 3)
    assert matmul(d1, d0) == zero_matrix(3, 1)

    # Generic local triple incidence is away from K=0, so the source-local
    # Cayley--Menger face subcomplex has no generator in this minimal carrier.
    e_cm_rows: list[list[int]] = []
    e_cm_stable = True

    # The special Orlik--Solomon circuit is visible only after p=0.  As an
    # abstract degree-two row it is stable because d=0, but using it as J kills
    # the candidate target row by definition and is recorded separately from the
    # non-tautological quotient option J=0.
    circuit_row = [[1, -1, 1]]
    j_options = {
        "J_zero": {
            "degree_2_relation_rank": 0,
            "quotient_degree_2_rank": 3,
            "tautologically_kills_circuit": False,
            "differential_stable": True,
        },
        "J_special_circuit_row": {
            "degree_2_relation_rank": 1,
            "quotient_degree_2_rank": 2,
            "tautologically_kills_circuit": True,
            "differential_stable": True,
        },
    }

    witnesses = {}
    for prime in (101, 103):
        assert rank_mod_prime(d0, prime) == 0
        assert rank_mod_prime(d1, prime) == 0
        assert rank_mod_prime(circuit_row, prime) == 1
        witnesses[str(prime)] = {
            "rank_d0": 0,
            "rank_d1": 0,
            "rank_E_CM": 0,
            "rank_special_circuit_row": 1,
            "H2_rank_with_J_zero": 3,
            "H2_rank_after_special_circuit_quotient": 2,
        }

    # Because d1=0, no H in degree one has dH=p*Xi with nonzero Xi over the
    # polynomial source ring where p is not made zero.  This is the adjacent
    # obstruction: the missing datum is not E_CM stability but a source-derived
    # bulk-face differential or primitive hitting the p-multiple.
    nonzero_lift_possible_in_minimal_carrier = False

    result = {
        "schema": "marici.voevodsky.cosmology-minimal-log-face-carrier-census.v1",
        "status": "minimal_local_carrier_constructed_bockstein_lift_absent",
        "source_normal": "p=x+y+3*z",
        "carrier_scope": "source-local logarithmic three-wall algebra at generic Cayley--Menger-nonsingular triple incidence",
        "bases": bases,
        "differentials": {
            "d0_matrix_rows_degree1_cols_degree0": d0,
            "d1_matrix_rows_degree2_cols_degree1": d1,
            "d_squared_zero": True,
        },
        "E_CM": {
            "generators": [],
            "reason_empty": "the generic triple-incidence point is not on the Cayley--Menger face K=0 in the cited source packet",
            "differential_stable": e_cm_stable,
            "rank": len(e_cm_rows),
        },
        "J_circuit_options": j_options,
        "finite_field_witnesses": witnesses,
        "p_non_zero_divisor_assumed_from_source_ring": True,
        "H_p_with_nonzero_dH_equals_p_Xi_exists": nonzero_lift_possible_in_minimal_carrier,
        "first_new_missing_datum": "a source-derived bulk-face differential or primitive H_p whose boundary is the p-multiple of the logarithmic circuit class",
        "ideal_dual_evaluation_applied": False,
        "ambient_division_by_p": False,
        "global_contour_or_physical_period_constructed": False,
        "conclusion": "The minimal local logarithmic carrier closes d^2 and has a stable empty E_CM subcomplex, but its differential is zero. The special circuit row can be seen by rank specialization, yet quotienting by it would kill the candidate class tautologically. Therefore this carrier cannot supply dH_p=p Xi_p with Xi_p nonzero; the next construction must add source-derived bulk-face data rather than only repair E_CM stability.",
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
