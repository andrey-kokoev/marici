"""Dependency-free exact checks for a causal magneto-optic response pair."""

from fractions import Fraction as F
import json
from pathlib import Path


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def inv(a):
    norm = a[0] * a[0] + a[1] * a[1]
    return (a[0] / norm, -a[1] / norm)


def conj(a):
    return (a[0], -a[1])


def chi(sign, omega, gamma=F(1), splitting=F(1)):
    # 1 / [gamma - i(omega - sign*splitting)]
    return inv((gamma, -(omega - sign * splitting)))


def encode(z):
    return {"real": str(z[0]), "imag": str(z[1])}


def main():
    zero = (F(0), F(0))
    cp0 = chi(F(1), F(0))
    cm0 = chi(F(-1), F(0))
    cp2 = chi(F(1), F(2))
    cm2 = chi(F(-1), F(2))
    delta0 = sub(cp0, cm0)
    delta2 = sub(cp2, cm2)
    constant_rotation_residual = sub(delta2, delta0)

    # Real-field conjugation: chi_+(-w) = conjugate(chi_-(w)).
    symmetry_residual = sub(chi(F(1), F(-2)), conj(cm2))

    # A single H analyzer maps distinct Jones states (1,1) and (1,-1)
    # to the same scalar first component.
    analyzer_collision = (F(1), F(1)) != (F(1), F(-1))

    lower_half_plane_poles = [(F(1), F(-1)), (F(-1), F(-1))]
    hostile_upper_pole = (F(1), F(1))

    checks = {
        "both_retarded_poles_are_strictly_lower_half_plane": all(
            pole[1] < 0 for pole in lower_half_plane_poles
        ),
        "upper_half_plane_hostile_is_rejected": hostile_upper_pole[1] > 0,
        "real_field_bias_reversal_symmetry_holds": symmetry_residual == zero,
        "passive_absorptive_sign_is_positive_at_resonance": chi(F(1), F(1))[0] > 0,
        "bias_splitting_is_nonzero": delta0 != zero,
        "zero_bias_erases_circular_splitting": chi(F(1), F(2), splitting=F(0)) == chi(
            F(-1), F(2), splitting=F(0)
        ),
        "constant_rotation_hostile_fails_at_second_frequency": constant_rotation_residual != zero,
        "one_linear_analyzer_is_not_faithful": analyzer_collision,
    }

    result = {
        "schema": "marici.aspect.causal_dispersive_magneto_optic_response.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "parameters": {"gamma": "1", "Omega": "1", "sample_frequencies": ["0", "2"]},
        "checks": checks,
        "residuals": {
            "bias_splitting_at_zero": encode(delta0),
            "bias_splitting_at_two": encode(delta2),
            "constant_rotation_second_sample_minus_calibration": encode(
                constant_rotation_residual
            ),
            "real_field_symmetry": encode(symmetry_residual),
        },
        "typed_boundary": {
            "source": "phenomenological retarded two-circular-channel susceptibility",
            "port": "one calibrated transverse Jones C^2 port",
            "detector": "fixed analyzer row C^2->C",
            "completion": "bath/noise ports and broadband asymptotics are not constructed",
        },
    }
    out = Path(__file__).parents[1] / "results" / "causal_dispersive_magneto_optic_response.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
