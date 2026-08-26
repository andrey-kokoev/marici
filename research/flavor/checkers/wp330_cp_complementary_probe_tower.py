"""WP330: exact complementary-probe rank audit for CP-domain source parameters."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def jacobian(readouts, parameters):
    return sp.Matrix([[sp.diff(readout, parameter) for parameter in parameters] for readout in readouts])


def main():
    beta, epsilon, c0 = sp.symbols("beta epsilon c0", real=True, positive=True)
    parameters = (beta, epsilon, c0)
    log_odds = 2 * beta * epsilon * c0
    thermometer = beta
    cp_scale = c0
    raw = jacobian((log_odds,), parameters)
    with_temperature = jacobian((log_odds, thermometer), parameters)
    with_scale = jacobian((log_odds, cp_scale), parameters)
    complete = jacobian((log_odds, thermometer, cp_scale), parameters)
    determinant = sp.factor(complete.det())
    epsilon_inverse = sp.simplify(log_odds / (2 * thermometer * cp_scale))
    checks = {
        "branch_log_odds_alone_has_rank_one": raw.rank() == 1,
        "adding_only_thermometer_has_rank_two": with_temperature.rank() == 2,
        "adding_only_cp_scale_has_rank_two": with_scale.rank() == 2,
        "complete_tower_has_rank_three": complete.rank() == 3,
        "complete_determinant_is_nonzero_on_domain": determinant == -2 * beta * c0,
        "bias_is_exactly_reconstructed": epsilon_inverse == epsilon,
        "each_single_complement_leaves_a_kernel": len(with_temperature.nullspace()) == 1 and len(with_scale.nullspace()) == 1,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP330",
        "admitted_state_domain": "positive source parameters beta, epsilon, c0 for the WP328 thermal CP-domain channel",
        "faithful_quotient_coordinate": "the full source triple (beta,epsilon,c0), conditional on three common-frame readouts",
        "candidate_probe_family": ["calibrated CP branch log-odds", "independent inverse-temperature readout", "independent CP-scale readout"],
        "source_authorization": "only the log-odds channel is algebraically connected to WP328; physical thermometer and CP-scale constructors on the same freeze-out history remain unproved",
        "rank_sequence": {
            "log_odds_only": raw.rank(),
            "log_odds_plus_temperature": with_temperature.rank(),
            "log_odds_plus_cp_scale": with_scale.rank(),
            "complete_tower": complete.rank(),
        },
        "complete_response_jacobian": [[str(value) for value in row] for row in complete.tolist()],
        "complete_determinant": str(determinant),
        "bias_inverse": "epsilon=log_odds/(2*beta*c0)",
        "contextual_partition": "each single complementary probe reduces the source fiber from dimension two to one; both complements make it singleton on the positive domain",
        "classification": "formal source identification is complete with two complementary probes, but no new selector is created and physical joint executability is not established",
        "smallest_exact_falsifier": "omitting either the thermometer or CP-scale readout leaves a rank-two response and a one-dimensional source kernel",
        "remaining_physical_instrument_gate": "derive and calibrate threshold-local measurements of beta and c0 with common support, time, normalization, and uncertainty bounds; otherwise the full-rank matrix combines objects from different frames",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp330_cp_complementary_probe_tower.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
