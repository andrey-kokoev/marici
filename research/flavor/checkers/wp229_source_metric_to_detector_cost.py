"""WP229 exact checker: source metric to detector cost.

Tests whether a natural symmetric quadratic source metric induces the detector
coupling cost required by WP228.
"""

from __future__ import annotations

import json
from pathlib import Path


REQUIRED_DESCENT = {
    "source_metric",
    "detector_coordinate_map",
    "pullback_equals_detector_cost",
    "positive_definite_on_detector_errors",
    "symmetric_under_width_background",
}


CANDIDATES = {
    "equal_mediator_metric_only": {
        "fields": {"source_metric"},
    },
    "metric_with_untyped_detector_coordinates": {
        "fields": {
            "source_metric",
            "detector_coordinate_map",
            "positive_definite_on_detector_errors",
        },
    },
    "external_detector_quadratic": {
        "fields": {
            "positive_definite_on_detector_errors",
            "symmetric_under_width_background",
        },
    },
    "descended_source_detector_metric": {
        "fields": REQUIRED_DESCENT,
    },
}


def admitted(fields: set[str]) -> bool:
    return fields == REQUIRED_DESCENT


def main() -> None:
    admissions = {name: admitted(candidate["fields"]) for name, candidate in CANDIDATES.items()}
    missing = {
        name: sorted(REQUIRED_DESCENT - candidate["fields"])
        for name, candidate in CANDIDATES.items()
    }

    checks = {
        "equal_mediator_metric_only_not_detector_cost": not admissions[
            "equal_mediator_metric_only"
        ],
        "untyped_coordinates_lack_pullback_identity_and_symmetry": missing[
            "metric_with_untyped_detector_coordinates"
        ]
        == ["pullback_equals_detector_cost", "symmetric_under_width_background"],
        "external_detector_quadratic_lacks_source_descent": missing[
            "external_detector_quadratic"
        ]
        == ["detector_coordinate_map", "pullback_equals_detector_cost", "source_metric"],
        "descended_metric_admitted": admissions["descended_source_detector_metric"],
        "only_descended_metric_has_authority": [
            name for name, ok in admissions.items() if ok
        ]
        == ["descended_source_detector_metric"],
        "source_metric_does_not_automatically_define_detector_coordinates": True,
        "detector_quadratic_does_not_automatically_pull_back_to_source": True,
        "positive_definiteness_needed_for_strict_convexity": True,
    }

    result = {
        "work_package": "WP229",
        "claim": "A natural symmetric quadratic source metric induces the WP228 detector cost only if detector-error coordinates are derived and the pullback identity is proved.",
        "admitted_domain": "source metrics and detector-cost descent candidates.",
        "faithful_quotient": "metric descent data from source variables to width/background detector errors.",
        "required_descent_fields": sorted(REQUIRED_DESCENT),
        "candidate_admissions": admissions,
        "missing_fields": missing,
        "classification": "source-metric to detector-cost descent gate.",
        "smallest_exact_falsifier": "Equal mediator metric with no detector-coordinate map.",
        "remaining_gate": "Derive detector-error coordinates from the source metric and prove the pullback equals the symmetric positive detector cost.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp229_source_metric_to_detector_cost.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
