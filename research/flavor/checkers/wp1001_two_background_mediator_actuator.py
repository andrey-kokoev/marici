import json
from pathlib import Path

import sympy as sp

a, c, ka, ks = sp.symbols("a c ka ks", positive=True)
j = sp.Matrix([[-ka / a, 0], [-6 * ka / a, -ks / c]])
det_j = sp.factor(j.det())

assert det_j == ka * ks / (a * c)
assert j.subs({a: 1, c: 1, ka: 1, ks: 1}).rank() == 2

# Exact deletion tests.
assert j.subs(ka, 0).rank() == 1
assert j.subs(ks, 0).rank() == 1
assert j.subs({ka: 0, ks: 0}).rank() == 0

# Deliberate-failure test: a duplicated first port is not an independent
# actuator even though two command labels are present.
duplicated = sp.Matrix([[-1, -1], [-6, -6]])
assert duplicated.rank() == 1

result = {
    "schema": "marici.flavor.wp1001.v1",
    "status": "PASS",
    "source_extension": ["phi_A tr(A^2)", "phi_s s^2"],
    "log_response_matrix": [["-kappa_A/a", 0], ["-6*kappa_A/a", "-kappa_s/c"]],
    "determinant": "kappa_A*kappa_s/(a*c)",
    "rank_two_condition": "a,c>0 and kappa_A*kappa_s != 0",
    "deletion_tests": {"kappa_A=0": "rank 1", "kappa_s=0": "rank 1", "both=0": "rank 0"},
    "classification": "candidate source-derived actuator; neither selector nor rigidifier",
    "physical_instrument": "withheld pending calibration, reset, widths, stability, cost, and uncertainty",
}

out = Path(__file__).parents[1] / "results" / "wp1001_two_background_mediator_actuator.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("WP1001 PASS: two singlet background ports generate an exact rank-two coefficient response")

