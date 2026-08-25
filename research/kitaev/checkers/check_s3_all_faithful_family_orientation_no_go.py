#!/usr/bin/env python3
"""Orientation-stabilizer census for every faithful subset of CDEFGH."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
WILSON = K / "results" / "s3-controlled-wilson-executability.json"
MINIMUM = K / "results" / "s3-minimum-family-orientation-stabilizer.json"
OUT = K / "results" / "s3-all-faithful-family-orientation-no-go.json"


def transform(word: tuple[int, ...], signs: tuple[int, ...], shift: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((signs[j]*word[j] + shift[j]) % 4 for j in range(len(word)))


def main() -> None:
    wilson = json.loads(WILSON.read_text(encoding="utf-8"))
    ports = tuple("CDEFGH")
    sectors = tuple("ABCDEFGH")
    faithful = {}
    unfaithful = []
    transformations_checked = 0
    for size in range(1, len(ports)+1):
        for family_tuple in itertools.combinations(ports, size):
            family = "".join(family_tuple)
            words = {
                sector: tuple(wilson["logical_normalizer_test"][port]["wilson_eigenvalues"][index] % 4
                              for port in family_tuple)
                for index, sector in enumerate(sectors)
            }
            codebook = set(words.values())
            if len(codebook) != len(sectors):
                unfaithful.append(family)
                continue
            inverse = {word: sector for sector, word in words.items()}
            stabilizer = []
            for signs in itertools.product((1, -1), repeat=size):
                for shift in itertools.product(range(4), repeat=size):
                    transformations_checked += 1
                    if {transform(word, signs, shift) for word in codebook} == codebook:
                        stabilizer.append({
                            "conjugated_ports": [family_tuple[j] for j, sign in enumerate(signs) if sign == -1],
                            "shift": list(shift),
                            "permutation": {
                                sector: inverse[transform(word, signs, shift)]
                                for sector, word in words.items()
                            },
                        })
            assert len(stabilizer) == 2
            nontrivial = stabilizer[1]
            expected_orientation_ports = [port for port in family_tuple if port in ("D", "E")]
            assert nontrivial["conjugated_ports"] == expected_orientation_ports
            assert nontrivial["shift"] == [0] * size
            assert nontrivial["permutation"] == {
                "A": "B", "B": "A", "C": "C", "D": "E", "E": "D",
                "F": "F", "G": "G", "H": "H",
            }
            faithful[family] = {
                "size": size,
                "stabilizer_order": 2,
                "orientation_generator_conjugates": expected_orientation_ports,
            }
    size_census = {
        str(size): sum(record["size"] == size for record in faithful.values())
        for size in range(1, 7)
    }
    assert size_census == {"1": 0, "2": 0, "3": 0, "4": 8, "5": 6, "6": 1}
    assert len(faithful) == 15
    assert transformations_checked == 8*8**4 + 6*8**5 + 8**6
    assert faithful["CDEFGH"]["orientation_generator_conjugates"] == ["D", "E"]

    minimum = json.loads(MINIMUM.read_text(encoding="utf-8"))
    assert minimum["families_checked"] == 8
    result = {
        "schema": "marici.kitaev.s3-all-faithful-family-orientation-no-go.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (WILSON, MINIMUM)
        },
        "available_ports": list(ports),
        "faithful_family_count": len(faithful),
        "faithful_size_census": size_census,
        "signed_affine_transformations_checked": transformations_checked,
        "family_records": faithful,
        "full_six_port_result": {
            "family": "CDEFGH",
            "stabilizer": "C2",
            "nontrivial_generator": "simultaneous D- and E-port conjugation",
            "sector_permutation": "(A B)(D E)",
        },
        "no_go": {
            "adding_available_Wilson_ports_removes_orientation_C2": False,
            "all_faithful_subsets_have_same_C2": True,
            "required_remedy": "external orientation root or a physical constructor that derives absolute D/E orientation",
        },
        "explanation": "The full six-coordinate Wilson packet already has the orientation automorphism. Every faithful subfamily is a projection that retains this action; exact enumeration shows none acquires a smaller stabilizer. Redundant ports improve neither the A/B nor D/E orientation distinction.",
        "boundary": {
            "ports_outside_CDEFGH_considered": False,
            "non_signed_affine_faults_classified": False,
            "physical_orientation_constructor_supplied": False,
        },
        "verdict": "No faithful subset of the six available Wilson spectral ports removes the hidden orientation C2. All fifteen faithful families, including full CDEFGH, retain (A B)(D E); with both orientation ports present the generator conjugates D and E simultaneously. The ambiguity is intrinsic to this entire Wilson-coordinate packet, so redundant port acquisition cannot replace an independently derived orientation root.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
