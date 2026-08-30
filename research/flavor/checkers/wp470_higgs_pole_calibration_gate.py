import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
wp469 = json.loads((root / "results" / "wp469_source_radial_lift.json").read_text(encoding="utf-8"))

v = sp.Rational(12311, 50)
measured = sp.Rational(626, 5)
sigma = sp.Rational(11, 100)
working_multiplier = sp.Rational(49, 25)
working_upper = sp.simplify(measured + working_multiplier * sigma)

lambda_minus = 206 - 2 * sp.sqrt(10009)
lambda_plus = 206 + 2 * sp.sqrt(10009)
m_minus = sp.simplify(v * sp.sqrt(lambda_minus / 2))
m_dilaton = sp.simplify(sp.sqrt(6) * v)
m_plus = sp.simplify(v * sp.sqrt(lambda_plus / 2))

higgs_residue_minus = sp.Rational(1, 3) + 100 * sp.sqrt(10009) / 30027
higgs_residue_dilaton = sp.Rational(1, 3)
higgs_residue_plus = sp.Rational(1, 3) - 100 * sp.sqrt(10009) / 30027

checks = {
    "wp469_dependency_passed": wp469["passed"],
    "all_higgs_radial_residues_are_positive": all(
        residue > 0 for residue in (higgs_residue_minus, higgs_residue_dilaton, higgs_residue_plus)
    ),
    "lightest_radial_pole_is_m_minus": m_minus < m_dilaton < m_plus,
    "lightest_pole_exceeds_working_interval": sp.simplify(m_minus**2 - working_upper**2) > 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP470",
    "instrument": {
        "source": "Particle Data Group 2025 Higgs listing",
        "mass_GeV": str(measured),
        "sigma_GeV": str(sigma),
        "working_95_percent_upper_GeV": str(working_upper),
    },
    "frozen_electroweak_scale_GeV": str(v),
    "predicted_radial_poles_GeV": {
        "m_minus_exact": str(m_minus),
        "m_minus_numeric": float(sp.N(m_minus, 16)),
        "m_dilaton_exact": str(m_dilaton),
        "m_dilaton_numeric": float(sp.N(m_dilaton, 16)),
        "m_plus_exact": str(m_plus),
        "m_plus_numeric": float(sp.N(m_plus, 16)),
    },
    "higgs_radial_residues": {
        "m_minus": str(higgs_residue_minus),
        "m_dilaton": str(higgs_residue_dilaton),
        "m_plus": str(higgs_residue_plus),
    },
    "lightest_gap_above_working_upper_GeV": float(sp.N(m_minus - working_upper, 16)),
    "classification": "unit common-dilaton benchmark rejected by the calibrated Higgs pole before width composition",
    "remaining_gate": "independently select coefficients, recompute Hessian and residues, then use Higgs mass and width as withheld tests",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp470_higgs_pole_calibration_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)

