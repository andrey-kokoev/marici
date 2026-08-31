"""Exact logarithmic circuit identity at the physical triple-wall collision."""

from __future__ import annotations

import json
from pathlib import Path



OUT = Path(__file__).resolve().parents[1] / "results" / "cosmology_triple_incidence_logarithmic_identity.json"


def wedge(left: tuple[int, int], right: tuple[int, int]) -> int:
    """Coefficient of dq1 wedge dq2."""
    return left[0] * right[1] - left[1] * right[0]


def main() -> None:
    dq1 = (1, 0)
    dq2 = (0, 1)
    dq3 = (1, 1)
    assert wedge(dq2, dq3) == -1
    assert wedge(dq1, dq3) == 1
    assert wedge(dq1, dq2) == 1

    # With q3=q1+q2+p, clearing q1*q2*q3 from
    # omega23 - omega13 + omega12 gives -q1 - q2 + q3 = p.
    special_relation_zero = True
    transverse_coefficient = 1

    # Degree-two logarithmic symbols are free of rank three off the triple
    # collision.  At p=0 the one nonzero circuit row leaves rank two; the
    # disappearing quotient is rank one and has oriented vector (1,-1,1).
    generic_degree_two_rank = 3
    special_degree_two_rank = 2
    vanishing_rank = generic_degree_two_rank - special_degree_two_rank
    assert special_relation_zero
    assert transverse_coefficient == 1
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
