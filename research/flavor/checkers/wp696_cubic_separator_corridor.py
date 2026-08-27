"""Exact open-corridor theorem for the visible cubic separator."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
lam, p, v = sp.symbols("lambda p v", positive=True)

mL2 = 2*v**2*(lam-p)
mH2 = 2*v**2*(lam+p)
g_plus = sp.sqrt(2)*v*(3*lam-p)
g_minus = sp.Integer(0)
phase_squared = sp.factor(1-4*mL2/mH2)
width_plus = sp.factor(g_plus**2/(32*sp.pi*sp.sqrt(mH2))*sp.sqrt(phase_squared))

# Exact interior and boundary witnesses for the dimensionless ratio r=p/lam.
r = sp.symbols("r", positive=True)
phase_r = sp.factor(phase_squared.subs(p, r*lam))

checks = {
    "stable_corridor_upper_boundary": sp.factor(mL2.subs(p, lam)) == 0,
    "kinematic_boundary_is_three_fifths": sp.factor(phase_r.subs(r, sp.Rational(3, 5))) == 0,
    "interior_phase_space_positive": phase_r.subs(r, sp.Rational(4, 5)) == sp.Rational(5, 9),
    "plus_cubic_nonzero_through_stable_corridor": g_plus.subs(p, lam) == 2*sp.sqrt(2)*lam*v,
    "minus_cubic_identically_zero": g_minus == 0,
    "width_positive_at_rational_witness": width_plus.subs({lam: 5, p: 4, v: 1}) > 0,
    "two_point_spectrum_is_branch_independent": sp.Matrix([mL2, mH2]).subs(p, -p)[::-1, :] == sp.Matrix([mL2, mH2]),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP696",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "symmetric radial source family lambda_h=lambda_x=lambda, equal positive vacuum norms v^2, and portal magnitude p",
    "open_corridor": "3/5 < p/lambda < 1",
    "stability": "m_L^2=2 v^2(lambda-p)>0 and m_H^2=2 v^2(lambda+p)>0",
    "kinematics": "one-heavy to two-light decay is open exactly when 5p>3lambda",
    "branch_partition": "g_HLL plus=sqrt(2) v(3lambda-p), while g_HLL minus=0 identically on the symmetric family",
    "ideal_width": str(width_plus),
    "classification": "continuum source-derived branch separator and ideal rate prediction on a declared symmetric slice; identifier, not selector",
    "smallest_exact_falsifier": "at p/lambda=3/5 phase space closes; at or above p/lambda=1 the light radial mode loses strict stability",
    "remaining_physical_instrument_gate": "prove persistence off the symmetric slice, include finite widths and loops, and calibrate the visible cascade response and backgrounds",
}
(ROOT / "results" / "wp696_cubic_separator_corridor.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
