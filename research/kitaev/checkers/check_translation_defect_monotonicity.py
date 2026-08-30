import hashlib
import json
from pathlib import Path

import sympy as sp


b = sp.symbols("b", real=True)
rotation = sp.Matrix([[sp.cos(b), -sp.sin(b)], [sp.sin(b), sp.cos(b)]])
f = sp.Matrix([1, 0])
displacement = rotation * f - f
D = sp.simplify((displacement.T * displacement)[0])
D_prime = sp.diff(D, b)
D_second = sp.diff(D, b, 2)

assert sp.simplify(D - (2 - 2 * sp.cos(b))) == 0
assert sp.simplify(D.subs(b, 0)) == 0
assert sp.simplify(D_prime.subs(b, 0)) == 0
assert sp.simplify(D_second.subs(b, 0)) == 2
assert sp.simplify(D_prime - 2 * sp.sin(b)) == 0
assert D_prime.subs(b, sp.pi / 2) == 2
assert D_prime.subs(b, 3 * sp.pi / 2) == -2
assert D.subs(b, 2 * sp.pi) == 0

# Generic differentiable curve x(b)=b*v+O(b^2) has squared norm curvature 2||v||^2.
v1, v2 = sp.symbols("v1 v2", real=True)
linear_displacement = b * sp.Matrix([v1, v2])
generic_defect = sp.expand((linear_displacement.T * linear_displacement)[0])
assert sp.simplify(
    sp.diff(generic_defect, b, 2).subs(b, 0) - 2 * (v1**2 + v2**2)
) == 0

payload = {
    "status": "pass",
    "theorem": "positive_curvature_of_squared_translation_defect_does_not_imply_tilt_monotonicity",
    "defect": "2-2*cos(b)",
    "even": True,
    "nonnegative": True,
    "curvature_at_zero": "2",
    "derivative": "2*sin(b)",
    "derivative_at_pi_over_two": "2",
    "derivative_at_three_pi_over_two": "-2",
    "returns_to_zero_at_two_pi": True,
    "positive_curvature_implies_global_monotonicity": False,
    "generic_squared_defect_curvature": "2*norm(T'_0 f)^2",
    "required_global_capability": "source-derived spectral no-wrap or nonunitary semigroup theorem",
    "theta_tilt_identified_as_unitary": False,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "translation-defect-monotonicity.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
