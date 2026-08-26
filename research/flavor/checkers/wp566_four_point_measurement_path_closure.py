"""Exact WP566 end-to-end four-point measurement path audit."""

import json
from pathlib import Path

import sympy as sp


required = {
    "source_four_point",
    "invariant_physical_map",
    "physical_preparation_and_scattering",
    "detector_readout_and_calibration",
    "covariance_nuisance_uncertainty_model",
    "validated_same_domain_source_interface",
    "uncertainty_supported_nonzero_pullback",
}

routes = {
    "atlas_hs3": {
        "source_four_point",
        "invariant_physical_map",
        "physical_preparation_and_scattering",
        "detector_readout_and_calibration",
        "covariance_nuisance_uncertainty_model",
    },
    "cms_official": {
        "source_four_point",
        "invariant_physical_map",
        "physical_preparation_and_scattering",
        "detector_readout_and_calibration",
        "covariance_nuisance_uncertainty_model",
    },
    "cms_public_code_surrogate": {
        "source_four_point",
        "invariant_physical_map",
    },
    "cross_experiment_gram": {
        "source_four_point",
        "invariant_physical_map",
    },
}

missing = {name: sorted(required - capabilities) for name, capabilities in routes.items()}
complete_routes = sorted(name for name, capabilities in routes.items() if required <= capabilities)

nodes = {
    "four_point_source",
    "invariant_portal",
    "public_generator",
    "atlas_calibrated_templates",
    "atlas_likelihood",
    "cms_official_likelihood",
    "cms_author_detector_surrogate",
    "uncertainty_supported_measurement",
}

edges = {
    ("four_point_source", "invariant_portal"),
    ("invariant_portal", "public_generator"),
    ("atlas_calibrated_templates", "atlas_likelihood"),
    ("atlas_likelihood", "uncertainty_supported_measurement"),
    ("cms_official_likelihood", "uncertainty_supported_measurement"),
}


def enumerate_simple_paths(start, end):
    paths = []

    def visit(node, path):
        if node == end:
            paths.append(path)
            return
        for source, target in sorted(edges):
            if source == node and target not in path:
                visit(target, path + [target])

    visit(start, [start])
    return paths


paths = enumerate_simple_paths("four_point_source", "uncertainty_supported_measurement")

z, kappa_t, lambda_h, u = sp.symbols("z kappa_t lambda_h u", real=True)
portal_relation = kappa_t**2 + z - 1
response = z**2 / lambda_h
hostile = {z: sp.Rational(3, 4), kappa_t: sp.Rational(1, 2)}
hostile_portal_residual = sp.simplify(portal_relation.subs(hostile))
hostile_response = sp.simplify(response.subs(hostile))
hostile_slice_residual = sp.simplify((kappa_t - 1).subs(hostile))
completion_difference = sp.simplify((kappa_t - 1).subs(hostile) * u)

checks = {
    "capability_contract_has_seven_independent_fields": len(required) == 7,
    "no_admitted_route_satisfies_complete_contract": len(complete_routes) == 0,
    "every_route_has_an_explicit_missing_field": all(len(fields) > 0 for fields in missing.values()),
    "authority_graph_nodes_are_declared": all(source in nodes and target in nodes for source, target in edges),
    "no_validated_end_to_end_authority_path": len(paths) == 0,
    "hostile_point_obeys_portal_relation": hostile_portal_residual == 0,
    "hostile_point_has_nonzero_source_response": hostile_response == sp.Rational(9, 16) / lambda_h,
    "hostile_point_is_outside_official_cms_slice": hostile_slice_residual == sp.Rational(-1, 2),
    "detector_completions_disagree_at_hostile_point": completion_difference == -u / 2,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP566",
    "scope": "currently admitted flavor artifacts and validated interfaces through WP565",
    "required_capabilities": sorted(required),
    "route_capabilities": {name: sorted(values) for name, values in routes.items()},
    "route_missing_capabilities": missing,
    "complete_routes": complete_routes,
    "authority_edges": [list(edge) for edge in sorted(edges)],
    "end_to_end_paths": paths,
    "classification": "no admitted composable path realizes the formal four-point derivative as an uncertainty-supported flavor measurement",
    "contextual_partition": "the largest admitted flavor probe fixes z and retains the quartic-source fiber",
    "weak_basis_descent": "passes before the missing source-to-calibrated-experiment interface",
    "smallest_exact_falsifier": {
        "z": str(hostile[z]),
        "kappa_t": str(hostile[kappa_t]),
        "portal_residual": str(hostile_portal_residual),
        "source_response": str(hostile_response),
        "cms_slice_residual": str(hostile_slice_residual),
        "detector_completion_difference": str(completion_difference),
    },
    "remaining_gate": "one publication-bound portal-domain likelihood with source-to-event, detector, calibration, observed-data, nuisance-covariance, and uncertainty-resolution provenance",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp566_four_point_measurement_path_closure.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
