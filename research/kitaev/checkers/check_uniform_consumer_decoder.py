import hashlib
import json
from pathlib import Path

import sympy as sp


n = sp.symbols("n", positive=True, integer=True)
e = 1 / n
R = sp.Matrix([[1, 0], [1, e]])
L = sp.eye(2)
Q = sp.simplify(R.T * R)
assert sp.simplify(R.det()) == e
assert sp.simplify(Q.det()) == e**2

lambda_min = sp.simplify((2 + e**2 - sp.sqrt(4 + e**4)) / 2)
lambda_min_rationalized = sp.simplify(
    2 * e**2 / (2 + e**2 + sp.sqrt(4 + e**4))
)
assert sp.simplify(lambda_min - lambda_min_rationalized) == 0
assert sp.limit(n**2 * lambda_min_rationalized, n, sp.oo) == sp.Rational(1, 2)
assert sp.limit(1 / (n**2 * lambda_min_rationalized), n, sp.oo) == 2

v = sp.Matrix([0, 1])
assert L * v == v
assert R * v == sp.Matrix([0, e])

seam = sp.Matrix([[0, 1]])
Q_full = sp.simplify(Q + seam.T * seam)
shifted = sp.simplify(Q_full - sp.eye(2) / 2)
assert shifted[0, 0] == sp.Rational(3, 2)
assert sp.simplify(shifted.det()) == sp.Rational(3, 4) + e**2 / 2

payload = {
    "status": "pass",
    "theorem": "uniform_consumer_compilation_needs_a_bounded_decoder",
    "finite_kernel": "zero for every N",
    "approximate_hidden_state": [0, 1],
    "observation_norm_on_hidden_state": "1/N",
    "consumer_norm_on_hidden_state": "1",
    "lambda_min_asymptotic": "1/(2*N^2)",
    "sharp_decoder_constant_squared_asymptotic": "2*N^2",
    "repair_row": [0, 1],
    "augmented_uniform_lower_bound": "1/2",
    "augmented_decoder_bound": "sqrt(2)",
    "source_authority_required_for_repair": True,
    "theta_application_frozen": True,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "uniform-consumer-decoder.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
