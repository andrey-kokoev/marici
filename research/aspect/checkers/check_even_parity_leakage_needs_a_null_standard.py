from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def parity_channels(forward, reverse):
    return (forward + reverse) / 2, (forward - reverse) / 2


def main() -> None:
    endpoint_target = Fraction(1, 3)
    even_link_leakage = Fraction(1, 10)
    odd_link_bias = Fraction(1, 4)

    science_forward = endpoint_target + even_link_leakage + odd_link_bias
    science_reverse = endpoint_target + even_link_leakage - odd_link_bias
    science_even, science_odd = parity_channels(science_forward, science_reverse)

    assert science_forward == Fraction(41, 60)
    assert science_reverse == Fraction(11, 60)
    assert science_even == Fraction(13, 30)
    assert science_even != endpoint_target
    assert science_odd == odd_link_bias

    null_endpoint = Fraction(0)
    null_forward = null_endpoint + even_link_leakage + odd_link_bias
    null_reverse = null_endpoint + even_link_leakage - odd_link_bias
    null_even, null_odd = parity_channels(null_forward, null_reverse)

    assert null_forward == Fraction(7, 20)
    assert null_reverse == Fraction(-3, 20)
    assert null_even == even_link_leakage
    assert null_odd == odd_link_bias

    null_corrected_endpoint = science_even - null_even
    assert null_corrected_endpoint == endpoint_target

    result = {
        "schema": "marici.aspect.even-parity-leakage-null-standard.v1",
        "status": "pass",
        "true_endpoint_target": str(endpoint_target),
        "even_link_leakage": str(even_link_leakage),
        "odd_link_bias": str(odd_link_bias),
        "science_forward": str(science_forward),
        "science_reverse": str(science_reverse),
        "uncorrected_science_even_channel": str(science_even),
        "uncorrected_endpoint_is_biased": science_even != endpoint_target,
        "science_odd_channel": str(science_odd),
        "null_forward": str(null_forward),
        "null_reverse": str(null_reverse),
        "null_even_channel": str(null_even),
        "null_odd_channel": str(null_odd),
        "null_corrected_endpoint": str(null_corrected_endpoint),
        "null_correction_recovers_target": null_corrected_endpoint == endpoint_target,
        "verdict": "An orientation-even link leakage of 1/10 biases the reversal half-sum from endpoint 1/3 to 13/30 while leaving the odd channel correct. A matched zero-endpoint null identifies the even leakage and restores the target exactly. Reversal alone cannot separate terms in the same parity representation.",
        "claim_boundary": "additive constant even leakage shared by science and null, constant odd bias, and exact zero endpoint; no null mismatch, state dependence, drift, or noise",
    }
    output = Path(__file__).parents[1] / "results" / "even_parity_leakage_needs_a_null_standard.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
