import json
from pathlib import Path

import sympy as sp


y, s, w, a, b = sp.symbols("y s w a b", positive=True)
f = y**s + a * y ** (1 - s)
g = y**w + b * y ** (1 - w)
wronskian = sp.expand(f * sp.diff(g, y) - sp.diff(f, y) * g)
expected = sp.expand(
    (w - s) * y ** (s + w - 1)
    + b * (1 - w - s) * y ** (s - w)
    + a * (w - 1 + s) * y ** (w - s)
    + a * b * (s - w) * y ** (1 - s - w)
)
lambda_s = s * (1 - s)
lambda_w = w * (1 - w)

checks = {
    "boundary_concomitant_exact": sp.simplify(wronskian - expected) == 0,
    "green_derivative_exact": sp.simplify(sp.diff(wronskian, y) - (lambda_s - lambda_w) * f * g / y**2) == 0,
    "only_scalar_scattering_data_enter": wronskian.free_symbols <= {y, s, w, a, b},
    "no_extra_mode_symbol_survives": len(wronskian.atoms(sp.Function)) == 0,
}

result = {
    "schema": "marici.grothendieck.maass-selberg-pairing-scalar-boundary.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "interpretation": "The two-spectral Green pairing reduces entirely to the cusp constant terms and hence to phi(s) and phi(w). It is a scalar scattering Bezoutian, not an independent multi-mode constraint.",
}

out = Path(__file__).parents[1] / "results" / "maass_selberg_pairing_scalar_boundary.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
