from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def cavity(amplitude, loop_gain):
    return sp.simplify(amplitude / (1 - loop_gain * amplitude))


def main() -> None:
    amplitude, loop_gain = sp.symbols("a r", positive=True)
    response = cavity(amplitude, loop_gain)
    source_sensitivity = sp.diff(response, amplitude)
    loop_sensitivity = sp.diff(response, loop_gain)
    assert sp.simplify(source_sensitivity - 1 / (amplitude * loop_gain - 1) ** 2) == 0
    assert sp.simplify(loop_sensitivity - amplitude**2 / (amplitude * loop_gain - 1) ** 2) == 0
    assert sp.simplify(source_sensitivity / loop_sensitivity) == 1 / amplitude**2

    a_left = sp.Rational(1)
    a_right = sp.Rational(99, 100)
    r = sp.Rational(9, 10)
    single_pass_separation = a_left - a_right
    cavity_left = cavity(a_left, r)
    cavity_right = cavity(a_right, r)
    cavity_separation = sp.simplify(cavity_left - cavity_right)
    amplification = sp.simplify(cavity_separation / single_pass_separation)
    assert cavity_left == 10
    assert cavity_right == sp.Rational(990, 109)
    assert cavity_separation == sp.Rational(100, 109)
    assert amplification == sp.Rational(10000, 109)

    # A one-percent loop-gain uncertainty creates a response interval wider
    # than the amplified source separation.
    r_interval = (sp.Rational(89, 100), sp.Rational(91, 100))
    calibration_interval = tuple(cavity(a_left, endpoint) for endpoint in r_interval)
    assert calibration_interval == (sp.Rational(100, 11), sp.Rational(100, 9))
    calibration_width = sp.simplify(calibration_interval[1] - calibration_interval[0])
    assert calibration_width == sp.Rational(200, 99)
    assert calibration_width > cavity_separation

    # Internal loss and mirror return enter only through their product.
    mirror_return, internal_survival = sp.symbols("m eta", positive=True)
    lossy_response = cavity(amplitude, mirror_return * internal_survival)
    product_jacobian = sp.Matrix(
        [[sp.diff(lossy_response, mirror_return), sp.diff(lossy_response, internal_survival)]]
    )
    assert product_jacobian.rank() == 1
    assert cavity(a_left, sp.Rational(9, 10) * sp.Rational(4, 5)) == cavity(
        a_left, sp.Rational(3, 4) * sp.Rational(24, 25)
    )

    result = {
        "schema": "marici.aspect.cavity-discrimination-conditioning.v1",
        "status": "pass",
        "source_sensitivity": str(source_sensitivity),
        "loop_gain_sensitivity": str(loop_sensitivity),
        "sensitivity_ratio": str(sp.simplify(source_sensitivity / loop_sensitivity)),
        "single_pass_separation": str(single_pass_separation),
        "cavity_records": [str(cavity_left), str(cavity_right)],
        "cavity_separation": str(cavity_separation),
        "additive_noise_amplification": str(amplification),
        "loop_gain_interval": [str(value) for value in r_interval],
        "calibration_response_interval": [str(value) for value in calibration_interval],
        "calibration_interval_width": str(calibration_width),
        "loss_return_jacobian_rank": 1,
        "verdict": "Near resonance amplifies separation against downstream additive readout noise, but it amplifies source and loop-gain perturbations with the same resonant denominator. It cannot improve first-order discrimination against shared loop-gain calibration uncertainty. Mirror return and internal survival are separately unidentifiable from one steady-state cavity record.",
        "claim_boundary": "stable scalar steady-state coherent cavity with exact amplitude records; no shot-noise scaling, dynamical ringdown, nonlinear response, or phase noise",
    }
    output = Path(__file__).parents[1] / "results" / "cavity_discrimination_conditioning.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
