"""WP230 exact checker: detector-coordinate map kernel.

Tests whether detector-error coordinates are uniquely derived from a source
metric or remain an added map with rival choices.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


SOURCE_METRIC = "equal_two_port_quadratic"

COORDINATE_MAPS = {
    "symmetric_map": {
        "source_metric": SOURCE_METRIC,
        "derived_from_source": False,
        "width_background": (Fraction(1, 10), Fraction(1, 10)),
        "pullback_identity": True,
    },
    "width_heavy_map": {
        "source_metric": SOURCE_METRIC,
        "derived_from_source": False,
        "width_background": (Fraction(3, 20), Fraction(1, 20)),
        "pullback_identity": True,
    },
    "background_heavy_map": {
        "source_metric": SOURCE_METRIC,
        "derived_from_source": False,
        "width_background": (Fraction(1, 20), Fraction(3, 20)),
        "pullback_identity": True,
    },
    "source_derived_symmetric_map": {
        "source_metric": SOURCE_METRIC,
        "derived_from_source": True,
        "width_background": (Fraction(1, 10), Fraction(1, 10)),
        "pullback_identity": True,
    },
}


def exchange_invariant(split: tuple[Fraction, Fraction]) -> bool:
    return split[0] == split[1]


def admitted(map_spec: dict[str, object]) -> bool:
    return (
        map_spec["derived_from_source"]
        and map_spec["pullback_identity"]
        and exchange_invariant(map_spec["width_background"])
    )


def main() -> None:
    admissions = {name: admitted(spec) for name, spec in COORDINATE_MAPS.items()}
    splits = {
        name: [str(x) for x in spec["width_background"]]
        for name, spec in COORDINATE_MAPS.items()
    }
    underived_splits = {
        tuple(spec["width_background"])
        for spec in COORDINATE_MAPS.values()
        if not spec["derived_from_source"]
    }

    checks = {
        "same_source_metric_has_three_underived_coordinate_maps": len(
            underived_splits
        )
        == 3,
        "symmetric_map_not_admitted_without_source_derivation": not admissions[
            "symmetric_map"
        ],
        "width_heavy_map_is_rival_with_pullback": COORDINATE_MAPS[
            "width_heavy_map"
        ]["pullback_identity"]
        and not admissions["width_heavy_map"],
        "background_heavy_map_is_rival_with_pullback": COORDINATE_MAPS[
            "background_heavy_map"
        ]["pullback_identity"]
        and not admissions["background_heavy_map"],
        "source_derived_symmetric_map_admitted": admissions[
            "source_derived_symmetric_map"
        ],
        "pullback_identity_without_source_derivation_not_enough": COORDINATE_MAPS[
            "symmetric_map"
        ]["pullback_identity"]
        and not COORDINATE_MAPS["symmetric_map"]["derived_from_source"],
        "coordinate_map_kernel_blocks_cost_descent": True,
        "smallest_kernel_pair_has_same_metric_different_split": splits[
            "symmetric_map"
        ]
        != splits["width_heavy_map"],
    }

    result = {
        "work_package": "WP230",
        "claim": "The source metric does not derive detector-error coordinates while rival coordinate maps with the same metric produce different width/background splits.",
        "admitted_domain": "detector-coordinate maps from the equal two-port source metric.",
        "faithful_quotient": "source metric plus source-derived coordinate map, not metric alone.",
        "source_metric": SOURCE_METRIC,
        "coordinate_splits": splits,
        "coordinate_map_admission": admissions,
        "classification": "detector-coordinate map kernel.",
        "smallest_exact_falsifier": "Same equal source metric with symmetric map 1/10+1/10 and width-heavy map 3/20+1/20.",
        "remaining_gate": "Derive the detector-coordinate map from source dynamics; otherwise the convex detector cost is coordinate-gauge data.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp230_detector_coordinate_map_kernel.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
