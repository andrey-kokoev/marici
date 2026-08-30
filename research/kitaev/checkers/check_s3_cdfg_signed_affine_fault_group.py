#!/usr/bin/env python3
"""Exact signed-affine fault-action stabilizer of the CDFG residue codebook."""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
KICKBACK = K / "results" / "s3-coherent-wilson-phase-kickback.json"
PROPAGATION = K / "results" / "s3-common-mode-readout-propagation.json"
REFERENCE = K / "results" / "s3-common-mode-external-reference.json"
OUT = K / "results" / "s3-cdfg-signed-affine-fault-group.json"


def transform(word: tuple[int, ...], signs: tuple[int, ...], shift: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((signs[j]*word[j] + shift[j]) % 4 for j in range(4))


def main() -> None:
    kickback = json.loads(KICKBACK.read_text(encoding="utf-8"))
    signatures = {
        sector: tuple(values)
        for sector, values in kickback["exact_modular_phase_estimation"][
            "chosen_residue_labels_mod_4"
        ].items()
    }
    codebook = set(signatures.values())
    inverse = {word: sector for sector, word in signatures.items()}
    stabilizer = []
    overlap_census = Counter()
    for signs in itertools.product((1, -1), repeat=4):
        for shift in itertools.product(range(4), repeat=4):
            image = {transform(word, signs, shift) for word in codebook}
            overlap_census[len(image & codebook)] += 1
            if image == codebook:
                permutation = {
                    sector: inverse[transform(word, signs, shift)]
                    for sector, word in signatures.items()
                }
                stabilizer.append({
                    "signs_CDFG": list(signs),
                    "shift_CDFG": list(shift),
                    "sector_permutation": permutation,
                })
    assert sum(overlap_census.values()) == 8**4 == 4096
    assert dict(sorted(overlap_census.items())) == {0: 3398, 1: 522, 2: 106, 3: 6, 4: 54, 5: 8, 8: 2}
    assert len(stabilizer) == 2
    identity, d_conjugation = stabilizer
    assert identity["signs_CDFG"] == [1, 1, 1, 1]
    assert d_conjugation["signs_CDFG"] == [1, -1, 1, 1]
    assert d_conjugation["shift_CDFG"] == [0, 0, 0, 0]
    assert d_conjugation["sector_permutation"] == {
        "A": "B", "B": "A", "C": "C", "D": "E", "E": "D",
        "F": "F", "G": "G", "H": "H",
    }
    orbits = [["A", "B"], ["C"], ["D", "E"], ["F"], ["G"], ["H"]]

    propagation = json.loads(PROPAGATION.read_text(encoding="utf-8"))
    reference = json.loads(REFERENCE.read_text(encoding="utf-8"))
    assert propagation["global_adjoint_fault"]["sectors_sent_outside_valid_codebook"] == ["C", "F", "G", "H"]
    assert reference["CDFG_readout_repair"]["information_lower_bound_bits"] == 1
    result = {
        "schema": "marici.kitaev.s3-cdfg-signed-affine-fault-group.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (KICKBACK, PROPAGATION, REFERENCE)
        },
        "ambient_fault_action_group": {
            "action": "r_j -> epsilon_j r_j + t_j mod 4 independently on C,D,F,G",
            "order": 4096,
            "overlap_census_image_intersection_codebook": {str(k): v for k, v in sorted(overlap_census.items())},
        },
        "setwise_codebook_stabilizer": {
            "order": len(stabilizer),
            "isomorphic_to": "C2",
            "elements": stabilizer,
            "nontrivial_generator": "D-port conjugation r_D -> -r_D",
            "sector_orbits_when_orientation_unobserved": orbits,
            "orbit_count": len(orbits),
        },
        "detection_hierarchy": {
            "identity": "no fault",
            "D_port_conjugation": "fully codebook-invisible logical permutation",
            "global_adjoint": "partly invisible: swaps A/B,D/E but flags C,F,G,H",
            "all_other_signed_affine_actions": "fail codebook preservation and are detectable on at least one sector",
        },
        "reference_consequence": {
            "orientation_bits_needed_to_lift_C2_quotient": 1,
            "reference_must_fix": "D-port residue orientation",
            "generic_untyped_mode_bit_is_less_precise_than": "an independently rooted D-orientation reference",
        },
        "boundary": {
            "physical_fault_actions_exhausted_by_signed_affine_group": False,
            "D_conjugation_physically_realizable_by_controller_fault": False,
            "nonunitary_and_leakage_faults_classified": False,
        },
        "verdict": "The exact undetectable signed-affine fault group of the CDFG codebook is C2, generated solely by D-port residue conjugation. It swaps A/B and D/E while fixing C,F,G,H, leaving six quotient classes when D orientation is unknown. Global adjoint is only partially invisible. One external bit is therefore best typed as a D-orientation reference, not an abstract mode flag. This census does not classify non-affine, nonunitary, or leakage faults.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
