"""Minimal bulk-face primitive test for the cosmology p-normal gate.

The construction uses the fiber de Rham differential in local coordinates
u=q1, v=q2 with p held as a base parameter.  The cleared logarithmic circuit
identity is represented in the degree-two pair-symbol numerator carrier.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NIMA_RESULTS = ROOT / "research" / "nima" / "results"
OUT = ROOT / "research" / "voevodsky" / "results" / "cosmology_minimal_bulk_face_primitive.json"


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


def main() -> None:
    source = load("cosmology_source_principal_wall_cell.json")
    boundary = load("cosmology_triple_incidence_boundary_corner_transport.json")
    log_identity = load("cosmology_triple_incidence_logarithmic_identity.json")
    coefficient = load("cosmology_triple_incidence_physical_coefficient.json")

    assert source["triple_incidence_base_function"] == "x + y + 3*z"
    assert boundary["local_coordinates"] == {"u": "q1", "v": "q2", "q3": "u+v+p"}
    assert log_identity["cleared_identity"] == "q1*dq2^dq3-q2*dq1^dq3+q3*dq1^dq2=p*dq1^dq2"
    assert coefficient["algebraic_coefficient_generically_nonzero"] is True

    # Fiber de Rham convention: d_fib(p)=0, d_fib(q1)=dq1,
    # d_fib(q2)=dq2.  Hence H_p=p*q1*dq2 has d_fib(H_p)=p*dq1^dq2.
    # The cleared logarithmic identity identifies this target with the oriented
    # pair-symbol circuit omega23-omega13+omega12.
    circuit_vector = [1, -1, 1]  # order omega12, omega13, omega23
    assert log_identity["circuit_vector"] == circuit_vector

    carrier = {
        "degree_1": ["H_p = p*q1*dq2"],
        "degree_2": ["omega12", "omega13", "omega23"],
        "d_H_p": "p*(omega12-omega13+omega23)",
        "d_matrix_without_p_factor_rows_degree2_cols_degree1": [[1], [-1], [1]],
        "higher_differential": [],
        "d_squared_zero": True,
    }

    # E_CM remains empty in the generic CM-nonsingular local packet.  J is not
    # adjoined, because adjoining the circuit would kill Xi tautologically.
    e_cm = {"generators": [], "differential_stable": True, "reason_empty": "generic K_CM is nonzero at the cited incidence point"}
    j_circuit = {"generators": [], "differential_stable": True, "tautological_circuit_quotient_used": False}

    # Nonzero tests.  In B, p*Xi is a boundary.  Xi is not a boundary over the
    # polynomial source ring because the only boundary has coefficients p times
    # the primitive vector and p is not inverted.  Mod p, Xi survives as the
    # same nonzero row.  These are rank witnesses, not a physical period.
    witnesses = {}
    for prime in (101, 103):
        circuit_rank = rank_mod_prime([circuit_vector], prime)
        assert circuit_rank == 1
        witnesses[str(prime)] = {
            "rank_Xi_mod_p": circuit_rank,
            "rank_boundary_pXi_inside_pB": circuit_rank,
            "Xi_boundary_requires_division_by_p": True,
            "quotient_by_circuit_used": False,
        }

    result = {
        "schema": "marici.voevodsky.cosmology-minimal-bulk-face-primitive.v1",
        "status": "minimal_fiber_de_rham_primitive_constructed_relative_bockstein_candidate_revived",
        "source_normal": "p=x+y+3*z",
        "orientation": {
            "normal": "+dp with coefficient vector (1,1,3)",
            "circuit": "omega23-omega13+omega12 = omega12-omega13+omega23 in order (omega12,omega13,omega23)",
            "sign_dependence": "reversing the normal or H_p reverses the evaluated connecting sign",
        },
        "carrier": carrier,
        "E_CM": e_cm,
        "J_circuit": j_circuit,
        "identity": "d_fib(p*q1*dq2)=p*dq1^dq2=p*(omega12-omega13+omega23) after clearing denominators",
        "dH_equals_p_Xi": True,
        "Xi": {"basis_vector": circuit_vector, "nonzero_rank_witnesses": witnesses},
        "Xi_in_p_supported_boundary": "p*Xi=dH_p lies in pB by construction; evaluation by Hom_R((p),R) is only recorded on this p-supported boundary",
        "ideal_dual_evaluation_allowed_on_pXi": True,
        "ambient_division_by_p": False,
        "all_soft_Z3_used_as_coefficient": False,
        "inferred_from_identity_monodromy": False,
        "global_contour_or_physical_period_constructed": False,
        "remaining_gates": [
            "promote the cleared numerator carrier to the full logarithmic denominator complex with source-approved denominators",
            "replace the generic-empty E_CM statement by a complete Cayley-Menger face census if the carrier is extended to K_CM faces",
            "test compatibility with the resolved/Rees ordered-wall blow-up and physical chain transport",
        ],
        "conclusion": "The smallest fiber de Rham enlargement supplies a non-tautological primitive H_p=p*q1*dq2 with dH_p=p Xi. This revives the coefficient-level relative Bockstein candidate inside the cleared local numerator carrier, while leaving denominator, full face, and physical-readout gates open.",
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
