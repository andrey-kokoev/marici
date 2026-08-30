#!/usr/bin/env python3
"""Exact audit of real-structure transport and unit-fixed ambiguity."""

import hashlib
import json
from pathlib import Path

from sympy import I, Matrix, conjugate


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/real-structure-transport.json"


def residual(transport, source_structure, target_structure):
    return transport * source_structure - target_structure * conjugate(transport)


def fixed(structure, vector):
    return structure * conjugate(vector) == vector


def main():
    one = Matrix([[1]])
    minus_one = Matrix([[-1]])
    identity_transport = Matrix([[1]])
    phase_transport = Matrix([[I]])

    # Identity does not transport R to iR; multiplication by i does.
    failed_line_residual = residual(identity_transport, one, minus_one)
    repaired_line_residual = residual(phase_transport, one, minus_one)
    assert failed_line_residual == Matrix([[2]])
    assert repaired_line_residual == Matrix.zeros(1)

    # Two distinct real structures fix the same unit in dimension two.
    standard = Matrix.eye(2)
    twisted = Matrix.diag(1, -1)
    unit = Matrix([1, 0])
    assert fixed(standard, unit)
    assert fixed(twisted, unit)
    assert standard != twisted
    assert fixed(standard, Matrix([0, 1]))
    assert not fixed(twisted, Matrix([0, 1]))
    assert fixed(twisted, Matrix([0, I]))

    # Identity preserves the unit but fails the full intertwiner law.
    identity = Matrix.eye(2)
    higher_rank_residual = residual(identity, standard, twisted)
    assert identity * unit == unit
    assert higher_rank_residual * conjugate(unit) == Matrix.zeros(2, 1)
    assert higher_rank_residual != Matrix.zeros(2)
    assert higher_rank_residual.rank() == 1

    # A scalar probe on the unit cannot distinguish the two structures.
    unit_probe = Matrix([[1, 0]])
    assert unit_probe * standard * conjugate(unit) == unit_probe * twisted * conjugate(unit)

    payload = {
        "schema": "marici.kitaev.real_structure_transport.v1",
        "status": "pass",
        "transport_law": "D S_plus = S_minus conjugate(D)",
        "one_dimensional_fixture": {
            "identity_residual": [[int(v) for v in row] for row in failed_line_residual.tolist()],
            "phase_i_residual_zero": repaired_line_residual == Matrix.zeros(1),
            "real_line_torsor": "U(1)/{+1,-1}",
        },
        "unit_fixed_ambiguity": {
            "dimension": 2,
            "structures_distinct": True,
            "common_fixed_unit": [1, 0],
            "identity_preserves_unit": True,
            "full_transport_residual_rank": higher_rank_residual.rank(),
            "unit_probe_distinguishes_structures": False,
        },
        "higher_rank_residual_family": "U(n-1)/O(n-1)",
        "required_source_datum": "full transported conjugation, not only a unit",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope_exclusions": ["theta/Tate conjugation", "gamma factor", "completion", "RH"],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
