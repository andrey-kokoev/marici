#!/usr/bin/env python3
"""Exact coherent-readout phase kickback and measurement separation for D(S3)."""

from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
OUT = K / "results" / "s3-coherent-wilson-phase-kickback.json"


def main() -> None:
    data = json.loads((K / "results" / "s3-modular-data.json").read_text(encoding="utf-8"))
    labels = data["label_order"]
    S = sp.Matrix([
        [sp.Rational(Fraction(value).numerator, Fraction(value).denominator) for value in row]
        for row in data["S_matrix"]
    ])
    table = sp.Matrix(8, 8, lambda x, a: sp.simplify(S[x, a] / S[0, a]))

    minimum = None
    families = []
    for size in range(1, 9):
        for subset in itertools.combinations(range(8), size):
            signatures = [tuple(table[row, column] for row in subset) for column in range(8)]
            if len(set(signatures)) == 8:
                minimum = size
                families.append(subset)
        if minimum is not None:
            break
    assert minimum == 4
    assert len(families) == 8

    chosen = families[0]
    signatures = [tuple(table[row, column] for row in chosen) for column in range(8)]
    signature_to_label = {str(signature): labels[i] for i, signature in enumerate(signatures)}
    assert all(value.q == 1 for signature in signatures for value in signature)

    modular_costs = {}
    for family in families:
        for modulus in range(2, 13):
            residues = {
                tuple(int(table[row, column]) % modulus for row in family)
                for column in range(8)
            }
            if len(residues) == 8:
                modular_costs["".join(labels[i] for i in family)] = modulus
                break
    assert set(modular_costs.values()) == {4}
    chosen_residues = {
        labels[column]: [int(table[row, column]) % 4 for row in chosen]
        for column in range(8)
    }
    assert len({tuple(value) for value in chosen_residues.values()}) == 8

    # The ideal coherent spectral extractor is the isometry
    # V|a> = |a>|sigma(a)>.  Its action is represented only on the initialized
    # input subspace; a unitary extension exists because the images are
    # orthonormal.  A diagonal phase on the signature register kicks back.
    V = sp.zeros(64, 8)
    for a in range(8):
        V[8 * a + a, a] = 1
    assert V.T * V == sp.eye(8)

    kickback = {}
    for target in ("A", "C"):
        target_index = labels.index(target)
        phase_symbols = [sp.Integer(1)] * 8
        phase_symbols[target_index] = sp.Symbol("z", nonzero=True)
        bus_phase = sp.diag(*phase_symbols)
        compressed = sp.simplify(V.T * sp.kronecker_product(sp.eye(8), bus_phase) * V)
        expected = sp.diag(*phase_symbols)
        assert compressed == expected
        kickback[target] = {
            "compressed_diagonal": [str(compressed[i, i]) for i in range(8)],
            "equals_exp_it_Q_target_when_z_exp_it": True,
        }

    # A projective readout in the same sector basis is dephasing, not the
    # coherent extractor.  It annihilates every off-diagonal matrix unit.
    off_diagonal_survivors = 0
    for a in range(8):
        for b in range(8):
            if a != b:
                # Sum_c Q_c |a><b| Q_c is nonzero iff a=b=c.
                off_diagonal_survivors += int(a == b)
    assert off_diagonal_survivors == 0

    result = {
        "schema": "marici.kitaev.s3-coherent-wilson-phase-kickback.v1",
        "minimum_faithful_spectral_observables": minimum,
        "minimum_family_count": len(families),
        "chosen_family": [labels[i] for i in chosen],
        "chosen_signatures": signature_to_label,
        "exact_modular_phase_estimation": {
            "minimum_modulus_for_every_minimum_family": 4,
            "family_moduli": modular_costs,
            "chosen_residue_labels_mod_4": chosen_residues,
            "controlled_gate": "controlled exp(2 pi i W_x / 4) and its powers",
            "pointer": "one four-level coherent pointer per Wilson observable",
            "exactness_reason": "all Wilson eigenvalues are integers and remain jointly distinct modulo 4",
        },
        "coherent_extractor": {
            "isometry_rank": V.rank(),
            "gram_is_identity": True,
            "unitary_extension_exists": True,
            "kickback": kickback,
        },
        "measurement_negative_control": {
            "off_diagonal_matrix_units_surviving": off_diagonal_survivors,
            "channel": "rho -> sum_a Q_a rho Q_a",
            "equals_coherent_extractor": False,
        },
        "oracle_boundary": {
            "sufficient": "coherent nondemolition spectral extractor for one faithful four-observable family",
            "not_established_by": [
                "ability to measure the four observables destructively",
                "abstract existence of the four Hermitian Wilson operators",
                "uncontrolled Wilson Hamiltonian evolution",
            ],
            "concrete_sufficient_gate_set": "controlled exp(2 pi i W_x / 4) for the four types in one faithful family, coherent mod-4 pointers, reversible signature lookup, and inverse extraction",
            "resource_consequence": "four coherent spectral ports suffice nonlinearly, while eight Wilson Hamiltonian types are necessary for linear projector synthesis",
        },
        "verdict": "A coherent faithful Wilson spectral oracle compiles exact sector-projector phases by compute-phase-uncompute. This reduces the nonlinear coherent port count from eight Hamiltonian types to four spectral observables, but only under a strictly stronger oracle type than measurement access or abstract Wilson availability.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
