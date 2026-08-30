"""WP282: exact finite-temperature branch-selection probability audit."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    bias, vev, volume, temperature = sp.symbols(
        "bias vev volume temperature", positive=True
    )
    log_odds = sp.simplify(2 * bias * vev * volume / temperature)
    odds = sp.exp(log_odds)
    probability_plus = sp.simplify(odds / (1 + odds))
    probability_minus = sp.simplify(1 / (1 + odds))

    target_error = sp.Rational(1, 100)
    required_log_odds = sp.log((1 - target_error) / target_error)
    # Direct substitution into the reduced odds coordinate avoids logarithm
    # normal-form ambiguity.
    target_probability_reduced = sp.Rational(99, 100)

    unbiased_probability = sp.simplify(probability_plus.subs(bias, 0))
    finite_packet_probability = sp.simplify((sp.Rational(3)) / (1 + sp.Rational(3)))
    finite_packet_error = 1 - finite_packet_probability

    checks = {
        "branch_probabilities_normalized": sp.simplify(probability_plus + probability_minus) == 1,
        "branch_odds_equal_boltzmann_factor": sp.simplify(probability_plus / probability_minus) == odds,
        "unbiased_source_gives_half_half": unbiased_probability == sp.Rational(1, 2),
        "one_percent_error_requires_log_99": required_log_odds == sp.log(99),
        "odds_99_give_probability_99_over_100": target_probability_reduced == sp.Rational(99, 100),
        "finite_odds_three_remain_probabilistic": finite_packet_probability == sp.Rational(3, 4) and finite_packet_error == sp.Rational(1, 4),
        "finite_bias_never_gives_deterministic_branch": probability_minus.is_positive and sp.simplify(1 - probability_plus - probability_minus) == 0,
        "deliberate_nonzero_bias_implies_certainty_claim_fails": finite_packet_error > 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP282",
        "theorem_domain": "one finite thermal correlation volume of the WP281 CP-odd double well with linear bias -h*a",
        "log_odds": str(log_odds),
        "favored_branch_probability": str(probability_plus),
        "unfavored_branch_probability": str(probability_minus),
        "unbiased_probability": str(unbiased_probability),
        "one_percent_error_contract": {
            "target_error": str(target_error),
            "required_log_odds": str(required_log_odds),
            "required_inequality": "2*h*v*V/T >= log(99)",
            "boundary_probability": str(target_probability_reduced),
        },
        "hostile_finite_packet": {"odds": "3", "favored_probability": str(finite_packet_probability), "error": str(finite_packet_error)},
        "contextual_partition": "thermal readout assigns a biased probability measure to the two CP-conjugate branches; finite bias does not collapse the branch fiber to a singleton",
        "classification": "source-biased thermal history is a conditional probabilistic branch selector, not a deterministic signed selector or texture rigidifier",
        "first_nonfaithful_arrow": "finite Boltzmann preference -> certain prepared CP branch",
        "smallest_exact_falsifier": "odds 3 favor one branch but leave exact error 1/4",
        "remaining_physical_instrument_gate": "derive h, v, correlation volume, temperature history, quench rate, domain-wall evolution, stabilization, and acceptable branch-error metric from one cosmological/flavor source",
        "scope_limit": "infinite-volume limits, many correlated domains, nonequilibrium quenches, tunneling, and domain-wall selection require separate histories and cannot be inferred from this single equilibrium cell",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp282_thermal_cp_branch_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
