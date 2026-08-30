#!/usr/bin/env python3
"""Exact linearized-GR gauge-descent check for the Machian localization lane."""

import hashlib
import json
from pathlib import Path
import sympy as sp

x = sp.symbols("t x y z")
n = 4

# A generic-enough polynomial perturbation and cubic gauge parameter.
h = [[sp.expand((mu + 1) * (nu + 2) * x[(mu + nu) % n] ** 2
                + (mu + nu + 1) * x[mu] * x[nu])
      for nu in range(n)] for mu in range(n)]
h = [[sp.expand((h[mu][nu] + h[nu][mu]) / 2) for nu in range(n)] for mu in range(n)]
xi = [
    x[mu] ** 3 + (mu + 2) * x[(mu + 1) % n] * x[(mu + 2) % n] ** 2
    for mu in range(n)
]

delta_h = [
    [sp.diff(xi[nu], x[mu]) + sp.diff(xi[mu], x[nu]) for nu in range(n)]
    for mu in range(n)
]
hp = [[sp.expand(h[mu][nu] + delta_h[mu][nu]) for nu in range(n)] for mu in range(n)]


def riemann(metric_perturbation, mu, nu, rho, sig):
    return sp.expand(sp.Rational(1, 2) * (
        sp.diff(metric_perturbation[mu][sig], x[rho], x[nu])
        + sp.diff(metric_perturbation[nu][rho], x[sig], x[mu])
        - sp.diff(metric_perturbation[mu][rho], x[sig], x[nu])
        - sp.diff(metric_perturbation[nu][sig], x[rho], x[mu])
    ))


checked = 0
nonzero = 0
electric = []
for mu in range(n):
    for nu in range(n):
        for rho in range(n):
            for sig in range(n):
                r = riemann(h, mu, nu, rho, sig)
                rp = riemann(hp, mu, nu, rho, sig)
                assert sp.expand(rp - r) == 0
                checked += 1
                nonzero += int(r != 0)

for i in range(1, n):
    electric.append([str(riemann(h, 0, i, 0, j)) for j in range(1, n)])

assert nonzero > 0
assert any(value != "0" for row in electric for value in row)

packet = {
    "schema": "marici.machian-linearized-gauge-descent.v1",
    "status": "pass",
    "claims": {
        "gauge_descent": "R^(1)[h+d xi+d xi] = R^(1)[h] for all 256 tested indexed components",
        "local_readout": "E_ij=R^(1)_0i0j is a nonzero gauge-invariant local tidal record",
        "scope": "codomain/descent test only; the source-to-h retarded Einstein map remains unconstructed",
    },
    "components_checked": checked,
    "nonzero_components": nonzero,
    "electric_tidal_block": electric,
}
canonical = json.dumps(packet, indent=2, sort_keys=True) + "\n"
packet["sha256_without_digest"] = hashlib.sha256(canonical.encode()).hexdigest()
out = Path(__file__).resolve().parents[1] / "results" / "machian-linearized-gauge-descent.json"
out.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"passed": True, "components": checked, "output": str(out)}))
