from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def main() -> None:
    source = {"reset": Fraction(1), "control": Fraction(6, 5)}
    pilot_transmission = {"reset": Fraction(1), "control": Fraction(3, 4)}
    pilot_off = dict(source)
    pilot_on = {
        condition: source[condition] * pilot_transmission[condition]
        for condition in source
    }
    assert pilot_off == {"reset": 1, "control": Fraction(6, 5)}
    assert pilot_on == {"reset": 1, "control": Fraction(9, 10)}

    true_contrast = source["control"] - source["reset"]
    encoded_contrast = pilot_on["control"] - pilot_on["reset"]
    assert true_contrast == Fraction(1, 5)
    assert encoded_contrast == Fraction(-1, 10)
    assert true_contrast * encoded_contrast < 0

    interaction = (
        pilot_on["control"]
        - pilot_off["control"]
        - (pilot_on["reset"] - pilot_off["reset"])
    )
    assert interaction == Fraction(-3, 10)

    # A transmission calibration derived on an independent source-invariant
    # reference recovers the pre-encoder source record exactly.
    recovered = {
        condition: pilot_on[condition] / pilot_transmission[condition]
        for condition in pilot_on
    }
    assert recovered == source
    assert recovered["control"] - recovered["reset"] == true_contrast

    # A common gain ratio would cancel only common pilot loading, not the
    # condition-dependent transmission frozen here.
    encoded_ratio = pilot_on["control"] / pilot_on["reset"]
    source_ratio = source["control"] / source["reset"]
    assert encoded_ratio == Fraction(9, 10)
    assert source_ratio == Fraction(6, 5)
    assert encoded_ratio != source_ratio

    result = {
        "schema": "marici.aspect.pilot-back-action-factorial.v1",
        "status": "pass",
        "pre_encoder_source": {key: str(value) for key, value in source.items()},
        "pilot_transmissions": {key: str(value) for key, value in pilot_transmission.items()},
        "pilot_off_records": {key: str(value) for key, value in pilot_off.items()},
        "pilot_on_records": {key: str(value) for key, value in pilot_on.items()},
        "true_source_contrast": str(true_contrast),
        "encoded_detector_contrast": str(encoded_contrast),
        "contrast_sign_reversed": True,
        "pilot_by_condition_interaction": str(interaction),
        "recovered_source": {key: str(value) for key, value in recovered.items()},
        "encoded_ratio": str(encoded_ratio),
        "source_ratio": str(source_ratio),
        "verdict": "A perfectly decoded pilot can reverse the apparent condition contrast when its optical transmission depends on the encoded condition. The pilot-on/off factorial interaction detects the back-action. A pre-authorized condition-specific transmission calibration recovers the source contrast; common-ratio normalization does not. Pilot incidence and pilot neutrality are separate claims.",
        "claim_boundary": "two exact conditions, multiplicative memoryless pilot transmission, exact pilot-off interleave, and independently calibrated inverse; no source drift, nonlinear modulation, polarization-dependent science response, tap back-action, or calibration uncertainty",
    }
    output = Path(__file__).parents[1] / "results" / "pilot_back_action_factorial.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
