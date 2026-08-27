from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def main() -> None:
    offset = Fraction(1, 100)
    gain = Fraction(5, 4)
    actual_reference = Fraction(51, 100)
    reference_interval = (Fraction(1, 2), Fraction(13, 25))
    science_input = Fraction(1, 4)

    dark_record = offset
    bright_record = offset + gain * actual_reference
    science_record = offset + gain * science_input
    bright_contrast = bright_record - dark_record
    science_contrast = science_record - dark_record
    contrast_ratio = science_contrast / bright_contrast

    inferred_interval = tuple(contrast_ratio * endpoint for endpoint in reference_interval)
    nominal_estimate = contrast_ratio * reference_interval[0]
    assert contrast_ratio == Fraction(25, 51)
    assert inferred_interval == (Fraction(25, 102), Fraction(13, 51))
    assert inferred_interval[0] < science_input < inferred_interval[1]
    assert nominal_estimate - science_input == Fraction(-1, 204)

    source_candidates = (Fraction(1, 4), Fraction(3, 10))
    admitted_candidates = tuple(
        candidate
        for candidate in source_candidates
        if inferred_interval[0] <= candidate <= inferred_interval[1]
    )
    assert admitted_candidates == (science_input,)
    assert inferred_interval[1] - inferred_interval[0] == Fraction(1, 102)

    result = {
        "schema": "marici.aspect.reference-uncertainty-source-monitor.v1",
        "status": "pass",
        "monitor_law": "y=o+g*x",
        "actual_reference": str(actual_reference),
        "declared_reference_interval": [str(value) for value in reference_interval],
        "observed_contrast_ratio": str(contrast_ratio),
        "inferred_science_interval": [str(value) for value in inferred_interval],
        "true_science_input": str(science_input),
        "nominal_low_endpoint_estimate": str(nominal_estimate),
        "nominal_estimate_bias": "-1/204",
        "interval_width": "1/102",
        "source_candidates": [str(value) for value in source_candidates],
        "admitted_source_candidates": [str(value) for value in admitted_candidates],
        "verdict": "A bounded bright-reference level produces a bounded physical science input, not a point. The monitor ratio is exact in reference units. A source-supplied discrete candidate set can still make the joint inverse unique when exactly one candidate intersects the calibration interval.",
        "claim_boundary": "static positive affine response; exact dark and record values; bounded bright-reference amplitude; no drift, saturation, dark-reference uncertainty, or crosstalk",
    }
    output = Path(__file__).parents[1] / "results" / "reference_uncertainty_source_monitor.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
