"""WP371: exact finite-sample Fisher audit for the threshold detector."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    gamma, sigma, mu = sp.symbols("gamma sigma mu", positive=True)
    tau = sp.symbols("tau", real=True, nonnegative=True)
    sample_count = sp.symbols("N", integer=True, positive=True)
    L, omega = sp.symbols("L Omega", positive=True)

    confusion = sp.Matrix([
        [(1 + gamma) / 2, (1 - gamma) / 2],
        [(1 - gamma) / 2, (1 + gamma) / 2],
    ])
    threshold_coordinates = sp.Matrix([
        -mu**2 * L / (2 * (L**2 + omega**2)),
        -mu**2 * omega / (2 * (L**2 + omega**2)),
    ])
    threshold_jacobian = threshold_coordinates.jacobian([L, omega])
    detector_jacobian = sp.simplify(confusion * threshold_jacobian)

    statistical_variance = sigma**2 / sample_count
    covariance = statistical_variance * sp.eye(2) + tau**2 * sp.Matrix([[1, -1], [-1, 1]])
    covariance_determinant = sp.factor(covariance.det())
    fisher = sp.simplify(detector_jacobian.T * covariance.inv() * detector_jacobian)
    fisher_determinant = sp.factor(fisher.det())
    expected_fisher_determinant = (
        sample_count**2 * gamma**2 * mu**8
        / (16 * (L**2 + omega**2)**4 * sigma**2 * (sigma**2 + 2 * sample_count * tau**2))
    )

    difference = sp.Matrix([1, -1])
    nuisance_augmented = detector_jacobian.row_join(difference)
    nuisance_augmented_rank = int(nuisance_augmented.rank())
    zero_contrast_fisher_determinant = sp.simplify(fisher_determinant.subs(gamma, 0))
    zero_background_fisher_determinant = sp.factor(fisher_determinant.subs(tau, 0))
    expected_zero_background = (
        sample_count**2 * gamma**2 * mu**8
        / (16 * (L**2 + omega**2)**4 * sigma**4)
    )

    checks = {
        "confusion_common_gain_is_one": confusion * sp.Matrix([1, 1]) == sp.Matrix([1, 1]),
        "confusion_difference_gain_is_gamma": confusion * difference == gamma * difference,
        "covariance_common_variance_is_statistical": covariance * sp.Matrix([1, 1]) == statistical_variance * sp.Matrix([1, 1]),
        "covariance_difference_variance_has_background_floor": covariance * difference == (statistical_variance + 2 * tau**2) * difference,
        "covariance_determinant_has_declared_form": sp.simplify(
            covariance_determinant - statistical_variance * (statistical_variance + 2 * tau**2)
        ) == 0,
        "fisher_determinant_has_declared_form": sp.simplify(
            fisher_determinant - expected_fisher_determinant
        ) == 0,
        "zero_background_recovers_N_squared_scaling": sp.simplify(
            zero_background_fisher_determinant - expected_zero_background
        ) == 0,
        "zero_contrast_kills_information_volume": zero_contrast_fisher_determinant == 0,
        "unknown_fixed_background_augmented_rank_is_two": nuisance_augmented_rank == 2,
        "unknown_fixed_background_leaves_one_parameter_kernel": 3 - nuisance_augmented_rank == 1,
        "deliberate_single_point_three_parameter_identification_fails": nuisance_augmented_rank < 3,
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP371",
        "admitted_state_domain": "positive contrast gamma, positive effective sample count N, positive statistical scale sigma, nonnegative calibrated differential-background scale tau, and the WP369 two-parameter pole domain",
        "faithful_quotient_coordinate": "local pole coordinates (L,Omega) under the declared Gaussian likelihood; full physical16 remains downstream and projected",
        "source_authorized_probe_family": "finite-sample dispersive/absorptive detector records with calibrated confusion and differential-background covariance",
        "contextual_partition": "positive Fisher determinant separates local pole perturbations; zero contrast or an unknown fixed background nuisance reintroduces a kernel",
        "classification": "finite-sample local threshold identifier under a declared likelihood; neither numerical selector nor full source/physical16 identifier",
        "covariance": str(covariance),
        "covariance_determinant": str(covariance_determinant),
        "fisher_determinant": str(fisher_determinant),
        "unknown_background_augmented_rank": nuisance_augmented_rank,
        "unknown_background_kernel_dimension": 3 - nuisance_augmented_rank,
        "smallest_exact_falsifier": "gamma=0 forces det(F)=0; alternatively, treating differential background as an unknown fixed third parameter leaves a one-dimensional kernel at one scan point",
        "remaining_physical_instrument_gate": "justify the likelihood and effective N, calibrate background support, and add an independent background control or source-supported scan design for fixed nuisance rejection",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp371_threshold_finite_sample_fisher.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
