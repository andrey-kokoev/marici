from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def has_revival(sequence):
    return any(later > earlier for earlier, later in zip(sequence, sequence[1:]))


def main() -> None:
    true_sample_contrast = (Fraction(1), Fraction(1, 2), Fraction(1, 4))
    readout_gain = (Fraction(1), Fraction(1), Fraction(4))
    raw_sample_contrast = tuple(
        contrast * gain for contrast, gain in zip(true_sample_contrast, readout_gain)
    )
    raw_reference_response = readout_gain
    calibrated_sample_contrast = tuple(
        sample / reference
        for sample, reference in zip(raw_sample_contrast, raw_reference_response)
    )

    assert true_sample_contrast == (Fraction(1), Fraction(1, 2), Fraction(1, 4))
    assert raw_sample_contrast == (Fraction(1), Fraction(1, 2), Fraction(1))
    assert has_revival(raw_sample_contrast)
    assert calibrated_sample_contrast == true_sample_contrast
    assert not has_revival(calibrated_sample_contrast)

    raw_revival_amount = raw_sample_contrast[-1] - raw_sample_contrast[1]
    calibrated_final_change = calibrated_sample_contrast[-1] - calibrated_sample_contrast[1]
    assert raw_revival_amount == Fraction(1, 2)
    assert calibrated_final_change == Fraction(-1, 4)

    result = {
        "schema": "marici.aspect.readout-drift-fakes-coherence-revival.v1",
        "status": "pass",
        "true_sample_contrast": [str(value) for value in true_sample_contrast],
        "readout_gain": [str(value) for value in readout_gain],
        "raw_sample_contrast": [str(value) for value in raw_sample_contrast],
        "raw_reference_response": [str(value) for value in raw_reference_response],
        "raw_record_has_apparent_revival": has_revival(raw_sample_contrast),
        "raw_revival_amount": str(raw_revival_amount),
        "calibrated_sample_contrast": [str(value) for value in calibrated_sample_contrast],
        "calibrated_record_has_revival": has_revival(calibrated_sample_contrast),
        "calibrated_final_change": str(calibrated_final_change),
        "verdict": "A fourfold readout-gain change converts monotone sample decay into an apparent revival. A contemporaneous common-path reference exactly removes the scalar gain and restores the monotone verdict; revival witnesses require a frozen or calibrated observation map.",
        "claim_boundary": "common scalar multiplicative gain known exactly from a stable reference; no additive background, saturation, analyzer rotation, reference drift, or finite-sample uncertainty",
    }
    output = Path(__file__).parents[1] / "results" / "readout_drift_fakes_coherence_revival.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
