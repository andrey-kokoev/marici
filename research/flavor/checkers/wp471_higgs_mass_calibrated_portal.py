import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
wp470 = json.loads((root / "results" / "wp470_higgs_pole_calibration_gate.json").read_text(encoding="utf-8"))

eta, x = sp.symbols("eta x", real=True)
v = sp.Rational(12311, 50)
m_h = sp.Rational(626, 5)
target = sp.simplify(2 * m_h**2 / v**2)
R = sp.Matrix(
    [
        [106, 2 * sp.sqrt(6), -98 * sp.sqrt(3)],
        [2 * sp.sqrt(6), 4 * eta + 4, (-4 * eta + 2) * sp.sqrt(2)],
        [-98 * sp.sqrt(3), (-4 * eta + 2) * sp.sqrt(2), 302 + 8 * eta],
    ]
)
pole_equation = sp.factor((R - target * sp.eye(3)).det())
solutions = sp.solve(pole_equation, eta)
eta_h = sp.factor(solutions[0])
R_h = sp.simplify(R.subs(eta, eta_h))
spectrum = R_h.eigenvals()

projectors = {}
for eigenvalue in spectrum:
    projector = sp.eye(3)
    for other in spectrum:
        if other != eigenvalue:
            projector = sp.simplify(projector * (R_h - other * sp.eye(3)) / (eigenvalue - other))
    projectors[str(eigenvalue)] = {
        "flavor_radial": str(sp.factor(projector[0, 0])),
        "higgs_radial": str(sp.factor(projector[1, 1])),
        "singlet_radial": str(sp.factor(projector[2, 2])),
    }

heavy = sp.Rational(12109182640, 30233769)
higgs_residue = sp.Rational(45822595065274178, 68734007773010799)
derivative = sp.simplify(sp.diff(pole_equation, eta))

checks = {
    "wp470_dependency_passed": wp470["passed"],
    "calibration_equation_is_linear": sp.Poly(pole_equation, eta).degree() == 1,
    "calibration_solution_is_unique": len(solutions) == 1,
    "calibrated_eta_is_positive": eta_h > 0,
    "target_is_exact_eigenvalue": spectrum.get(target) == 1,
    "lifted_pole_is_preserved": spectrum.get(12) == 1,
    "heavy_pole_is_exact": spectrum.get(heavy) == 1,
    "all_radial_poles_are_positive": all(value > 0 for value in spectrum),
    "calibration_response_is_nonzero": derivative != 0,
    "higgs_residue_matches_projector": projectors[str(target)]["higgs_radial"] == str(higgs_residue),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP471",
    "calibration_instrument": "PDG 2025 Higgs central mass",
    "target_mass_GeV": str(m_h),
    "target_dimensionless_curvature": str(target),
    "calibrated_eta": {"exact": str(eta_h), "numeric": float(sp.N(eta_h, 16))},
    "radial_spectrum": {str(value): int(multiplicity) for value, multiplicity in spectrum.items()},
    "radial_diagonal_residues": projectors,
    "higgs_pole_higgs_residue": {
        "exact": str(higgs_residue),
        "numeric": float(sp.N(higgs_residue, 16)),
    },
    "target_ratio_dependence_on_eta": "none",
    "classification": "rank-one detector calibration of eta with g_F*f/v unchanged; residues are withheld predictions",
    "remaining_gate": "test frozen Higgs residues with rate and width likelihood, then derive complete scalar and vector widths",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp471_higgs_mass_calibrated_portal.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)

