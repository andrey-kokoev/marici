"""Exact four-thickness no-refit protocol for neutral-kaon regeneration."""

import json
from pathlib import Path

import sympy as sp


x = sp.symbols("x", real=True)
b0r, b1r, b2r, b0i, b1i, b2i = sp.symbols(
    "b0r b1r b2r b0i b1i b2i", real=True
)
re_shift = b0r + b1r * x + b2r * x**2
im_shift = b0i + b1i * x + b2i * x**2

calibration_points = (0, 1, 2)
withheld_point = 3
design = sp.Matrix([[1, point, point**2] for point in calibration_points])
withheld_row = sp.Matrix([[1, withheld_point, withheld_point**2]])
weights = sp.simplify(withheld_row * design.inv())

observed_re = sp.Matrix(sp.symbols("r0:3", real=True))
observed_im = sp.Matrix(sp.symbols("i0:3", real=True))
predicted_re = sp.expand((weights * observed_re)[0])
predicted_im = sp.expand((weights * observed_im)[0])

# Quadratic coefficient is the second divided difference on equally spaced
# thicknesses.  It is tested before the fourth context is opened.
quadratic_contrast = sp.Matrix([[1, -2, 1]])

# Use CPLEAR's 450--550 MeV/c covariance as a conservative concrete scale for
# one setting.  Independent equal-precision calibration settings propagate by
# the squared interpolation weights.
Sigma = sp.Matrix([[sp.Rational(9, 100), sp.Rational(9, 25)],
                   [sp.Rational(9, 25), sp.Integer(4)]])
prediction_covariance = sp.simplify(sum(w**2 for w in weights) * Sigma)

# A separately measured withheld vector d is accepted by a predeclared
# Mahalanobis threshold after adding its independently calibrated covariance.
dr, di = sp.symbols("d_r d_i", real=True)
residual = sp.Matrix([dr - predicted_re, di - predicted_im])
combined_covariance = prediction_covariance + Sigma
mahalanobis = sp.factor((residual.T * combined_covariance.inv() * residual)[0])

checks = {
    "three_calibration_thicknesses_identify_quadratic": design.det() != 0,
    "withheld_context_not_in_calibration_set": withheld_point not in calibration_points,
    "no_refit_weights_are_unique": weights == sp.Matrix([[1, -3, 3]]),
    "withheld_real_prediction_fixed": predicted_re == observed_re[0] - 3 * observed_re[1] + 3 * observed_re[2],
    "withheld_imag_prediction_fixed": predicted_im == observed_im[0] - 3 * observed_im[1] + 3 * observed_im[2],
    "quadratic_contrast_detects_x_squared": (quadratic_contrast * sp.Matrix([0, 1, 4]))[0] != 0,
    "prediction_covariance_positive_definite": prediction_covariance.det() > 0 and prediction_covariance[0, 0] > 0,
    "withheld_acceptance_statistic_nonnegative": combined_covariance.det() > 0,
    "zero_residual_has_zero_statistic": sp.simplify(
        mahalanobis.subs({dr: predicted_re, di: predicted_im}, simultaneous=True)
    ) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP408",
    "title": "Four-thickness kaon no-refit protocol",
    "physical_settings": {
        "fixed": "carbon composition, kaon momentum bin, geometry, beam preparation, and detector selection",
        "calibration_thicknesses": ["0", "t", "2t"],
        "withheld_thickness": "3t",
    },
    "quadratic_design_determinant": str(design.det()),
    "no_refit_prediction_weights": [str(value) for value in weights],
    "withheld_complex_prediction": {"real": str(predicted_re), "imaginary": str(predicted_im)},
    "quadratic_contrast": [str(value) for value in quadratic_contrast],
    "example_prediction_covariance": [[str(x) for x in row] for row in prediction_covariance.tolist()],
    "withheld_mahalanobis_statistic": str(mahalanobis),
    "blinding_rule": "seal all 3t event identifiers before fitting 0,t,2t; unseal once; reject or accept without refitting",
    "smallest_exact_falsifier": "a nonzero second divided difference rejects the affine source shift before the 3t record is opened",
    "status": "executable protocol derived; no qualifying four-thickness dataset located or executed",
    "checks": checks,
    "passed": all(checks.values()),
}

if not result["passed"]:
    failed = [name for name, value in checks.items() if not value]
    raise SystemExit(f"WP408 exact checks failed: {failed}")

out = Path(__file__).parents[1] / "results" / "wp408_four_thickness_kaon_protocol.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
