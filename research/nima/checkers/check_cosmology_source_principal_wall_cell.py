"""Source-derived triple-incidence parameter for the physical shared walls."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


OUT = Path(__file__).resolve().parents[1] / "results" / "cosmology_source_principal_wall_cell.json"


def main() -> None:
    a, b, x, y, z = sp.symbols("a b x y z")
    q1 = b - y - z
    q2 = a - x - z
    q3 = a + b + z
    p = x + y + 3 * z
    coefficients = sp.Matrix((-1, -1, 1))
    walls = sp.Matrix((q1, q2, q3))

    source_relation = sp.expand((coefficients.T * walls)[0] - p)
    assert source_relation == 0

    fiber_jacobian = walls.jacobian((a, b))
    base_jacobian = walls.jacobian((x, y, z))
    assert coefficients.T * fiber_jacobian == sp.zeros(1, 2)
    induced_base_class = (coefficients.T * base_jacobian).applyfunc(sp.expand)
    dp = sp.Matrix(((sp.diff(p, x), sp.diff(p, y), sp.diff(p, z)),))
    assert induced_base_class == dp

    # The augmented row annihilates the labelled wall/principal column.
    # This is the algebraic cell (-q1-q2+q3)-p=0, not a homogeneous wall
    # syzygy and not a fitted null vector.
    augmented_coefficients = sp.Matrix(((-1, -1, 1, -1),))
    augmented_generators = sp.Matrix((q1, q2, q3, p))
    assert sp.expand((augmented_coefficients * augmented_generators)[0]) == 0

    pair_solutions = {
        "q1_q2": {a: x + z, b: y + z},
        "q1_q3": {b: y + z, a: -y - 2 * z},
        "q2_q3": {a: x + z, b: -x - 2 * z},
    }
    remaining_restrictions = {
        "q1_q2": sp.expand(q3.subs(pair_solutions["q1_q2"])),
        "q1_q3": sp.expand(q2.subs(pair_solutions["q1_q3"])),
        "q2_q3": sp.expand(q1.subs(pair_solutions["q2_q3"])),
    }
    assert remaining_restrictions == {"q1_q2": p, "q1_q3": -p, "q2_q3": -p}

    packet = {
        "schema": "marici.cosmology-source-triple-incidence-parameter.v2",
        "wall_order": ["q_g1", "q_g2", "q_g3"],
        "wall_relation_coefficients": [-1, -1, 1],
        "triple_incidence_base_function": str(p),
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
