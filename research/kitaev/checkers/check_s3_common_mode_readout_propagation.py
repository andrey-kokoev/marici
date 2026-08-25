#!/usr/bin/env python3
"""Exact propagation of algebraic common-mode faults through CDFG readout."""

from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
KICKBACK = K / "results" / "s3-coherent-wilson-phase-kickback.json"
COMPLEX = K / "results" / "lockstep-controller-repetition-complex.json"
OUT = K / "results" / "s3-common-mode-readout-propagation.json"


def neg(signature: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((-entry) % 4 for entry in signature)


def main() -> None:
    kickback = json.loads(KICKBACK.read_text(encoding="utf-8"))
    complex_result = json.loads(COMPLEX.read_text(encoding="utf-8"))
    labels = kickback["exact_modular_phase_estimation"]["chosen_residue_labels_mod_4"]
    signatures = {sector: tuple(values) for sector, values in labels.items()}
    inverse = {signature: sector for sector, signature in signatures.items()}
    assert len(inverse) == 8

    adjoint_action = {}
    observations: dict[tuple[int, ...], list[tuple[str, int]]] = defaultdict(list)
    for sector, signature in signatures.items():
        inverted = neg(signature)
        target = inverse.get(inverted)
        adjoint_action[sector] = {
            "nominal": list(signature),
            "global_adjoint": list(inverted),
            "valid_sector_after_adjoint": target,
            "detected_as_outside_codebook": target is None,
        }
        observations[signature].append((sector, 0))
        observations[inverted].append((sector, 1))

    assert {sector: record["valid_sector_after_adjoint"] for sector, record in adjoint_action.items()} == {
        "A": "B", "B": "A", "C": None, "D": "E", "E": "D",
        "F": None, "G": None, "H": None,
    }
    ambiguous = {
        str(signature): [f"{sector}:mode{mode}" for sector, mode in inputs]
        for signature, inputs in observations.items() if len(inputs) > 1
    }
    assert len(observations) == 12
    assert len(ambiguous) == 4
    assert all(len(inputs) == 2 for inputs in ambiguous.values())

    zero = (0, 0, 0, 0)
    assert zero not in inverse
    assert complex_result["coding_theorem"]["common_mode_error"].endswith("acts as logical X")
    result = {
        "schema": "marici.kitaev.s3-common-mode-readout-propagation.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (KICKBACK, COMPLEX)
        },
        "global_adjoint_fault": {
            "typed_action": "replace all four controlled quarter evolutions by their adjoints, so r -> -r mod 4",
            "sector_action": adjoint_action,
            "valid_permutation_pairs": [["A", "B"], ["D", "E"]],
            "sectors_sent_outside_valid_codebook": ["C", "F", "G", "H"],
            "unknown_mode_domain_size": 16,
            "observation_image_size": len(observations),
            "ambiguous_observation_count": len(ambiguous),
            "ambiguous_fibers": ambiguous,
            "joint_readout_faithful_when_mode_unobserved": False,
        },
        "global_omission_proxy": {
            "typed_action": "omit every controlled phase interaction",
            "output_signature": list(zero),
            "inside_valid_codebook": False,
            "detectable_by_codebook_membership": True,
        },
        "constructor_boundary": {
            "controller_logical_X_physically_equals_global_adjoint": False,
            "controller_logical_X_physically_equals_global_omission": False,
            "reason": "the missing code-switch constructor has no admitted fault-action homomorphism from controller errors to logical Wilson operations",
            "required_map": "Phi_fault: controller fault classes -> logical CPTP maps on data and pointers",
        },
        "verdict": "A common mode is not automatically harmless or uniformly detectable. Under the global-adjoint algebraic fault, A/B and D/E become undetected sector swaps while C,F,G,H leave the valid codebook; with the mode unobserved the 16 sector-mode inputs collapse to 12 observations. Global omission instead yields the invalid 0000 word. Which action represents a physical controller logical X is not derivable until the interface supplies a fault-action map.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
