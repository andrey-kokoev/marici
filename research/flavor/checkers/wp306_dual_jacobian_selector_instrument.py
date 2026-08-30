"""WP306: exact dual-Jacobian typing for prediction and instrumentation."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def audit(source_jacobian, detector_jacobian, metric):
    source_rank = source_jacobian.rank()
    detector_rank = detector_jacobian.rank()
    detector_gram = sp.simplify(detector_jacobian.T * metric * detector_jacobian)
    return {
        "source_rank": source_rank,
        "detector_rank": detector_rank,
        "detector_gram_determinant": str(detector_gram.det()),
        "predictive": bool(source_rank == 0),
        "instrument_faithful": bool(detector_rank == detector_jacobian.cols and detector_gram.det() > 0),
    }


def main():
    zero = sp.zeros(2, 2)
    identity = sp.eye(2)
    rank_one = sp.Matrix([[1, 0], [0, 0]])
    metric = sp.diag(2, 3)
    cases = {
        "both": audit(zero, identity, metric),
        "prediction_only": audit(zero, rank_one, metric),
        "readout_only": audit(identity, identity, metric),
        "neither": audit(identity, rank_one, metric),
    }

    checks = {
        "both_case_passes_both_gates": cases["both"]["predictive"] and cases["both"]["instrument_faithful"],
        "prediction_only_case_has_detector_kernel": cases["prediction_only"]["predictive"] and not cases["prediction_only"]["instrument_faithful"],
        "readout_only_case_has_source_ambiguity": not cases["readout_only"]["predictive"] and cases["readout_only"]["instrument_faithful"],
        "neither_case_fails_both_gates": not cases["neither"]["predictive"] and not cases["neither"]["instrument_faithful"],
        "full_detector_gram_is_positive": cases["both"]["detector_gram_determinant"] == "6",
        "rank_one_detector_gram_is_singular": cases["prediction_only"]["detector_gram_determinant"] == "0",
        "source_and_detector_ranks_are_logically_independent": len({(case["predictive"], case["instrument_faithful"]) for case in cases.values()}) == 4,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP306",
        "pipeline": "free source moduli theta -> selected physical coordinates x_star -> calibrated detector records y",
        "source_predictivity_jacobian": "J_src=d x_star/d theta; required rank 0 after quotienting admitted source redundancies",
        "detector_faithfulness_jacobian": "J_det=d y/d x; required full column rank, equivalently det(J_det^T W J_det)>0 for positive calibrated W",
        "exact_cases": cases,
        "classification": "predictivity and instrument faithfulness are independent gates on opposite arrows; zero source response and full detector response are compatible and jointly required for an identified numerical prediction",
        "smallest_exact_falsifier": "J_src=I and J_det=I gives perfect readout but no source prediction; J_src=0 and rank-one J_det gives prediction without identifiable detector response",
        "remaining_physical_instrument_gate": "derive a zero-rank source-to-physical16 image on the admitted source quotient and a full-rank calibrated physical16-to-record response in the same support domain",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp306_dual_jacobian_selector_instrument.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
