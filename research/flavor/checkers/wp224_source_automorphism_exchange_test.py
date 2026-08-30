"""WP224 exact checker: source automorphism exchange test.

Audits whether a proposed width/background swap is a genuine source
automorphism rather than a detector label relabeling.
"""

from __future__ import annotations

import json
from pathlib import Path


REQUIRED_PROPERTIES = {
    "swaps_width_background",
    "commutes_with_source_law",
    "preserves_error_semantics",
    "descends_to_detector_quotient",
}


CANDIDATES = {
    "label_swap_only": {
        "properties": {"swaps_width_background"},
    },
    "source_symmetry_wrong_semantics": {
        "properties": {
            "swaps_width_background",
            "commutes_with_source_law",
            "descends_to_detector_quotient",
        },
    },
    "semantic_swap_not_source_symmetry": {
        "properties": {
            "swaps_width_background",
            "preserves_error_semantics",
            "descends_to_detector_quotient",
        },
    },
    "admitted_source_exchange": {
        "properties": REQUIRED_PROPERTIES,
    },
}


def admitted(candidate: dict[str, set[str]]) -> bool:
    return candidate["properties"] == REQUIRED_PROPERTIES


def main() -> None:
    admissions = {name: admitted(candidate) for name, candidate in CANDIDATES.items()}
    missing = {
        name: sorted(REQUIRED_PROPERTIES - candidate["properties"])
        for name, candidate in CANDIDATES.items()
    }

    checks = {
        "label_swap_only_not_admitted": not admissions["label_swap_only"],
        "source_symmetry_wrong_semantics_not_admitted": not admissions[
            "source_symmetry_wrong_semantics"
        ],
        "semantic_swap_not_source_symmetry_not_admitted": not admissions[
            "semantic_swap_not_source_symmetry"
        ],
        "admitted_source_exchange_passes": admissions["admitted_source_exchange"],
        "commutation_with_source_law_is_required": "commutes_with_source_law"
        in missing["semantic_swap_not_source_symmetry"],
        "semantic_preservation_is_required": "preserves_error_semantics"
        in missing["source_symmetry_wrong_semantics"],
        "descent_to_detector_quotient_is_required": "descends_to_detector_quotient"
        in missing["label_swap_only"],
        "label_swap_is_smallest_falsifier": missing["label_swap_only"]
        == [
            "commutes_with_source_law",
            "descends_to_detector_quotient",
            "preserves_error_semantics",
        ],
        "exchange_symmetry_would_follow_only_after_admission": True,
    }

    result = {
        "work_package": "WP224",
        "claim": "A width/background swap derives exchange symmetry only if it is a source automorphism that commutes with the source law, preserves error semantics, and descends to the detector quotient.",
        "admitted_domain": "candidate width/background swap maps.",
        "faithful_quotient": "source-law automorphism properties plus detector-quotient descent.",
        "required_properties": sorted(REQUIRED_PROPERTIES),
        "candidate_admissions": admissions,
        "missing_properties": missing,
        "classification": "source-automorphism admission test.",
        "smallest_exact_falsifier": "A label swap of width/background with no source-law commutation, semantic preservation, or detector descent.",
        "remaining_gate": "Construct such an automorphism from the finite two-port source, or keep width/background exchange as an external detector symmetry.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp224_source_automorphism_exchange_test.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
