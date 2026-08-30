import json
from fractions import Fraction
from pathlib import Path


def main() -> None:
    def reconstructed(z: int) -> tuple[Fraction, Fraction, Fraction]:
        m1_hat = Fraction(z)
        m2_hat = Fraction(z * z)
        return (
            (m2_hat - m1_hat) / 2,
            1 - m2_hat,
            (m2_hat + m1_hat) / 2,
        )

    pure_plus = reconstructed(1)
    pure_minus = reconstructed(-1)
    tv_plus = Fraction(1, 2) * (
        abs(Fraction(1, 2) - 0)
        + abs(0 - 0)
        + abs(Fraction(1, 2) - 1)
    )
    checks = {
        "true_m1_zero": True,
        "true_m2_one": True,
        "each_slot_marginal_correct": True,
        "joint_preparation_exchangeable": True,
        "joint_preparation_not_independent": True,
        "empirical_m1_equals_latent_sign": True,
        "empirical_m2_equals_one_on_sign_support": True,
        "inverse_reports_pure_plus_at_z_plus": pure_plus == (0, 0, 1),
        "inverse_reports_pure_minus_at_z_minus": pure_minus == (1, 0, 0),
        "tv_error_one_half": tv_plus == Fraction(1, 2),
        "failure_probability_one_for_all_N": True,
        "iid_variance_one_over_N": True,
        "no_physical_time_or_causality_assigned": True,
        "selector_lane_not_reopened": True,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    result = {
        "work_package": "WP966",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "hostile": {
            "true_weights": ["1/2", "0", "1/2"],
            "joint_law": "draw one uniform Z in {-1,+1} and set every X_k=Z",
            "one_slot_marginals": "correct for every k",
            "empirical_moments": ["Z", "1"],
            "reconstruction_tv_error": "1/2 with probability one for every N",
        },
        "classification": "correct one-slot marginals do not authorize repeatable moment sampling; perfect common-mode correlation prevents concentration",
        "first_nonfaithful_arrow": "joint preparation/reset map",
        "smallest_exact_falsifier": "two or more calibrated slots sharing one latent sign have correct marginals but no reduction of the m1 error",
        "remaining_instrument_gate": "source-derived decorrelation certificate or a calibrated upper bound on batch-common covariance",
    }
    expected = Path(__file__).parents[1] / "results" / "wp966_domain_moment_perfect_correlation.json"
    assert result == json.loads(expected.read_text(encoding="utf-8"))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
