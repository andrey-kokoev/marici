"""Exact kinetic-normalization descent test for the WP664 stability gate."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
s, Z, y, lam = sp.symbols("s Z y lam", positive=True)
Zp = Z/s**2
yp = y/s
lamp = lam/s**4
canonical_y4 = y**4/Z**2
canonical_lam = lam/Z**2

Zn, Zm, ln, lm, lx = sp.symbols("Zn Zm ln lm lx", positive=True)
sn, sm = sp.symbols("sn sm", positive=True)
Dhat = (4*ln*lm-lx**2)/(Zn**2*Zm**2)
Dhat_prime = sp.simplify(Dhat.subs({
    Zn: Zn/sn**2, Zm: Zm/sm**2,
    ln: ln/sn**4, lm: lm/sm**4, lx: lx/(sn**2*sm**2),
}, simultaneous=True))

checks = {
    "canonical_yukawa_strength_descends": sp.simplify(yp**4/Zp**2-canonical_y4) == 0,
    "canonical_quartic_descends": sp.simplify(lamp/Zp**2-canonical_lam) == 0,
    "canonical_radial_margin_descends": sp.simplify(Dhat_prime-Dhat) == 0,
    "raw_yukawa_fourth_power_does_not_descend": sp.simplify(yp**4-y**4) != 0,
    "hostile_raw_pair_same_canonical_strength": sp.Rational(1)**4/sp.Rational(1)**2 == sp.Rational(2)**4/sp.Rational(4)**2,
    "hostile_raw_pair_different_raw_strength": sp.Rational(1)**4 != sp.Rational(2)**4,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP666", "status": "PASS", "checks": checks,
    "field_redefinition": "n'=s n gives Z'=Z/s^2, y'=y/s, lambda'=lambda/s^4",
    "descending_strength": "y^4/Z^2",
    "descending_radial_margin": "(4lambda_n lambda_m-lambda_x^2)/(Z_n^2 Z_m^2)",
    "hostile_pair": [{"Z": "1", "y": "1"}, {"Z": "4", "y": "2"}],
    "classification": "WP664's numerical bound is physical only after canonical kinetic normalization or invariant replacement F=sum d y^4/Z^2",
    "smallest_exact_falsifier": "the hostile pair has raw y^4 values 1 and 16 but identical canonical strength 1",
    "remaining_gate": "derive the kinetic Gram and canonical threshold matching from the source model before evaluating the finite-scale RG gate",
}
(ROOT / "results" / "wp666_kinetic_normalization_descent.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
