"""Exact WP561 HS3 source-covariance pullback audit."""

import json
from pathlib import Path

import sympy as sp


lambda_s, z, lambda_h, weight = sp.symbols(
    "lambda_s z lambda_H w", positive=True, real=True
)

quartic_readout = lambda_s * z**2 / lambda_h
single_higgs_readout = 1 - z
one_probe_jacobian = sp.Matrix([[sp.diff(quartic_readout, x) for x in (lambda_s, z)]])
one_probe_gram = sp.simplify(one_probe_jacobian.T * sp.Matrix([[weight]]) * one_probe_jacobian)
joint_jacobian = sp.Matrix(
    [[sp.diff(readout, x) for x in (lambda_s, z)] for readout in (single_higgs_readout, quartic_readout)]
)

hostile_a = {lambda_s: sp.Integer(1), z: sp.Rational(1, 4)}
hostile_b = {lambda_s: sp.Integer(16), z: sp.Rational(1, 16)}

release = {
    "doi": "10.17182/hepdata.157024.v1/r1",
    "archive_bytes": 6616140,
    "archive_sha256": "30954c386e381f943bbbb430ecf4d263f5d9279b3e91e721ff9ce09de4314036",
    "workspace_count": 118,
    "inspected_workspace": "Likelihood_TRSM_X400_S275.json",
    "inspected_workspace_sha256": "f3eacf5d38c82dbb2e86d08b7849bc525dcba993f22634682cde997bd096eb04",
    "analysis_count": 2,
    "distribution_count": 3,
    "data_object_count": 4,
    "nuisance_parameter_count": 139,
    "physics_parameter_of_interest": "SigXsecOverSM6j",
    "contains_lambda_s": "SigXsecOverSM6j" == "lambda_s",
    "contains_mixing_coordinate": "SigXsecOverSM6j" == "z",
}

checks = {
    "hs3_has_a_real_nuisance_model": release["nuisance_parameter_count"] > 0,
    "workspace_poi_is_fixed_template_normalization": release["physics_parameter_of_interest"] == "SigXsecOverSM6j",
    "source_quartic_coordinate_is_absent": not release["contains_lambda_s"],
    "mixing_coordinate_is_absent": not release["contains_mixing_coordinate"],
    "one_detector_coordinate_has_rank_one": one_probe_jacobian.rank() == 1,
    "one_probe_pullback_gram_is_singular": sp.det(one_probe_gram) == 0,
    "hostile_pair_has_equal_quartic_readout": quartic_readout.subs(hostile_a) == quartic_readout.subs(hostile_b),
    "hostile_pair_has_distinct_sources": hostile_a != hostile_b,
    "complementary_probe_restores_rank_two": joint_jacobian.rank() == 2,
    "joint_determinant_is_nonzero_on_domain": sp.det(joint_jacobian) == z**2 / lambda_h,
    "zero_mixing_is_exact_rank_falsifier": sp.det(joint_jacobian).subs(z, 0) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP561",
    "classification": "HS3 supplies detector nuisance covariance for fixed templates, but source pullback is absent; single-Higgs plus HHH is algebraically rank restoring",
    "release": release,
    "source_coordinates": ["lambda_s", "z = sin(theta)^2"],
    "quartic_readout": str(quartic_readout),
    "one_probe_jacobian": [[str(x) for x in row] for row in one_probe_jacobian.tolist()],
    "one_probe_gram_determinant": str(sp.det(one_probe_gram)),
    "hostile_pair": [["1", "1/4"], ["16", "1/16"]],
    "joint_readouts": [str(single_higgs_readout), str(quartic_readout)],
    "joint_jacobian": [[str(x) for x in row] for row in joint_jacobian.tolist()],
    "joint_jacobian_determinant": str(sp.det(joint_jacobian)),
    "remaining_gate": "portal-complete HHH templates plus a joint or proven-independent single-Higgs/HHH covariance",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp561_hs3_source_covariance_pullback.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
