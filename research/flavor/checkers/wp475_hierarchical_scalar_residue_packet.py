import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
wp474 = json.loads((root / "results" / "wp474_kaon_conditioned_higgs_alignment.json").read_text(encoding="utf-8"))

a = sp.sympify(wp474["a_current_ceiling"]["exact"])
v_tev = sp.Rational(12311, 50000)
m_h_tev = sp.Rational(626, 5000)
ell = sp.simplify(2 * m_h_tev**2 / v_tev**2)
eta = sp.factor(ell * (a * ell - 400) / (4 * (2 * a**2 * ell + a * ell - 200 * a - 400)))

L_h = sp.simplify(a * ell)
L_d = sp.simplify(8 + 4 * a)
L_heavy = sp.factor(200 * (a + 2) * (a * ell - 400) / (2 * a**2 * ell + a * ell - 200 * a - 400))

denominator = 2 * a**3 * ell**2 + a**2 * ell**2 - 400 * a**2 * ell - 800 * a * ell + 80000 * a + 160000
Z_h = sp.factor((a * ell - 400) ** 2 / denominator)
Z_d = sp.factor(a / (a + 2))
Z_heavy = sp.factor(1 - Z_h - Z_d)

A, E, l_symbol = sp.symbols("A E l", positive=True)
eta_symbolic = sp.factor(l_symbol * (A * l_symbol - 400) / (4 * (2 * A**2 * l_symbol + A * l_symbol - 200 * A - 400)))
R_symbolic = sp.Matrix(
    [
        [106, 2 * sp.sqrt(6 * A), -98 * sp.sqrt(3)],
        [2 * sp.sqrt(6 * A), 4 * A * (E + 1), 2 * sp.sqrt(2 * A) * (1 - 2 * A * E)],
        [-98 * sp.sqrt(3), 2 * sp.sqrt(2 * A) * (1 - 2 * A * E), 302 + 8 * A**2 * E],
    ]
)
x = sp.symbols("x")
symbolic_heavy = sp.factor(200 * (A + 2) * (A * l_symbol - 400) / (2 * A**2 * l_symbol + A * l_symbol - 200 * A - 400))
characteristic_identity = sp.factor(
    R_symbolic.subs(E, eta_symbolic).charpoly(x).as_expr()
    - (x - A * l_symbol) * (x - (8 + 4 * A)) * (x - symbolic_heavy)
)

f_min_tev = sp.sympify(wp474["f_min_TeV"])
w_tev = sp.simplify(f_min_tev / sp.sqrt(6))
m_d_tev = sp.simplify(w_tev * sp.sqrt(L_d))
m_heavy_tev = sp.simplify(w_tev * sp.sqrt(L_heavy))
sm_width_mev = sp.Rational(41, 10)
width_mev = sp.simplify(Z_h * sm_width_mev)
rate_lower = sp.Rational(2379, 2500)

checks = {
    "wp474_dependency_passed": wp474["passed"],
    "eta_is_positive": eta > 0,
    "characteristic_polynomial_factorizes_exactly": characteristic_identity == 0,
    "all_radial_curvatures_are_positive": all(value > 0 for value in (L_h, L_d, L_heavy)),
    "residues_are_positive": all(value > 0 for value in (Z_h, Z_d, Z_heavy)),
    "residues_are_complete": sp.simplify(Z_h + Z_d + Z_heavy) == 1,
    "higgs_residue_passes_rate_gate": Z_h > rate_lower,
    "higgs_mass_is_exactly_calibrated": sp.simplify(w_tev * sp.sqrt(L_h) - m_h_tev) == 0,
    "new_radial_thresholds_are_closed_to_higgs": m_d_tev > 2 * m_h_tev and m_heavy_tev > 2 * m_h_tev,
    "leading_width_is_in_direct_summary_interval": sp.Rational(23, 10) < width_mev < sp.Rational(28, 5),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP475",
    "inherited_domain": "WP474 exact kaon-conditioned endpoint with y=kappa=lambda=rho=1",
    "a": {"exact": str(a), "numeric": float(sp.N(a, 16))},
    "eta_higgs_calibrated": {"exact": str(eta), "numeric": float(sp.N(eta, 16))},
    "dimensionless_radial_spectrum": {
        "higgs": str(L_h),
        "lifted": str(L_d),
        "heavy": str(L_heavy),
    },
    "radial_masses_TeV": {
        "higgs": str(m_h_tev),
        "lifted_numeric": float(sp.N(m_d_tev, 16)),
        "heavy_numeric": float(sp.N(m_heavy_tev, 16)),
    },
    "higgs_channel_residues": {
        "higgs": {"exact": str(Z_h), "numeric": float(sp.N(Z_h, 16))},
        "lifted": {"exact": str(Z_d), "numeric": float(sp.N(Z_d, 16))},
        "heavy": {"exact": str(Z_heavy), "numeric": float(sp.N(Z_heavy, 16))},
    },
    "leading_higgs_width_MeV": {"exact": str(width_mev), "numeric": float(sp.N(width_mev, 16))},
    "classification": "conditional hierarchical scalar packet compatible with provisional current, Higgs mass, rate, and width instruments",
    "remaining_gate": "recompute flavor-vector current response and all vector widths with the hierarchical scalar thresholds frozen",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp475_hierarchical_scalar_residue_packet.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
