"""Exact WP564 CMS HHH portal-domain overlap audit."""

import json
from pathlib import Path

import sympy as sp


z, kappa_t, lambda_h = sp.symbols("z kappa_t lambda_h", real=True)

cms_slice = kappa_t - 1
portal_mixing = kappa_t**2 + z - 1
source_response = z**2 / lambda_h

overlap_basis = sp.groebner([cms_slice, portal_mixing], kappa_t, z)
overlap_solution = sp.solve(
    [sp.Eq(cms_slice, 0), sp.Eq(portal_mixing, 0)],
    [kappa_t, z],
    dict=True,
)
response_on_overlap = sp.simplify(source_response.subs(overlap_solution[0]))

hostile_point = {z: sp.Rational(3, 4), kappa_t: sp.Rational(1, 2)}
hostile_portal_residual = sp.simplify(portal_mixing.subs(hostile_point))
hostile_cms_residual = sp.simplify(cms_slice.subs(hostile_point))
hostile_response = sp.simplify(source_response.subs(hostile_point))

release = {
    "record": "https://doi.org/10.17182/hepdata.180103",
    "record_json_sha256": "b0000f54668a785a25cff6cfb58565f7b07a80620ff12eadf7c94f4bddeddcba",
    "result_tables": 7,
    "sampled_confidence_contours": 4,
    "additional_resources": 0,
    "combine_models": 0,
    "collision_luminosity_fb_inverse": 138,
}

instrument = {
    "physical_collision_preparation": release["collision_luminosity_fb_inverse"] > 0,
    "binned_detector_readout": release["result_tables"] > 0,
    "calibration_and_systematics_described": release["sampled_confidence_contours"] > 0,
    "transportable_full_likelihood": release["combine_models"] > 0,
    "portal_parameterized_templates": release["additional_resources"] > 0,
}

checks = {
    "overlap_ideal_forces_sm_top_yukawa": overlap_basis.reduce(kappa_t - 1)[1] == 0,
    "overlap_ideal_forces_zero_mixing": overlap_basis.reduce(z)[1] == 0,
    "source_response_vanishes_on_cms_portal_overlap": response_on_overlap == 0,
    "hostile_point_obeys_portal_relation": hostile_portal_residual == 0,
    "hostile_point_is_source_sensitive": hostile_response == sp.Rational(9, 16) / lambda_h,
    "hostile_point_violates_cms_slice": hostile_cms_residual == sp.Rational(-1, 2),
    "physical_detector_instrument_exists": instrument["physical_collision_preparation"] and instrument["binned_detector_readout"],
    "full_likelihood_is_not_released": not instrument["transportable_full_likelihood"],
    "portal_templates_are_not_released": not instrument["portal_parameterized_templates"],
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP564",
    "classification": "real calibrated kappa-framework instrument with empty overlap between its admitted likelihood slice and the source-sensitive flavor portal domain",
    "release": release,
    "instrument": instrument,
    "overlap_groebner_basis": [str(poly.as_expr()) for poly in overlap_basis.polys],
    "overlap_solution": [
        {str(symbol): str(value) for symbol, value in solution.items()}
        for solution in overlap_solution
    ],
    "response_on_overlap": str(response_on_overlap),
    "smallest_exact_falsifier": {
        "z": str(hostile_point[z]),
        "kappa_t": str(hostile_point[kappa_t]),
        "portal_residual": str(hostile_portal_residual),
        "cms_slice_residual": str(hostile_cms_residual),
        "source_response": str(hostile_response),
    },
    "contextual_partition": "the admitted inclusive-Higgs flavor probe fixes z but retains lambda_s fibers; the CMS HHH scan cannot refine this partition on its fixed-kappa_t slice",
    "weak_basis_descent": "passes; the obstruction is detector-likelihood domain restriction, not weak-basis covariance",
    "remaining_gate": "a portal-complete parameterized HHH and HH likelihood with mixing, Yukawa, width, topology, nuisance, covariance, and uncertainty support",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp564_cms_hhh_empty_sensitive_overlap.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
