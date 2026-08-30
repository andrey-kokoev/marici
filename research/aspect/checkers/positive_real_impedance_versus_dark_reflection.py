"""Exact port-taxonomy checks for positive-real impedance and reflection zeros."""

from fractions import Fraction as F
import json
from pathlib import Path


def add(z, w):
    return (z[0] + w[0], z[1] + w[1])


def sub(z, w):
    return (z[0] - w[0], z[1] - w[1])


def mul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def inv(z):
    n = z[0] * z[0] + z[1] * z[1]
    return (z[0] / n, -z[1] / n)


def div(z, w):
    return mul(z, inv(w))


def conj(z):
    return (z[0], -z[1])


def scale(q, z):
    return (q * z[0], q * z[1])


def impedance(s, a):
    return scale(F(1, 1) / a, s)


def reflection(s, a):
    return div(sub(s, (a, F(0))), add(s, (a, F(0))))


def norm2(z):
    return z[0] * z[0] + z[1] * z[1]


def encode(z):
    return {"real": str(z[0]), "imag": str(z[1])}


def main():
    a = F(2)
    zero = (F(0), F(0))
    off_seam_zero = reflection((a, F(0)), a)
    right_half_sample = (F(3), F(4))
    z_sample = impedance(right_half_sample, a)
    h_sample = reflection(right_half_sample, a)
    seam_samples = [(F(0), F(w)) for w in (-3, -1, 0, 1, 3)]

    sewing_point = (F(3), F(4))
    reflected_point = (-sewing_point[0], sewing_point[1])
    sewing_left = reflection(reflected_point, a)
    sewing_right = inv(conj(reflection(sewing_point, a)))

    # Rosenbrock matrix [[s+a,-1],[-2a,1]] has determinant s-a.
    rosenbrock_at_zero = (a + a) * F(1) - F(-1) * F(-2) * a
    hostile_state = F(1)
    hostile_input = F(2) * a
    state_equation_residual = (a + a) * hostile_state - hostile_input
    output_residual = -F(2) * a * hostile_state + hostile_input

    checks = {
        "cayley_identity_at_exact_sample": reflection(right_half_sample, a) == div(
            sub(z_sample, (F(1), F(0))), add(z_sample, (F(1), F(0)))
        ),
        "strict_positive_real_impedance_at_right_half_sample": z_sample[0] > 0,
        "schur_reflection_inside_right_half_plane": norm2(h_sample) < 1,
        "reflection_has_off_seam_zero": off_seam_zero == zero,
        "reflection_pole_is_in_left_half_plane": -a < 0,
        "reciprocal_sewing_holds": sewing_left == sewing_right,
        "seam_reflection_is_lossless": all(norm2(reflection(s, a)) == 1 for s in seam_samples),
        "rosenbrock_rank_drops_at_off_seam_zero": rosenbrock_at_zero == 0,
        "nonzero_state_input_make_selected_output_dark": (
            hostile_state != 0
            and hostile_input != 0
            and state_equation_residual == 0
            and output_residual == 0
        ),
        "one_state_realization_is_controllable_and_observable": F(1) != 0 and -F(2) * a != 0,
    }

    result = {
        "schema": "marici.aspect.positive_real_impedance_versus_dark_reflection.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "parameters": {"a": str(a)},
        "checks": checks,
        "residuals": {
            "off_seam_reflection_at_s_equal_a": encode(off_seam_zero),
            "rosenbrock_determinant_at_s_equal_a": str(rosenbrock_at_zero),
            "hostile_state_equation": str(state_equation_residual),
            "hostile_selected_output": str(output_residual),
            "right_half_sample_impedance": encode(z_sample),
            "right_half_sample_reflection_norm_squared": str(norm2(h_sample)),
            "sewing_residual": encode(sub(sewing_left, sewing_right)),
        },
        "typed_disposition": {
            "verified": "strict positive-real Z permits a zero of its Cayley reflection h",
            "physical_boundary": "s=a is off the frequency seam and is not an on-shell power-routing observation",
            "missing_authority": "no source operation canonically types an RH scalar as driving-point impedance",
        },
    }
    out = Path(__file__).parents[1] / "results" / "positive_real_impedance_versus_dark_reflection.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
