"""Regression of regular eta-jet reconstruction of Stieltjes constants."""
import json
import math
from pathlib import Path

L = math.log(2)
g0, g1, g2, g3 = (0.5772156649015328606, -0.0728158454836767249,
                  -0.00969036319287231848, 0.0020538344203033459)
c0 = L
c1 = L*g0 - L**2/2
c2 = -L*g1 - L**2*g0/2 + L**3/6
c3 = L*g2/2 + L**2*g1/2 + L**3*g0/6 - L**4/24
c4 = -L*g3/6 - L**2*g2/4 - L**3*g1/6 - L**4*g0/24 + L**5/120
r0 = (c1 + L**2/2)/L
r1 = -(c2 + L**2*r0/2 - L**3/6)/L
r2 = 2*(c3 - L**2*r1/2 - L**3*r0/6 + L**4/24)/L
r3 = -6*(c4 + L**2*r2/4 + L**3*r1/6 + L**4*r0/24 - L**5/120)/L
residuals = [r0-g0, r1-g1, r2-g2, r3-g3]
assert max(map(abs, residuals)) < 2e-16
result = {
    "eta_derivatives_at_one": [c0, c1, 2*c2, 6*c3, 24*c4],
    "reconstructed_stieltjes_constants": [r0, r1, r2, r3],
    "roundtrip_residuals": residuals,
    "triangular_reconstruction_passed": True,
    "interval_certified": False,
    "zero_locations_used": False,
}
if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "eta-jet-stieltjes-reconstruction.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
