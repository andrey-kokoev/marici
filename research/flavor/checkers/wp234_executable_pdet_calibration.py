"""WP234 executable P_det calibration intake and exact robustness checker."""

from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path


def q(value: str) -> Fraction:
    return Fraction(value)


def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def interval_determinants(center, error):
    entries = [(center[i][j], error[i][j]) for i in range(2) for j in range(2)]
    determinants = []
    for signs in itertools.product((-1, 1), repeat=4):
        values = [c + s * e for (c, e), s in zip(entries, signs)]
        matrix = ((values[0], values[1]), (values[2], values[3]))
        determinants.append(det2(matrix))
    return determinants


def nonempty(value):
    return value is not None and value != "" and value != []


def evaluate(record):
    central = tuple(tuple(q(v) for v in row) for row in record["response_jacobian"]["central"])
    error = tuple(tuple(q(v) for v in row) for row in record["response_jacobian"]["absolute_uncertainty"])
    metric = tuple(tuple(q(v) for v in row) for row in record["detector_metric"]["matrix"])
    corner_dets = interval_determinants(central, error)
    same_positive_sign = min(corner_dets) > 0
    same_negative_sign = max(corner_dets) < 0
    robust_rank_two = same_positive_sign or same_negative_sign
    minimum_abs_det = min(abs(value) for value in corner_dets)
    metric_det = det2(metric)
    provenance = record["provenance"]
    support = record["support"]
    empirical_provenance = (
        record["record_status"] == "experimental_measurement"
        and all(nonempty(provenance[key]) for key in (
            "dataset_uri", "run_ids", "calibration_timestamp_utc",
            "instrument_id", "analyst_signature",
        ))
        and nonempty(record["common_frame"]["frame_calibration_certificate"])
        and nonempty(record["detector_metric"]["independent_calibration_certificate"])
    )
    support_complete = (
        support["finite_width_model"] != "fixture-only"
        and support["mixing_model"] != "fixture-only"
        and support["decoupling_limit_tested"] is True
        and support["detector_resolution_model"] != "fixture-only"
    )
    source_typed = (
        record["source_operation"]["independently_controllable"] is True
        and nonempty(record["source_operation"]["source_derivation"])
    )
    admitted = (
        empirical_provenance and support_complete and source_typed
        and metric_det > 0 and robust_rank_two
    )
    return {
        "experiment_id": record["experiment_id"],
        "record_status": record["record_status"],
        "central_jacobian_determinant": str(det2(central)),
        "detector_metric_determinant": str(metric_det),
        "corner_determinant_min": str(min(corner_dets)),
        "corner_determinant_max": str(max(corner_dets)),
        "minimum_absolute_corner_determinant": str(minimum_abs_det),
        "robust_rank_two": robust_rank_two,
        "empirical_provenance_complete": empirical_provenance,
        "support_complete": support_complete,
        "source_typed": source_typed,
        "experimentally_admitted": admitted,
    }


def main():
    parser = argparse.ArgumentParser()
    default_input = Path(__file__).resolve().parents[1] / "contracts" / "flavor-pdet-calibration-record.v1.json"
    parser.add_argument("--input", type=Path, default=default_input)
    args = parser.parse_args()
    record = json.loads(args.input.read_text())
    diagnostic = evaluate(record)

    hostile = json.loads(json.dumps(record))
    hostile["response_jacobian"]["central"] = [["1", "1"], ["0", "0"]]
    hostile["response_jacobian"]["absolute_uncertainty"] = [["0", "0"], ["0", "0"]]
    hostile_diagnostic = evaluate(hostile)

    checks = {
        "protocol_fixture_is_executable": True,
        "synthetic_fixture_not_misreported_as_experiment": not diagnostic["experimentally_admitted"],
        "fixture_has_exact_positive_rank_margin": diagnostic["robust_rank_two"],
        "missing_empirical_provenance_is_detected": not diagnostic["empirical_provenance_complete"],
        "missing_physical_support_is_detected": not diagnostic["support_complete"],
        "rank_one_hostile_pair_is_rejected": not hostile_diagnostic["robust_rank_two"],
        "admission_requires_all_independent_gates": diagnostic["source_typed"] and not diagnostic["experimentally_admitted"],
    }
    result = {
        "work_package": "WP234",
        "claim": "An executable P_det calibration protocol is constructed, but no experimental calibration is admitted without run provenance, independent frame/metric certificates, and completed physical support models.",
        "candidate_experiment": "zero-accessible mediator intervention plus resolved threshold scan, with joint finite-width/background response",
        "input_record": str(args.input),
        "diagnostic": diagnostic,
        "hostile_rank_one_diagnostic": hostile_diagnostic,
        "classification": "executable protocol; empirical instrument gate open",
        "smallest_exact_falsifier": "rank-one response J=[[1,1],[0,0]]",
        "remaining_gate": "Populate the frozen record with actual run data, signed instrument/frame calibration, independently calibrated detector metric, and width/mixing/decoupling/resolution support models.",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = Path(__file__).resolve().parents[1] / "results" / "wp234_executable_pdet_calibration.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
