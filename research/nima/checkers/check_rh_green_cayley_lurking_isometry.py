from fractions import Fraction
import json
from pathlib import Path


alpha = Fraction(3, 2)


def half_plane_coordinate(w):
    return alpha * (1 + w) / (1 - w)


samples = [
    (Fraction(0), Fraction(1, 3)),
    (Fraction(-1, 2), Fraction(1, 4)),
    (Fraction(2, 5), Fraction(-1, 3)),
]

records = []
for w, v in samples:
    zeta = half_plane_coordinate(w)
    eta = half_plane_coordinate(v)
    left = zeta + eta
    right = 2 * alpha * (1 - w * v) / ((1 - w) * (1 - v))
    assert left == right

    # Scalar exact feature sample G(zeta)=1+zeta.
    g_zeta = 1 + zeta
    g_eta = 1 + eta
    half_plane_kernel = g_eta * g_zeta
    disk_feature_w = Fraction(2) * alpha * g_zeta / (1 - w)
    # Avoid square roots by storing the scaled Gram product directly.
    disk_kernel = 2 * alpha * half_plane_kernel / ((1 - w) * (1 - v))
    boundary_half_plane = (zeta + eta) * half_plane_kernel
    boundary_disk = (1 - w * v) * disk_kernel
    assert boundary_half_plane == boundary_disk
    records.append(
        {
            "w": str(w),
            "v": str(v),
            "zeta": str(zeta),
            "eta": str(eta),
            "boundary_pairing": str(boundary_half_plane),
        }
    )

result = {
    "chart_scale": str(alpha),
    "two_height_samples": len(samples),
    "cayley_polarization_identity_verified": True,
    "green_boundary_factor_equals_disk_defect_factor": True,
    "records": records,
    "theta_boundary_pairing_constructed": False,
    "endpoint_input_output_factorization_constructed": False,
    "verdict": "the polarized Green conservation law and the lurking-isometry defect are the same gate in half-plane and disk coordinates",
}

out = Path(__file__).parents[1] / "results" / "rh-green-cayley-lurking-isometry.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
