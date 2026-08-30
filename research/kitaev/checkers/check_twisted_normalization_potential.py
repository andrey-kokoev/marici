import hashlib
import json
from pathlib import Path

import sympy as sp


def compose(second, first):
    ell2, eps2 = second
    ell1, eps1 = first
    return sp.simplify(ell2 + eps2 * ell1), eps2 * eps1


phi = [sp.Integer(1), sp.Integer(3), sp.Integer(-2)]
edge_01 = (phi[1] - phi[0], 1)
edge_12 = (phi[2] + phi[1], -1)
edge_20_even = (phi[0] + phi[2], -1)
edge_20_odd = (phi[0] - phi[2], 1)

assert edge_01 == (2, 1)
assert edge_12 == (1, -1)
assert edge_20_even == (-1, -1)
assert edge_20_odd == (3, 1)

even_loop = compose(edge_20_even, compose(edge_12, edge_01))
odd_loop = compose(edge_20_odd, compose(edge_12, edge_01))
assert even_loop == (0, 1)
assert odd_loop == (2, -1)
assert sp.Rational(odd_loop[0], 2) == phi[0]

# Spanning tree 01,12 predicts each chord exactly.
predicted_even_chord = phi[0] - edge_20_even[1] * phi[2]
predicted_odd_chord = phi[0] - edge_20_odd[1] * phi[2]
assert predicted_even_chord == edge_20_even[0]
assert predicted_odd_chord == edge_20_odd[0]

# A local chord perturbation is exactly the loop anomaly.
delta = sp.symbols("delta", real=True)
perturbed_even = (edge_20_even[0] + delta, edge_20_even[1])
perturbed_loop = compose(perturbed_even, compose(edge_12, edge_01))
assert perturbed_loop == (delta, 1)

payload = {
    "status": "pass",
    "theorem": "single_twisted_normalization_potential_exists_exactly_when_all_chord_residuals_vanish",
    "edge_potential_law": "ell_e=phi_target-epsilon_e*phi_source",
    "even_loop_condition": "ell_C=0",
    "odd_loop_condition": "ell_C=2*phi_base",
    "spanning_tree_vertices": ["0", "1", "2"],
    "vertex_potential": ["1", "3", "-2"],
    "even_triangle_holonomy": {"ell": "0", "epsilon": 1},
    "odd_triangle_holonomy": {"ell": "2", "epsilon": -1, "center": "1"},
    "chord_perturbation_anomaly": "delta",
    "one_residual_per_independent_cycle": True,
    "theta_source_potential_derived": False,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "twisted-normalization-potential.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
