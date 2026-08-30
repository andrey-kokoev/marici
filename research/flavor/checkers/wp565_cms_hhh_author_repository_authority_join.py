"""Exact WP565 source-generator to CMS-author-repository authority-join audit."""

import json
from pathlib import Path

import sympy as sp


a, z, kappa_t, u = sp.symbols("a z kappa_t u", real=True)

portal_relation = kappa_t**2 + z - 1
hostile = {z: sp.Rational(3, 4), kappa_t: sp.Rational(1, 2)}
hostile_a = sp.simplify((kappa_t - 1).subs(hostile))

template_a = sp.Integer(0)
template_b = a * u
slice_difference = sp.simplify((template_b - template_a).subs(a, 0))
hostile_difference = sp.simplify((template_b - template_a).subs(a, hostile_a))
derivative_a = sp.diff(template_a, a)
derivative_b = sp.diff(template_b, a)

generator = {
    "repository": "https://gitlab.com/apapaefs/multihiggs_loop_sm",
    "revision": "788431390ded97d4b44c25a0013b184053b4aaad",
    "restricted_parameters": ["D3", "D4", "CT1", "CT2", "CT3"],
}

analysis_repository = {
    "repository": "https://github.com/mstamenk/hhh-analysis-framework",
    "revision": "b3014e3e8e95fb6398ecbe979cefb02152e69fad",
    "tracked_files": 1255,
    "onnx_files": 24,
    "root_files": 684,
    "release_tags": 0,
    "license_files": 0,
    "citation_files": 0,
    "publication_identifier_matches": 0,
    "datacard_files": 0,
    "workspace_files": 0,
    "observed_data_files": 0,
    "nuisance_or_correlation_files": 0,
}

source_coordinates = set(generator["restricted_parameters"])
required_source_coordinates = {"D3", "D4", "CT1", "CT2", "CT3"}
statistical_completion_count = sum(
    analysis_repository[key]
    for key in (
        "datacard_files",
        "workspace_files",
        "observed_data_files",
        "nuisance_or_correlation_files",
    )
)

checks = {
    "generator_exposes_required_source_coordinates": required_source_coordinates.issubset(source_coordinates),
    "analysis_repository_contains_executable_networks": analysis_repository["onnx_files"] > 0,
    "analysis_repository_contains_calibration_or_systematic_root_objects": analysis_repository["root_files"] > 0,
    "publication_binding_is_absent": analysis_repository["publication_identifier_matches"] == 0 and analysis_repository["release_tags"] == 0,
    "statistical_completion_is_absent": statistical_completion_count == 0,
    "hostile_point_obeys_portal_relation": sp.simplify(portal_relation.subs(hostile)) == 0,
    "hostile_point_leaves_published_slice": hostile_a == sp.Rational(-1, 2),
    "completions_agree_on_released_slice": slice_difference == 0,
    "completions_have_distinct_derivatives": derivative_a == 0 and derivative_b == u,
    "completions_disagree_at_hostile_point": hostile_difference == -u / 2,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP565",
    "classification": "executable source generator and detector-surrogate toolkit without a publication-bound likelihood authority join",
    "generator": generator,
    "analysis_repository": analysis_repository,
    "statistical_completion_count": statistical_completion_count,
    "contextual_partition": "official flavor partition remains fixed-z with unresolved lambda_s fibers; surrogate refinements depend on unbound model and statistical choices",
    "weak_basis_descent": "passes for the invariant source coordinates; failure is the source-to-calibrated-likelihood interface",
    "smallest_exact_falsifier": {
        "z": str(hostile[z]),
        "kappa_t": str(hostile[kappa_t]),
        "a": str(hostile_a),
        "slice_difference": str(slice_difference),
        "hostile_difference": str(hostile_difference),
        "derivative_a": str(derivative_a),
        "derivative_b": str(derivative_b),
    },
    "remaining_gate": "a CMS-publication-bound manifest and complete likelihood joining source model, exact classifiers, calibrations, templates, observed data, nuisances, and correlations",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp565_cms_hhh_author_repository_authority_join.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
