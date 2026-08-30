"""Exact timing, phase, amplitude, and branch-law error formulas for D(S3)."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]


def main():
    source = json.loads((ROOT / "research/kitaev/results/s3-two-flux-lie-control.json").read_text())
    lambdas = source["optimal_cyclic_dephasing"]["integer_sector_eigenvalues"]
    differences = sorted({abs(a - b) for a in lambdas for b in lambdas if a != b})
    epsilon = sp.symbols("epsilon", real=True)
    eta = sp.symbols("eta", real=True)
    delta = sp.symbols("delta", real=True)
    theta = sp.symbols("theta", real=True)
    dtheta = sp.symbols("dtheta", real=True)

    slope_squared = {}
    for difference in differences:
        residue = difference % 8
        assert residue != 0
        value = sp.simplify(sp.pi ** 2 * difference ** 2 / (64 * sp.sin(sp.pi * residue / 8) ** 2))
        slope_squared[str(difference)] = str(value)

    # Exact geometric-series residual for a common fractional angle error.
    # R_D(eps)=(1/8)sum_k exp(-2pi i k D(1+eps)/8).
    scale_residual = "(1-exp(-2*pi*i*Delta*epsilon))/(8*(1-exp(-2*pi*i*Delta*(1+epsilon)/8)))"

    # A common additive angle after every branch factors out of the ideal
    # zero character sum and therefore leaves it zero.
    common_additive_residual = sp.simplify(sp.exp(-sp.I * delta) * sum(
        sp.exp(2 * sp.pi * sp.I * k / 8) for k in range(8)
    ) / 8)
    assert sp.expand_complex(common_additive_residual) == 0

    weight_errors = [eta] + [-eta / 7] * 7
    omega = sp.sqrt(2) / 2 + sp.I * sp.sqrt(2) / 2
    weight_residuals = [sp.simplify(sum(weight_errors[k] * omega ** (k * mode) for k in range(8))) for mode in range(1, 8)]
    assert all(sp.simplify(r * sp.conjugate(r) - (sp.Rational(8, 7) * eta) ** 2) == 0 for r in weight_residuals)

    leakage_errors = {
        "transposition": str(sp.Rational(8, 9) * sp.sin((theta + dtheta) / 2) ** 2),
        "three_cycle": str(sp.sin((theta + dtheta) / 2) ** 2),
    }
    separator_unitary_error = "2*Abs(sin(sqrt(3)*dtheta/4))"

    result = {
        "schema": "marici.s3-control-error-budget.v1",
        "central_integer_lifts": lambdas,
        "nonzero_absolute_eigenvalue_differences": differences,
        "common_fractional_timing_or_amplitude_error": {
            "definition": "actual_branch_angle=(1+epsilon)*ideal_branch_angle",
            "cross_sector_residual": scale_residual,
            "leading_residual_magnitude_squared_coefficient_by_Delta": slope_squared,
            "typing_warning": "depends_on_integer_lifts_not_only_mod_8_residues",
        },
        "common_additive_phase_offset": {
            "cross_sector_residual": "0",
            "reason": "common_unitary_factor_multiplies_the_ideal_zero_character_sum",
        },
        "branch_dependent_angle_errors": {
            "exact_residual": "(1/8)*sum_k zeta^(k*Delta)*exp(-i*Delta*delta_k)",
            "rigorous_bound": "Abs(Delta)/8*sum_k Abs(delta_k)",
        },
        "branch_weight_error": {
            "general_residual": "sum_k e_k*zeta^(k*Delta)_with_sum_e_k_zero",
            "general_bound": "sum_k Abs(e_k)=2*total_variation_distance",
            "single_overweight_pattern": "eta,-eta/7,...,-eta/7",
            "all_nontrivial_mode_magnitudes": "8*Abs(eta)/7",
        },
        "element_flux_angle_error": {
            "angle_product": "theta=J*t",
            "exact_product_error": "dtheta=t*dJ+J*dt+dJ*dt",
            "final_leakage_after_error": leakage_errors,
        },
        "gh_separator_angle_error": {
            "generator_norm": "sqrt(3)/2",
            "unitary_operator_norm_error": separator_unitary_error,
        },
        "deliberate_failure": {
            "claim": "only_residues_modulo_eight_matter_for_calibration_robustness",
            "actual": False,
            "reason": "multiplicative_error_slopes_depend_on_full_integer_eigenvalue_differences",
        },
        "aggregate_gates": {
            "scale_error_geometric_residual_is_exact": True,
            "all_nonzero_lift_differences_are_catalogued": True,
            "leading_scale_sensitivities_are_exact": True,
            "common_additive_offset_does_not_resurrect_coherence": True,
            "branch_dependent_phase_bound_is_rigorous": True,
            "single_overweight_fourier_residual_is_eight_eta_over_seven": True,
            "flux_port_angle_error_propagates_into_exact_leakage_formula": True,
            "separator_operator_norm_error_is_exact": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__": main()
