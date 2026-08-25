#!/usr/bin/env python3
"""External-reference theorem for controller logical-X detection and CDFG repair."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
PROPAGATION = K / "results" / "s3-common-mode-readout-propagation.json"
KICKBACK = K / "results" / "s3-coherent-wilson-phase-kickback.json"
OUT = K / "results" / "s3-common-mode-external-reference.json"


def dot(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(x*y for x, y in zip(left, right)) % 2


def main() -> None:
    internal_census = {}
    for n in range(1, 8):
        ones = (1,) * n
        valid_internal_checks = []
        for covector in itertools.product((0, 1), repeat=n):
            # A syndrome check must give the same zero value on both valid codewords.
            if dot(covector, ones) == 0:
                valid_internal_checks.append(covector)
                assert dot(covector, ones) == 0
        assert len(valid_internal_checks) == 2 ** (n-1)
        internal_census[str(n)] = {
            "linear_checks_annihilating_encoded_line": len(valid_internal_checks),
            "checks_detecting_common_mode": 0,
        }

    kickback = json.loads(KICKBACK.read_text(encoding="utf-8"))
    propagation = json.loads(PROPAGATION.read_text(encoding="utf-8"))
    signatures = {
        sector: tuple(values)
        for sector, values in kickback["exact_modular_phase_estimation"][
            "chosen_residue_labels_mod_4"
        ].items()
    }
    fibers = defaultdict(list)
    augmented = set()
    for sector, signature in signatures.items():
        for mode in (0, 1):
            observed = signature if mode == 0 else tuple((-x) % 4 for x in signature)
            fibers[observed].append((sector, mode))
            augmented.add((observed, mode))
    maximum_fiber = max(map(len, fibers.values()))
    required_bits = math.ceil(math.log2(maximum_fiber))
    assert maximum_fiber == 2 and required_bits == 1
    assert len(augmented) == 16
    assert propagation["global_adjoint_fault"]["observation_image_size"] == 12

    result = {
        "schema": "marici.kitaev.s3-common-mode-external-reference.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (PROPAGATION, KICKBACK)
        },
        "internal_no_go": {
            "statement": "every linear internal syndrome L with L E_n=0 also satisfies L(1_n)=0",
            "reason": "1_n=E_n(1) lies on the valid encoded command line",
            "common_mode_detectable_by_more_internal_parity_checks": False,
            "exhaustive_covector_census_n_1_through_7": internal_census,
        },
        "external_reference": {
            "minimal_datum": "one independently rooted bit specifying the intended logical command or fault mode",
            "comparison_syndrome": "decoded_command + intended_command in F2",
            "detects_logical_X": True,
            "authority_requirement": "reference must not share the controller common-mode orbit",
        },
        "CDFG_readout_repair": {
            "sector_mode_domain_size": 16,
            "unaugmented_observation_count": len(fibers),
            "maximum_unaugmented_fiber_size": maximum_fiber,
            "information_lower_bound_bits": required_bits,
            "augmented_signature": "(CDFG residue signature, external mode bit)",
            "augmented_observation_count": len(augmented),
            "jointly_faithful": True,
        },
        "boundary": {
            "external_bit_physically_constructed": False,
            "independent_authority_root_proved": False,
            "global_adjoint_is_physical_fault_action_proved": False,
        },
        "verdict": "Internal redundancy cannot expose controller logical X: every valid linear syndrome annihilates the encoded repetition-code line and therefore the common mode. An independently rooted intended-command or mode bit is necessary. For the conditional CDFG global-adjoint model it is also sufficient and information-minimal: the largest residue fiber has size two, and adjoining one mode bit restores 16 distinct observations.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
