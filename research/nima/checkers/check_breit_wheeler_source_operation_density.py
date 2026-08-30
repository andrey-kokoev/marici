import json
import sys
from pathlib import Path

import numpy as np

NIMA = Path(__file__).parents[1]
sys.path.insert(0, str(NIMA))
from check_nonforward_breit_wheeler_cut import cut_matrix  # noqa: E402


def main():
    s = 10.0
    forward = cut_matrix(s, 0.0, order=20)
    theta = np.arccos(1 - 2 / s)
    cross_angle = cut_matrix(s, theta, order=20)

    forward_hermitian = np.max(np.abs(forward - forward.conjugate().T))
    forward_eigenvalues = np.linalg.eigvalsh(
        (forward + forward.conjugate().T) / 2
    )
    cross_angle_hermitian = np.max(
        np.abs(cross_angle - cross_angle.conjugate().T)
    )
    cross_angle_distance = np.max(np.abs(cross_angle - forward))

    gates = {
        "forward_cut_is_hermitian": bool(forward_hermitian < 1e-11),
        "forward_cut_is_positive": bool(forward_eigenvalues.min() > -1e-11),
        # Hermiticity or positivity cannot type this object as an effect:
        # source and target are distinct angular fibers.  Numerically we only
        # certify that it is a genuinely different comparison kernel.
        "cross_angle_is_a_distinct_fiber_comparison": bool(cross_angle_distance > 1e-8),
        "cut_has_cross_section_not_probability_normalization": (
            float(np.trace(forward).real) > 0
            and float(np.trace(forward).real) != 1.0
        ),
    }
    assert all(gates.values()), gates

    result = {
        "schema": "marici.breit-wheeler-source-operation-density.v1",
        "gates": gates,
        "forward_hermitian_residual": float(forward_hermitian),
        "forward_min_eigenvalue": float(forward_eigenvalues.min()),
        "forward_trace": float(np.trace(forward).real),
        "cross_angle_hermitian_residual": float(cross_angle_hermitian),
        "cross_angle_distance_from_forward_effect": float(cross_angle_distance),
        "conclusion": (
            "The source amplitude supplies a positive forward operation/effect "
            "density. The cross-angle kernel is comparison data, and neither "
            "becomes a normalized instrument without exposure and a no-event branch."
        ),
    }
    out = NIMA / "results" / "breit-wheeler-source-operation-density.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
