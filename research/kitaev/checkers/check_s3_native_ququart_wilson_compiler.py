#!/usr/bin/env python3
"""Direct native-ququart compilation of faithful D(S3) Wilson extraction."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
WILSON = K / "results" / "s3-controlled-wilson-executability.json"
KICKBACK = K / "results" / "s3-coherent-wilson-phase-kickback.json"
OUT = K / "results" / "s3-native-ququart-wilson-compiler.json"


def equal_phase(left: np.ndarray, right: np.ndarray, tol: float = 1e-12) -> bool:
    overlap = np.vdot(right.reshape(-1), left.reshape(-1))
    if abs(overlap) < tol:
        return False
    phase = overlap / abs(overlap)
    return np.max(np.abs(left - phase * right)) < tol


def mixed_paulis() -> tuple[list[np.ndarray], list[np.ndarray]]:
    x2 = np.array([[0, 1], [1, 0]], complex)
    z2 = np.diag([1, -1]).astype(complex)
    x4 = np.roll(np.eye(4, dtype=complex), 1, axis=0)
    z4 = np.diag([1, 1j, -1, -1j]).astype(complex)
    paulis = []
    for a, b, c, d in itertools.product(range(2), range(2), range(4), range(4)):
        paulis.append(np.kron(np.linalg.matrix_power(x2, a) @ np.linalg.matrix_power(z2, b),
                              np.linalg.matrix_power(x4, c) @ np.linalg.matrix_power(z4, d)))
    generators = [np.kron(x2, np.eye(4)), np.kron(z2, np.eye(4)),
                  np.kron(np.eye(2), x4), np.kron(np.eye(2), z4)]
    return paulis, generators


def normalizes(unitary: np.ndarray, paulis: list[np.ndarray], generators: list[np.ndarray]) -> bool:
    return all(any(equal_phase(unitary @ generator @ unitary.conj().T, candidate)
                   for candidate in paulis) for generator in generators)


def mobius_mod4(values: list[int]) -> dict[int, int]:
    result = {}
    for mask in range(1, 8):
        coefficient = 0
        subset = mask
        while True:
            coefficient += (-1) ** (mask.bit_count() - subset.bit_count()) * values[subset]
            if subset == 0:
                break
            subset = (subset - 1) & mask
        if coefficient % 4:
            result[mask] = coefficient % 4
    reconstructed = [sum(c for mask, c in result.items() if value & mask == mask) % 4
                     for value in range(8)]
    assert reconstructed == values
    return result


def main() -> None:
    paulis, generators = mixed_paulis()
    primitive = {}
    for coefficient in (1, 2, 3):
        diagonal = np.diag([1j ** (coefficient * bit * residue)
                            for bit in range(2) for residue in range(4)]).astype(complex)
        primitive[str(coefficient)] = {
            "mixed_qubit_ququart_Clifford": normalizes(diagonal, paulis, generators),
            "inverse_coefficient_mod4": (-coefficient) % 4,
        }
    assert primitive["1"]["mixed_qubit_ququart_Clifford"] is False
    assert primitive["2"]["mixed_qubit_ququart_Clifford"] is True
    assert primitive["3"]["mixed_qubit_ququart_Clifford"] is False

    wilson = json.loads(WILSON.read_text(encoding="utf-8"))
    kickback = json.loads(KICKBACK.read_text(encoding="utf-8"))
    ports = {}
    for label, record in wilson["logical_normalizer_test"].items():
        residues = [value % 4 for value in record["wilson_eigenvalues"]]
        # Normalize the residue function by its value at sector 000. The
        # removed constant is a pointer-local Z4 phase and is native Clifford.
        normalized = [(value - residues[0]) % 4 for value in residues]
        coefficients = mobius_mod4(normalized)
        odd = sum(value % 2 for value in coefficients.values())
        even = sum(value == 2 for value in coefficients.values())
        ports[label] = {
            "constant_pointer_phase_mod4": residues[0],
            "boolean_coefficients_mod4": {str(mask): value for mask, value in coefficients.items()},
            "odd_hybrid_phase_invocations_full_cycle": 2 * odd,
            "even_Clifford_hybrid_phase_invocations_full_cycle": 2 * even,
            "data_predicates": [f"{mask:03b}" for mask in sorted(coefficients) if mask.bit_count() >= 2],
        }

    families = {}
    for family in sorted(kickback["exact_modular_phase_estimation"]["family_moduli"]):
        odd = sum(ports[label]["odd_hybrid_phase_invocations_full_cycle"] for label in family)
        even = sum(ports[label]["even_Clifford_hybrid_phase_invocations_full_cycle"] for label in family)
        predicates = {predicate for label in family for predicate in ports[label]["data_predicates"]}
        # Pair predicates 011,101,110 plus triple 111; the triple reuses one
        # pair as its first ladder level.
        shared_episodes = 3 + (1 if "111" in predicates else 0)
        families[family] = {
            "odd_nonClifford_hybrid_phase_invocations_full_cycle": odd,
            "even_Clifford_hybrid_phase_invocations_full_cycle": even,
            "shared_data_predicates": sorted(predicates),
            "ideal_shared_conjunction_episodes": shared_episodes,
            "native_F4_magic_invocations": 0,
        }
    winner = families["CDFG"]
    differences = {family: [record[key] - winner[key] for key in (
        "odd_nonClifford_hybrid_phase_invocations_full_cycle",
        "even_Clifford_hybrid_phase_invocations_full_cycle",
        "ideal_shared_conjunction_episodes")]
        for family, record in families.items() if family != "CDFG"}
    keys = ("odd_nonClifford_hybrid_phase_invocations_full_cycle",
            "even_Clifford_hybrid_phase_invocations_full_cycle",
            "ideal_shared_conjunction_episodes")
    pareto = [family for family, record in families.items() if not any(
        other != family
        and all(families[other][key] <= record[key] for key in keys)
        and any(families[other][key] < record[key] for key in keys)
        for other in families)]
    assert pareto == ["CDFG", "CDFH", "CDGH"]
    assert families["CDFG"]["odd_nonClifford_hybrid_phase_invocations_full_cycle"] == 26
    result = {
        "schema": "marici.kitaev.s3-native-ququart-wilson-compiler.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (WILSON, KICKBACK)
        },
        "hybrid_primitive_classification": primitive,
        "ports": ports,
        "families": families,
        "CDFG_difference_table": differences,
        "pareto_optimal_families": pareto,
        "cost_boundary": "Odd hybrid controlled-Z4 coefficients define a non-Clifford primitive species but no T-state conversion cost is inferred. Native F4 is Clifford. Shared predicate compute/uncompute is ideal and retains the prior fault-light-cone blocker.",
        "verdict": "A direct native-ququart compiler exists without importing the binary circuit: Boolean Wilson predicates control Z4^c on each ququart pointer. Coefficient c=2 is mixed-Pauli Clifford, while c=1,3 are non-Clifford. The result supplies exact primitive counts and family Pareto data, not a binary T-count or a fault-tolerant exRec.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
