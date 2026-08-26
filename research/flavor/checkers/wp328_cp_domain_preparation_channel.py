"""WP328: exact thermal CP-domain preparation and identification audit."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    beta, epsilon, c0 = sp.symbols("beta epsilon c0", real=True, positive=True)
    theta = sp.simplify(beta * epsilon * c0)
    p_plus = sp.simplify(sp.exp(theta) / (sp.exp(theta) + sp.exp(-theta)))
    p_minus = sp.simplify(1 - p_plus)
    log_odds = sp.simplify(sp.log(p_plus / p_minus))
    response = sp.Matrix([[sp.diff(log_odds, variable) for variable in (beta, epsilon, c0)]])
    kernel_one = sp.Matrix([beta, -epsilon, 0])
    kernel_two = sp.Matrix([beta, 0, -c0])
    unbiased_limit = sp.simplify(p_plus.subs(epsilon, 0))
    checks = {
        "probabilities_are_normalized": sp.simplify(p_plus + p_minus) == 1,
        "log_odds_equal_twice_thermal_bias": sp.expand_log(log_odds, force=True) == 2 * beta * c0 * epsilon,
        "zero_bias_gives_equal_branch_probability": unbiased_limit == sp.Rational(1, 2),
        "response_jacobian_has_rank_one": response.rank() == 1,
        "first_scaling_direction_is_in_kernel": sp.simplify((response * kernel_one)[0]) == 0,
        "second_scaling_direction_is_in_kernel": sp.simplify((response * kernel_two)[0]) == 0,
        "kernel_directions_are_independent": sp.Matrix.hstack(kernel_one, kernel_two).rank() == 2,
        "positive_bias_favors_positive_branch": sp.simplify(p_plus - sp.Rational(1, 2)) > 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP328",
        "admitted_state_domain": "two CP-conjugate domains with energies -epsilon*c0 and +epsilon*c0, prepared by a thermal channel at inverse temperature beta",
        "faithful_quotient_coordinate": "CP-resolved branch probability p_plus, or equivalently its log-odds",
        "source_operation": "Gibbs preparation of the two WP327 branches followed by repeated CP-sensitive branch counts",
        "p_plus": str(p_plus),
        "p_minus": str(p_minus),
        "log_odds": str(log_odds),
        "response_jacobian": [[str(value) for value in row] for row in response.tolist()],
        "response_rank": response.rank(),
        "kernel_basis": [[str(value) for value in vector] for vector in (kernel_one, kernel_two)],
        "contextual_partition": "CP-insensitive observations collapse both domains; calibrated repeated CP-sensitive counts identify one thermal log-odds coordinate",
        "classification": "a biased thermal channel is a stochastic preparation selector over domains, but its branch counts identify only beta*epsilon*c0 and cannot identify the underlying source parameters",
        "smallest_exact_falsifier": "two independent rescalings of beta, epsilon, and c0 leave the log-odds unchanged, giving an exact two-dimensional source-identification kernel",
        "remaining_physical_instrument_gate": "derive the freeze-out temperature, CP scale, bias, domain independence, and detector confusion matrix on one common history; one observed domain is not a calibrated probability measurement",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp328_cp_domain_preparation_channel.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
