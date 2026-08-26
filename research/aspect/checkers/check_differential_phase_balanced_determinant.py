from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


Vector = tuple[F, F]


def rotate(vector: Vector, cosine: F, sine: F) -> Vector:
    x, y = vector
    return cosine * x - sine * y, sine * x + cosine * y


def norm_squared(vector: Vector) -> F:
    return vector[0] ** 2 + vector[1] ** 2


def average(left: Vector, right: Vector) -> Vector:
    return (left[0] + right[0]) / 2, (left[1] + right[1]) / 2


def main() -> None:
    cosine, sine = F(3, 5), F(4, 5)
    assert cosine**2 + sine**2 == 1

    # A true determinant-boundary coherence: |z|^2 = bc.
    z: Vector = (F(3, 100), F(4, 100))
    b = c = F(1, 20)
    assert norm_squared(z) == b * c == F(1, 400)

    plus = rotate(z, cosine, sine)
    minus = rotate(z, cosine, -sine)
    assert norm_squared(plus) == norm_squared(minus) == norm_squared(z)

    # Unsafe assembly takes x from the -epsilon block and y from the +epsilon
    # block. The components no longer belong to one rotated vector.
    cross_time: Vector = (minus[0], plus[1])
    cross_time_residual = norm_squared(cross_time) - b * c
    assert cross_time == (F(1, 20), F(6, 125))
    assert cross_time_residual == F(36, 15625)
    assert cross_time_residual > 0

    # Mirrored acquisition averages complete quadrature pairs. Odd phase drift
    # cancels exactly; the remaining common attenuation is cosine.
    balanced = average(plus, minus)
    assert balanced == (cosine * z[0], cosine * z[1])
    balanced_residual = norm_squared(balanced) - b * c
    assert balanced_residual == F(-1, 625)
    assert balanced_residual < 0

    # With a calibrated lower visibility gamma <= |cos(epsilon)|, divide the
    # measured norm by gamma^2 for a safe upper bound on the true norm.
    gamma = F(3, 5)
    corrected_ppt_upper = norm_squared(balanced) / gamma**2 - b * c
    assert corrected_ppt_upper == 0

    # An NPT record remains one-sided safe without correcting attenuation:
    # measured positivity implies true positivity because |cos| <= 1.
    npt_z: Vector = (F(3, 50), F(2, 25))
    npt_balanced = average(
        rotate(npt_z, cosine, sine), rotate(npt_z, cosine, -sine)
    )
    npt_measured_residual = norm_squared(npt_balanced) - b * c
    assert npt_measured_residual == F(11, 10000)
    assert npt_measured_residual > 0

    result = {
        "schema": "marici.aspect.differential-phase-balanced-determinant.v1",
        "status": "pass",
        "phase_rotation": {"cosine": str(cosine), "sine": str(sine)},
        "true_boundary_residual": "0",
        "unsafe_cross_time_vector": [str(value) for value in cross_time],
        "unsafe_cross_time_false_npt_residual": str(cross_time_residual),
        "balanced_vector": [str(value) for value in balanced],
        "balanced_uncorrected_residual": str(balanced_residual),
        "visibility_lower_bound": str(gamma),
        "balanced_corrected_ppt_upper": str(corrected_ppt_upper),
        "npt_balanced_measured_residual": str(npt_measured_residual),
        "verdict": "Mirrored complete-quadrature blocks cancel odd differential phase drift and prevent cross-time false NPT assembly; PPT certification additionally needs a lower bound on phase visibility.",
        "claim_boundary": "two mirrored blocks with one common phase angle per complete four-setting block; exact rotations; no within-block drift, loss imbalance, or finite-count model",
    }
    output = Path(__file__).parents[1] / "results" / "differential_phase_balanced_determinant.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
