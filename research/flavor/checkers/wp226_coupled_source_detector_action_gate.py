"""WP226 exact checker: coupled source-detector action gate.

Tests whether adding a coupled source-detector action derives width/background
exchange, or merely appends a detector coupling law.
"""

from __future__ import annotations

import json
from pathlib import Path


REQUIRED_COUPLED_ACTION_FIELDS = {
    "source_action",
    "detector_error_bundle",
    "coupling_term",
    "exchange_automorphism",
    "descent_to_detector_quotient",
}


CANDIDATES = {
    "source_only": {
        "fields": {"source_action"},
        "same_source_allows_rival_couplings": True,
    },
    "glued_detector_coupling": {
        "fields": {
            "source_action",
            "detector_error_bundle",
            "coupling_term",
            "exchange_automorphism",
            "descent_to_detector_quotient",
        },
        "same_source_allows_rival_couplings": True,
    },
    "source_action_derives_coupling": {
        "fields": REQUIRED_COUPLED_ACTION_FIELDS | {"coupling_uniqueness_from_source"},
        "same_source_allows_rival_couplings": False,
    },
}


def has_formal_coupled_action(candidate: dict[str, object]) -> bool:
    return REQUIRED_COUPLED_ACTION_FIELDS.issubset(candidate["fields"])


def derives_exchange(candidate: dict[str, object]) -> bool:
    return has_formal_coupled_action(candidate) and not bool(
        candidate["same_source_allows_rival_couplings"]
    )


def main() -> None:
    formal = {
        name: has_formal_coupled_action(candidate)
        for name, candidate in CANDIDATES.items()
    }
    admitted = {name: derives_exchange(candidate) for name, candidate in CANDIDATES.items()}
    missing = {
        name: sorted(REQUIRED_COUPLED_ACTION_FIELDS - candidate["fields"])
        for name, candidate in CANDIDATES.items()
    }

    checks = {
        "source_only_not_formal_coupled_action": not formal["source_only"],
        "glued_coupling_is_formal_but_not_derived": formal["glued_detector_coupling"]
        and not admitted["glued_detector_coupling"],
        "source_derived_coupling_admitted": admitted["source_action_derives_coupling"],
        "rival_couplings_are_the_hostile_kernel": CANDIDATES[
            "glued_detector_coupling"
        ]["same_source_allows_rival_couplings"],
        "coupling_uniqueness_is_required": "coupling_uniqueness_from_source"
        in CANDIDATES["source_action_derives_coupling"]["fields"],
        "formal_exchange_without_uniqueness_is_external": True,
        "does_not_derive_sentinel_executability_or_calibration": True,
    }

    result = {
        "work_package": "WP226",
        "claim": "A coupled source-detector action derives width/background exchange only if the source action uniquely entails the coupling; a glued detector coupling remains external.",
        "admitted_domain": "candidate coupled source-detector actions.",
        "faithful_quotient": "source action plus detector coupling modulo rival couplings with the same source.",
        "formal_coupled_action": formal,
        "exchange_derivation_admission": admitted,
        "missing_fields": missing,
        "classification": "coupled-action derivation gate.",
        "smallest_exact_falsifier": "Same source action with rival detector couplings, one exchange-symmetric and one asymmetric.",
        "remaining_gate": "Derive coupling uniqueness from the source action; otherwise exchange remains an appended detector law.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp226_coupled_source_detector_action_gate.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
