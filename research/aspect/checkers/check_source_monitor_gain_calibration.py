from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


def monitor(x: F, gain: F, offset: F) -> F:
    return gain * x + offset


def calibrate(dark: F, bright: F, reference: F) -> tuple[F, F]:
    offset = dark
    gain = (bright - dark) / reference
    return gain, offset


def intercept(t1: F, m1: F, t2: F, m2: F) -> F:
    return (t2 * m1 - t1 * m2) / (t2 - t1)


def main() -> None:
    source, loading = F(1, 8), F(1, 4)
    t1, t2 = F(1, 10), F(1, 5)
    reference = F(1, 2)
    gains = {t1: F(3, 4), t2: F(5, 4)}
    offsets = {t1: F(1, 100), t2: F(-1, 50)}

    observed_science = {}
    corrected_science = {}
    for tap in (t1, t2):
        physical = source + loading * tap
        dark = monitor(F(0), gains[tap], offsets[tap])
        bright = monitor(reference, gains[tap], offsets[tap])
        observed_science[tap] = monitor(physical, gains[tap], offsets[tap])
        recovered_gain, recovered_offset = calibrate(dark, bright, reference)
        assert (recovered_gain, recovered_offset) == (gains[tap], offsets[tap])
        corrected_science[tap] = (
            observed_science[tap] - recovered_offset
        ) / recovered_gain
        assert corrected_science[tap] == physical

    recovered_source = intercept(t1, corrected_science[t1], t2, corrected_science[t2])
    assert recovered_source == source

    # Ignoring monitor gain and offset turns the same two records into a wrong
    # source intercept.
    naive_source = intercept(t1, observed_science[t1], t2, observed_science[t2])
    assert naive_source != source

    # One bright reference cannot separate gain from offset.
    tap = t1
    bright_record = monitor(reference, gains[tap], offsets[tap])
    gain_shift = F(1, 8)
    alternative_gain = gains[tap] + gain_shift
    alternative_offset = offsets[tap] - gain_shift * reference
    assert monitor(reference, alternative_gain, alternative_offset) == bright_record
    assert (alternative_gain, alternative_offset) != (gains[tap], offsets[tap])
    alternative_science = (
        observed_science[tap] - alternative_offset
    ) / alternative_gain
    assert alternative_science != corrected_science[tap]

    result = {
        "schema": "marici.aspect.source-monitor-gain-calibration.v1",
        "status": "pass",
        "tap_strengths": [str(t1), str(t2)],
        "known_reference_level": str(reference),
        "monitor_gains": {str(key): str(value) for key, value in gains.items()},
        "monitor_offsets": {str(key): str(value) for key, value in offsets.items()},
        "observed_science_records": {str(key): str(value) for key, value in observed_science.items()},
        "corrected_physical_records": {str(key): str(value) for key, value in corrected_science.items()},
        "recovered_untapped_source": str(recovered_source),
        "naive_uncalibrated_source": str(naive_source),
        "one_bright_reference_identifies_gain_and_offset": False,
        "dark_plus_bright_reference_exact_for_affine_monitor": True,
        "verdict": "Tap-family extrapolation requires an epoch-keyed dark and known-bright reference at every tap strength; one reference or uncalibrated monitor records leave gain-loading aliases.",
        "claim_boundary": "affine monitor response with known reference level; no saturation, reference uncertainty, temporal interpolation, or monitor-source crosstalk",
    }
    output = Path(__file__).parents[1] / "results" / "source_monitor_gain_calibration.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
