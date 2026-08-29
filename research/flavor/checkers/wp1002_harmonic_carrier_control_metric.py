import json
from pathlib import Path

import sympy as sp

j = sp.Matrix([[-1, 0], [-6, -1]])
g_epsilon = sp.eye(2)
g_z = sp.simplify(j.inv().T * g_epsilon * j.inv())

assert g_z == sp.Matrix([[37, -6], [-6, 1]])
assert g_z.det() == 1
assert g_z[0, 0] > 0 and g_z.det() > 0

# The pullback reproduces carrier cost for an exact hostile displacement.
dz = sp.Matrix([1, 0])
epsilon = j.inv() * dz
assert (epsilon.T * g_epsilon * epsilon)[0] == (dz.T * g_z * dz)[0] == 37

# Deliberate-failure test: the observer-side identity metric gives the wrong
# cost and therefore cannot inherit source authority.
assert (dz.T * sp.eye(2) * dz)[0] == 1
assert (dz.T * sp.eye(2) * dz)[0] != (dz.T * g_z * dz)[0]

result = {
    "schema": "marici.flavor.wp1002.v1",
    "status": "PASS",
    "carrier_potential": "sum_i (M_i^2 phi_i^2/2 - j_i phi_i)",
    "reset_attribute": "j_A=j_s=0 implies unique phi_A=phi_s=0",
    "unit_response_matrix": [[-1, 0], [-6, -1]],
    "unit_induced_coefficient_gram": [[37, -6], [-6, 1]],
    "gram_determinant": 1,
    "hostile_cost": {"delta_log_q_log_k": [1, 0], "source_cost_squared_twice": 37, "naive_euclidean": 1},
    "classification": "source-priced local actuator and carrier rigidifier; not flavor selector",
    "physical_instrument": "not experimentally calibrated",
}

out = Path(__file__).parents[1] / "results" / "wp1002_harmonic_carrier_control_metric.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("WP1002 PASS: harmonic carriers induce the exact positive coefficient-control metric")

