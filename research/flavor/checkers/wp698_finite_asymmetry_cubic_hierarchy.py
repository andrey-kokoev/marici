"""Exact nonasymptotic cubic hierarchy in mass-basis coordinates."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
t, lam, p, v = sp.symbols("t lambda p v", positive=True)

# Heavy eigenvector components (a,b), with t=b/a.  The quartic asymmetry is
# delta/p=(1-t^2)/(2t), and R=sqrt(p^2+delta^2).
a = 1/sp.sqrt(1+t**2)
b = t/sp.sqrt(1+t**2)
delta = p*(1-t**2)/(2*t)
R = sp.factor(p*(1+t**2)/(2*t))

common = sp.factor(v*(6*lam*t-p*(t**2+1))/(t**2+1)**sp.Rational(3, 2))
gplus = sp.factor((t+1)*common)
gminus = sp.factor((t-1)*common)
ratio = sp.factor(gminus/gplus)
rate_ratio = sp.factor(ratio**2)

mL2 = 2*v**2*(lam-R)
mH2 = 2*v**2*(lam+R)
phase_numerator = sp.factor(mH2-4*mL2)

checks = {
    "mass_basis_asymmetry_identity": sp.simplify(p**2+delta**2-R**2) == 0,
    "amplitude_ratio_exact": ratio == (t-1)/(t+1),
    "rate_ratio_exact": rate_ratio == (t-1)**2/(t+1)**2,
    "symmetric_limit_recovers_zero": ratio.subs(t, 1) == 0,
    "finite_asymmetry_witness_strict_hierarchy": rate_ratio.subs(t, 2) == sp.Rational(1, 9),
    "stability_makes_common_factor_positive": sp.simplify((6*lam*t-p*(t**2+1)).subs(lam, R)) == 2*p*(t**2+1),
    "open_decay_boundary": sp.simplify(phase_numerator-2*v**2*(-3*lam+5*R)) == 0,
    "stable_open_witness": mL2.subs({lam: sp.Rational(3, 2), p: 1, v: 1, t: 1}) == 1 and phase_numerator.subs({lam: sp.Rational(3, 2), p: 1, v: 1, t: 1}) == 1,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP698",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "equal-vacuum radial source with arbitrary finite quartic asymmetry encoded by positive mass-basis ratio t and portal magnitude p",
    "stable_open_decay_domain": "3 lambda/5 < R < lambda, with R=p(t^2+1)/(2t)",
    "exact_amplitude_ratio": "g_HLL minus/g_HLL plus=(t-1)/(t+1)",
    "exact_rate_ratio": "Gamma minus/Gamma plus=((t-1)/(t+1))^2 when common masses and phase space are used",
    "nonvanishing_result": "strict stability makes the common cubic factor positive, so neither branch loses all cubic sensitivity inside the domain except the symmetry-protected minus zero at t=1",
    "classification": "nonasymptotic source-derived rate hierarchy over the full finite-asymmetry radial domain; identifier, not selector",
    "smallest_exact_falsifier": "the hierarchy loses strictness only in the singular orientation limits t->0 or t->infinity; phase space closes at R=3lambda/5 and stability closes at R=lambda",
    "remaining_physical_instrument_gate": "embed t and R covariantly in the full flavor source and propagate finite widths, loops, detector efficiencies, backgrounds, and uncertainty into a lower bound on the measured rate contrast",
}
(ROOT / "results" / "wp698_finite_asymmetry_cubic_hierarchy.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
