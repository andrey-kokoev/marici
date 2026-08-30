"""Exact visible cubic separator for the WP694 hostile source pair."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
h, x = sp.symbols("h x", real=True)
rt2 = sp.sqrt(2)
lam = sp.Rational(3, 2)
p = sp.Integer(1)

def potential(portal, mass2):
    return -mass2*h**2/2 - mass2*x**2/2 + lam*h**4/4 + lam*x**4/4 + portal*h**2*x**2/2

V_plus = potential(p, lam + p)
V_minus = potential(-p, lam - p)
M_plus = sp.Matrix([[2*lam, 2*p], [2*p, 2*lam]])
M_minus = sp.Matrix([[2*lam, -2*p], [-2*p, 2*lam]])

light_plus = sp.Matrix([1, -1]) / rt2
heavy_plus = sp.Matrix([1, 1]) / rt2
light_minus = sp.Matrix([1, 1]) / rt2
heavy_minus = sp.Matrix([1, -1]) / rt2
visible = sp.Matrix([1, 0])

fields = (h, x)
def cubic(V, a, b, c):
    return sp.simplify(sum(
        a[i]*b[j]*c[k]*sp.diff(V, fields[i], fields[j], fields[k]).subs({h: 1, x: 1})
        for i in range(2) for j in range(2) for k in range(2)
    ))

g_plus = cubic(V_plus, heavy_plus, light_plus, light_plus)
g_minus = cubic(V_minus, heavy_minus, light_minus, light_minus)
evals_plus = sorted(M_plus.eigenvals().keys(), key=lambda value: float(value))
evals_minus = sorted(M_minus.eigenvals().keys(), key=lambda value: float(value))

checks = {
    "two_point_spectra_identical": evals_plus == evals_minus == [1, 5],
    "heavy_visible_overlap_equal": (visible.dot(heavy_plus))**2 == (visible.dot(heavy_minus))**2 == sp.Rational(1, 2),
    "light_visible_overlap_equal": (visible.dot(light_plus))**2 == (visible.dot(light_minus))**2 == sp.Rational(1, 2),
    "plus_cubic_nonzero": g_plus == 7*rt2/2,
    "minus_cubic_exactly_zero": g_minus == 0,
    "on_shell_two_light_channel_open": sp.sqrt(5) > 2*sp.sqrt(1),
    "both_source_mass_parameters_positive": lam + p > 0 and lam - p > 0,
    "both_radial_hessians_stable": M_plus.det() == M_minus.det() == 5,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP695",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "symmetric minimal radial source with lambda_h=lambda_x=3/2, target vacuum norms one, and portal branches lambda_p=plus or minus one",
    "shared_two_point_record": "both branches have scalar mass-squared spectrum {1,5} and visible production overlap one half for each eigenstate",
    "source_generated_probe": "the heavy-to-two-light mass-eigenstate cubic, followed by visible decays through the nonzero Higgs overlaps",
    "contextual_partition": "the plus branch has cubic 7 sqrt(2)/2 while the minus branch has zero; the WP694 pair is separated",
    "kinematic_result": "mass squared values 5 and 1 satisfy m_heavy greater than two m_light, so the cubic is an on-shell decay discriminator",
    "classification": "source-derived visible branch separator and candidate instrument topology; it identifies the hostile pair but does not select which branch nature must realize",
    "smallest_exact_falsifier": "the minus branch predicts an exact absence of the heavy-to-two-light decay at tree level while retaining identical poles and visible overlaps",
    "remaining_physical_instrument_gate": "embed the radial witness in the complete flavor tensor source, include widths and loop corrections, and calibrate heavy-to-two-light visible final-state efficiency and backgrounds",
}
(ROOT / "results" / "wp695_visible_cubic_branch_separator.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
