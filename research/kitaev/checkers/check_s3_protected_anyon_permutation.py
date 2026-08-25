#!/usr/bin/env python3
"""Exact D(S3) modular-data automorphisms and their three-bit Clifford type."""

from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
OUT = K / "results" / "s3-protected-anyon-permutation.json"


def parse_rational(text: str) -> Fraction:
    return Fraction(text)


def xor(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a ^ b for a, b in zip(left, right))


def main() -> None:
    modular = json.loads((K / "results" / "s3-modular-data.json").read_text(encoding="utf-8"))
    fusion = json.loads((K / "results" / "s3-fusion-ring.json").read_text(encoding="utf-8"))
    labels = modular["label_order"]
    index = {label: i for i, label in enumerate(labels)}
    smatrix = [[parse_rational(value) for value in row] for row in modular["S_matrix"]]
    twists = modular["topological_spins"]

    # Enumerate every vacuum-fixing permutation preserving S and T exactly.
    automorphisms = []
    for tail in itertools.permutations(range(1, len(labels))):
        p = (0,) + tail
        if any(twists[labels[i]] != twists[labels[p[i]]] for i in range(len(labels))):
            continue
        if any(
            smatrix[i][j] != smatrix[p[i]][p[j]]
            for i in range(len(labels))
            for j in range(len(labels))
        ):
            continue
        automorphisms.append(p)

    identity = tuple(range(len(labels)))
    cf_swap = list(identity)
    cf_swap[index["C"]], cf_swap[index["F"]] = cf_swap[index["F"]], cf_swap[index["C"]]
    cf_swap = tuple(cf_swap)
    assert automorphisms == [identity, cf_swap]

    # Independently verify the nontrivial permutation preserves the complete
    # fusion table, not only the modular S,T readout.
    rules = fusion["unordered_nontrivial_fusion_rules"]

    def product(a: str, b: str) -> list[str]:
        if a == "A":
            return [b]
        if b == "A":
            return [a]
        key = a + "x" + b if index[a] <= index[b] else b + "x" + a
        return rules[key]

    image = {labels[i]: labels[cf_swap[i]] for i in range(len(labels))}
    fusion_preserved = all(
        sorted(image[x] for x in product(a, b)) == sorted(product(image[a], image[b]))
        for a in labels
        for b in labels
    )
    assert fusion_preserved

    # Frozen label encoding A,...,H = 000,...,111.  A computational-basis
    # permutation is Clifford only if conjugation maps every X translation to
    # an affine Pauli translation (constant XOR displacement with affine sign).
    bitstrings = [tuple((i >> shift) & 1 for shift in (2, 1, 0)) for i in range(8)]
    inverse_p = [0] * 8
    for i, value in enumerate(cf_swap):
        inverse_p[value] = i

    x_displacements = {}
    for bit in range(3):
        displacement = []
        for output_index, y in enumerate(bitstrings):
            preimage = bitstrings[inverse_p[output_index]]
            flipped = list(preimage)
            flipped[bit] ^= 1
            mapped = bitstrings[cf_swap[bitstrings.index(tuple(flipped))]]
            displacement.append(xor(y, mapped))
        x_displacements[f"X{bit}"] = displacement

    constant_translation = {
        generator: len(set(displacements)) == 1
        for generator, displacements in x_displacements.items()
    }
    is_product_pauli_normalizer = all(constant_translation.values())
    assert not is_product_pauli_normalizer

    result = {
        "schema": "marici.kitaev.s3-protected-anyon-permutation.v1",
        "label_order": labels,
        "modular_data_automorphism_group": {
            "order": len(automorphisms),
            "isomorphic_to": "Z2",
            "elements": [
                {labels[i]: labels[p[i]] for i in range(len(labels))}
                for p in automorphisms
            ],
            "unique_nontrivial_action": "C<->F",
        },
        "exact_gates": {
            "vacuum_fixed": True,
            "S_preserved": True,
            "T_preserved": True,
            "complete_fusion_ring_preserved": fusion_preserved,
        },
        "frozen_three_bit_label_encoding": {
            "encoding": {label: "".join(map(str, bitstrings[i])) for i, label in enumerate(labels)},
            "C_codeword": "010",
            "F_codeword": "101",
            "permutation_is_single_basis_transposition": True,
            "X_generator_has_nonconstant_conjugated_displacement": {
                generator: not value for generator, value in constant_translation.items()
            },
            "normalizes_product_Pauli_group": is_product_pauli_normalizer,
            "clifford": is_product_pauli_normalizer,
        },
        "source_boundary": {
            "finite_checker_proves": "the modular-data automorphism group is exactly Z2 and its nontrivial C-F action is non-Clifford in the frozen binary sector-label encoding",
            "finite_checker_does_not_prove": "a locality-preserving microscopic circuit",
            "external_source_claim": "Li-Song arXiv:2602.10110v1 constructs constant-depth local circuits for quantum-double anyon permutations; Lu-Wang-Vishwanath arXiv:2608.05294v1 realizes the D(S3) C-F exchange by translation in a self-dual lattice model",
        },
        "verdict": "The protected-operation frontier is strictly larger than the frozen product-Clifford compiler. The unique nontrivial D(S3) modular-data automorphism exchanges C and F, preserves the full fusion ring, and acts as a non-Clifford single transposition on the frozen three-bit torus-sector basis. Local physical protection is source-supported by recent circuit/lattice constructions but is not derived by this finite checker.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
