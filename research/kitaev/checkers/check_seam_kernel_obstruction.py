import hashlib
import json
from pathlib import Path

import sympy as sp


z = sp.symbols("z")
F_plus = sp.expand((z - sp.I) * (z - 2 * sp.I))
F_minus = sp.expand((z + sp.I) * (z + 2 * sp.I))
F_sum = sp.expand(F_plus + F_minus)

roots_plus = sp.solve(F_plus, z)
roots_minus = sp.solve(F_minus, z)
roots_sum = sp.solve(F_sum, z)

assert F_plus == z**2 - 3 * sp.I * z - 2
assert F_minus == z**2 + 3 * sp.I * z - 2
assert F_sum == 2 * z**2 - 4
assert set(roots_plus) == {sp.I, 2 * sp.I}
assert set(roots_minus) == {-sp.I, -2 * sp.I}
assert set(roots_sum) == {-sp.sqrt(2), sp.sqrt(2)}
assert all(sp.re(root) == 0 for root in roots_plus + roots_minus)
assert all(sp.re(root) != 0 for root in roots_sum)

# Finite-dimensional PSD kernel closure: if Hv=Hw=0 then H(v+w)=0.
h11, h12, h22 = sp.symbols("h11 h12 h22")
H = sp.Matrix([[h11, h12], [sp.conjugate(h12), h22]])
v, w = sp.Matrix([1, 0]), sp.Matrix([0, 1])
assert sp.simplify(H * (v + w) - (H * v + H * w)) == sp.zeros(2, 1)

payload = {
    "status": "pass",
    "theorem": "seam_confinement_cannot_be_the_kernel_of_an_additive_quadratic_energy",
    "first_seam_polynomial": str(F_plus),
    "second_seam_polynomial": str(F_minus),
    "sum_polynomial": str(F_sum),
    "sum_roots": ["-sqrt(2)", "sqrt(2)"],
    "seam_confined_class_linear": False,
    "psd_quadratic_kernel_linear": True,
    "kernel_can_equal_full_seam_class": False,
    "surviving_role": "linear source defect plus separate spectral implication, or quadratic energy after source-derived nonlinear lift",
    "theta_admissibility_inferred": False,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "seam-kernel-obstruction.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
