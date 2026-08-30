"""WP314: exact authority audit for a softly broken exchange-ratio selector."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    ratio = sp.symbols("ratio", positive=True)
    stiffness = sp.symbols("stiffness", positive=True)
    breaking = sp.symbols("breaking", real=True)
    angular_potential = sp.simplify(
        (stiffness * (ratio - 1) ** 2 + breaking * (ratio**2 - 1)) / (1 + ratio**2)
    )
    derivative = sp.factor(sp.diff(angular_potential, ratio))
    selected_ratio = sp.simplify((sp.sqrt(breaking**2 + stiffness**2) - breaking) / stiffness)
    stationarity_residual = sp.simplify(derivative.subs(ratio, selected_ratio))
    authority_inversion = sp.simplify((1 - ratio**2) / (2 * ratio))
    response = sp.simplify(sp.diff(selected_ratio, breaking))

    packet_two = selected_ratio.subs({stiffness: 4, breaking: -3})
    packet_three = selected_ratio.subs({stiffness: 3, breaking: -4})
    symmetric_packet = selected_ratio.subs(breaking, 0)
    solved_breaking = sp.solve(
        sp.Eq(2 * breaking * ratio + stiffness * ratio**2 - stiffness, 0), breaking
    )[0]
    second_derivative = sp.diff(angular_potential, ratio, 2)

    checks = {
        "angular_derivative_has_exact_quadratic_numerator": sp.simplify(
            derivative - 2 * (2 * breaking * ratio + stiffness * ratio**2 - stiffness) / (ratio**2 + 1) ** 2
        ) == 0,
        "selected_positive_root_is_stationary": stationarity_residual == 0,
        "unbroken_exchange_selects_ratio_one": symmetric_packet == 1,
        "breaking_response_is_nonzero": response != 0,
        "target_ratio_inverts_to_breaking_over_stiffness": sp.simplify(solved_breaking / stiffness - authority_inversion) == 0,
        "first_rival_packet_selects_ratio_two": packet_two == 2,
        "second_rival_packet_selects_ratio_three": packet_three == 3,
        "both_rival_stationary_points_are_strict_minima": second_derivative.subs({ratio: 2, stiffness: 4, breaking: -3}) > 0 and second_derivative.subs({ratio: 3, stiffness: 3, breaking: -4}) > 0,
        "same_potential_architecture_selects_distinct_ratios": packet_two != packet_three,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP314",
        "theorem_domain": "positive vacuum ratio t=v1/v2 on a fixed radial shell with exchange-even stiffness kappa>0 and real soft breaking epsilon",
        "angular_potential": "U(t)=[kappa*(t-1)^2+epsilon*(t^2-1)]/(1+t^2)",
        "selected_ratio": "t_star=(sqrt(epsilon^2+kappa^2)-epsilon)/kappa",
        "authority_inversion": "epsilon/kappa=(1-t_star^2)/(2*t_star)",
        "source_response": str(response),
        "rival_packets": [
            {"kappa": "4", "epsilon": "-3", "selected_ratio": str(packet_two)},
            {"kappa": "3", "epsilon": "-4", "selected_ratio": str(packet_three)},
        ],
        "descent": "the soft term is a declared exchange-odd source deformation in the enlarged vacuum experiment; its matching into physical16 remains conditional",
        "classification": "genuine tunable ratio selector, but not a parameter-independent prediction unless epsilon/kappa is independently fixed by source structure",
        "smallest_exact_falsifier": "the same softly broken architecture selects t=2 for epsilon/kappa=-3/4 and t=3 for epsilon/kappa=-4/3",
        "remaining_physical_instrument_gate": "derive a discrete or zero-modulus value of epsilon/kappa before flavor fitting, propagate it through realistic matching, and test its proper physical16 prediction on the full ensemble",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp314_soft_exchange_breaking_ratio.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
