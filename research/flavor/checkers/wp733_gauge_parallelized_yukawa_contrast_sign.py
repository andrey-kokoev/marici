"""Exact sign theorem for gauge-parallelized separate A/B Yukawa nullclines."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
g1, g2, T = sp.symbols("g_1 g_2 T", positive=True)
yA, kA, yB, kB = sp.symbols("y_A kappa_A y_B kappa_B", real=True)

eqA = [
    8 * yA + 2 * kA - 12 * g1,
    3 * yA + 9 * kA + 6 * T - sp.Rational(15, 2) * g1 - sp.Rational(9, 2) * g2,
]
eqB = [
    12 * yB + sp.Rational(1, 2) * kB - 12 * g1 - 24 * g2,
    3 * yB + sp.Rational(23, 4) * kB + 6 * T - sp.Rational(15, 2) * g1 - sp.Rational(33, 2) * g2,
]
solA = sp.solve(eqA, (yA, kA), dict=True)[0]
solB = sp.solve(eqB, (yB, kB), dict=True)[0]
qA = sp.factor(solA[yA] * solA[kA])
qB = sp.factor(solB[yB] * solB[kB])
source_contrast = sp.factor(-4 * qA + 3 * qB)

r, t = sp.symbols("r t", nonnegative=True)
scaled_contrast = sp.factor(source_contrast.subs({g2: r * g1, T: t * g1}) / g1**2)
P = sp.factor(scaled_contrast * sp.Rational(27225, 2))
t_star = sp.factor((91144 * r - 11544) / (2 * 5264))
t_boundary = (2 + 3 * r) / 4
r0 = sp.Rational(1443, 11393)
r1 = sp.Rational(191, 946)
P_at_zero = sp.factor(P.subs(t, 0))
P_at_star = sp.factor(P.subs(t, t_star))
P_at_boundary = sp.factor(P.subs(t, t_boundary))
middle_quadratic = 737 * r**2 - 596 * r + 8

checks = {
    "model_A_nullclines_solve_exactly": all(sp.simplify(e.subs(solA)) == 0 for e in eqA),
    "model_B_nullclines_solve_exactly": all(sp.simplify(e.subs(solB)) == 0 for e in eqB),
    "model_A_product_formula": sp.simplify(qA - (-4 * T + 2 * g1 + 3 * g2) * (4 * T + 31 * g1 - 3 * g2) / 121) == 0,
    "model_B_product_formula": sp.simplify(qB - 2 * (-4 * T + 3 * g1 + 7 * g2) * (4 * T + 87 * g1 + 173 * g2) / 675) == 0,
    "scaled_contrast_polynomial": sp.expand(P) == 150581 * r**2 - 91144 * r * t + 97338 * r + 5264 * t**2 + 11544 * t + 3681,
    "low_r_minimum_at_zero_is_positive_polynomial": P_at_zero == 150581 * r**2 + 97338 * r + 3681,
    "interior_minimum_formula": sp.simplify(P_at_star + sp.Rational(108900, 329) * middle_quadratic) == 0,
    "middle_quadratic_negative_at_left_endpoint": middle_quadratic.subs(r, r0) < 0,
    "middle_quadratic_negative_at_right_endpoint": middle_quadratic.subs(r, r1) < 0,
    "convex_middle_quadratic_is_negative_between_negative_endpoints": sp.diff(middle_quadratic, r, 2) > 0,
    "high_r_boundary_minimum_is_positive": sp.simplify(P_at_boundary - 121 * (4 * r + 1) * (176 * r + 89)) == 0,
    "vertex_crosses_zero_and_boundary_at_exact_breakpoints": t_star.subs(r, r0) == 0 and sp.simplify((t_star - t_boundary).subs(r, r1)) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP733",
    "status": "PASS",
    "checks": checks,
    "source_domain": "the separately published one-loop A and B Yukawa nullclines evaluated over shared positive gauge coordinates and common top-bottom sum",
    "source_relation": "each independent flavor sector is parallelized by the same electroweak gauge coordinates rather than a common flavor intertwiner",
    "sign_result": "the additive portal contrast -4 q_A + 3 q_B is strictly positive wherever the displayed A/B Yukawa nullcline coordinates are positive",
    "cancellation_result": "q_B/q_A=4/3 has no point in that positive truncated domain",
    "classification": "source-derived sign selector on the separate-nullcline truncation, not yet a simultaneous-theory magnitude or basin selector",
    "smallest_exact_falsifier": "any physical positive simultaneous fixed point at which cross anomalous dimensions restore -4 q_A + 3 q_B=0",
    "claim_boundary": "cross A/B anomalous-dimension terms and combined gauge beta coefficients are absent from the separately published systems",
    "remaining_rg_gate": "derive the simultaneous gauge-Yukawa beta system and test persistence of the strict sign and irrelevance margins",
    "remaining_threshold_instrument_gate": "complete finite matching and a calibrated rank-two singlet/triplet detector response",
    "primary_source": "https://arxiv.org/abs/2008.08606",
}
(ROOT / "results" / "wp733_gauge_parallelized_yukawa_contrast_sign.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
