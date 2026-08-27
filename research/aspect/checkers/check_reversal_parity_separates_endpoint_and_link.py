from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def main() -> None:
    endpoint_offset = Fraction(1, 3)
    odd_link_bias = Fraction(1, 4)
    forward = endpoint_offset + odd_link_bias
    reversed_path = endpoint_offset - odd_link_bias
    recovered_endpoint = (forward + reversed_path) / 2
    recovered_link_bias = (forward - reversed_path) / 2

    assert forward == Fraction(7, 12)
    assert reversed_path == Fraction(1, 12)
    assert recovered_endpoint == endpoint_offset
    assert recovered_link_bias == odd_link_bias

    linear_drift_per_step = Fraction(1, 60)
    orientations = (1, -1, -1, 1)
    abba_records = tuple(
        endpoint_offset + time * linear_drift_per_step + orientation * odd_link_bias
        for time, orientation in enumerate(orientations)
    )
    plus_mean = (abba_records[0] + abba_records[3]) / 2
    minus_mean = (abba_records[1] + abba_records[2]) / 2
    abba_even_midpoint = (plus_mean + minus_mean) / 2
    abba_odd_component = (plus_mean - minus_mean) / 2
    true_midpoint_endpoint = endpoint_offset + Fraction(3, 2) * linear_drift_per_step

    assert abba_records == (
        Fraction(7, 12),
        Fraction(1, 10),
        Fraction(7, 60),
        Fraction(19, 30),
    )
    assert abba_even_midpoint == true_midpoint_endpoint == Fraction(43, 120)
    assert abba_odd_component == odd_link_bias

    result = {
        "schema": "marici.aspect.reversal-parity-separates-endpoint-and-link.v1",
        "status": "pass",
        "true_endpoint_offset": str(endpoint_offset),
        "true_odd_link_bias": str(odd_link_bias),
        "forward_orientation_measurement": str(forward),
        "reversed_orientation_measurement": str(reversed_path),
        "recovered_even_endpoint": str(recovered_endpoint),
        "recovered_odd_link_bias": str(recovered_link_bias),
        "linear_endpoint_drift_per_step": str(linear_drift_per_step),
        "abba_records": [str(value) for value in abba_records],
        "abba_recovered_midpoint_endpoint": str(abba_even_midpoint),
        "true_midpoint_endpoint": str(true_midpoint_endpoint),
        "abba_recovered_odd_link_bias": str(abba_odd_component),
        "verdict": "A target-even, nuisance-odd path reversal exactly separates endpoint offset 1/3 from link bias 1/4. Symmetric ABBA ordering also recovers both at the common midpoint under linear endpoint drift. The repair depends on the parity law and drift model, not reversal labels alone.",
        "claim_boundary": "exact target-even and nuisance-odd reversal parity, constant odd bias, equally spaced acquisition, and linear endpoint drift; no switching transient, nonlinear drift, incomplete reversal, or noise",
    }
    output = Path(__file__).parents[1] / "results" / "reversal_parity_separates_endpoint_and_link.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
