"""Exact chain-rule obstruction and Hodge-connection repair audit."""

import hashlib
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
RESULT = ROOT / "results" / "local_hodge_selector_connection_checks.json"

c, s, da, connection = sp.symbols("c s da connection", real=True)
x1, x2, dx1, dx2 = sp.symbols("x1 x2 dx1 dx2", real=True)
I = sp.eye(2)
J = sp.Matrix([[0, -1], [1, 0]])
R = c * I + s * J
field = sp.Matrix([x1, x2])
dfield = sp.Matrix([dx1, dx2])
dR = da * (-s * I + c * J)

ordinary_transformed_derivative = dR * field + R * dfield
expected_covariant_part = R * dfield
selector_current = sp.simplify(ordinary_transformed_derivative - expected_covariant_part)
universal_current = sp.simplify(da * J * R * field)

shifted_connection = connection - da
gauged_transformed = sp.simplify(
    ordinary_transformed_derivative + shifted_connection * J * R * field
)
gauged_expected = sp.simplify(R * (dfield + connection * J * field))

witness = {c: 1, s: 0, da: 2, x1: 3, x2: 5, dx1: 7, dx2: 11}
witness_current = selector_current.subs(witness)

checks = {
    "hodge_rotation_commutes_with_generator": sp.simplify(R * J - J * R) == sp.zeros(2),
    "rotation_derivative_is_da_times_JR": sp.simplify(dR - da * J * R) == sp.zeros(2),
    "local_selector_chain_rule_has_universal_current": selector_current == universal_current,
    "constant_selector_has_zero_current": selector_current.subs(da, 0) == sp.zeros(2, 1),
    "nonconstant_selector_hostile_current_is_nonzero": witness_current != sp.zeros(2, 1),
    "connection_shift_cancels_selector_current": sp.simplify(gauged_transformed - gauged_expected) == sp.zeros(2, 1),
    "wrong_connection_sign_fails": sp.simplify(
        ordinary_transformed_derivative + (connection + da) * J * R * field - gauged_expected
    ) != sp.zeros(2, 1),
}

payload = {
    "schema": "marici.strominger.local-hodge-selector-connection.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "selector_current": [str(x) for x in selector_current],
    "hostile_witness_current": [str(x) for x in witness_current],
    "repair": {
        "constructor": "Hodge U(1) connection A",
        "covariant_derivative": "D_A = d + A J",
        "local_rotation": "C maps to R_alpha C",
        "connection_law": "A maps to A - d alpha",
        "authority_boundary": "the algebra determines the required type and law but does not construct a gravitational source for A",
    },
}
payload["checker_sha256"] = hashlib.sha256(HERE.read_bytes()).hexdigest()
RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="ascii")
print(f"{payload['passed']}/{payload['total']} checks passed")
print(payload["checker_sha256"])
raise SystemExit(0 if payload["status"] == "passed" else 1)
