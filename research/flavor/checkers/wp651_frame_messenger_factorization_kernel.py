"""Exact WP651 messenger-factorization kernel for frame coefficients."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
n = 6
x = sp.symbols("x0:6", nonzero=True)
y = sp.symbols("y0:6", nonzero=True)
M = sp.symbols("M0:6", positive=True)
coefficients = sp.Matrix([-x[k]*y[k]/M[k] for k in range(n)])
jacobian = coefficients.jacobian(list(x)+list(y))
benchmark = {**{z: 1 for z in x}, **{z: 1 for z in y}, **{z: 1 for z in M}}
J0 = jacobian.subs(benchmark)

t = sp.symbols("t", nonzero=True)
hostile_a = {"x": sp.Integer(1), "y": sp.Integer(1), "M": sp.Integer(1)}
hostile_b = {"x": sp.Integer(2), "y": sp.Rational(1, 2), "M": sp.Integer(1)}
c_a = -hostile_a["x"]*hostile_a["y"]/hostile_a["M"]
c_b = -hostile_b["x"]*hostile_b["y"]/hostile_b["M"]

checks = {
    "six_coefficient_matching_jacobian_shape": J0.shape == (6, 12),
    "matching_jacobian_has_full_output_rank": J0.rank() == 6,
    "vertex_kernel_has_six_complex_dimensions": len(J0.nullspace()) == 6,
    "rescaling_is_exact_matching_symmetry": sp.simplify(-(t*x[0])*(y[0]/t)/M[0]-coefficients[0]) == 0,
    "hostile_uv_pair_has_same_low_energy_coefficient": c_a == c_b == -1,
    "hostile_uv_pair_has_different_left_vertex_strength": hostile_a["x"]**2 != hostile_b["x"]**2,
}
if not all(checks.values()):
    raise SystemExit(checks)
result = {
    "work_package": "WP651", "status": "PASS", "checks": checks,
    "matching": "c_k=-x_k y_k/M_k for six complex frame coefficients with frozen messenger masses",
    "contextual_partition": "twelve complex vertex couplings map with rank six to six complex coefficients; kernel dimension six complex",
    "hostile_uv_pair": {"A": "x=1,y=1,M=1", "B": "x=2,y=1/2,M=1", "common_c": -1, "left_strengths": [1, 4]},
    "classification": "executable low-energy matching carrier; neither coefficient selector nor UV source identifier",
    "smallest_exact_falsifier": "failure of x->tx, y->y/t to preserve the matched coefficient",
    "physical_instrument_gate": "threshold-sensitive calibrated observables must resolve vertex strengths, finite widths, mixing, decoupling, and detector resolution",
}
(ROOT / "results" / "wp651_frame_messenger_factorization_kernel.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
