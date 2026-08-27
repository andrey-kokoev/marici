from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def response(x, offset, gain, saturation):
    return sp.expand(offset + gain * x - saturation * x**2)


def main() -> None:
    offset, gain, saturation = sp.Rational(1, 100), sp.Rational(5, 4), sp.Rational(1, 2)
    dark_level, mid_level, bright_level = sp.Rational(0), sp.Rational(1, 2), sp.Rational(1)
    dark = response(dark_level, offset, gain, saturation)
    mid = response(mid_level, offset, gain, saturation)
    bright = response(bright_level, offset, gain, saturation)
    assert (dark, mid, bright) == (sp.Rational(1, 100), sp.Rational(51, 100), sp.Rational(19, 25))

    # Dark plus one bright level admits an affine fit that matches both anchors
    # but biases an intermediate science value.
    affine_gain = sp.simplify((mid - dark) / mid_level)
    assert affine_gain == 1
    science_x = sp.Rational(1, 4)
    science_y = response(science_x, offset, gain, saturation)
    affine_science_x = sp.simplify((science_y - dark) / affine_gain)
    assert affine_science_x == sp.Rational(9, 32)
    assert affine_science_x - science_x == sp.Rational(1, 32)

    # Three levels identify offset, gain, and quadratic saturation exactly.
    a_mid = sp.simplify((mid - dark) / mid_level)
    a_bright = sp.simplify((bright - dark) / bright_level)
    recovered_saturation = sp.simplify((a_mid - a_bright) / (bright_level - mid_level))
    recovered_gain = sp.simplify(a_mid + recovered_saturation * mid_level)
    assert (dark, recovered_gain, recovered_saturation) == (offset, gain, saturation)

    x = sp.symbols("x", real=True)
    roots = sp.solve(
        sp.Eq(response(x, dark, recovered_gain, recovered_saturation), science_y), x
    )
    assert roots == [sp.Rational(1, 4), sp.Rational(9, 4)]
    admitted_roots = [root for root in roots if 0 <= root <= 1]
    assert admitted_roots == [science_x]

    # Outside the declared monotone range, even the calibrated polynomial is
    # noninjective and cannot identify the physical input from one output.
    alias_left, alias_right = sp.Rational(1), sp.Rational(3, 2)
    assert response(alias_left, offset, gain, saturation) == response(
        alias_right, offset, gain, saturation
    )

    result = {
        "schema": "marici.aspect.source-monitor-saturation.v1",
        "status": "pass",
        "response_law": "y=o+g*x-h*x^2",
        "true_parameters": {
            "offset": str(offset), "gain": str(gain), "saturation": str(saturation)
        },
        "reference_levels": [str(dark_level), str(mid_level), str(bright_level)],
        "reference_records": [str(dark), str(mid), str(bright)],
        "two_level_affine_science_estimate": str(affine_science_x),
        "two_level_affine_bias": "1/32",
        "three_level_parameters_recovered": True,
        "science_inverse_roots": [str(root) for root in roots],
        "admitted_range": "0<=x<=1",
        "unique_admitted_science_value": str(admitted_roots[0]),
        "out_of_range_alias": [str(alias_left), str(alias_right)],
        "verdict": "Dark plus one bright anchor cannot detect quadratic monitor compression; a third level identifies the quadratic response, but physical inversion additionally requires a source-authorized monotone input range.",
        "claim_boundary": "static quadratic monitor response with exact reference levels and admitted input range; no higher nonlinearity, temporal drift, reference uncertainty, or crosstalk",
    }
    output = Path(__file__).parents[1] / "results" / "source_monitor_saturation.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
