#!/usr/bin/env python3
"""Exact audit of the phase-cone obstruction and density-lift typing."""

import hashlib
import json
from pathlib import Path

from sympy import I, Matrix, conjugate, simplify


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/complex-phase-cone-obstruction.json"


def adjoint(matrix):
    return conjugate(matrix.T)


def density(vector):
    return vector * adjoint(vector)


def main():
    e1 = Matrix([1, 0])
    e2 = Matrix([0, 1])

    # The phase orbit contains x and -x, so its conic hull contains a line.
    phase_orbit_pair = [e1, -e1]
    assert phase_orbit_pair[0] + phase_orbit_pair[1] == Matrix.zeros(2, 1)
    assert phase_orbit_pair[0] != Matrix.zeros(2, 1)

    # Density lift is phase invariant and not vector faithful.
    assert density(I * e1) == density(e1)
    assert I * e1 != e1
    assert density(Matrix.zeros(2, 1)) == Matrix.zeros(2)

    # It is not additive; the defect is exactly the mixed interference.
    plus = e1 + e2
    additive_defect = density(plus) - density(e1) - density(e2)
    expected_cross_terms = e1 * adjoint(e2) + e2 * adjoint(e1)
    assert additive_defect == expected_cross_terms
    assert additive_defect != Matrix.zeros(2)

    # Equal coordinate intensities can carry opposite coherences.
    minus = e1 - e2
    plus_density = density(plus)
    minus_density = density(minus)
    assert plus_density.diagonal() == minus_density.diagonal()
    coherence_difference = plus_density - minus_density
    assert coherence_difference == 2 * expected_cross_terms

    # Downstream density merely squares a scalar divisor.
    m = 2 + I
    scaled_density = density(m * plus)
    modulus_squared = simplify(conjugate(m) * m)
    assert modulus_squared == 5
    assert (scaled_density - modulus_squared * plus_density).applyfunc(simplify) == Matrix.zeros(2)

    payload = {
        "schema": "marici.kitaev.complex_phase_cone_obstruction.v1",
        "status": "pass",
        "phase_cone_theorem": "full U(1) invariance plus pointedness forces the zero cone",
        "minus_one_line_witness": [[1, 0], [-1, 0]],
        "density_lift": {
            "phase_invariant": True,
            "vector_faithful": False,
            "projective_ray_faithful_for_nonzero_vectors": True,
            "additive": False,
            "interference_defect": [[int(v) for v in row] for row in additive_defect.tolist()],
        },
        "diagonal_intensity_hostile": {
            "states": ["e1+e2", "e1-e2"],
            "same_diagonal": True,
            "coherence_difference": [[int(v) for v in row] for row in coherence_difference.tolist()],
        },
        "scalar_square_fixture": {
            "multiplier": "2 + I",
            "modulus_squared": str(modulus_squared),
            "density_zero_equivalent_to_scalar_zero_for_nonzero_reference": True,
            "explanatory_if_built_downstream": False,
        },
        "remaining_routes": [
            "source-derived transported real/phase frame",
            "source-derived polarization-complete operator kernel before scalar completion",
        ],
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope_exclusions": ["theta/Tate real form", "source operator kernel", "completion", "RH"],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
