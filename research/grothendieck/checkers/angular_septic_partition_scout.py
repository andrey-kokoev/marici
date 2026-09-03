"""Scout an angular quadratic partition built from the septic transition."""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp

mp.mp.dps = 50
t = sp.symbols("t", real=True)
s = 35 * t**4 - 84 * t**5 + 70 * t**6 - 20 * t**7
rho = sp.sin(sp.pi * s / 2)
rho_other = sp.cos(sp.pi * s / 2)
third = sp.diff(rho, t, 3)
third_mp = sp.lambdify(t, third, "mpmath")

roots = []
segments = 2000
last_x = mp.mpf("0")
last_y = third_mp(last_x)
for index in range(1, segments + 1):
    x = mp.mpf(index) / segments
    y = third_mp(x)
    if y == 0 or last_y * y < 0:
        try:
            root = mp.findroot(third_mp, (last_x, x))
            if mp.mpf("1e-12") < root < 1 - mp.mpf("1e-12"):
                if all(abs(root - old) > mp.mpf("1e-10") for old in roots):
                    roots.append(root)
        except (ValueError, ZeroDivisionError):
            pass
    last_x, last_y = x, y
roots.sort()
points = [mp.mpf("0"), *roots, mp.mpf("1")]
l1 = sum(mp.quad(lambda x: abs(third_mp(x)), [a, b]) for a, b in zip(points, points[1:]))
budget = 2 * mp.pi * l1 / 3
normalized_angular_budget = budget / mp.pi**2

result = {
    "schema": "marici.grothendieck.angular-septic-partition-scout.v1",
    "quadratic_identity_symbolic": sp.trigsimp(rho**2 + rho_other**2 - 1) == 0,
    "interior_third_derivative_roots": [mp.nstr(root, 18) for root in roots],
    "rho_third_derivative_l1": mp.nstr(l1, 25),
    "two_window_two_transition_budget_h_one": mp.nstr(budget, 25),
    "normalized_cover_budget_h_theta_pi": mp.nstr(normalized_angular_budget, 25),
    "claim_boundary": "High-precision scan/root finding and quadrature, not directed certification.",
}
assert result["quadratic_identity_symbolic"]
output = Path(__file__).parents[1] / "results" / "angular-septic-partition-scout.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
