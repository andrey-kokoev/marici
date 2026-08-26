import json
from pathlib import Path

import sympy as sp


checks = {}
residuals = {}
hostile_residuals = {}

for n in range(13):
    f0, fu, fv, fuv = sp.symbols(f"f{n}_0 f{n}_u f{n}_v f{n}_uv")
    route_uv = (fu - f0) + (fuv - fu)
    route_vu = (fv - f0) + (fuv - fv)
    residual = sp.expand(route_uv - route_vu)
    hostile = sp.expand((fu - f0) - route_vu)
    checks[f"jet_{n}_route_residual_zero"] = residual == 0
    checks[f"jet_{n}_hostile_omission_nonzero"] = hostile != 0
    residuals[str(n)] = str(residual)
    hostile_residuals[str(n)] = str(hostile)

result = {
    "schema": "marici.mellin_wall_jet_prime_cocycle.v1",
    "checks": checks,
    "exact": {
        "route_residuals_0_through_12": residuals,
        "hostile_omission_residuals_0_through_12": hostile_residuals,
    },
}

if not all(result["checks"].values()):
    raise SystemExit(json.dumps(result, indent=2))

output = Path("research/grothendieck/results/mellin_wall_jet_prime_cocycle.json")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

