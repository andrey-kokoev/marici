"""WP269: exact UV-fixed-point audit for the selector boundary coefficient."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    alpha, beta, time, initial = sp.symbols("alpha beta time initial", real=True)
    fixed_point = sp.simplify(-beta / alpha)
    solution = sp.simplify(fixed_point + (initial - fixed_point) * sp.exp(alpha * time))
    flow_residual = sp.simplify(sp.diff(solution, time) - (alpha * solution + beta))

    # Same UV-attractive exponent, distinct additive matching coefficients.
    packet_one = {alpha: sp.Rational(-1), beta: sp.Rational(1)}
    packet_two = {alpha: sp.Rational(-1), beta: sp.Rational(2)}
    fixed_one = sp.simplify(fixed_point.subs(packet_one))
    fixed_two = sp.simplify(fixed_point.subs(packet_two))
    selected_one = sp.simplify(1 / (2 * fixed_one))
    selected_two = sp.simplify(1 / (2 * fixed_two))

    memory_one = sp.simplify(sp.diff(solution.subs(packet_one), initial))
    memory_two = sp.simplify(sp.diff(solution.subs(packet_two), initial))
    beta_at_fixed_one = sp.simplify((alpha * fixed_point + beta).subs(packet_one))
    beta_at_fixed_two = sp.simplify((alpha * fixed_point + beta).subs(packet_two))

    checks = {
        "affine_flow_solution_exact": flow_residual == 0,
        "both_packets_have_exact_fixed_points": beta_at_fixed_one == 0 and beta_at_fixed_two == 0,
        "both_fixed_points_are_uv_attractive": packet_one[alpha] < 0 and packet_two[alpha] < 0,
        "initial_boundary_memory_decays": memory_one == sp.exp(-time) and memory_two == sp.exp(-time),
        "hostile_fixed_points_distinct": fixed_one == 1 and fixed_two == 2,
        "hostile_fixed_points_select_distinct_mixing": selected_one == sp.Rational(1, 2) and selected_two == sp.Rational(1, 4),
        "fixed_point_value_is_beta_ratio": fixed_point == -beta / alpha,
        "deliberate_attractiveness_implies_numerical_uniqueness_claim_fails": selected_one != selected_two,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP269",
        "theorem_domain": "one renormalized selector coefficient c with affine UV beta function dc/dt=alpha*c+beta",
        "fixed_point": str(fixed_point),
        "exact_flow": str(solution),
        "uv_attraction_condition": "alpha<0 for increasing t=log(mu/mu0)",
        "hostile_uv_packets": [
            {"alpha": "-1", "beta": "1", "fixed_c": str(fixed_one), "selected_x": str(selected_one), "initial_memory": str(memory_one)},
            {"alpha": "-1", "beta": "2", "fixed_c": str(fixed_two), "selected_x": str(selected_two), "initial_memory": str(memory_two)},
        ],
        "classification": "a UV-attractive fixed point is a genuine conditional boundary selector and removes initial-condition memory, but its numerical prediction is the source-dependent beta-function ratio -beta/alpha",
        "first_nonfaithful_arrow": "fixed-point existence and attractiveness -> numerical beta-function coefficients",
        "smallest_exact_falsifier": "the equally UV-attractive beta functions -c+1 and -c+2 select c*=1 and 2, hence x*=1/2 and 1/4",
        "remaining_authority_gate": "derive alpha and beta from a complete anomaly-free UV field content and threshold/matching calculation, then verify the fixed point, basin, decoupling, three-generation potential, and physical instrument",
        "scope_limit": "does not deny selector authority to a complete UV theory that independently fixes its beta coefficients; it denies uniqueness from fixed-point attractiveness alone",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp269_uv_fixed_point_boundary_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
