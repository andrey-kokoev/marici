import hashlib
import json
from pathlib import Path

import sympy as sp


N = sp.symbols("N", integer=True, positive=True)
k = sp.symbols("k", integer=True, positive=True)

harmonic_partial = sp.summation(1 / k, (k, 1, N))
assert harmonic_partial == sp.harmonic(N)
assert sp.limit(harmonic_partial, N, sp.oo) == sp.oo
assert sp.limit(1 / N, N, sp.oo) == 0

alternating_limit = sp.summation((-1) ** (k + 1) / k, (k, 1, sp.oo))
assert alternating_limit == sp.log(2)

# Exact finite affine recurrence for paired exchange mismatches.
x0 = sp.symbols("x0", real=True)
position = x0
harmonic_positions = []
for index in range(1, 9):
    position = sp.simplify(position + sp.Rational(1, index))
    harmonic_positions.append(position)
assert harmonic_positions[-1] == x0 + sp.Rational(761, 280)

position = x0
alternating_positions = []
for index in range(1, 9):
    position = sp.simplify(position + (-1) ** (index + 1) * sp.Rational(1, index))
    alternating_positions.append(position)
assert all(abs(float(value.subs(x0, 0))) <= 1 for value in alternating_positions)

payload = {
    "status": "pass",
    "theorem": "vanishing_exchange_center_errors_can_accumulate_into_unbounded_gain_drift",
    "paired_recurrence": "x_N=x_0+sum_{k<=N} delta_k",
    "bounded_orbit_condition": "uniformly bounded partial sums",
    "limiting_frame_condition": "convergence of sum delta_k",
    "robust_sufficient_condition": "absolute summability",
    "hostile_errors": "delta_k=1/k -> 0",
    "hostile_drift": "H_N -> infinity",
    "conditional_repair": "delta_k=(-1)^(k+1)/k -> log(2)",
    "finite_harmonic_drift_N8": "761/280",
    "multiplicative_error_budget": "exp(-E)M_0 <= M_N <= exp(E)M_0",
    "theta_center_errors_computed": False,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "exchange-center-error-accumulation.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
