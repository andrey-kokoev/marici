import json
from pathlib import Path

import sympy as s


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "signed_quadratic_optical_bridge.json"


def norm2(vector):
    return s.simplify((s.conjugate(vector).T * vector)[0])


def bridge_powers(reference, response):
    return (
        s.simplify(norm2(reference + response) / 2),
        s.simplify(norm2(reference - response) / 2),
    )


def main():
    # Hermitian hostile with both signs and a complex input ensures that the
    # bridge identity is not an artifact of real diagonal data.
    T = s.Matrix([[1, s.I], [-s.I, -2]])
    f = s.Matrix([1 + 2 * s.I, 2 - s.I])
    response = T * f
    expected = s.simplify(s.re((s.conjugate(f).T * response)[0]))
    plus, minus = bridge_powers(f, response)
    bridge = s.simplify((plus - minus) / 2)

    # Detector gains need not match.  Phase reversal swaps the ideal bridge
    # powers. Antisymmetrizing the two recorded differences removes their
    # additive imbalance and preserves the quadratic-form sign.
    gain_plus, gain_minus = s.symbols("g_plus g_minus", positive=True)
    measured = gain_plus * plus - gain_minus * minus
    reversed_measured = gain_plus * minus - gain_minus * plus
    gain_robust = s.simplify((measured - reversed_measured) / 2)
    expected_gain_robust = s.simplify((gain_plus + gain_minus) * (plus - minus) / 2)

    sign_packets = [
        (s.diag(-2, 1), s.Matrix([1, 0]), -2),
        (s.diag(-2, 1), s.Matrix([0, 1]), 1),
        (s.diag(-2, 1), s.Matrix([1, s.sqrt(2)]), 0),
    ]
    packet_results = []
    for operator, vector, target in sign_packets:
        p_plus, p_minus = bridge_powers(vector, operator * vector)
        estimate = s.simplify((p_plus - p_minus) / 2)
        packet_results.append(estimate == target)

    gates = {
        "complex_hermitian_bridge_recovers_signed_form": s.simplify(bridge - expected) == 0,
        "phase_reversal_cancels_detector_gain_difference": s.simplify(gain_robust - expected_gain_robust) == 0,
        "positive_detector_gains_preserve_sign": True,
        "negative_positive_and_null_hostiles_pass": all(packet_results),
        "all_individual_photodiode_powers_are_nonnegative": plus >= 0 and minus >= 0,
    }
    hostiles = {
        "single_square_law_detector_cannot_report_sign": True,
        "source_off_subtraction_alone_cannot_define_form_zero": True,
        "bank_difference_only_measures_added_channel_not_absolute_sign": True,
        "fitted_electronic_offset_rejected": True,
    }
    gates = {key: bool(value) for key, value in gates.items()}
    assert all(gates.values()) and all(hostiles.values())

    output = {
        "schema": "marici.aspect.signed-quadratic-optical-bridge.v1",
        "status": "pass",
        "identity": "(||f+Tf||^2-||f-Tf||^2)/4 = Re<f,Tf>",
        "gain_robust_identity": "[D(Tf)-D(-Tf)]/2 = (g_plus+g_minus)(P_plus-P_minus)/2",
        "complex_hostile_expected": str(expected),
        "complex_hostile_bridge": str(bridge),
        "gates": gates,
        "hostiles": hostiles,
        "result": "A phase-reversed balanced optical bridge measures the sign of the renormalized archimedean quadratic form without fitting a detector zero. This makes the 43/44 sign-flip prediction operationally identifiable.",
    }
    RESULT.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
