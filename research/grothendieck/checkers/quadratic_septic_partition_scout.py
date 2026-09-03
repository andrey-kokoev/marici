"""High-precision scout for the quadratic normalization of septic windows."""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp

mp.mp.dps = 50
t = sp.symbols("t", real=True)
s = 35 * t**4 - 84 * t**5 + 70 * t**6 - 20 * t**7
d = sp.sqrt(s**2 + (1 - s) ** 2)
rho = sp.simplify(s / d)
rho_other = sp.simplify((1 - s) / d)
third = sp.diff(rho, t, 3)
num, _ = sp.together(third).as_numer_denom()
roots = []
for root in sp.nroots(num, maxsteps=200):
    if abs(complex(root).imag) < 1e-20:
        value = float(sp.re(root))
        if 1e-10 < value < 1 - 1e-10:
            roots.append(value)
roots = sorted(set(round(value, 14) for value in roots))
third_mp = sp.lambdify(t, third, "mpmath")
points = [mp.mpf("0")] + [mp.mpf(str(value)) for value in roots] + [mp.mpf("1")]
l1 = mp.mpf("0")
for left, right in zip(points, points[1:]):
    l1 += mp.quad(lambda x: abs(third_mp(x)), [left, right])
quadratic_budget_h1 = 2 * mp.pi * l1 / 3

result = {
    "schema": "marici.grothendieck.quadratic-septic-partition-scout.v1",
    "quadratic_identity_symbolic": sp.simplify(rho**2 + rho_other**2 - 1) == 0,
    "symmetry_symbolic": sp.simplify(rho_other - rho.subs(t, 1 - t)) == 0,
    "interior_third_derivative_roots": roots,
    "rho_third_derivative_l1": mp.nstr(l1, 25),
    "two_window_two_transition_budget_h_one": mp.nstr(quadratic_budget_h1, 25),
    "claim_boundary": "High-precision root finding and quadrature, not directed certification.",
}
assert result["quadratic_identity_symbolic"] and result["symmetry_symbolic"]
output = Path(__file__).parents[1] / "results" / "quadratic-septic-partition-scout.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
