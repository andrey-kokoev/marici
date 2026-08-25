#!/usr/bin/env python3
"""Exact magic witness on the coherent native-ququart Wilson trajectory."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
NATIVE = K / "results" / "s3-native-ququart-wilson-compiler.json"
INTERFACE = K / "results" / "s3-hybrid-z4-binary-interface.json"
WITNESS = K / "results" / "ququart-digit-interface-magic-witness.json"
OUT = K / "results" / "ququart-wilson-coherence-magic.json"


def kron(*matrices: sp.Matrix) -> sp.Matrix:
    result = matrices[0]
    for matrix in matrices[1:]:
        result = sp.kronecker_product(result, matrix)
    return result


def unit_pauli_expectations(state: sp.Matrix, qubits: int) -> list[dict[str, str]]:
    x = sp.Matrix([[0, 1], [1, 0]])
    z = sp.diag(1, -1)
    unit = []
    for exponents in itertools.product(range(2), repeat=2*qubits):
        factors = [(x**exponents[2*j])*(z**exponents[2*j+1]) for j in range(qubits)]
        pauli = kron(*factors)
        expectation = sp.simplify((sp.conjugate(state).T*pauli*state)[0])
        if sp.simplify(expectation*sp.conjugate(expectation)) == 1:
            unit.append({"XZ_exponents": "".join(map(str, exponents)),
                         "expectation": str(expectation)})
    return unit


def main() -> None:
    i = sp.I
    # Digit order is r=2a+d. These are the four native F4 character states.
    branch_tests = {}
    for residue in range(4):
        pointer = sp.Matrix([i**(residue*r)/2 for r in range(4)])
        unit = unit_pauli_expectations(pointer, 2)
        assert len(unit) == 4
        branch_tests[str(residue)] = {
            "unit_magnitude_Pauli_count": len(unit),
            "is_binary_stabilizer": True,
            "unit_Paulis": unit,
        }

    # A coherent Boolean Wilson predicate b controls native Z4 on |+_4>.
    # The input is a free mixed stabilizer product in the native theory.
    input_state = sp.ones(8, 1)/sp.sqrt(8)
    controlled_z4 = sp.diag(*[
        i**(b*(2*a+d))
        for b, a, d in itertools.product(range(2), repeat=3)
    ])
    output_state = controlled_z4*input_state
    assert sp.simplify((sp.conjugate(output_state).T*output_state)[0]) == 1
    coherent_unit = unit_pauli_expectations(output_state, 3)
    assert len(coherent_unit) == 2
    assert len(coherent_unit) < 8

    sources = (NATIVE, INTERFACE, WITNESS)
    native, interface, witness = [json.loads(path.read_text(encoding="utf-8")) for path in sources]
    assert native["hybrid_primitive_classification"]["1"]["mixed_qubit_ququart_Clifford"] is False
    assert interface["exact_hybrid_decompositions"]["1"]["CS_or_CSdagger_count"] == 1
    assert witness["interface_consequence"]["task_specific_partial_interface_ruled_out"] is False
    result = {
        "schema": "marici.kitaev.ququart-wilson-coherence-magic.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sources
        },
        "fixed_residue_branches": {
            "states": "F4 character states sum_r i^(k r)|r>/2 under r=2a+d",
            "tests": branch_tests,
            "all_binary_stabilizer": True,
        },
        "coherent_control_test": {
            "input": "|+>_b tensor |+_4>_r",
            "operation": "sum_b |b><b| tensor Z4^b",
            "digit_decomposition": "CZ(b,a) CS(b,d)",
            "unit_magnitude_binary_Pauli_count": len(coherent_unit),
            "required_count_for_pure_three_qubit_stabilizer": 8,
            "unit_Paulis": coherent_unit,
            "is_binary_stabilizer": False,
        },
        "typing": {
            "classically_resolved_pointer_branches_need_magic_witness": False,
            "coherent_odd_Wilson_interaction_needs_nonstabilizer_resource_under_digit_map": True,
            "full_code_switch_cost_derived": False,
            "fault_tolerant_interface_admitted": False,
        },
        "verdict": "The restricted Wilson trajectory does not evade the interface obstruction. Each classically fixed F4 pointer branch is a binary stabilizer, so branchwise testing misses the cost. Before sector decoherence, however, the odd controlled-Z4 primitive sends the free product |+>|+4> to a binary nonstabilizer with only two unit Pauli expectations rather than eight. The resource is coherence-activated and lies in the controlled interaction, while its fault-tolerant conversion cost remains untyped.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
