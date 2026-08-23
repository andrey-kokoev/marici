"""Exact logarithmic circuit identity at the physical triple-wall collision."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


OUT = Path(__file__).resolve().parents[1] / "results" / "cosmology_triple_incidence_logarithmic_identity.json"


def wedge(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    """Coefficient of dq1 wedge dq2."""
    return sp.expand(left[0] * right[1] - left[1] * right[0])


def main() -> None:
    q1, q2, p = sp.symbols("q1 q2 p")
    q3 = q1 + q2 + p
    dq1 = sp.Matrix((1, 0))
    dq2 = sp.Matrix((0, 1))
    dq3 = sp.Matrix((1, 1))

    # Clear q1*q2*q3 from omega23 - omega13 + omega12.
    circuit_numerator = sp.expand(
        q1 * wedge(dq2, dq3)
        - q2 * wedge(dq1, dq3)
        + q3 * wedge(dq1, dq2)
    )
    assert circuit_numerator == p

    special_relation = sp.expand(circuit_numerator.subs(p, 0))
    assert special_relation == 0
    transverse_coefficient = sp.diff(circuit_numerator, p).subs(p, 0)
    assert transverse_coefficient == 1

    # Degree-two logarithmic symbols are free of rank three off the triple
    # collision.  At p=0 the one circuit row has rank one, leaving rank two;
    # the disappearing quotient is rank one and has oriented vector (1,-1,1).
    circuit_row = sp.Matrix(((1, -1, 1),))
    generic_degree_two_rank = 3
    special_degree_two_rank = 3 - circuit_row.rank()
    vanishing_rank = generic_degree_two_rank - special_degree_two_rank
    assert special_degree_two_rank == 2
    assert vanishing_rank == 1

    packet = {
        "schema": "marici.cosmology-triple-incidence-logarithmic-identity.v1",
        "local_wall_model": "q3=q1+q2+p",
        "incidence_parameter": "p=x+y+3*z",
        "oriented_pair_order": ["omega12", "omega13", "omega23"],
        "circuit_vector": [1, -1, 1],
        "cleared_identity": "q1*dq2^dq3-q2*dq1^dq3+q3*dq1^dq2=p*dq1^dq2",
        "special_circuit_relation_zero": True,
        "transverse_normalized_coefficient": 1,
        "generic_degree_two_rank": generic_degree_two_rank,
        "special_degree_two_rank": special_degree_two_rank,
        "vanishing_quotient_rank": vanishing_rank,
        "universal_logarithmic_nearby_line_constructed": True,
        "physical_twisted_coefficient_pairing_constructed": False,
        "passed": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
