"""Within-theory source-weight falsifier for connected-capacity preference."""

import json
from pathlib import Path
import sympy as sp


z = sp.symbols("z", real=True)  # z=cos(theta)^2 in [0,1]
y = (3 + z)/2                  # f2/g2=1
rate = sp.factor(1 + y**2)     # common Phi1^2 removed
capacity_support = sp.factor(y**2/(1 + y**2)**2)  # det rho_A

drate = sp.factor(sp.diff(rate, z))
dcap = sp.factor(sp.diff(capacity_support, z))

# On z in [0,1], y>1: rate derivative positive and capacity derivative negative.
assert drate.subs(z, 0) > 0 and drate.subs(z, 1) > 0
assert dcap.subs(z, 0) < 0 and dcap.subs(z, 1) < 0

z0, z1 = sp.Rational(0), sp.Rational(1, 4)
R0, R1 = sp.factor(rate.subs(z, z0)), sp.factor(rate.subs(z, z1))
C0, C1 = sp.factor(capacity_support.subs(z, z0)), sp.factor(capacity_support.subs(z, z1))
assert R1 > R0
assert C1 < C0

result = {
    "status": "PASS",
    "eft_ray": "f2/g2=1, g2>0",
    "angle_coordinate": "z=cos(theta)^2 in [0,1]",
    "helicity_ratio": str(y),
    "scaled_differential_source_weight": str(rate),
    "connected_capacity_support": str(capacity_support),
    "rate_derivative": str(drate),
    "capacity_derivative": str(dcap),
    "exact_comparison": {
        "z0": str(z0), "z1": str(z1),
        "rate_z0": str(R0), "rate_z1": str(R1),
        "capacity_z0": str(C0), "capacity_z1": str(C1),
    },
    "conclusion": (
        "Within one admitted dimension-eight photon EFT ray, angular source "
        "weight increases while connected helicity capacity decreases. The "
        "ordinary Born/rate weighting therefore does not implement monotone "
        "preference for larger connected capacity."
    ),
}
out = Path(__file__).parents[1] / "results" / "photon_capacity_preference_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
