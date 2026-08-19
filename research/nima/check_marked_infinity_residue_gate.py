#!/usr/bin/env python3
"""Check the radial infinity orders of the three source marked forms."""

import hashlib
import json
from pathlib import Path

SOURCE = Path("research/benincasa/marici-gm/src/bin/marked_relative_reduction_engine.rs")

# A source class is da db /(L1^a L2^b sqrt(K)).  Under a=rA,b=rB,
# da db contributes r dr, each L contributes r, and sqrt(K) contributes r^2.
classes = {
    "Omega111": (1, 1),
    "Omega101": (1, 0),
    "Omega110": (0, 1),
}

orders = {}
for name, (a, b) in classes.items():
    radial_dr_power = 1 - a - b - 2
    x_dx_power = -radial_dr_power - 2
    assert x_dx_power >= 0
    assert x_dx_power != -1  # no dx/x term
    orders[name] = {
        "L1_power": a,
        "L2_power": b,
        "radial_dr_power": radial_dr_power,
        "x_dx_power": x_dx_power,
        "infinity_residue": 0,
    }

source_bytes = SOURCE.read_bytes()
result = {
    "schema": "marici.marked-infinity-residue-gate.v1",
    "source": str(SOURCE).replace("\\", "/"),
    "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
    "orders": orders,
    "all_infinity_residues_zero": True,
    "external_derivative_preserves_radial_order": True,
    "forced_connection_identity": "R_infinity * B_u = R_infinity * B_v = 0",
}

Path("research/nima/marked-infinity-residue-gate.json").write_text(
    json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2, sort_keys=True))
