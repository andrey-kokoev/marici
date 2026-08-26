"""WP338: exact background-sector correction for binary coincidence towers."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def forward_matrix(size, background, contrast):
    return sp.Matrix([
        [sp.binomial(j, ell) * background ** (j - ell) * contrast**ell if ell <= j else 0
         for ell in range(size + 1)]
        for j in range(size + 1)
    ])


def inverse_matrix(size, background, contrast):
    return sp.Matrix([
        [sp.binomial(j, ell) * (-background) ** (j - ell) / contrast**j if ell <= j else 0
         for ell in range(size + 1)]
        for j in range(size + 1)
    ])


def main():
    size = 6
    alpha, gamma = sp.symbols("alpha gamma", real=True)
    forward = forward_matrix(size, alpha, gamma)
    inverse = inverse_matrix(size, alpha, gamma)
    determinant = sp.factor(forward.det())
    source_moments = sp.Matrix(sp.symbols("u0:7"))
    observed_moments = sp.simplify(forward * source_moments)
    reconstructed = sp.simplify(inverse * observed_moments)
    hostile_a = {"p": sp.Rational(1, 2), "alpha": sp.Rational(0), "gamma": sp.Rational(1, 2)}
    hostile_b = {"p": sp.Rational(1, 4), "alpha": sp.Rational(0), "gamma": sp.Integer(1)}
    observed_probability_a = hostile_a["alpha"] + hostile_a["gamma"] * hostile_a["p"]
    observed_probability_b = hostile_b["alpha"] + hostile_b["gamma"] * hostile_b["p"]
    hostile_tower_a = [observed_probability_a**j for j in range(size + 1)]
    hostile_tower_b = [observed_probability_b**j for j in range(size + 1)]
    checks = {
        "forward_transform_is_lower_triangular": forward.is_lower,
        "diagonal_is_contrast_power_tower": forward.diagonal() == sp.Matrix(1, size + 1, [gamma**j for j in range(size + 1)]),
        "determinant_is_contrast_power_21": determinant == gamma**21,
        "declared_background_subtraction_is_exact_inverse": sp.simplify(inverse * forward) == sp.eye(size + 1),
        "calibrated_tower_reconstructs_source_moments": reconstructed == source_moments,
        "first_observed_moment_contains_background": observed_moments[1] == alpha * source_moments[0] + gamma * source_moments[1],
        "second_observed_moment_contains_all_lower_sectors": observed_moments[2] == alpha**2 * source_moments[0] + 2 * alpha * gamma * source_moments[1] + gamma**2 * source_moments[2],
        "hostile_uncalibrated_towers_are_identical": hostile_tower_a == hostile_tower_b,
        "zero_contrast_collapses_to_background_only": forward.subs(gamma, 0).rank() == 1,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP338",
        "admitted_state_domain": "normalized exchangeable coincidence moments u_0 through u_6 observed through calibrated false-positive background alpha and detector contrast gamma",
        "faithful_quotient_coordinate": "the source coincidence tower conditional on independently calibrated alpha and nonzero gamma",
        "candidate_probe_family": "observed coincidence tower plus known-negative background and known-positive contrast calibration ports",
        "forward_rule": "r_j=sum_{ell<=j} binomial(j,ell) alpha^(j-ell) gamma^ell u_ell",
        "inverse_rule": "u_j=gamma^(-j) sum_{ell<=j} binomial(j,ell) (-alpha)^(j-ell) r_ell",
        "determinant": str(determinant),
        "first_three_observed_moments": [str(observed_moments[j]) for j in range(3)],
        "contextual_partition": "fixed calibrated alpha,gamma with gamma nonzero gives singleton source-moment fibers; floating detector parameters group distinct source towers",
        "classification": "a complete calibrated background-subtraction theorem; raw coincidence correlators include lower-order detector sectors and are not source-faithful",
        "smallest_exact_falsifier": "the source/detector pairs (p,alpha,gamma)=(1/2,0,1/2) and (1/4,0,1) have identical complete observed coincidence towers",
        "remaining_physical_instrument_gate": "realize traceable negative and positive calibration ports, bound background and contrast drift, and test conditional independence and occupancy dependence across coincidence order",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp338_confused_coincidence_tower.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
