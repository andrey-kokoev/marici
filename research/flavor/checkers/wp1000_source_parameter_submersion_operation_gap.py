import json
from pathlib import Path

import sympy as sp

a, c, mu, gamma, q_target, k_target = sp.symbols(
    "a c mu gamma q_target k_target", positive=True
)
q = mu**2 / (2 * a)
k = gamma**2 * mu**6 / (2 * c * a**6)

# Logarithmic response: variable*d/dvariable of each log response.
jlog = sp.Matrix(
    [
        [sp.simplify(a * sp.diff(q, a) / q), sp.simplify(c * sp.diff(q, c) / q)],
        [sp.simplify(a * sp.diff(k, a) / k), sp.simplify(c * sp.diff(k, c) / k)],
    ]
)
assert jlog == sp.Matrix([[-1, 0], [-6, -1]])
assert jlog.det() == 1

a_inv = mu**2 / (2 * q_target)
c_inv = 32 * gamma**2 * q_target**6 / (mu**6 * k_target)
assert sp.simplify(q.subs(a, a_inv) - q_target) == 0
assert sp.simplify(k.subs({a: a_inv, c: c_inv}) - k_target) == 0

# Deliberate-failure test: freezing c collapses the two-input response to one
# source direction even though the full source map has rank two.
assert jlog[:, 0].rank() == 1
assert jlog.rank() == 2

result = {
    "schema": "marici.flavor.wp1000.v1",
    "status": "PASS",
    "source_coordinates": ["log(m_A^2)", "log(m_s^2)"],
    "effective_coordinates": ["log(q)", "log(k)"],
    "log_response_matrix": [[-1, 0], [-6, -1]],
    "determinant": 1,
    "positive_image": "full positive (q,k) quadrant at leading elimination",
    "classification": "algebraically complete constructor; neither selector nor rigidifier",
    "first_nonfaithful_arrow": "source-parameter choice -> repeatable within-experiment intervention",
    "physical_instrument": "absent",
}

out = Path(__file__).parents[1] / "results" / "wp1000_source_parameter_submersion_operation_gap.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("WP1000 PASS: mediator source map has rank two, but parameter variation is not an actuator")

