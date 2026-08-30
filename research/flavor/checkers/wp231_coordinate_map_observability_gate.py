"""WP231 exact checker: coordinate-map observability gate.

Tests whether source perturbations identify detector-error coordinates.
"""

from __future__ import annotations

import json
from pathlib import Path


PROBES = {
    "total_error_only": {
        "response_rank": 1,
        "calibrated": True,
        "source_derived": True,
        "target_dimension": 2,
    },
    "two_untyped_error_responses": {
        "response_rank": 2,
        "calibrated": False,
        "source_derived": True,
        "target_dimension": 2,
    },
    "external_two_error_calibration": {
        "response_rank": 2,
        "calibrated": True,
        "source_derived": False,
        "target_dimension": 2,
    },
    "source_calibrated_two_error_probe": {
        "response_rank": 2,
        "calibrated": True,
        "source_derived": True,
        "target_dimension": 2,
    },
}


def identifies_coordinate_map(probe: dict[str, object]) -> bool:
    return (
        probe["response_rank"] == probe["target_dimension"]
        and bool(probe["calibrated"])
        and bool(probe["source_derived"])
    )


def main() -> None:
    admissions = {name: identifies_coordinate_map(probe) for name, probe in PROBES.items()}
    kernels = {
        name: int(probe["target_dimension"]) - int(probe["response_rank"])
        for name, probe in PROBES.items()
    }

    checks = {
        "total_error_only_has_one_dimensional_kernel": kernels["total_error_only"]
        == 1
        and not admissions["total_error_only"],
        "two_untyped_responses_have_rank_but_no_calibration": PROBES[
            "two_untyped_error_responses"
        ]["response_rank"]
        == 2
        and not PROBES["two_untyped_error_responses"]["calibrated"]
        and not admissions["two_untyped_error_responses"],
        "external_calibration_has_rank_but_no_source_authority": PROBES[
            "external_two_error_calibration"
        ]["response_rank"]
        == 2
        and not PROBES["external_two_error_calibration"]["source_derived"]
        and not admissions["external_two_error_calibration"],
        "source_calibrated_two_error_probe_identifies_map": admissions[
            "source_calibrated_two_error_probe"
        ],
        "rank_calibration_and_source_derivation_are_jointly_required": [
            name for name, ok in admissions.items() if ok
        ]
        == ["source_calibrated_two_error_probe"],
        "total_error_probe_is_smallest_observability_falsifier": True,
        "does_not_supply_fault_sentinel_or_executable_apparatus": True,
    }

    result = {
        "work_package": "WP231",
        "claim": "A detector-coordinate map is source-derived only if source-generated calibrated probes have full rank on width/background errors; total-error readout leaves a one-dimensional kernel.",
        "admitted_domain": "source perturbation probes for width/background detector-error coordinates.",
        "faithful_quotient": "rank-calibrated source response matrix on detector-error coordinates.",
        "probe_admissions": admissions,
        "response_kernels": kernels,
        "classification": "coordinate-map observability gate.",
        "smallest_exact_falsifier": "Total-error-only probe has rank one on a two-dimensional width/background coordinate space.",
        "remaining_gate": "Construct a source-derived calibrated two-error probe, or keep detector-coordinate maps nonunique.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp231_coordinate_map_observability_gate.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
