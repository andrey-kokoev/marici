"""Exact coefficient-positivity gate for the physical five-pole families."""

from __future__ import annotations

import json


VARIABLES = ("X1", "X2", "X3", "y12", "y23", "y31")

# Coefficient vectors in the source convention.  Every connected-subgraph
# denominator is the sum of its site energies and the edge weights leaving it.
FORMS = {
    "q_g1": (1, 0, 0, 1, 0, 1),
    "q_g2": (0, 1, 0, 1, 1, 0),
    "q_g3": (0, 0, 1, 0, 1, 1),
    "q_G12": (1, 1, 1, 1, 0, 0),
    "q_g23": (0, 1, 1, 1, 0, 1),
    "q_g31": (1, 0, 1, 1, 1, 0),
}


def main() -> None:
    rows = {}
    for name, coefficients in FORMS.items():
        nonnegative = all(coefficient >= 0 for coefficient in coefficients)
        has_positive_energy = any(
            coefficients[index] > 0 for index in range(3)
        )
        rows[name] = {
            "coefficients": dict(zip(VARIABLES, coefficients, strict=True)),
            "all_coefficients_nonnegative": nonnegative,
            "contains_strictly_positive_energy": has_positive_energy,
            "strictly_positive_on_physical_chamber": (
                nonnegative and has_positive_energy
            ),
        }

    families = {
        "123_G12_23": ("q_g1", "q_g2", "q_g3", "q_G12", "q_g23"),
        "123_G12_31": ("q_g1", "q_g2", "q_g3", "q_G12", "q_g31"),
    }
    family_results = {
        name: all(rows[form]["strictly_positive_on_physical_chamber"] for form in forms)
        for name, forms in families.items()
    }
    assert all(family_results.values())

    print(
        json.dumps(
            {
                "schema": "marici.physical-positive-chamber-q-wall-gate.v1",
                "physical_chamber": "X1,X2,X3 > 0 and y12,y23,y31 >= 0",
                "forms": rows,
                "families_strictly_positive": family_results,
                "physical_contour_intersects_q_wall_divisor": False,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
