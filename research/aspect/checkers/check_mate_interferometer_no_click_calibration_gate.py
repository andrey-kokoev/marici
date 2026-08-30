from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


def detected_law(signal_plus, eta_plus, eta_minus):
    signal_minus = F(1) - signal_plus
    click_plus = eta_plus * signal_plus
    click_minus = eta_minus * signal_minus
    no_click = F(1) - click_plus - click_minus
    assert click_plus >= 0 and click_minus >= 0 and no_click >= 0
    return click_plus, click_minus, no_click


def click_postselected_share(law):
    click_plus, click_minus, _ = law
    return click_plus / (click_plus + click_minus)


def calibrated_signal_plus(law, eta_plus, eta_minus):
    click_plus, click_minus, _ = law
    recovered_plus = click_plus / eta_plus
    recovered_minus = click_minus / eta_minus
    assert recovered_plus + recovered_minus == 1
    return recovered_plus


def visibility(curve):
    maximum = max(curve)
    minimum = min(curve)
    return (maximum - minimum) / (maximum + minimum)


def main():
    cosines = [F(1), F(0), F(-1), F(0)]
    eta_plus = [F(1), F(3, 4), F(1, 2), F(3, 4)]
    eta_minus = [F(1, 2), F(3, 4), F(1), F(3, 4)]

    flat = [F(1, 2)] * 4
    flat_laws = [detected_law(p, ep, em) for p, ep, em in zip(flat, eta_plus, eta_minus)]
    fake_curve = [click_postselected_share(law) for law in flat_laws]
    assert fake_curve == [F(2, 3), F(1, 2), F(1, 3), F(1, 2)]
    assert visibility(fake_curve) == F(1, 3)

    ideal_one_third_curve = [(F(1) + F(1, 3) * cosine) / 2 for cosine in cosines]
    assert fake_curve == ideal_one_third_curve

    recovered_flat = [
        calibrated_signal_plus(law, ep, em)
        for law, ep, em in zip(flat_laws, eta_plus, eta_minus)
    ]
    assert recovered_flat == flat
    assert visibility(recovered_flat) == 0

    true_gamma = F(3, 5)
    true_curve = [(F(1) + true_gamma * cosine) / 2 for cosine in cosines]
    true_laws = [
        detected_law(p, ep, em)
        for p, ep, em in zip(true_curve, eta_plus, eta_minus)
    ]
    biased_true_curve = [click_postselected_share(law) for law in true_laws]
    assert biased_true_curve == [F(8, 9), F(1, 2), F(1, 9), F(1, 2)]
    assert visibility(biased_true_curve) == F(7, 9)

    recovered_true = [
        calibrated_signal_plus(law, ep, em)
        for law, ep, em in zip(true_laws, eta_plus, eta_minus)
    ]
    assert recovered_true == true_curve
    assert visibility(recovered_true) == true_gamma

    result = {
        "schema": "marici.aspect.mate-interferometer-no-click-calibration-gate.v1",
        "status": "pass",
        "phase_samples": ["0", "pi/2", "pi", "3pi/2"],
        "efficiency_manifest": {
            "plus_port": [str(value) for value in eta_plus],
            "minus_port": [str(value) for value in eta_minus],
        },
        "flat_source_hostile": {
            "true_unconditional_curve": [str(value) for value in flat],
            "click_postselected_curve": [str(value) for value in fake_curve],
            "apparent_visibility": str(visibility(fake_curve)),
            "exactly_matches_ideal_coherent_visibility_one_third": True,
            "herald_and_no_click_calibrated_curve": [str(value) for value in recovered_flat],
            "recovered_visibility": "0",
            "full_detected_outcomes": [
                {
                    "click_plus": str(law[0]),
                    "click_minus": str(law[1]),
                    "no_click": str(law[2]),
                }
                for law in flat_laws
            ],
        },
        "true_coherent_control": {
            "environment_overlap": str(true_gamma),
            "true_curve": [str(value) for value in true_curve],
            "click_postselected_curve": [str(value) for value in biased_true_curve],
            "biased_visibility": str(visibility(biased_true_curve)),
            "calibrated_curve": [str(value) for value in recovered_true],
            "calibrated_visibility": str(visibility(recovered_true)),
        },
        "tower_gate": {
            "output": "retain herald, click-plus, click-minus, and no-click outcomes",
            "control": "bind phase-indexed efficiencies to a live calibration epoch",
            "mate": "totalize the full calibrated outcome law, never the click-conditioned projection alone",
        },
        "decisive_rule": "an unconditional fringe claim is admissible only after efficiency inversion on the full herald-normalized outcome law",
        "claim_boundary": "exact finite single-photon loss hostile; no dark counts, multipair emission, memory, jitter, or continuum detector theorem",
    }
    output = Path(__file__).parents[1] / "results" / "mate_interferometer_no_click_calibration_gate.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
