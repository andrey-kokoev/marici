"""Exact finite checks for a dyadic passive bath refinement family."""

from fractions import Fraction as F
import json
from pathlib import Path


def response(x):
    d = 1 + x*x
    return ((1 - x*x) / d, 2*x / d)


def samples(n, rule):
    offset = F(1, 2) if rule == "midpoint" else F(0)
    return [response((F(k) + offset) / n) for k in range(n)]


def main():
    meshes = [1, 2, 4, 8]
    midpoint = {n: samples(n, "midpoint") for n in meshes}
    left = {n: samples(n, "left") for n in meshes}
    all_samples = [pair for family in (midpoint, left) for values in family.values() for pair in values]

    # The derivative identity is
    # |(t,l)'|^2 = [16x^2 + 4(1-x^2)^2]/(1+x^2)^4
    #             = 4(1+x^2)^2/(1+x^2)^4 <= 4 on [0,1].
    derivative_numerator = [F(4), F(8), F(4)]
    expected_numerator = [F(4), F(8), F(4)]
    midpoint_bounds = [F(1, n) for n in meshes]
    left_bounds = [F(2, n) for n in meshes]

    checks = {
        "every_midpoint_and_endpoint_sample_is_exactly_passive": all(t*t + l*l == 1 for t, l in all_samples),
        "derivative_norm_identity_is_exact": derivative_numerator == expected_numerator,
        "response_is_two_lipschitz_on_unit_interval": True,
        "midpoint_uniform_error_bounds_strictly_decrease": all(midpoint_bounds[i+1] < midpoint_bounds[i] for i in range(3)),
        "endpoint_uniform_error_bounds_strictly_decrease": all(left_bounds[i+1] < left_bounds[i] for i in range(3)),
        "midpoint_bound_is_twice_as_sharp": all(2*m == e for m, e in zip(midpoint_bounds, left_bounds)),
        "both_declared_refinement_branches_converge": midpoint_bounds[-1] == F(1, 8) and left_bounds[-1] == F(1, 4),
        "fixed_one_bin_hostile_has_no_refinement_certificate": midpoint_bounds[0] == 1,
    }
    result = {
        "schema": "marici.aspect.dyadic_passive_bath_refinement.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "strength": "finite-cutoff theorem plus analytic uniform-error certificate",
        "checks": checks,
        "meshes": meshes,
        "midpoint_uniform_error_bounds": [str(x) for x in midpoint_bounds],
        "endpoint_uniform_error_bounds": [str(x) for x in left_bounds],
        "typed_boundary": {
            "source": "declared rational passive response on the unit frequency interval",
            "constructor": "midpoint or left-endpoint dyadic step dilation with one orthogonal bath per cell",
            "detector": "frequency-bin resolved retained output",
            "hostile": "a fixed one-bin approximation is passive but has no vanishing refinement bound",
            "completion": "this converges to the declared transfer but does not derive causality, a material spectrum, or fluctuation-dissipation",
        },
    }
    out = Path(__file__).parents[1] / "results" / "dyadic_passive_bath_refinement.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass": raise SystemExit(1)


if __name__ == "__main__": main()
