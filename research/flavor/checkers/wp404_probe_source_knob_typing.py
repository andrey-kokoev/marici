"""Exact checker for WP404 probe-context versus source-knob typing."""

import json
from pathlib import Path

import sympy as sp


M2, J0, J1, c, omega, luminosity = sp.symbols(
    "M2 J0 J1 c omega luminosity", nonzero=True, real=True
)
theta = sp.Matrix([M2, J0, J1])
H = M2 + c
N = J0 + J1 * c
A_static = sp.cancel(N / H)
A_dynamic = sp.cancel(N / (H - omega**2))

probe_source_jacobian = theta.jacobian([omega, luminosity])
source_knob_tangent = sp.Matrix([H, N]).jacobian([c])
joint_error_jacobian = sp.Matrix(
    [
        [sp.diff(H, M2), sp.diff(H, J0)],
        [sp.diff(A_static, M2), sp.diff(A_static, J0)],
    ]
)
joint_det = sp.factor(joint_error_jacobian.det())
displacement_error_jacobian = sp.Matrix(
    [[sp.diff(A_static, M2), sp.diff(A_static, J0)]]
)

benchmark = {M2: sp.Integer(3), J0: sp.Integer(2), J1: sp.Integer(1), c: sp.Integer(1)}
source_tangent_benchmark = source_knob_tangent.subs(benchmark)
dynamic_probe_derivative = sp.factor(sp.diff(A_dynamic, omega))
dynamic_probe_derivative_benchmark = dynamic_probe_derivative.subs(
    benchmark | {omega: sp.Integer(1)}
)

checks = {
    "probe_scan_changes_dynamic_readout": dynamic_probe_derivative_benchmark != 0,
    "probe_scan_source_jacobian_zero": probe_source_jacobian == sp.zeros(3, 2),
    "source_knob_changes_curvature": source_tangent_benchmark[0] != 0,
    "source_knob_changes_tadpole": source_tangent_benchmark[1] != 0,
    "joint_readout_error_rank_two": joint_error_jacobian.rank() == 2,
    "joint_readout_determinant_nonzero": joint_det != 0,
    "displacement_only_error_rank_one": displacement_error_jacobian.rank() == 1,
    "one_source_knob_has_one_dimensional_tangent": source_knob_tangent.rank() == 1,
}

result = {
    "work_package": "WP404",
    "title": "Probe-context versus source-knob typing",
    "affine_source_map": {"H": str(H), "N": str(N)},
    "dynamic_readout": str(A_dynamic),
    "probe_source_jacobian": [[str(x) for x in row] for row in probe_source_jacobian.tolist()],
    "source_knob_tangent_at_benchmark": [str(x) for x in source_tangent_benchmark],
    "joint_error_jacobian_determinant": str(joint_det),
    "dynamic_probe_derivative_at_benchmark": str(dynamic_probe_derivative_benchmark),
    "classification": {
        "omega_or_beam_energy_scan": "executable probe context, not a source intervention",
        "luminosity_scan": "exposure change, not a source intervention",
        "affine_c_map": "formal source intervention with no admitted apparatus binding",
    },
    "smallest_exact_falsifier": (
        "A nonzero readout derivative with respect to omega coexists with an "
        "identically zero source-parameter Jacobian."
    ),
    "remaining_gate": (
        "Name and independently calibrate an executable apparatus map into c "
        "that produces both H and N shifts in one source/readout frame."
    ),
    "checks": checks,
    "all_checks_pass": all(checks.values()),
}

if not result["all_checks_pass"]:
    raise SystemExit("WP404 exact checks failed")

out = Path(__file__).parents[1] / "results" / "wp404_probe_source_knob_typing.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
