"""Compare the fixed toy prediction with quoted recoil determinations.

Uses published values quoted in the research note, not raw experimental data.
Exact rational arithmetic; no artifacts written and no fitted coefficients.
"""
from fractions import Fraction as F

baseline = F(137)
gain = F(45, 170368)
prediction = baseline / (1 - gain)
measurements = {
    "Rb 2020": (F("137.035999206"), F("0.000000011")),
    "Cs 2018": (F("137.035999046"), F("0.000000027")),
}
print(f"Fixed toy inverse coupling: {float(prediction):.12f}")
for label, (inverse, uncertainty) in measurements.items():
    difference = prediction - inverse
    # Measurement uncertainty only; the toy model has no uncertainty budget.
    units = difference / uncertainty
    q_ratio = (inverse / prediction)**2
    leading_magnetic_ratio = inverse / prediction
    print(f"{label}: inverse difference={float(difference):.12f}, "
          f"measurement-uncertainty units={float(units):.1f}")
    print(f"  alpha^2 prediction/measurement={float(q_ratio):.12f}")
    print(f"  leading magnetic term prediction/measurement={float(leading_magnetic_ratio):.12f}")
    assert abs(difference) > 1000 * uncertainty
    # Both routes reconstruct the same alpha when generated from it.
    alpha = 1/inverse
    q = alpha**2
    assert q == 1/inverse**2
    # No independent magnetic experiment is encoded in this identity.

print("Precision mismatch confirmed. No carrier correction derived by this test.")
