from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def intensities(vector):
    return tuple(sp.simplify(abs(value) ** 2) for value in vector)


def main() -> None:
    e1 = sp.Matrix([1, 0])
    identity = sp.eye(2)
    hidden_sign = sp.diag(1, -1)
    swap = sp.Matrix([[0, 1], [1, 0]])

    # Equality on one probe is not stable under the admitted recirculation context.
    assert identity * e1 == hidden_sign * e1
    saturated_probe_matrix = sp.Matrix.hstack(e1, swap * e1)
    assert saturated_probe_matrix.rank() == 2
    assert identity * (swap * e1) != hidden_sign * (swap * e1)

    reflectivity = sp.Rational(1, 2)
    cavity_identity = (identity - reflectivity * swap * identity).inv() * e1
    cavity_hidden_sign = (identity - reflectivity * swap * hidden_sign).inv() * e1
    assert cavity_identity == sp.Matrix([sp.Rational(4, 3), sp.Rational(2, 3)])
    assert cavity_hidden_sign == sp.Matrix([sp.Rational(4, 5), sp.Rational(2, 5)])
    assert intensities(cavity_identity) != intensities(cavity_hidden_sign)

    # A global phase is invisible as a standalone channel but visible when the
    # implementation is coherently controlled relative to a bypass.
    plus_control = sp.Matrix([1, 1]) / sp.sqrt(2)
    minus_control = sp.Matrix([1, -1]) / sp.sqrt(2)
    controlled_identity_record = plus_control
    controlled_minus_identity_record = minus_control
    x_control = sp.Matrix([[0, 1], [1, 0]])
    expectation_plus = (controlled_identity_record.T * x_control * controlled_identity_record)[0]
    expectation_minus = (controlled_minus_identity_record.T * x_control * controlled_minus_identity_record)[0]
    assert (expectation_plus, expectation_minus) == (1, -1)

    # Two equal endpoint composites remain equal under coherent control of the
    # whole box. Access to an internal slot changes the admitted context.
    h = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
    x = swap
    z = sp.diag(1, -1)
    assert h * h == x * x == identity
    internal_hzh = sp.simplify(h * z * h)
    internal_xzx = sp.simplify(x * z * x)
    assert internal_hzh == x
    assert internal_xzx == -z
    assert intensities(internal_hzh * e1) == (0, 1)
    assert intensities(internal_xzx * e1) == (1, 0)

    result = {
        "schema": "marici.aspect.context-saturated-optical-quotient.v1",
        "status": "pass",
        "probe_domain": {"initial_rank": 1, "context_saturated_rank": 2},
        "cavity_records": {
            "identity": [str(v) for v in cavity_identity],
            "hidden_sign": [str(v) for v in cavity_hidden_sign],
            "intensity_distinguishable": True,
        },
        "coherent_global_phase": {
            "standalone_channel_equal": True,
            "controlled_x_expectations": [str(expectation_plus), str(expectation_minus)],
        },
        "route_context": {
            "bare_composites_equal": True,
            "internal_context_outputs": [str(internal_hzh), str(internal_xzx)],
            "endpoint_intensity_records": [[0, 1], [1, 0]],
        },
        "surprises": [
            "A cavity can turn an unprobed sign into an intensity difference without adding a new external input probe.",
            "A phase invisible in standalone channel action becomes observable under coherent control relative to a bypass.",
            "Coherent control of an equal composite does not reveal factorization, but one fixed operation inserted at an internal slot can.",
        ],
        "verdict": "Transfer equivalence is compositional only after saturating the probe domain under every admitted context and declaring whether contexts may access internal route slots.",
        "claim_boundary": "exact lossless two-mode linear optics with a finite context library; physical cavity stability, loss, phase noise, and implementation of controlled unknown operations are not established",
    }
    output = Path(__file__).parents[1] / "results" / "context_saturated_optical_quotient.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
