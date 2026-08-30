#!/usr/bin/env python3
"""Test whether the two Wilson magic species coincide with intrinsic anyon strata."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
OUT = K / "results" / "s3-magic-species-categorical-origin.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mobius_coefficients_mod4(values: list[int]) -> list[int]:
    return [
        sum(
            (-1) ** (mask.bit_count() - subset.bit_count()) * values[subset]
            for subset in range(8) if subset & ~mask == 0
        ) % 4
        for mask in range(8)
    ]


def main() -> None:
    modular_path = K / "results" / "s3-modular-data.json"
    execution_path = K / "results" / "s3-controlled-wilson-executability.json"
    kickback_path = K / "results" / "s3-coherent-wilson-phase-kickback.json"
    modular = json.loads(modular_path.read_text(encoding="utf-8"))
    execution = json.loads(execution_path.read_text(encoding="utf-8"))
    kickback = json.loads(kickback_path.read_text(encoding="utf-8"))
    labels = modular["label_order"]
    S = sp.Matrix([
        [sp.Rational(Fraction(value).numerator, Fraction(value).denominator) for value in row]
        for row in modular["S_matrix"]
    ])
    total_dimension = modular["total_quantum_dimension"]
    dimensions = {
        label: int(sp.simplify(total_dimension * S[0, index]))
        for index, label in enumerate(labels)
    }
    assert dimensions == {"A": 1, "B": 1, "C": 2, "D": 3, "E": 3,
                          "F": 2, "G": 2, "H": 2}

    frozen_geometry = {
        "A": ("identity", "trivial"),
        "B": ("identity", "sign"),
        "C": ("identity", "standard"),
        "D": ("transposition", "plus"),
        "E": ("transposition", "minus"),
        "F": ("three-cycle", "trivial"),
        "G": ("three-cycle", "omega"),
        "H": ("three-cycle", "omega^2"),
    }
    species = execution["clifford_assisted_magic_equivalence"]["species"]
    species_by_dimension = {
        str(dimension): sorted(label for label in "CDEFGH" if dimensions[label] == dimension)
        for dimension in (2, 3)
    }
    assert sorted(species) == sorted(species_by_dimension.values())

    table = sp.Matrix(8, 8, lambda x, a: sp.simplify(S[x, a] / S[0, a]))
    phase_degree = {}
    quarter_phase_spectra = {}
    for label in "CDEFGH":
        row = labels.index(label)
        values = [int(table[row, sector]) % 4 for sector in range(8)]
        coefficients = mobius_coefficients_mod4(values)
        spectrum = {str(residue): values.count(residue) for residue in sorted(set(values))}
        quarter_phase_spectra[label] = spectrum
        odd_support_degrees = [
            mask.bit_count() for mask, coefficient in enumerate(coefficients)
            if coefficient % 2
        ]
        maximum_odd_degree = max(odd_support_degrees)
        phase_degree[label] = {
            "quantum_dimension": dimensions[label],
            "conjugacy_sector": frozen_geometry[label][0],
            "centralizer_irrep": frozen_geometry[label][1],
            "mobius_coefficients_mod_4": coefficients,
            "maximum_odd_phase_polynomial_degree": maximum_odd_degree,
        }
    assert all(phase_degree[label]["maximum_odd_phase_polynomial_degree"] == 3
               for label in "CFGH")
    assert all(phase_degree[label]["maximum_odd_phase_polynomial_degree"] == 2
               for label in "DE")
    assert len({json.dumps(quarter_phase_spectra[label], sort_keys=True)
                for label in "CFGH"}) == 1
    assert len({json.dumps(quarter_phase_spectra[label], sort_keys=True)
                for label in "DE"}) == 1
    assert quarter_phase_spectra["C"] != quarter_phase_spectra["D"]
    spectral_species = {}
    for label in "CDEFGH":
        key = json.dumps(quarter_phase_spectra[label], sort_keys=True)
        spectral_species.setdefault(key, []).append(label)
    assert sorted(spectral_species.values()) == sorted(species_by_dimension.values())

    family_census = {}
    for family in kickback["exact_modular_phase_estimation"]["family_moduli"]:
        census = {str(d): sum(dimensions[label] == d for label in family) for d in (2, 3)}
        assert census == {"2": 3, "3": 1}
        family_census[family] = census

    result = {
        "schema": "marici.kitaev.s3-magic-species-categorical-origin.v1",
        "inputs": {
            str(path.relative_to(ROOT)).replace("\\", "/"): digest(path)
            for path in (modular_path, execution_path, kickback_path)
        },
        "quantum_dimensions_from_S_first_row": dimensions,
        "magic_species_by_quantum_dimension": species_by_dimension,
        "species_equals_dimension_partition": True,
        "phase_polynomial_audit": phase_degree,
        "encoding_independent_quarter_phase_spectra": quarter_phase_spectra,
        "unitary_conjugacy_species": sorted(spectral_species.values()),
        "unitary_conjugacy_species_equals_dimension_partition": True,
        "minimum_family_dimension_census": family_census,
        "encoding_dependence": {
            "categorical_invariant": "quantum dimension and conjugacy/centralizer label",
            "encoding_independent_operator_invariant": "quarter-evolution eigenvalue multiplicity spectrum",
            "frozen_encoding_invariant": "maximum odd degree under affine relabeling and diagonal Clifford correction",
            "not_proven_invariant_under": "resource theories allowing multiplication by unrestricted non-Clifford corrections",
        },
        "explanatory_status": {
            "derived": "the two computed magic species coincide exactly with the intrinsic d=2 and d=3 anyon strata",
            "not_yet_derived": "a general theorem forcing Wilson quarter-evolution magic class from quantum dimension alone",
            "falsifier": "another frozen encoding/source-preserving free equivalence merging d=2 and d=3 quarter evolutions, or a D(G) example where equal dimension fails to predict the magic class",
        },
        "verdict": "The two-species split is not a binary-label accident: in frozen D(S3) it exactly equals both the categorical quantum-dimension partition and the encoding-independent unitary-conjugacy partition determined by quarter-phase spectra. Dimension-two sectors C,F,G,H have odd cubic phase content; dimension-three sectors D,E have odd quadratic but no odd cubic content. This is an exact finite explanation of the observed split, but not yet a universal theorem that quantum dimension determines magic species.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
