"""Exact covariance and design audit of the CPLEAR carbon calibration."""

import json
from pathlib import Path

import sympy as sp


# Values transcribed from CPLEAR, Phys. Lett. B 413 (1997) 422, Table 2.
# Each row is momentum interval, Re(df), sigma_Re, Im(df), sigma_Im, correlation.
rows = [
    ("250-350", sp.Rational(-38, 10), sp.Rational(13, 10), sp.Rational(-24, 10), sp.Rational(12, 10), sp.Rational(-76, 100)),
    ("350-450", sp.Rational(-49, 10), sp.Rational(5, 10), sp.Rational(-12, 10), sp.Rational(16, 10), sp.Rational(-76, 100)),
    ("450-550", sp.Rational(-42, 10), sp.Rational(3, 10), sp.Rational(-49, 10), sp.Rational(20, 10), sp.Rational(60, 100)),
    ("550-650", sp.Rational(-51, 10), sp.Rational(6, 10), sp.Rational(-28, 10), sp.Rational(19, 10), sp.Rational(96, 100)),
    ("650-750", sp.Rational(-57, 10), sp.Rational(18, 10), sp.Rational(-43, 10), sp.Rational(36, 10), sp.Rational(99, 100)),
]

calibrations = []
for interval, re_df, sre, im_df, sim, corr in rows:
    covariance = sp.Matrix(
        [[sre**2, corr * sre * sim], [corr * sre * sim, sim**2]]
    )
    calibrations.append(
        {
            "momentum_MeV_c": interval,
            "mean_fm": [str(re_df), str(im_df)],
            "covariance_fm2": [[str(x) for x in row] for row in covariance.tolist()],
            "covariance_determinant": str(sp.factor(covariance.det())),
            "rank": covariance.rank(),
        }
    )

# Absent/present carbon gives only two settings.  It identifies an affine slope
# after the vacuum intercept is fixed, but cannot distinguish an added quadratic
# coefficient from a changed slope.
binary_design = sp.Matrix([[1, 0, 0], [1, 1, 1]])
three_density_design = sp.Matrix([[1, 0, 0], [1, 1, 1], [1, 2, 4]])

checks = {
    "five_common_frame_complex_bins": len(rows) == 5,
    "every_covariance_has_rank_two": min(item["rank"] for item in calibrations) == 2,
    "every_covariance_determinant_positive": all(
        sp.sympify(item["covariance_determinant"]) > 0 for item in calibrations
    ),
    "both_measured_components_nonzero_in_every_bin": all(
        row[1] != 0 and row[3] != 0 for row in rows
    ),
    "binary_absorber_design_cannot_test_quadratic": binary_design.rank() == 2,
    "third_density_would_identify_quadratic": three_density_design.rank() == 3,
    "third_density_design_determinant_nonzero": three_density_design.det() != 0,
}

result = {
    "work_package": "WP407",
    "title": "CPLEAR common-knob complex calibration",
    "source": "CPLEAR Phys. Lett. B 413 (1997) 422-430, Table 2",
    "instrument": "tagged K0 and anti-K0 two-pion decay rates with and without a 2.5 cm graphite absorber",
    "calibrations": calibrations,
    "contextual_partition": "absorber absent versus present, resolved into dispersive and absorptive response in five momentum bins",
    "classification": "empirical rank-two calibration of one binary material intervention; not a three-density completion test",
    "smallest_exact_falsifier": "either component response is zero or a reported covariance has determinant zero",
    "remaining_gate": "execute at least three independently certified carbon column densities and reserve a fourth displacement before fitting",
    "checks": checks,
    "passed": all(checks.values()),
}

if not result["passed"]:
    raise SystemExit("WP407 exact checks failed")

out = Path(__file__).parents[1] / "results" / "wp407_cplear_common_knob_calibration.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
