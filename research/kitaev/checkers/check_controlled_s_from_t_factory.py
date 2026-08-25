#!/usr/bin/env python3
"""Exact three-T synthesis and phase-polynomial lower bound for controlled-S."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
OUT = K / "results" / "controlled-s-from-t-factory.json"


def main() -> None:
    omega = np.exp(1j * np.pi / 4)
    target_exponents = [0, 0, 0, 2]  # CS phases in lexicographic |xy> order.

    solutions = []
    for cx, cy, cp in itertools.product(range(8), repeat=3):
        values = []
        for x, y in itertools.product(range(2), repeat=2):
            values.append((cx * x + cy * y + cp * (x ^ y)) % 8)
        if values == target_exponents:
            t_count = sum(coefficient % 2 for coefficient in (cx, cy, cp))
            solutions.append({"coefficients": [cx, cy, cp], "t_count": t_count})
    assert solutions
    minimum_t_count = min(row["t_count"] for row in solutions)
    minimum_solutions = [row for row in solutions if row["t_count"] == minimum_t_count]
    assert minimum_t_count == 3
    assert {tuple(row["coefficients"]) for row in minimum_solutions} == {(1, 1, 7), (5, 5, 3)}

    # Explicit circuit: T on x and y, compute x xor y into y, T-dagger on
    # that parity, then uncompute. Diagonal phases are omega^(x+y-(x xor y)).
    circuit_phases = np.array([
        omega ** ((x + y - (x ^ y)) % 8)
        for x, y in itertools.product(range(2), repeat=2)
    ])
    cs = np.diag([1, 1, 1, 1j]).astype(complex)
    assert np.max(np.abs(np.diag(circuit_phases) - cs)) < 1e-9

    # Applying the circuit to |++> prepares the shared injection resource.
    plus_plus = np.ones(4, dtype=complex) / 2
    prepared = np.diag(circuit_phases) @ plus_plus
    expected = np.array([1, 1, 1, 1j], dtype=complex) / 2
    assert np.max(np.abs(prepared - expected)) < 1e-9

    result = {
        "schema": "marici.kitaev.controlled-s-from-t-factory.v1",
        "phase_identity": "2*x*y = x+y-(x xor y) mod 8",
        "exact_circuit": ["T(x)", "T(y)", "CNOT(x->y)", "T_dagger(y)", "CNOT(x->y)"],
        "resources": {"T_or_T_dagger_injections": 3, "CNOT": 2, "workspace_ancillas": 0},
        "prepares_CS_magic_state_from_plus_plus": True,
        "phase_polynomial_search": {
            "linear_forms": ["x", "y", "x xor y"],
            "coefficient_domain": "Z/8",
            "solutions": solutions,
            "minimum_T_count": minimum_t_count,
            "minimum_solutions": minimum_solutions,
            "scope": "ancilla-free diagonal CNOT+T synthesis; arbitrary Clifford+T circuits with measurement are outside the lower bound",
        },
        "factory_reduction": {
            "CS_factory_from_verified_T_states": "consume three verified encoded |T> or conjugate states and execute the Clifford parity network",
            "new_magic_species_if_T_factory_exists": 0,
            "frozen_source_status": "no source-derived verified T-state factory is admitted",
            "fault_tolerance_boundary": "three injection exRecs plus two logical CNOTs must be scheduled and verified; algebraic T-count is not a physical error-rate estimate",
        },
        "verdict": "A CS magic-state factory is not an independent algebraic species if verified T states are available: exactly three T/T-dagger injections and two CNOTs prepare CS|++>, with no workspace ancilla. Three is optimal within ancilla-free diagonal phase-polynomial synthesis. The frozen source still lacks the upstream verified T factory, so this is a resource reduction rather than executable production.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
