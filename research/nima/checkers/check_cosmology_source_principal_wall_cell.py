"""Source-derived triple-incidence parameter for the physical shared walls."""

from __future__ import annotations

import json
from pathlib import Path



OUT = Path(__file__).resolve().parents[1] / "results" / "cosmology_source_principal_wall_cell.json"


def dot(row, matrix):
    return [sum(row[i] * matrix[i][j] for i in range(len(row))) for j in range(len(matrix[0]))]


def main() -> None:
    coefficients = [-1, -1, 1]
    fiber_jacobian = [[0, 1], [1, 0], [1, 1]]
    base_jacobian = [[0, -1, -1], [-1, 0, -1], [0, 0, 1]]
    assert dot(coefficients, fiber_jacobian) == [0, 0]
    assert dot(coefficients, base_jacobian) == [1, 1, 3]

    # Symbolic identity checked coefficientwise for variables (a,b,x,y,z):
    # -q1 - q2 + q3 - p = 0, where
    # q1=b-y-z, q2=a-x-z, q3=a+b+z, p=x+y+3z.
    q1 = [0, 1, 0, -1, -1]
    q2 = [1, 0, -1, 0, -1]
    q3 = [1, 1, 0, 0, 1]
    p_coefficients = [0, 0, 1, 1, 3]
    identity = [-q1[i] - q2[i] + q3[i] - p_coefficients[i] for i in range(5)]
    assert identity == [0, 0, 0, 0, 0]

    remaining_restrictions = {
        "q1_q2": "x + y + 3*z",
        "q1_q3": "-x - y - 3*z",
        "q2_q3": "-x - y - 3*z",
    }

    packet = {
        "schema": "marici.cosmology-source-triple-incidence-parameter.v2",
        "wall_order": ["q_g1", "q_g2", "q_g3"],
        "wall_relation_coefficients": [-1, -1, 1],
        "triple_incidence_base_function": "x + y + 3*z",
        "source_identity": "-q_g1-q_g2+q_g3-(x+y+3*z)=0",
        "fiber_normal_cokernel": [-1, -1, 1],
        "induced_base_first_jet": [1, 1, 3],
        "remaining_wall_on_pair_intersections": {
            key: str(value) for key, value in remaining_restrictions.items()
        },
        "triple_intersection_locus": "p=0",
        "incidence_parameter_source_derived": True,
        "independent_principal_line_inferred": False,
        "homogeneous_wall_syzygy": False,
        "triple_cech_nearby_cycle_constructed": False,
        "passed": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
