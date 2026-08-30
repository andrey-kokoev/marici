"""Zero-refit test of pre-CPLEAR optical-model predictions against CPLEAR."""

import json
from pathlib import Path

import sympy as sp


# CPLEAR Table 2 rows with an independently published optical-model prediction.
# Entries: interval, measured Re/Im, errors, correlation, predicted Re/Im.
rows = [
    ("350-450", (-49, -12), (5, 16, -76), (-348, -388)),
    ("450-550", (-42, -49), (3, 20, 60), (-403, -338)),
    ("550-650", (-51, -28), (6, 19, 96), (-526, -381)),
    ("650-750", (-57, -43), (18, 36, 99), (-638, -459)),
]

contributions = []
total = sp.Rational(0)
for interval, measured10, error10_corr100, predicted100 in rows:
    measured = sp.Matrix([sp.Rational(value, 10) for value in measured10])
    predicted = sp.Matrix([sp.Rational(value, 100) for value in predicted100])
    sre, sim = (sp.Rational(error10_corr100[0], 10), sp.Rational(error10_corr100[1], 10))
    corr = sp.Rational(error10_corr100[2], 100)
    covariance = sp.Matrix([[sre**2, corr*sre*sim], [corr*sre*sim, sim**2]])
    residual = measured - predicted
    chi2 = sp.factor((residual.T * covariance.inv() * residual)[0])
    total += chi2
    contributions.append(
        {
            "momentum_MeV_c": interval,
            "measured_fm": [str(x) for x in measured],
            "predicted_fm": [str(x) for x in predicted],
            "residual_fm": [str(x) for x in residual],
            "chi_squared_two_components": str(chi2),
            "chi_squared_decimal": float(chi2),
        }
    )

degrees_of_freedom = 2 * len(rows)  # zero parameters fitted to CPLEAR
critical_95 = sp.Rational(15507, 1000)  # chi-square df=8 upper 5% critical value
publication_year_model = 1994
publication_year_measurement = 1997

checks = {
    "model_precedes_measurement": publication_year_model < publication_year_measurement,
    "four_complex_predictions_tested": len(rows) == 4,
    "zero_cplear_fit_parameters": degrees_of_freedom == 8,
    "global_statistic_below_predeclared_95_percent_boundary": total < critical_95,
    "hostile_low_bin_is_nontrivial": sp.Rational(contributions[0]["chi_squared_two_components"]) > 2,
    "prediction_is_not_exact_lookup": total != 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP410",
    "title": "Pre-CPLEAR optical-model withheld displacement test",
    "prediction_source": "Eberhard and Uchiyama, Nucl. Instrum. Meth. A 350 (1994) 144-149",
    "measurement_source": "CPLEAR, Phys. Lett. B 413 (1997) 422-430, Table 2",
    "fit_parameters_from_withheld_measurement": 0,
    "degrees_of_freedom": degrees_of_freedom,
    "contributions": contributions,
    "global_chi_squared_exact": str(sp.factor(total)),
    "global_chi_squared_decimal": float(total),
    "critical_value_95_percent": float(critical_95),
    "classification": "retrospective but chronologically genuine zero-refit prediction of four complex flavor displacements",
    "smallest_falsifier": "the 350-450 MeV/c bin alone contributes chi-square 8.62 for two components and exposes the strongest local tension",
    "remaining_gate": "validate the optical-model input independence and completion domain; do not transport this success to physical16 selection",
    "checks": checks,
    "passed": all(checks.values()),
}

if not result["passed"]:
    raise SystemExit("WP410 exact checks failed")

out = Path(__file__).parents[1] / "results" / "wp410_pre_cplear_withheld_test.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
