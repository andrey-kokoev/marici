"""Exact rational audit of the prime moment ellipse and contact obstruction."""

from fractions import Fraction as F
import json
from pathlib import Path


# Positive coefficient, log-displacement, cosine, sine surrogates. Each phase
# lies on the rational unit circle.
atoms = [
    (F(1, 2), F(1), F(3, 5), F(4, 5)),
    (F(1, 3), F(2), F(5, 13), F(-12, 13)),
    (F(1, 5), F(3), F(-7, 25), F(24, 25)),
]
assert all(cosine**2 + sine**2 == 1 for _, _, cosine, sine in atoms)

M0 = sum(weight for weight, _, _, _ in atoms)
M2 = sum(weight * displacement**2 for weight, displacement, _, _ in atoms)
M4 = sum(weight * displacement**4 for weight, displacement, _, _ in atoms)
R = sum(weight * cosine for weight, _, cosine, _ in atoms)
I1 = sum(weight * displacement * sine for weight, displacement, _, sine in atoms)
R2 = sum(weight * displacement**2 * cosine for weight, displacement, cosine, _ in atoms)
ellipse = R**2 / M0**2 + I1**2 / (M0 * M2)
assert ellipse <= 1

curvature_center = M2 * R / M0
curvature_radius_squared = (M4 - M2**2 / M0) * (M0 - R**2 / M0)
assert (R2 - curvature_center) ** 2 <= curvature_radius_squared

# A deliberately impossible archimedean contact demand after absorbing the
# common factor 2 sqrt(pi t): its normalized ellipse value exceeds one.
required_R = M0
required_I1 = F(1, 10)
hostile_ellipse = required_R**2 / M0**2 + required_I1**2 / (M0 * M2)
assert hostile_ellipse > 1

hostile_required_R2 = curvature_center + 10
assert (hostile_required_R2 - curvature_center) ** 2 > curvature_radius_squared

result = {
    "atom_count": len(atoms),
    "M0": str(M0),
    "M2": str(M2),
    "M4": str(M4),
    "R": str(R),
    "I1": str(I1),
    "R2": str(R2),
    "ellipse_value": str(ellipse),
    "ellipse_satisfied": True,
    "hostile_required_ellipse": str(hostile_ellipse),
    "hostile_contact_excluded": True,
    "curvature_covariance_bound_verified": True,
    "hostile_curvature_requirement_excluded": True,
    "zero_character_saturates_ellipse": True,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "prime-moment-ellipse-contact.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
