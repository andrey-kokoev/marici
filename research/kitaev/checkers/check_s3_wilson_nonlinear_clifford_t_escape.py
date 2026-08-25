#!/usr/bin/env python3
"""Constructive nonlinear Clifford+T escape for D(S3) Wilson phase gates."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
SOURCE = K / "results" / "s3-wilson-phase-polynomial-resources.json"
WILSON_SOURCE = K / "results" / "s3-controlled-wilson-executability.json"
OUT = K / "results" / "s3-wilson-nonlinear-clifford-t-escape.json"


def single(gate: np.ndarray, qubit: int, count: int) -> np.ndarray:
    result = np.array([[1]], dtype=complex)
    for index in range(count):
        result = np.kron(result, gate if index == qubit else np.eye(2))
    return result


def controlled_x(control: int, target: int, count: int) -> np.ndarray:
    result = np.zeros((1 << count, 1 << count), dtype=complex)
    for value in range(1 << count):
        bits = [(value >> (count - 1 - q)) & 1 for q in range(count)]
        output = bits[:]
        if bits[control]:
            output[target] ^= 1
        out_value = sum(bit << (count - 1 - q) for q, bit in enumerate(output))
        result[out_value, value] = 1
    return result


def verify_seven_t_toffoli() -> float:
    h = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    t = np.diag([1, np.exp(1j * np.pi / 4)])
    tdg = t.conj().T
    gates = [
        single(h, 2, 3), controlled_x(1, 2, 3), single(tdg, 2, 3),
        controlled_x(0, 2, 3), single(t, 2, 3), controlled_x(1, 2, 3),
        single(tdg, 2, 3), controlled_x(0, 2, 3), single(t, 1, 3),
        single(t, 2, 3), single(h, 2, 3), controlled_x(0, 1, 3),
        single(t, 0, 3), single(tdg, 1, 3), controlled_x(0, 1, 3),
    ]
    circuit = np.eye(8, dtype=complex)
    for gate in gates:
        circuit = gate @ circuit
    target = np.eye(8, dtype=complex)
    target[6, 6] = target[7, 7] = 0
    target[6, 7] = target[7, 6] = 1
    residual = float(np.max(np.abs(circuit - target)))
    assert residual < 1e-12
    return residual


def compile_from_mobius(record: dict, target_values: list[int]) -> dict:
    coefficients = {
        int(mask): value
        for mask, value in record["divisibility_audit"]["multilinear_coefficients_mod8"].items()
        if value % 8
    }
    monomials = []
    total_t = 0
    total_toffoli = 0
    max_clean_ancillas = 0
    for mask, coefficient in sorted(coefficients.items()):
        degree = mask.bit_count()
        if degree == 1:
            toffoli = 0
            clean_ancillas = 0
        else:
            toffoli = 2 * (degree - 1)
            clean_ancillas = degree - 1
        phase_t = coefficient & 1
        t_upper = 7 * toffoli + phase_t
        total_t += t_upper
        total_toffoli += toffoli
        max_clean_ancillas = max(max_clean_ancillas, clean_ancillas)
        monomials.append({
            "mask": mask,
            "degree": degree,
            "coefficient_mod8": coefficient,
            "compute_uncompute_Toffoli": toffoli,
            "phase_T_or_Tdagger": phase_t,
            "T_count_upper_bound": t_upper,
        })
    reconstructed = []
    for value in range(len(target_values)):
        reconstructed.append(sum(
            coefficient
            for mask, coefficient in coefficients.items()
            if value & mask == mask
        ) % 8)
    residuals = [(left - right) % 8 for left, right in zip(reconstructed, target_values)]
    assert residuals == [0] * len(target_values)
    return {
        "construction": "compute each Boolean monomial by a clean-ancilla Toffoli ladder, apply T^coefficient to its indicator, and uncompute; reuse work ancillas between monomials",
        "exact": True,
        "monomials": monomials,
        "total_Toffoli": total_toffoli,
        "T_count_upper_bound_using_exact_7T_Toffoli": total_t,
        "maximum_reusable_clean_ancillas": max_clean_ancillas,
        "target_reconstruction_residuals_mod8": residuals,
        "optimality_claimed": False,
    }


def main() -> None:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    wilson = json.loads(WILSON_SOURCE.read_text(encoding="utf-8"))
    residual = verify_seven_t_toffoli()
    logical = {}
    controlled = {}
    for label, record in source["logical_quarter_evolutions"].items():
        exact = [(2 * (value % 4)) % 8
                 for value in wilson["logical_normalizer_test"][label]["wilson_eigenvalues"]]
        normalized = [(value - exact[0]) % 8 for value in exact]
        logical[label] = compile_from_mobius(record, normalized)
        controlled[label] = compile_from_mobius(
            source["controlled_quarter_evolutions"][label], [0] * 8 + exact
        )
    assert all(item["exact"] for item in logical.values())
    assert all(item["exact"] for item in controlled.values())
    assert max(item["maximum_reusable_clean_ancillas"] for item in logical.values()) <= 2
    assert max(item["maximum_reusable_clean_ancillas"] for item in controlled.values()) <= 3
    result = {
        "schema": "marici.kitaev.s3-wilson-nonlinear-clifford-t-escape.v1",
        "input_sha256": {
            str(SOURCE.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            str(WILSON_SOURCE.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(WILSON_SOURCE.read_bytes()).hexdigest(),
        },
        "seven_T_Toffoli_matrix_max_residual": residual,
        "logical_quarter_evolutions": logical,
        "controlled_quarter_evolutions": controlled,
        "resource_boundary": {
            "clean_ancillas": "at most two for logical gates and three for controlled gates, reusable between monomials",
            "T_states": "finite explicit upper bounds only; no optimality claim",
            "fault_tolerance": "not established",
            "source_factory": "not established",
        },
        "verdict": "Entry 2494 is an architectural no-go, not a general exact Clifford+T no-go. Nonlinear reversible conjunctions computed with exact 7T Toffolis give finite clean-ancilla Clifford+T constructions for every logical and controlled Wilson quarter gate. The remaining blocker is verified fault-tolerant production and scheduling, not algebraic exactness.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
