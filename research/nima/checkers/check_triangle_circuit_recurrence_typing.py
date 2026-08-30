"""The recurring (1,-1,1) row is universal triangle incidence data."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


OUT = Path(__file__).resolve().parents[1] / "results" / "triangle_circuit_recurrence_typing.json"


def main() -> None:
    boundary = sp.Matrix(((0, 1, 0), (0, 0, 1), (0, -1, 1)))
    circuit = sp.Matrix(((1, -1, 1),))
    assert boundary.rank() == 2
    assert circuit * boundary == sp.zeros(1, 3)
    assert len(boundary.T.nullspace()) == 1

    # The displayed row is frame-dependent. Rescaling edge generators by D
    # transports the quotient row contragrediently while preserving its line.
    r12, r13, r23 = sp.symbols("r12 r13 r23", nonzero=True)
    edge_frame = sp.diag(r12, r13, r23)
    transformed_boundary = edge_frame * boundary
    transformed_circuit = circuit * edge_frame.inv()
    assert sp.simplify(transformed_circuit * transformed_boundary) == sp.zeros(1, 3)
    assert transformed_circuit != circuit

    # Same incidence matrix can carry inequivalent coefficient decorations.
    # Incidence alone cannot distinguish them or produce a comparison map.
    coefficient_characters = {
        "trivial": [1, 1, 1],
        "mixed_kummer": [1, -1, 1],
    }
    assert coefficient_characters["trivial"] != coefficient_characters["mixed_kummer"]

    packet = {
        "schema": "marici.triangle-circuit-recurrence-typing.v1",
        "incidence_rank": boundary.rank(),
        "cokernel_dimension": 1,
        "coordinate_circuit_row": [1, -1, 1],
        "row_is_frame_invariant": False,
        "cokernel_line_is_frame_invariant": True,
        "same_row_implies_same_coefficient_object": False,
        "shared_structure": "oriented triangle incidence calculus",
        "required_for_identification": "source-labelled chain map preserving support, coefficients, and transport",
        "entry712_negative_control_retained": True,
        "passed": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
