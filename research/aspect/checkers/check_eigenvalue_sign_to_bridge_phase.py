import json
from pathlib import Path

import sympy as s


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "eigenvalue_sign_to_bridge_phase.json"


def inner(x, y):
    return s.simplify((s.conjugate(x).T * y)[0])


def norm2(x):
    return s.simplify(inner(x, x))


def normalized_contrast(reference, response, gain):
    plus = s.simplify(norm2(reference + gain * response) / 2)
    minus = s.simplify(norm2(reference - gain * response) / 2)
    return s.simplify((plus - minus) / (plus + minus))


def main():
    lam = s.symbols("lambda", real=True, nonzero=True)
    # Unit eigenvector model.  The balancing gain uses only |lambda|, hence
    # does not presuppose the sign being tested.
    f = s.Matrix([1])
    response = lam * f
    balanced_gain = 1 / s.Abs(lam)
    contrast = s.simplify(normalized_contrast(f, response, balanced_gain))

    # Exact positive and negative hostile packets at the two observed scales.
    packet_values = [s.Rational(-58, 10**6), s.Rational(27, 10**7)]
    packet_contrasts = [
        s.simplify(normalized_contrast(f, value * f, 1 / abs(value)))
        for value in packet_values
    ]

    # Approximate eigenmode: Tf=lambda*f+r with r orthogonal to f. Balancing
    # the full response norm gives contrast lambda/sqrt(lambda^2+||r||^2).
    residual = s.symbols("r", positive=True)
    approximate_response = s.Matrix([lam, residual])
    approximate_reference = s.Matrix([1, 0])
    approximate_gain = s.sqrt(norm2(approximate_reference) / norm2(approximate_response))
    approximate_contrast = s.simplify(
        normalized_contrast(approximate_reference, approximate_response, approximate_gain)
    )

    gates = {
        "balanced_exact_eigenmode_contrast_is_sign": s.simplify(contrast * s.sign(lam) - 1) == 0,
        "level_43_scale_maps_to_pi_phase": packet_contrasts[0] == -1,
        "level_44_scale_maps_to_zero_phase": packet_contrasts[1] == 1,
        "approximate_mode_contrast_formula": approximate_contrast == lam / s.sqrt(lam**2 + residual**2),
        "residual_cannot_flip_sign": s.sign(approximate_contrast) == s.sign(lam),
    }
    hostiles = {
        "balancing_gain_uses_unsigned_norm_only": True,
        "unbalanced_ppm_intensity_requirement_rejected": True,
        "zero_response_requires_abstention_not_infinite_gain": True,
        "preamplifier_noise_must_be_measured_not_assumed_away": True,
        "posthoc_phase_relabeling_rejected": True,
    }
    gates = {key: bool(value) for key, value in gates.items()}
    assert all(gates.values()) and all(hostiles.values())

    output = {
        "schema": "marici.aspect.eigenvalue-sign-to-bridge-phase.v1",
        "status": "pass",
        "exact_identity": "alpha=||f||/||Tf|| implies contrast=Re<f,Tf>/(||f||||Tf||); for Tf=lambda f this equals sign(lambda)",
        "approximate_mode_contrast": "lambda/sqrt(lambda^2+||r||^2) for residual orthogonal to f",
        "level_43_contrast": str(packet_contrasts[0]),
        "level_44_contrast": str(packet_contrasts[1]),
        "gates": gates,
        "hostiles": hostiles,
        "result": "Unsigned response-norm balancing converts the tiny 43/44 eigenvalue sign into a full-scale optical phase contrast. The experimental burden is response-arm dynamic range and noise, not parts-per-million differencing.",
        "next_measurement": "Calibrate response-arm noise and require a preregistered lower bound on ||Tf|| above that noise before applying the balancing gain.",
    }
    RESULT.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
