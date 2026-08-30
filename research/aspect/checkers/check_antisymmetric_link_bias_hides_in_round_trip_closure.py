from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def main() -> None:
    true_endpoint_offset = Fraction(0)
    forward_link_bias = Fraction(1, 4)
    reverse_link_bias = Fraction(-1, 4)

    forward_measurement = true_endpoint_offset + forward_link_bias
    reverse_measurement = -true_endpoint_offset + reverse_link_bias
    round_trip_closure_residual = forward_measurement + reverse_measurement
    standard_endpoint_estimate = (forward_measurement - reverse_measurement) / 2

    symmetric_link_component = (forward_link_bias + reverse_link_bias) / 2
    antisymmetric_link_component = (forward_link_bias - reverse_link_bias) / 2

    assert forward_measurement == Fraction(1, 4)
    assert reverse_measurement == Fraction(-1, 4)
    assert round_trip_closure_residual == 0
    assert symmetric_link_component == 0
    assert antisymmetric_link_component == Fraction(1, 4)
    assert standard_endpoint_estimate == Fraction(1, 4)
    assert standard_endpoint_estimate != true_endpoint_offset
    assert standard_endpoint_estimate == true_endpoint_offset + antisymmetric_link_component

    # A genuinely displaced endpoint with reciprocal zero-bias links yields the
    # same two directed observations, proving two-measurement nonidentifiability.
    alternate_endpoint_offset = Fraction(1, 4)
    alternate_forward = alternate_endpoint_offset
    alternate_reverse = -alternate_endpoint_offset
    assert (alternate_forward, alternate_reverse) == (forward_measurement, reverse_measurement)

    result = {
        "schema": "marici.aspect.antisymmetric-link-bias-round-trip-closure.v1",
        "status": "pass",
        "true_endpoint_offset": str(true_endpoint_offset),
        "forward_link_bias": str(forward_link_bias),
        "reverse_link_bias": str(reverse_link_bias),
        "forward_measurement": str(forward_measurement),
        "reverse_measurement": str(reverse_measurement),
        "round_trip_closure_residual": str(round_trip_closure_residual),
        "symmetric_link_component": str(symmetric_link_component),
        "antisymmetric_link_component": str(antisymmetric_link_component),
        "standard_endpoint_estimate": str(standard_endpoint_estimate),
        "endpoint_estimate_is_false": standard_endpoint_estimate != true_endpoint_offset,
        "alternate_true_offset_produces_identical_record": (alternate_forward, alternate_reverse) == (forward_measurement, reverse_measurement),
        "verdict": "Opposite quarter-unit directed link biases give zero round-trip closure but a false quarter-unit endpoint estimate. The same record also arises from a true endpoint offset with unbiased links, so antisymmetric link bias is unidentifiable without a new route, reversal, parity law, or local comparison.",
        "claim_boundary": "additive two-direction link model with exact scalar biases; no time-varying delay, dispersion, nonlinear phase, synchronization error, or finite-sample uncertainty",
    }
    output = Path(__file__).parents[1] / "results" / "antisymmetric_link_bias_hides_in_round_trip_closure.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
