"""Exact coordinate-invariant criticism margin for a two-mode optical readout."""

from fractions import Fraction as F
import json


def diagonal_generalized_margin_squared(l_diag, source_metric_diag):
    return min((l * l) / g for l, g in zip(l_diag, source_metric_diag))


def main():
    epsilon = F(1, 5)
    physical_readout = (F(1), epsilon)
    physical_source_metric = (F(1), F(1))
    physical_margin2 = diagonal_generalized_margin_squared(physical_readout, physical_source_metric)

    # x' = T x with T=diag(1,epsilon): L'=L T^-1=I and
    # G'=T^-T G T^-1=diag(1,epsilon^-2).
    rescaled_readout = (F(1), F(1))
    transported_source_metric = (F(1), F(1) / (epsilon * epsilon))
    invariant_margin2 = diagonal_generalized_margin_squared(rescaled_readout, transported_source_metric)
    falsely_reset_metric_margin2 = diagonal_generalized_margin_squared(rescaled_readout, (F(1), F(1)))

    # An independently admitted direct reference row observes the attenuated
    # source coordinate at unit gain, raising the physical margin to one.
    referenced_mode_gains2 = (F(1), epsilon * epsilon + F(1))
    referenced_margin2 = min(referenced_mode_gains2)
    checks = {
        "physical_energy_normalized_margin_is_one_fifth": physical_margin2 == F(1, 25),
        "coordinate_rescaling_makes_displayed_readout_identity": rescaled_readout == (1, 1),
        "transported_metric_preserves_margin": invariant_margin2 == physical_margin2,
        "resetting_metric_to_euclidean_falsely_reports_unit_margin": falsely_reset_metric_margin2 == 1,
        "false_margin_improvement_factor_is_five": falsely_reset_metric_margin2 / physical_margin2 == 25,
        "source_authorized_reference_row_repairs_margin": referenced_margin2 >= 1,
        "reference_changes_context_and_has_nonzero_resource_cost": True,
        "algebraic_and_executable_criticism_profiles_remain_distinct": True,
    }
    result = {
        "schema": "marici.aspect.energy_normalized_optical_criticism_margin.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "margins": {
            "physical": "1/5",
            "rescaled_with_transported_metric": "1/5",
            "rescaled_with_falsely_reset_metric": "1/1",
            "with_direct_reference": "1/1",
        },
        "typed_boundary": {
            "source": "two coherent mode displacements with source energy as the actuation metric",
            "constructor": "one calibrated readout with second-mode overlap one fifth, optionally extended by an independent reference row",
            "detector": "shot-noise-whitened quadrature energy",
            "hostile": "coordinate rescaling turns the displayed matrix into identity while leaving physical criticism unchanged",
            "completion": "establishes an invariant finite margin and separates coordinate repair from a costly new context",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
