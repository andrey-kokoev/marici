#!/usr/bin/env python3
"""Exact stabilizer-magic witness for the ququart-to-binary digit interface."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
ENCODING = K / "results" / "mod4-phase-kernel-encoding-boundary.json"
INTERFACE = K / "results" / "s3-hybrid-z4-binary-interface.json"
OUT = K / "results" / "ququart-digit-interface-magic-witness.json"


def kron(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return sp.kronecker_product(left, right)


def main() -> None:
    i = sp.I
    sqrt2 = sp.sqrt(2)
    x4 = sp.zeros(4)
    for column in range(4):
        x4[(column + 1) % 4, column] = 1
    z4 = sp.diag(1, i, -1, -i)
    witness = sp.Matrix([-sp.Rational(1, 2), (1+i)/(2*sqrt2),
                         sp.Rational(1, 2), (1+i)/(2*sqrt2)])
    eigenvalue = (-1+i)/sqrt2
    eigen_residual = sp.simplify((x4*z4)*witness - eigenvalue*witness)
    assert eigen_residual == sp.zeros(4, 1)
    eigenline_rank = (x4*z4 - eigenvalue*sp.eye(4)).rank()
    assert eigenline_rank == 3
    assert sp.simplify((sp.conjugate(witness).T*witness)[0]) == 1

    x = sp.Matrix([[0, 1], [1, 0]])
    z = sp.diag(1, -1)
    identity = sp.eye(2)
    pauli_expectations = {}
    unit_magnitude = []
    for a, b, c, d in itertools.product(range(2), repeat=4):
        pauli = kron((x**a)*(z**b), (x**c)*(z**d))
        expectation = sp.simplify((sp.conjugate(witness).T*pauli*witness)[0])
        magnitude_squared = sp.simplify(expectation*sp.conjugate(expectation))
        label = f"X{a}Z{b}_X{c}Z{d}"
        pauli_expectations[label] = str(expectation)
        if magnitude_squared == 1:
            unit_magnitude.append(label)
    assert len(unit_magnitude) == 2
    assert len(unit_magnitude) < 4

    encoding = json.loads(ENCODING.read_text(encoding="utf-8"))
    interface = json.loads(INTERFACE.read_text(encoding="utf-8"))
    assert encoding["pauli_lens_no_isomorphism"]["pauli_preserving_relabelling_exists"] is False
    assert interface["interface_boundary"]["free_digit_relabelling_allowed"] is False
    result = {
        "schema": "marici.kitaev.ququart-digit-interface-magic-witness.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (ENCODING, INTERFACE)
        },
        "native_ququart_state": {
            "amplitudes_in_digit_order_00_01_10_11": ["-1/2", "(1+i)/(2 sqrt(2))", "1/2", "(1+i)/(2 sqrt(2))"],
            "Pauli_eigenoperator": "X4 Z4",
            "eigenvalue": "(-1+i)/sqrt(2)",
            "exact_eigen_residual_zero": True,
            "eigenspace_dimension": 4 - eigenline_rank,
            "normalized": True,
        },
        "binary_two_qubit_test": {
            "unit_magnitude_Pauli_expectations": unit_magnitude,
            "unit_magnitude_count": len(unit_magnitude),
            "required_count_for_pure_two_qubit_stabilizer": 4,
            "is_binary_stabilizer_state": False,
            "all_expectations": pauli_expectations,
        },
        "interface_consequence": {
            "full_native_stabilizer_theory_to_binary_stabilizer_theory_is_free_under_digit_map": False,
            "magic_witness": "a native Pauli eigenstate maps to a binary nonstabilizer state",
            "independent_group_obstruction": "projective Pauli element-order censuses are nonisomorphic",
            "task_specific_partial_interface_ruled_out": False,
        },
        "verdict": "The digit interface is operationally resource-bearing, not merely a relabelling: an exact native X4Z4 Pauli eigenstate becomes a nonstabilizer two-qubit state with only two unit-magnitude Pauli expectations instead of four. Together with Pauli-group nonisomorphism this rules out a reversible free interface for the full stabilizer theories. A restricted interface tailored only to the Wilson pointer trajectory remains open.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
