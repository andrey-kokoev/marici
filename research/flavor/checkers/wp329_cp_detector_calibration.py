"""WP329: exact calibrated detector response for the CP-domain channel."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    p, alpha, delta = sp.symbols("p alpha delta", real=True)
    contrast = sp.simplify(1 - alpha - delta)
    observed = sp.simplify(alpha + contrast * p)
    negative_calibration = alpha
    positive_calibration = 1 - delta
    raw_response = sp.Matrix([[sp.diff(observed, variable) for variable in (p, alpha, delta)]])
    calibrated_response = sp.Matrix([
        [sp.diff(readout, variable) for variable in (p, alpha, delta)]
        for readout in (observed, negative_calibration, positive_calibration)
    ])
    determinant = sp.factor(calibrated_response.det())
    inverse_probability = sp.simplify((observed - negative_calibration) / (positive_calibration - negative_calibration))
    checks = {
        "raw_branch_frequency_has_rank_one": raw_response.rank() == 1,
        "raw_readout_has_two_parameter_kernel": len(raw_response.nullspace()) == 2,
        "calibrated_determinant_equals_negative_contrast": determinant == -contrast,
        "calibrated_response_is_generically_full_rank": calibrated_response.rank() == 3,
        "exact_inverse_recovers_true_probability": inverse_probability == p,
        "zero_contrast_is_exact_detector_kernel": sp.simplify(determinant.subs(delta, 1 - alpha)) == 0,
        "zero_contrast_makes_observation_independent_of_source_probability": sp.simplify(sp.diff(observed, p).subs(delta, 1 - alpha)) == 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP329",
        "admitted_state_domain": "true CP-positive probability p and a binary detector with false-positive alpha and false-negative delta",
        "faithful_quotient_coordinate": "p after detector inversion when the independently calibrated contrast 1-alpha-delta is nonzero",
        "candidate_probe_family": "raw domain counts plus separate known-negative and known-positive calibration preparations",
        "source_authorization": "conditional only; physical known-domain preparations and their common-frame interface have not been established",
        "raw_observed_probability": str(observed),
        "raw_response_jacobian": [[str(value) for value in row] for row in raw_response.tolist()],
        "calibrated_response_jacobian": [[str(value) for value in row] for row in calibrated_response.tolist()],
        "calibrated_determinant": str(determinant),
        "inverse_probability": str(inverse_probability),
        "contextual_partition": "raw counts identify one equivalence class in (p,alpha,delta); two calibration ports refine it to singleton parameters away from zero contrast",
        "classification": "the calibrated detector is a faithful physical readout of the preparation probability, not a selector of that probability or an identifier of beta, epsilon, and c0",
        "smallest_exact_falsifier": "alpha+delta=1 makes detector contrast zero, the determinant vanish, and the observed frequency independent of p",
        "reference_groupoid": "known-negative and known-positive preparations add two reference ports and define a new calibrated detector experiment; they do not reveal an absolute label in the raw-count experiment",
        "remaining_physical_instrument_gate": "realize pure or traceably bounded CP calibration preparations, measure alpha and delta with uncertainties and drift control, and keep the contrast margin nonzero on the same domain history",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp329_cp_detector_calibration.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
