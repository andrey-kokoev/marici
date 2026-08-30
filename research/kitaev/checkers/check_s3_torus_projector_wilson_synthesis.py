#!/usr/bin/env python3
"""Exact Wilson-loop synthesis cost for D(S3) torus sector projectors."""

from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
OUT = K / "results" / "s3-torus-projector-wilson-synthesis.json"


def main() -> None:
    data = json.loads((K / "results" / "s3-modular-data.json").read_text(encoding="utf-8"))
    labels = data["label_order"]
    S = sp.Matrix([[sp.Rational(Fraction(value).numerator, Fraction(value).denominator)
                    for value in row] for row in data["S_matrix"]])
    assert S.det() != 0

    # A Wilson loop of type x around one noncontractible cycle is diagonal in
    # the transverse anyon basis with eigenvalue S_xa/S_0a.
    eigenvalues = sp.Matrix(8, 8, lambda x, a: sp.simplify(S[x, a] / S[0, a]))
    assert eigenvalues.rank() == 8

    # Joint spectral readout only needs the selected rows to assign a distinct
    # eigenvalue signature to every sector.  This is weaker than spanning the
    # corresponding coherent projector Hamiltonians.
    distinguishing_families = []
    minimum_distinguishing = None
    for size in range(1, 9):
        for subset in itertools.combinations(range(8), size):
            signatures = {
                tuple(eigenvalues[row, column] for row in subset)
                for column in range(8)
            }
            if len(signatures) == 8:
                minimum_distinguishing = size
                distinguishing_families.append([labels[i] for i in subset])
        if minimum_distinguishing is not None:
            break
    assert minimum_distinguishing is not None

    synthesis = {}
    for target_index, target in enumerate(labels):
        desired = sp.zeros(8, 1)
        desired[target_index] = 1
        minimum = None
        families = []
        coefficients = None
        for size in range(1, 9):
            for subset in itertools.combinations(range(8), size):
                rows = eigenvalues[list(subset), :]
                # coefficients c obey c^T rows = desired^T.
                system = rows.T
                if system.rank() == sp.Matrix.hstack(system, desired).rank():
                    solution = sp.linsolve((system, desired))
                    vector = next(iter(solution))
                    if any(value.free_symbols for value in vector):
                        # Choose zero for any free parameters; minimal subsets
                        # below are independent in the cases of interest.
                        substitutions = {symbol: 0 for value in vector for symbol in value.free_symbols}
                        vector = tuple(sp.simplify(value.subs(substitutions)) for value in vector)
                    minimum = size
                    families.append([labels[i] for i in subset])
                    if coefficients is None:
                        coefficients = {
                            labels[subset[i]]: str(sp.simplify(vector[i]))
                            for i in range(size) if vector[i] != 0
                        }
            if minimum is not None:
                break
        assert minimum is not None
        synthesis[target] = {
            "minimum_wilson_loop_types": minimum,
            "minimum_families": families,
            "one_exact_coefficient_packet": coefficients,
        }

    # No native commuting-projector term distinguishes torus ground states:
    # their compression is a scalar.  Any nontrivial Q_a therefore lies
    # outside the direct native local Hamiltonian span.
    native_compressed_span_rank = 1
    assert all(item["minimum_wilson_loop_types"] > 1 for item in synthesis.values())

    completion_targets = ["A", "B", "C", "F"]
    completing_pairs = [("A", "C"), ("A", "F"), ("B", "C"), ("B", "F")]
    joint_synthesis = {}
    for left, right in completing_pairs:
        desired = sp.zeros(8, 2)
        desired[labels.index(left), 0] = 1
        desired[labels.index(right), 1] = 1
        minimum = None
        families = []
        coefficient_packet = None
        for size in range(1, 9):
            for subset in itertools.combinations(range(8), size):
                system = eigenvalues[list(subset), :].T
                if system.rank() != system.row_join(desired).rank():
                    continue
                solution = system.gauss_jordan_solve(desired)[0]
                substitutions = {
                    symbol: 0
                    for value in solution
                    for symbol in value.free_symbols
                }
                solution = solution.applyfunc(lambda value: sp.simplify(value.subs(substitutions)))
                minimum = size
                families.append([labels[i] for i in subset])
                if coefficient_packet is None:
                    coefficient_packet = {
                        target: {
                            labels[subset[i]]: str(solution[i, column])
                            for i in range(size) if solution[i, column] != 0
                        }
                        for column, target in enumerate((left, right))
                    }
            if minimum is not None:
                break
        assert minimum is not None
        joint_synthesis[f"{left}+{right}"] = {
            "minimum_joint_wilson_loop_types": minimum,
            "minimum_families": families,
            "one_exact_coefficient_packet": coefficient_packet,
        }

    cheapest_joint_cost = min(
        item["minimum_joint_wilson_loop_types"] for item in joint_synthesis.values()
    )
    cheapest_pairs = [
        pair for pair, item in joint_synthesis.items()
        if item["minimum_joint_wilson_loop_types"] == cheapest_joint_cost
    ]
    assert cheapest_joint_cost == 8
    result = {
        "schema": "marici.kitaev.s3-torus-projector-wilson-synthesis.v1",
        "wilson_character_table": {
            "rank": eigenvalues.rank(),
            "sector_projectors_are_reconstructible": True,
            "eigenvalue_formula": "lambda_x(a)=S[x,a]/S[A,a]",
        },
        "joint_spectral_readout": {
            "minimum_wilson_observables": minimum_distinguishing,
            "minimum_families": distinguishing_families,
            "faithful_on_sector_labels": True,
            "does_not_imply_coherent_projector_control": True,
        },
        "projector_synthesis": synthesis,
        "two_port_completion_targets": {
            label: synthesis[label] for label in completion_targets
        },
        "joint_two_port_synthesis": joint_synthesis,
        "cheapest_joint_completion": {
            "minimum_wilson_loop_types": cheapest_joint_cost,
            "pairs": cheapest_pairs,
        },
        "source_boundary": {
            "native_star_plaquette_compression_rank_on_torus_ground_space": native_compressed_span_rank,
            "native_local_terms_split_sector_degeneracy": False,
            "required_support": "noncontractible Wilson loops or an equivalent coherent global ancilla protocol",
            "phase_implementation": "requires coherent e^{it Q_a}; measuring Q_a or classically recording a does not supply it",
            "perturbative_alternative": "logical splitting can arise only at system-size order and is not an exact primitive port",
        },
        "verdict": "Every torus sector projector is exactly reconstructible from noncontractible Wilson-loop operators, but none is a native contractible Hamiltonian term. The minimal two-port controllability theorem therefore demands coherent global loop resources (or equivalent ancilla phase kickback), not local endpoint projectors. Measurement access remains strictly weaker than Hamiltonian control.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
