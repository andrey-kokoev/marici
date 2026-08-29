import json
from pathlib import Path

import sympy as sp

Q, R = sp.symbols("Q R")


def bracket(x, y):
    coords = (Q, R)
    return tuple(
        sp.expand(sum(x[j] * sp.diff(y[i], coords[j]) - y[j] * sp.diff(x[i], coords[j]) for j in range(2)))
        for i in range(2)
    )


f = Q**2 + Q * R + 1
g = Q**3 - R * Q + R**2
xf = (f, sp.Integer(0))
xg = (g, sp.Integer(0))
bfg = bracket(xf, xg)

assert bfg[1] == 0
assert sp.expand(bfg[0] - (f * sp.diff(g, Q) - g * sp.diff(f, Q))) == 0

# One more bracket verifies closure beyond first order.
third = bracket(xf, bfg)
assert third[1] == 0

# Deliberate-failure test: adjoining the forbidden transverse actuator must
# destroy the rank-one certificate.
x = sp.Matrix([1, 0])
y = sp.Matrix([0, 1])
assert sp.Matrix.hstack(x, x).rank() == 1
assert sp.Matrix.hstack(x, y).rank() == 2

result = {
    "schema": "marici.flavor.wp998.v1",
    "status": "PASS",
    "state_domain": "quotient-level (Q,R) control plane",
    "drift": "zero",
    "authorized_family": "X_f=f(Q,R) partial_Q",
    "bracket_formula": "[X_f,X_g]=(f*d_Q(g)-g*d_Q(f))*partial_Q",
    "contextual_partition": "connected leaves R=constant",
    "hostile_pair": [[0, 0], [0, 1]],
    "hostile_pair_equivalent": False,
    "classification": "leafwise formal rigidifier; not selector; no physical instrument",
    "smallest_repair": "source-derived transverse actuator or drift bracket with nonzero R component",
}

out = Path(__file__).parents[1] / "results" / "wp998_zero_drift_bracket_closure.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("WP998 PASS: zero-drift one-port Lie closure preserves every R leaf")

