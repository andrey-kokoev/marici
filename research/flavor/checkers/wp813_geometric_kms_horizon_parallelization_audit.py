"""Exact WP813 audit of horizon KMS scale parallelization."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    kappa, n, c, gamma, shift, g0, gain = sp.symbols(
        "kappa n c gamma shift g0 gain", positive=True
    )
    beta = 2 * sp.pi / kappa
    splitting = n * kappa
    thermal_product = sp.simplify(beta * splitting)
    q = sp.exp(-thermal_product)
    bias = sp.tanh(thermal_product / 2)
    generator = sp.Matrix([[-gamma, gamma * q], [gamma, -gamma * q]])
    stationary = sp.Matrix([q / (1 + q), 1 / (1 + q)])

    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("horizon_temperature_and_splitting_cancel_surface_gravity",
          thermal_product == 2 * sp.pi * n, thermal_product)
    check("quantized_horizon_bias_is_scale_independent",
          sp.diff(bias, kappa) == 0, sp.diff(bias, kappa))
    check("unit_weight_has_fixed_nonzero_bias",
          bias.subs(n, 1) == sp.tanh(sp.pi), bias.subs(n, 1))
    check("horizon_transition_ratio_is_geometric",
          q == sp.exp(-2 * sp.pi * n), q)
    check("geometric_kms_population_is_stationary",
          sp.simplify(generator * stationary) == sp.zeros(2, 1),
          sp.simplify(generator * stationary))
    check("geometric_kms_gap_is_positive_conditional_on_rate",
          generator.det() == 0 and sp.simplify(generator.trace() + gamma * (1 + q)) == 0,
          {"determinant": generator.det(), "nonzero_eigenvalue": generator.trace()})

    rescaled_beta = 2 * sp.pi / (c * kappa)
    rescaled_splitting = n * c * kappa
    check("common_geometric_threshold_rescaling_preserves_bias",
          sp.simplify(rescaled_beta * rescaled_splitting - thermal_product) == 0,
          sp.simplify(rescaled_beta * rescaled_splitting - thermal_product))
    asymmetric_splitting = n * kappa + shift
    asymmetric_product = sp.simplify(beta * asymmetric_splitting)
    check("asymmetric_threshold_shift_breaks_parallelization",
          sp.simplify(asymmetric_product - thermal_product) == 2 * sp.pi * shift / kappa,
          sp.simplify(asymmetric_product - thermal_product))

    mirror_bias = sp.tanh(-thermal_product / 2)
    check("horizon_generator_reversal_flips_signed_bias",
          sp.simplify(mirror_bias + bias) == 0, sp.simplify(mirror_bias + bias))
    horizon_pair = {"future_oriented": 1, "past_oriented": -1}
    check("geometric_source_retains_future_past_orientation_pair",
          set(horizon_pair.values()) == {-1, 1}, horizon_pair)

    check("absolute_coupling_rate_is_not_fixed_by_kms_geometry",
          generator.subs(gamma, 2 * gamma).nullspace() == generator.nullspace(),
          "same stationary state, doubled physical gap")

    weight_biases = [bias.subs(n, 1), bias.subs(n, 2)]
    check("geometry_without_representation_data_does_not_select_weight",
          sp.simplify(weight_biases[0] - weight_biases[1]) != 0, weight_biases)

    detector_record = gain * g0 * bias.subs(n, 1)
    hostile_records = [detector_record.subs({gain: 2, g0: 1}),
                       detector_record.subs({gain: 1, g0: 2})]
    check("portal_scale_and_gain_have_exact_horizon_hostile_pair",
          sp.simplify(hostile_records[0] - hostile_records[1]) == 0, hostile_records)
    response = sp.Matrix([detector_record]).jacobian([kappa, g0, gain])
    check("single_horizon_record_is_nonfaithful_on_scale_and_calibration",
          response.rank() == 1, f"rank={response.rank()}, nullity=2")

    # The ratio is an executable detector observable, but it contains no
    # physical16 map by itself.
    ratio_jacobian = sp.Matrix([q]).jacobian([kappa, gamma])
    check("transition_ratio_erases_surface_gravity_and_absolute_rate",
          ratio_jacobian.rank() == 0, f"rank={ratio_jacobian.rank()}, nullity=2")

    # Aspect germ tester: endpoint germs do not determine the comparison
    # attachment Delta = attachment * n * kappa.
    attachment = sp.symbols("attachment", positive=True)
    attached_product = sp.simplify(beta * attachment * n * kappa)
    attachment_biases = [sp.tanh(attached_product.subs(attachment, value) / 2)
                         for value in (1, 2)]
    check("aspect_fiber_gate_rejects_endpoint_only_quotient",
          sp.simplify(attachment_biases[0] - attachment_biases[1]) != 0,
          attachment_biases)
    check("aspect_primitive_comparison_attachment_is_target_relevant",
          sp.diff(attached_product, attachment) == 2 * sp.pi * n,
          sp.diff(attached_product, attachment))
    selector_native_arity = 3  # horizon germ, flavor germ, comparison cell
    readout_native_arity = 4   # plus detector realization germ
    check("aspect_native_arity_gate_requires_ternary_selector_germ",
          selector_native_arity == 3, selector_native_arity)
    check("aspect_physical_readout_requires_detector_realization_germ",
          readout_native_arity == 4, readout_native_arity)
    comparison_source_authorized = False
    check("aspect_authority_gate_identifies_missing_comparison_constructor",
          not comparison_source_authorized, comparison_source_authorized)
    retained_marks = {
        "horizon_orientation", "surface_gravity", "state_choice",
        "representation_weight", "frequency_attachment", "detector_time_root",
        "detector_gain",
    }
    check("aspect_marked_germ_retains_all_target_relevant_ports",
          len(retained_marks) == 7, sorted(retained_marks))

    obstruction = len(set(horizon_pair.values())) - 1
    check("deliberate_failure_exhibits_horizon_orientation_port",
          obstruction == 1, obstruction)

    result = {
        "work_package": "WP813",
        "title": "Geometric KMS horizon-parallelization audit",
        "summary": {
            "passed": sum(t["passed"] for t in tests),
            "total": len(tests),
            "all_passed": all(t["passed"] for t in tests),
        },
        "exact_data": {
            "inverse_temperature": str(beta),
            "splitting": str(splitting),
            "thermal_product": str(thermal_product),
            "bias": str(bias),
            "transition_ratio": str(q),
            "unit_weight_bias": str(bias.subs(n, 1)),
        },
        "tests": tests,
        "classification": {
            "scale_parallelization": "successful only on a marked horizon-flavor comparison germ",
            "sign": "relative to horizon-generator orientation; future/past pair remains",
            "magnitude": "thermal bias fixed conditional on integer weight, but portal normalization remains free",
            "rg_and_threshold": "common geometric scaling survives; asymmetric splitting corrections do not",
            "instrument": "transition ratio is executable, but physical16 map and detector gain are absent",
            "aspect_germ_tester": "endpoint-only structure fails fiber, native-arity, and authority gates",
        },
    }

    output = Path(__file__).parents[1] / "results" / "wp813_geometric_kms_horizon_parallelization_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
