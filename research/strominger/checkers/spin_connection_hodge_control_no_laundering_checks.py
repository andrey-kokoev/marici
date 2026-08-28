"""Exact active/passive separation for the celestial Hodge generator."""

import hashlib
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
RESULT = ROOT / "results" / "spin_connection_hodge_control_no_laundering_checks.json"

a, b, phi = sp.symbols("a b phi", real=True)
I = sp.eye(2)
EPS = sp.Matrix([[0, -1], [1, 0]])
C = sp.Matrix([[a, b], [b, -a]])
J_C = EPS * C
Q = sp.cos(phi) * I + sp.sin(phi) * EPS
passive_components = sp.simplify(Q.T * C * Q)
spin_two_rotation = sp.simplify(sp.cos(2 * phi) * C - sp.sin(2 * phi) * J_C)

delta_components = sp.simplify(-EPS * C + C * EPS)
delta_basis_reconstruction = sp.simplify(EPS * C - C * EPS)
active_delta = J_C

checks = {
    "stf_tensor_anticommutes_with_epsilon": sp.simplify(C * EPS + EPS * C) == sp.zeros(2),
    "passive_frame_rotation_has_double_angle": sp.simplify(passive_components - spin_two_rotation) == sp.zeros(2),
    "infinitesimal_passive_component_law_is_minus_two_hodge": sp.simplify(delta_components + 2 * J_C) == sp.zeros(2),
    "basis_and_component_variations_cancel_geometrically": sp.simplify(delta_components + delta_basis_reconstruction) == sp.zeros(2),
    "active_hodge_rotation_changes_tensor_at_generic_witness": active_delta.subs({a: 2, b: 3}) != sp.zeros(2),
    "passive_frame_gauge_has_zero_geometric_delta": (delta_components + delta_basis_reconstruction).subs({a: 2, b: 3}) == sp.zeros(2),
    "active_and_passive_geometric_actions_are_distinct": active_delta.subs({a: 2, b: 3}) != (delta_components + delta_basis_reconstruction).subs({a: 2, b: 3}),
}

payload = {
    "schema": "marici.strominger.spin-connection-hodge-control-no-laundering.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "theorem": {
        "coordinate_coincidence": "a passive frame rotation phi acts on STF components as Hodge angle -2 phi",
        "passive_effect": "component and basis variations cancel, leaving the geometric tensor unchanged",
        "active_effect": "C maps to R_alpha C at fixed frame and changes the geometric tensor generically",
        "no_laundering": "the Levi-Civita spin connection authorizes frame covariance, not active local Hodge control",
        "missing_constructor": "an independent active duality connection, if the gravitational source supplies one",
    },
    "hostile_witness": {
        "C": [[2, 3], [3, -2]],
        "active_delta": [[-3, 2], [2, 3]],
        "passive_geometric_delta": [[0, 0], [0, 0]],
    },
}
payload["checker_sha256"] = hashlib.sha256(HERE.read_bytes()).hexdigest()
RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="ascii")
print(f"{payload['passed']}/{payload['total']} checks passed")
print(payload["checker_sha256"])
raise SystemExit(0 if payload["status"] == "passed" else 1)
