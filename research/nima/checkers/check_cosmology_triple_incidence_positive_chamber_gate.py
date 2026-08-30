"""Positive-energy support gate for the triple-wall incidence divisor."""

from __future__ import annotations

import json
from pathlib import Path


OUT = Path(__file__).resolve().parents[1] / "results" / "cosmology_triple_incidence_positive_chamber_gate.json"


def main() -> None:
    # p = X1 + X2 + 3 X3 in the source positive-energy convention.
    coefficients = (1, 1, 3)
    assert all(value > 0 for value in coefficients)

    # On the closed nonnegative cone, a positive linear form vanishes only at
    # the origin.  Enumerate its face supports as an exact finite certificate.
    nonzero_faces = []
    for mask in range(1, 1 << 3):
        active_coefficients = [
            coefficients[index] for index in range(3) if mask & (1 << index)
        ]
        strictly_positive = all(value > 0 for value in active_coefficients)
        assert strictly_positive
        nonzero_faces.append(
            {"active_mask": mask, "active_coefficients": active_coefficients, "p_positive": True}
        )

    packet = {
        "schema": "marici.cosmology-triple-incidence-positive-chamber-gate.v1",
        "physical_energy_chamber": "X1,X2,X3>0",
        "incidence_parameter": "p=X1+X2+3*X3",
        "coefficient_vector": list(coefficients),
        "strict_positive_chamber_intersection": False,
        "closed_nonnegative_chamber_intersection": "X1=X2=X3=0 only",
        "nonzero_closed_faces_checked": len(nonzero_faces),
        "literal_positive_chain_activation": False,
        "analytic_continuation_activation_inferred": False,
        "all_soft_specialization_separate": True,
        "passed": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
