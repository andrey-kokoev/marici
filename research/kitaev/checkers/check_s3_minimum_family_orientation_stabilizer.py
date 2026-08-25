#!/usr/bin/env python3
"""Signed-affine orientation stabilizer across all minimum Wilson families."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
KICKBACK = K / "results" / "s3-coherent-wilson-phase-kickback.json"
WILSON = K / "results" / "s3-controlled-wilson-executability.json"
CDFG = K / "results" / "s3-cdfg-signed-affine-fault-group.json"
OUT = K / "results" / "s3-minimum-family-orientation-stabilizer.json"


def transform(word: tuple[int, ...], signs: tuple[int, ...], shift: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((signs[j]*word[j] + shift[j]) % 4 for j in range(4))


def main() -> None:
    kickback = json.loads(KICKBACK.read_text(encoding="utf-8"))
    wilson = json.loads(WILSON.read_text(encoding="utf-8"))
    families = sorted(kickback["exact_modular_phase_estimation"]["family_moduli"])
    sector_order = tuple("ABCDEFGH")
    records = {}
    transformations_checked = 0
    for family in families:
        ports = tuple(family)
        words = {
            sector: tuple(wilson["logical_normalizer_test"][port]["wilson_eigenvalues"][index] % 4
                          for port in ports)
            for index, sector in enumerate(sector_order)
        }
        codebook = set(words.values())
        inverse = {word: sector for sector, word in words.items()}
        assert len(codebook) == 8
        stabilizer = []
        for signs in itertools.product((1, -1), repeat=4):
            for shift in itertools.product(range(4), repeat=4):
                transformations_checked += 1
                if {transform(word, signs, shift) for word in codebook} == codebook:
                    stabilizer.append({
                        "signs": list(signs),
                        "shift": list(shift),
                        "permutation": {
                            sector: inverse[transform(word, signs, shift)]
                            for sector, word in words.items()
                        },
                    })
        assert len(stabilizer) == 2
        nontrivial = stabilizer[1]
        orientation_port = "D" if "D" in ports else "E"
        sign_flipped_ports = [ports[j] for j, sign in enumerate(nontrivial["signs"]) if sign == -1]
        assert sign_flipped_ports == [orientation_port]
        assert nontrivial["shift"] == [0, 0, 0, 0]
        assert nontrivial["permutation"] == {
            "A": "B", "B": "A", "C": "C", "D": "E", "E": "D",
            "F": "F", "G": "G", "H": "H",
        }
        records[family] = {
            "ports": list(ports),
            "unique_orientation_port": orientation_port,
            "signed_affine_stabilizer_order": len(stabilizer),
            "nontrivial_generator": f"r_{orientation_port} -> -r_{orientation_port}",
            "sector_permutation": nontrivial["permutation"],
        }
    assert len(records) == 8
    assert transformations_checked == 8 * 4096

    cdfg = json.loads(CDFG.read_text(encoding="utf-8"))
    assert cdfg["setwise_codebook_stabilizer"]["order"] == 2
    result = {
        "schema": "marici.kitaev.s3-minimum-family-orientation-stabilizer.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (KICKBACK, WILSON, CDFG)
        },
        "families_checked": len(records),
        "signed_affine_transformations_checked": transformations_checked,
        "family_records": records,
        "universal_result": {
            "every_minimum_family_stabilizer": "C2",
            "generator": "conjugate the unique D/E-species port",
            "sector_permutation": "(A B)(D E)",
            "fixed_sectors": ["C", "F", "G", "H"],
            "external_orientation_bits_required": 1,
            "family_selection_can_remove_orientation_ambiguity": False,
        },
        "explanation": "Every minimum faithful family contains exactly one port from the D/E magic species. That port is the antisymmetric orientation coordinate: conjugating it reverses the signs distinguishing A from B and D from E while leaving the other species and sectors fixed.",
        "boundary": {
            "all_faithful_families_larger_than_minimum_classified": False,
            "non_signed_affine_faults_classified": False,
            "physical_orientation_reference_constructed": False,
        },
        "verdict": "The hidden orientation C2 is universal across all eight minimum faithful Wilson families. Its generator always conjugates the family's unique D/E-species port and induces (A B)(D E). Resource-family selection cannot remove this ambiguity; every minimum compiler needs one independently rooted orientation bit unless its physical constructor fixes that orientation by derivation.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
