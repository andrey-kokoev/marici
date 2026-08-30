"""Exact WP577 necessary and sufficient local interface-calibration theorem."""

import json
from pathlib import Path

import sympy as sp


c = sp.symbols("c", real=True)
x = sp.Matrix([1, c])
n = sp.Matrix([-c, 1])
w = sp.Matrix([1, -1, 0])
h = w * n.T

d = sp.Matrix([[1, 0], [-1, 1], [0, -1]])
d_hostile = sp.simplify(d + h)

x_hostile = x.subs(c, 1)
n_hostile = n.subs(c, 1)
d_hostile_one = d_hostile.subs(c, 1)

x_two = sp.eye(2)
y_two = d * x_two
reconstructed = sp.simplify(y_two * x_two.inv())

checks = {
    "single_setting_has_transverse_covector": sp.simplify((n.T * x)[0]) == 0,
    "hostile_completion_is_nonzero": h != sp.zeros(3, 2),
    "hostile_completion_preserves_normalization": sp.ones(1, 3) * h == sp.zeros(1, 2),
    "base_transport_preserves_normalization": sp.ones(1, 3) * d == sp.zeros(1, 2),
    "hostile_transport_preserves_normalization": sp.ones(1, 3) * d_hostile == sp.zeros(1, 2),
    "hostile_pair_agrees_on_calibrated_setting": d * x_hostile == d_hostile_one * x_hostile,
    "hostile_pair_differs_transversely": d * n_hostile != d_hostile_one * n_hostile,
    "two_setting_design_is_nonsingular": x_two.det() == 1,
    "two_settings_reconstruct_transport": reconstructed == d,
    "one_setting_design_has_rank_one": x_hostile.rank() == 1,
    "two_setting_design_has_rank_two": x_two.rank() == 2,
}
checks = {name: bool(value) for name, value in checks.items()}


def encode_matrix(matrix):
    return [[str(sp.simplify(matrix[row, col])) for col in range(matrix.cols)] for row in range(matrix.rows)]


result = {
    "work_package": "WP577",
    "classification": "two noncollinear calibrated source perturbations are necessary and sufficient to identify a two-column local affine detector transport",
    "single_setting": encode_matrix(x_hostile),
    "transverse_covector": encode_matrix(n_hostile),
    "zero_sum_record_tangent": encode_matrix(w),
    "base_transport": encode_matrix(d),
    "hostile_transport": encode_matrix(d_hostile_one),
    "one_setting_response": encode_matrix(d * x_hostile),
    "base_transverse_response": encode_matrix(d * n_hostile),
    "hostile_transverse_response": encode_matrix(d_hostile_one * n_hostile),
    "two_setting_design": encode_matrix(x_two),
    "reconstructed_transport": encode_matrix(reconstructed),
    "smallest_exact_falsifier": "D and D+w*(-1,1) agree on x=(1,1) while differing on the transverse perturbation (-1,1)",
    "authority_boundary": "two settings identify only the frozen affine surrogate unless their full detector chain and calibration are publication-bound",
    "remaining_gate": "execute two noncollinear invariant portal perturbations through one completed, calibrated, covariance-bearing detector pipeline",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp577_two_setting_interface_identification.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
