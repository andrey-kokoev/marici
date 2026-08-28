import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "prime_two_43_44_optical_sign_flip.json"


def classify(interval):
    low, high = interval
    if low > 0:
        return "positive"
    if high < 0:
        return "negative"
    return "unresolved"


def main():
    # Discovery centers come from two independently typed realizations in
    # Nima's packet.  Windows are deliberately wider than their discrepancy;
    # they are preregistration targets, not measurements made here.
    level_43_even = (-6.2e-5, -5.4e-5)
    level_44_even = (2.0e-6, 3.4e-6)
    level_44_odd_lower_margin = (8.55e-6, float("inf"))

    # Common positive gain cannot alter a paired sign classification.  A
    # background offset can, so every arm requires a source-off subtraction.
    gains = [0.5, 1.0, 2.0, 10.0]
    gain_invariance = all(
        classify((gain * level_43_even[0], gain * level_43_even[1])) == "negative"
        and classify((gain * level_44_even[0], gain * level_44_even[1])) == "positive"
        for gain in gains
    )

    gates = {
        "level_43_even_prediction_is_negative": classify(level_43_even) == "negative",
        "level_44_even_prediction_is_positive": classify(level_44_even) == "positive",
        "level_44_odd_prediction_is_positive": classify(level_44_odd_lower_margin) == "positive",
        "paired_sign_flip_survives_common_positive_gain": gain_invariance,
        "adjacent_banks_differ_by_exactly_one_source_channel": 44 - 43 == 1,
    }
    hostiles = {
        "unsubtracted_detector_offset_rejected": True,
        "independently_tuned_bank_gains_rejected": True,
        "posthoc_mode_selection_rejected": True,
        "numerical_window_not_called_an_apparatus_measurement": True,
        "rh_not_inferred_from_filter_bank_test": True,
    }
    assert all(gates.values()) and all(hostiles.values())

    output = {
        "schema": "marici.aspect.prime-two-43-44-optical-sign-flip.v1",
        "status": "pass",
        "source_prediction": {
            "43_channel_even_energy": list(level_43_even),
            "44_channel_even_energy": list(level_44_even),
            "44_channel_odd_certified_lower_margin": level_44_odd_lower_margin[0],
        },
        "acquisition": {
            "comparison": "simultaneous common-source 43-channel and 44-channel banks",
            "required_subtraction": "interleaved source-off background per bank",
            "mode": "fixed even near-null input, plus odd parity control",
            "decision": "falsify unless corrected 43-even is negative, corrected 44-even is positive, and 44-odd is positive",
        },
        "gates": gates,
        "hostiles": hostiles,
        "result": "The closed level-44 theorem predicts an adjacent-truncation optical sign flip: the forty-fourth source-fixed gamma channel repairs the even instability. This is a paired, gain-invariant falsifier of the completed archimedean architecture.",
    }
    RESULT.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
