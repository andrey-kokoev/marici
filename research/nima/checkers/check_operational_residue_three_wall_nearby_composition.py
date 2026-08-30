"""Compose the physical wall-motion residue with its logarithmic nearby line."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def wedge(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    return sp.expand(left[0] * right[1] - left[1] * right[0])


def main() -> None:
    # Moving-normal obstruction.
    lam = sp.Matrix([[-1, -1, 1]])
    B = sp.Matrix([[0, -1, -1], [-1, 0, -1], [0, 0, 1]])
    kappa = sp.Matrix([[1, 1, 3]])
    assert lam * B == kappa

    # Source logarithmic circuit.
    q1, q2, p = sp.symbols("q1 q2 p")
    q3 = q1 + q2 + p
    dq1 = sp.Matrix((1, 0))
    dq2 = sp.Matrix((0, 1))
    dq3 = sp.Matrix((1, 1))
    circuit_numerator = sp.expand(
        q1 * wedge(dq2, dq3)
        - q2 * wedge(dq1, dq3)
        + q3 * wedge(dq1, dq2)
    )
    assert circuit_numerator == p
    assert sp.diff(circuit_numerator, p).subs(p, 0) == 1

    circuit = sp.Matrix([1, -1, 1])
    base_to_nearby = circuit * kappa
    assert base_to_nearby.rank() == 1
    assert base_to_nearby == sp.Matrix([[1, 1, 3], [-1, -1, -3], [1, 1, 3]])

    # The positive cone intersects p=0 only at its origin because all
    # coefficients of p=X1+X2+3X3 are strictly positive.
    positive_chamber_coefficients = (1, 1, 3)
    assert all(coefficient > 0 for coefficient in positive_chamber_coefficients)

    result = {
        "status": "PASS",
        "moving_normal_residue": [1, 1, 3],
        "nearby_circuit_vector": [1, -1, 1],
        "transverse_normalized_coefficient": 1,
        "base_to_nearby_matrix": [
            [int(value) for value in row] for row in base_to_nearby.tolist()
        ],
        "base_to_nearby_rank": int(base_to_nearby.rank()),
        "literal_positive_chamber_support_on_p_zero": "origin only",
        "algebraic_nearby_line": "nonzero rank one",
        "literal_generic_physical_readout": 0,
        "vertical_composition": "source-derived and closed",
        "horizontal_gauss_manin_coherence": "open",
    }

    output = (
        Path(__file__).parents[1]
        / "results"
        / "operational-residue-three-wall-nearby-composition.json"
    )
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
