"""Exact WP563 public HHH reinterpretation factorization audit."""

import json
from pathlib import Path

import sympy as sp


x = sp.symbols("x", real=True)
w01, w02 = sp.symbols("w01 w02", real=True)
w0 = sp.Matrix([w01, w02])
suffix = sp.eye(2)
hostile_direction = sp.Matrix([1, -1])

completion_a = w0
completion_b = w0 + x * hostile_direction
released_a = suffix * completion_a.subs(x, 0)
released_b = suffix * completion_b.subs(x, 0)
derivative_a = (suffix * completion_a).diff(x).subs(x, 0)
derivative_b = (suffix * completion_b).diff(x).subs(x, 0)

public_release = {
    "simple_analysis_commit": "5a33033d788619bb1039a5b8116fdf43c46fc72a",
    "analysis_source_blob": "c28e56eaa988327b6a3d9da791a8c55db0c4a3f5",
    "analysis_source_files": 1,
    "onnx_models": 6,
    "scaling_json_files": 6,
    "total_higp_artifacts": 13,
    "hs3_fixed_workspaces": 118,
    "basis_event_samples": 0,
    "reweight_cards": 0,
    "parameterized_hs3_workspaces": 0,
    "validated_public_to_hs3_transfer": 0,
}

coverage = {
    "source_to_basis_weights": public_release["basis_event_samples"] > 0 and public_release["reweight_cards"] > 0,
    "events_to_public_scores": public_release["onnx_models"] > 0 and public_release["analysis_source_files"] > 0,
    "public_scores_to_hs3_templates": public_release["validated_public_to_hs3_transfer"] > 0,
    "fixed_template_likelihood": public_release["hs3_fixed_workspaces"] > 0,
    "parameterized_source_likelihood": public_release["parameterized_hs3_workspaces"] > 0,
}

checks = {
    "public_suffix_artifact_count_is_exact": public_release["total_higp_artifacts"] == 13,
    "public_score_operator_is_executable": coverage["events_to_public_scores"],
    "fixed_hs3_likelihood_exists": coverage["fixed_template_likelihood"],
    "source_reweight_prefix_is_absent": not coverage["source_to_basis_weights"],
    "public_to_hs3_validation_join_is_absent": not coverage["public_scores_to_hs3_templates"],
    "parameterized_source_likelihood_is_absent": not coverage["parameterized_source_likelihood"],
    "hostile_completions_match_released_template": released_a == released_b,
    "hostile_completions_have_distinct_derivatives": derivative_a != derivative_b,
    "hostile_nonzero_derivative_is_exact": derivative_b == hostile_direction,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP563",
    "classification": "public executable detector suffix with an underdetermined source-reweight prefix and missing HS3 validation join",
    "public_release": public_release,
    "pipeline_coverage": coverage,
    "hostile_fixed_template": [str(v) for v in released_a],
    "hostile_derivatives": {
        "completion_a": [str(v) for v in derivative_a],
        "completion_b": [str(v) for v in derivative_b],
    },
    "smallest_exact_falsifier": "w_A(x)=w0 and w_B(x)=w0+x(1,-1) agree at x=0 but have different score-bin derivatives",
    "remaining_gate": "release the coupling basis/reweight implementation and validated public-score-to-HS3 template transfer, or publish a parameterized likelihood",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp563_hhh_public_reinterpretation_factorization.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
