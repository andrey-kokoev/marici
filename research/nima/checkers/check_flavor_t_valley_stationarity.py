"""Test whether the observed CKM ratio agrees with the t-purity stationary point."""

import contextlib
import importlib.util
import io
import json
import math
from pathlib import Path

base_path = Path(__file__).with_name("check_flavor_purity_hierarchy_split.py")
spec = importlib.util.spec_from_file_location("purity_split", base_path)
module = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    try:
        spec.loader.exec_module(module)
    except SystemExit as exc:
        if exc.code:
            raise


def objective(r):
    return module.purity(r * 1e-4, 1e-4)["t"]


# Golden-section maximization on the already established single valley.
lo, hi = 0.04, 0.14
phi = (1 + math.sqrt(5)) / 2
c = hi - (hi - lo) / phi
d = lo + (hi - lo) / phi
for _ in range(80):
    if objective(c) > objective(d):
        hi, d = d, c
        c = hi - (hi - lo) / phi
    else:
        lo, c = c, d
        d = lo + (hi - lo) / phi
r_star = (lo + hi) / 2

vub, svub = 0.003763, 0.000088
vcb, svcb = 0.04189, 0.00081
r_obs = vub / vcb
sigma_r = r_obs * math.sqrt((svub / vub) ** 2 + (svcb / vcb) ** 2)
z = abs(r_obs - r_star) / sigma_r
h = 2e-4
curvature = (objective(r_star + h) - 2 * objective(r_star) + objective(r_star - h)) / h**2

checks = {
    "interior_stationary_point": 0.04 < r_star < 0.14,
    "negative_curvature": curvature < 0,
    "observed_ratio_within_one_sigma": z < 1,
    "maximum_remains_below_one": objective(r_star) < 0.999,
    "stationarity_numerically_resolved": abs(objective(r_star + h) - objective(r_star - h)) < 1e-7,
}
report = {
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "conditional_on": "OBS17 central values except independently propagated Vub,Vcb errors; strict ray evaluated at s23=1e-4",
    "r_star": r_star,
    "F_t_at_r_star": objective(r_star),
    "curvature": curvature,
    "r_observed": r_obs,
    "sigma_r": sigma_r,
    "displacement_sigma": z,
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(0 if all(checks.values()) else 1)
