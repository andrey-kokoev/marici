#!/usr/bin/env python3
"""Exact phase-polynomial resource audit for D(S3) Wilson quarter gates."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from z3 import If, Int, Solver, Sum, sat


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
SOURCE = K / "results" / "s3-controlled-wilson-executability.json"
OUT = K / "results" / "s3-wilson-phase-polynomial-resources.json"


def parity(mask: int, value: int) -> int:
    return (mask & value).bit_count() & 1


def divisibility_obstruction(values: list[int], qubits: int) -> dict:
    """Return Boolean multilinear coefficients violating parity-phase divisibility."""
    coefficients = {}
    violations = []
    for mask in range(1, 1 << qubits):
        degree = mask.bit_count()
        coefficient = 0
        subset = mask
        while True:
            coefficient += (-1) ** (degree - subset.bit_count()) * values[subset]
            if subset == 0:
                break
            subset = (subset - 1) & mask
        coefficient %= 8
        required_divisor = min(8, 1 << (degree - 1))
        coefficients[str(mask)] = coefficient
        if coefficient % required_divisor:
            violations.append({
                "mask": mask,
                "degree": degree,
                "coefficient_mod8": coefficient,
                "required_divisor": required_divisor,
            })
    return {"multilinear_coefficients_mod8": coefficients, "violations": violations}


def minimize_phase_polynomial(values: list[int], qubits: int) -> dict:
    """Minimize odd coefficients in f(x)=sum a_m parity_m(x) mod 8."""
    assert len(values) == 1 << qubits
    coefficients = [Int(f"a_{qubits}_{mask}") for mask in range(1, 1 << qubits)]
    base_constraints = []
    for coefficient in coefficients:
        base_constraints.extend([coefficient >= 0, coefficient < 8])
    quotients = []
    for value in range(1 << qubits):
        quotient = Int(f"q_{qubits}_{value}_{id(values)}")
        quotients.append(quotient)
        expression = Sum([
            coefficients[mask - 1] * parity(mask, value)
            for mask in range(1, 1 << qubits)
        ])
        base_constraints.append(expression - values[value] == 8 * quotient)
    t_count = Sum([If(coefficient % 2 == 1, 1, 0) for coefficient in coefficients])
    model = None
    minimum = None
    rejected_bounds = []
    for bound in range(1 << qubits):
        solver = Solver()
        solver.add(*base_constraints, t_count <= bound)
        if solver.check() == sat:
            model = solver.model()
            minimum = bound
            break
        rejected_bounds.append(bound)
    if model is None:
        return {
            "realizable": False,
            "minimum_T_count": None,
            "coefficients_by_nonzero_parity_mask": None,
            "exact_mod8_residuals": None,
            "unsatisfiable_T_count_bounds": rejected_bounds,
        }
    # Canonicalize the optimal witness lexicographically so the result packet
    # is byte-stable across solver model choices.
    fixed = [t_count == minimum]
    solution = []
    for coefficient in coefficients:
        chosen = None
        for value in range(8):
            solver = Solver()
            solver.add(*base_constraints, *fixed, coefficient == value)
            if solver.check() == sat:
                chosen = value
                fixed.append(coefficient == value)
                break
        assert chosen is not None
        solution.append(chosen)
    residuals = [
        (sum(solution[mask - 1] * parity(mask, value)
             for mask in range(1, 1 << qubits)) - values[value]) % 8
        for value in range(1 << qubits)
    ]
    assert residuals == [0] * (1 << qubits)
    assert minimum == sum(coefficient & 1 for coefficient in solution)
    return {
        "realizable": True,
        "minimum_T_count": minimum,
        "coefficients_by_nonzero_parity_mask": solution,
        "exact_mod8_residuals": residuals,
        "unsatisfiable_T_count_bounds": rejected_bounds,
    }


def main() -> None:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    logical = {}
    controlled = {}
    for label, record in source["logical_normalizer_test"].items():
        residues4 = [value % 4 for value in record["wilson_eigenvalues"]]
        # i^r = exp(i*pi*(2r)/4), hence phase exponents live modulo eight.
        exact_values = [(2 * residue) % 8 for residue in residues4]
        # An uncontrolled unitary is equivalent up to global phase. Every
        # parity polynomial vanishes at zero, so choose that canonical gauge.
        logical_values = [(value - exact_values[0]) % 8 for value in exact_values]
        logical[label] = minimize_phase_polynomial(logical_values, 3)
        logical[label]["divisibility_audit"] = divisibility_obstruction(logical_values, 3)

        # Control is the most significant bit. Retain the exact target-block
        # phase: it becomes a relative phase and cannot be quotiented away.
        controlled_values = [0] * 8 + exact_values
        controlled[label] = minimize_phase_polynomial(controlled_values, 4)
        controlled[label]["divisibility_audit"] = divisibility_obstruction(controlled_values, 4)

    species = source["clifford_assisted_magic_equivalence"]["species"]
    species_costs = []
    for members in species:
        species_costs.append({
            "members": members,
            "logical_T_counts": sorted({logical[label]["minimum_T_count"] for label in members}),
            "controlled_T_counts": sorted({controlled[label]["minimum_T_count"] for label in members}),
        })

    assert {label for label, item in logical.items() if item["realizable"]} == {"D", "E"}
    assert logical["D"]["minimum_T_count"] == logical["E"]["minimum_T_count"] == 4
    assert all(not controlled[label]["realizable"] for label in controlled)
    assert all(not item["divisibility_audit"]["violations"]
               for item in logical.values() if item["realizable"])
    assert all(item["divisibility_audit"]["violations"]
               for item in logical.values() if not item["realizable"])
    assert all(item["divisibility_audit"]["violations"] for item in controlled.values())
    result = {
        "schema": "marici.kitaev.s3-wilson-phase-polynomial-resources.v1",
        "input_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "model": {
            "gate_set": "ancilla-free diagonal CNOT+T phase polynomials",
            "cost": "number of odd mod-8 parity coefficients",
            "logical_qubits": 3,
            "controlled_qubits": 4,
            "excluded": "measurement-assisted synthesis, ancillas, error correction, and physical T-state production",
        },
        "obstruction_theorem": "A parity phase on a subset expands with degree-d Boolean multilinear coefficient divisible by 2^(d-1). Modulo eight, every cubic coefficient must be divisible by four and every quartic coefficient must vanish. A displayed violation is an exact non-realizability certificate.",
        "logical_quarter_evolutions": logical,
        "controlled_quarter_evolutions": controlled,
        "species_costs": species_costs,
        "verdict": "Only the D/E logical species reduces to ancilla-free CNOT+T, at exact minimum T-count four. The C/F/G/H logical species violates cubic phase-polynomial divisibility, and all exact controlled lifts violate the degree constraints. Verified T states alone therefore do not close the frozen coherent Wilson-control interface.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
