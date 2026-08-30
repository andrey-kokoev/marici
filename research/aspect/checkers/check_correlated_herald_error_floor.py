from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def main() -> None:
    common_probability = Fraction(1, 1000)
    independent_probability = Fraction(1, 100)
    no_common = 1 - common_probability

    marginal = common_probability + no_common * independent_probability
    dual_actual = common_probability + no_common * independent_probability**2
    dual_independence_prediction = marginal**2
    triple_actual = common_probability + no_common * independent_probability**3
    triple_independence_prediction = marginal**3
    covariance = dual_actual - dual_independence_prediction
    dual_underestimate_factor = dual_actual / dual_independence_prediction

    assert marginal == Fraction(1099, 100000)
    assert dual_actual == Fraction(10999, 10000000)
    assert covariance > 0
    assert dual_underestimate_factor > 9
    assert triple_actual > common_probability
    assert triple_actual < common_probability + Fraction(1, 1000000)
    assert triple_actual > 700 * triple_independence_prediction

    result = {
        "schema": "marici.aspect.correlated-herald-error-floor.v1",
        "status": "pass",
        "common_false_trigger_probability": str(common_probability),
        "independent_per_detector_probability": str(independent_probability),
        "single_detector_marginal": str(marginal),
        "dual_actual_false_coincidence": str(dual_actual),
        "dual_independence_prediction": str(dual_independence_prediction),
        "dual_covariance": str(covariance),
        "dual_underestimate_factor": str(dual_underestimate_factor),
        "triple_actual_false_coincidence": str(triple_actual),
        "triple_independence_prediction": str(triple_independence_prediction),
        "common_mode_floor_survives_redundancy": triple_actual > common_probability,
        "verdict": "A one-per-thousand common false trigger makes the actual dual coincidence rate more than nine times the marginal-independence prediction. Triple coincidence remains near the same common-mode floor, so detector redundancy cannot replace joint event-law calibration.",
        "claim_boundary": "binary all-detector common event plus identical independent Bernoulli noise; no afterpulsing kernels, continuous-time windows, unequal detectors, or partial higher-order correlations",
    }
    output = Path(__file__).parents[1] / "results" / "correlated_herald_error_floor.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
