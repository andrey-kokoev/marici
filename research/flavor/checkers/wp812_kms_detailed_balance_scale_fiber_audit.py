"""Exact WP812 audit of KMS detailed balance as a flavor selector."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    gamma, q, beta, delta, g0, gain = sp.symbols(
        "gamma q beta delta g0 gain", positive=True
    )
    generator = sp.Matrix([[-gamma, gamma * q], [gamma, -gamma * q]])
    stationary = sp.Matrix([q / (1 + q), 1 / (1 + q)])
    bias = sp.simplify(stationary[1] - stationary[0])
    x = sp.symbols("x", positive=True)

    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("generator_conserves_probability",
          sp.Matrix([[1, 1]]) * generator == sp.zeros(1, 2),
          sp.Matrix([[1, 1]]) * generator)
    check("gibbs_population_is_stationary",
          sp.simplify(generator * stationary) == sp.zeros(2, 1),
          sp.simplify(generator * stationary))
    check("stationary_kernel_is_unique_for_positive_rates",
          len(generator.nullspace()) == 1, generator.nullspace())
    check("detailed_balance_gap_is_positive",
          set(generator.eigenvals().keys()) == {sp.Integer(0), -gamma * (1 + q)},
          generator.eigenvals())
    check("stationary_bias_is_rate_ratio_function",
          bias == (1 - q) / (1 + q), bias)

    kms_bias = sp.simplify(bias.subs(q, sp.exp(-x)))
    check("kms_bias_equals_thermal_tanh",
          sp.simplify(kms_bias - sp.tanh(x / 2)) == 0, kms_bias)
    check("infinite_temperature_has_no_orientation_bias",
          sp.limit(kms_bias, x, 0, dir="+") == 0,
          sp.limit(kms_bias, x, 0, dir="+"))
    check("zero_temperature_selects_lower_energy_sector",
          sp.limit(kms_bias, x, sp.oo) == 1, sp.limit(kms_bias, x, sp.oo))
    check("energy_reversal_flips_thermal_bias",
          sp.simplify(kms_bias.subs(x, -x, simultaneous=True) + kms_bias) == 0,
          sp.simplify(kms_bias.subs(x, -x, simultaneous=True) + kms_bias))

    thermal_coordinate = beta * delta
    hostile_coordinates = [thermal_coordinate.subs({beta: 1, delta: 2}),
                           thermal_coordinate.subs({beta: 2, delta: 1})]
    check("temperature_and_splitting_have_exact_hostile_pair",
          hostile_coordinates == [2, 2], hostile_coordinates)
    thermal_jacobian = sp.Matrix([thermal_coordinate]).jacobian([beta, delta])
    check("detailed_balance_readout_has_temperature_splitting_kernel",
          thermal_jacobian.rank() == 1, f"rank={thermal_jacobian.rank()}, nullity=1")

    check("absolute_relaxation_rate_is_not_fixed_by_kms_ratio",
          generator.subs(gamma, 2 * gamma).nullspace() == generator.nullspace(),
          "same stationary kernel, doubled gap")

    threshold_bias = sp.tanh(beta * (2 * delta) / 2)
    original_bias = sp.tanh(beta * delta / 2)
    check("generic_threshold_splitting_change_alters_selected_magnitude",
          sp.simplify(threshold_bias - original_bias) != 0,
          sp.simplify(threshold_bias - original_bias))

    detector_record = gain * g0 * sp.tanh(beta * delta / 2)
    record_pair = [detector_record.subs({gain: 2, g0: 1}),
                   detector_record.subs({gain: 1, g0: 2})]
    check("portal_scale_and_detector_gain_remain_confounded",
          sp.simplify(record_pair[0] - record_pair[1]) == 0, record_pair)
    response_rank = sp.Matrix([detector_record]).jacobian([beta, delta, g0, gain]).rank()
    check("single_thermal_record_is_nonfaithful_on_four_source_coordinates",
          response_rank == 1, f"rank={response_rank}, nullity=3")

    source_pair = {"delta_positive": 1, "delta_negative": -1}
    check("thermal_source_retains_mirror_hamiltonian_pair",
          set(source_pair.values()) == {-1, 1}, source_pair)
    obstruction = len(set(source_pair.values())) - 1
    check("deliberate_failure_exhibits_unselected_energy_orientation",
          obstruction == 1, obstruction)

    result = {
        "work_package": "WP812",
        "title": "KMS detailed-balance scale-fiber audit",
        "summary": {
            "passed": sum(t["passed"] for t in tests),
            "total": len(tests),
            "all_passed": all(t["passed"] for t in tests),
        },
        "exact_data": {
            "generator": str(generator),
            "stationary_state": [str(v) for v in stationary],
            "bias": str(bias),
            "kms_bias": str(kms_bias),
            "gap": str(gamma * (1 + q)),
            "hostile_beta_delta_products": [str(v) for v in hostile_coordinates],
        },
        "tests": tests,
        "classification": {
            "selector": "unique Gibbs attractor conditional on signed Hamiltonian splitting and temperature",
            "sign": "set by the sign of the energy splitting; mirror Hamiltonian reverses it",
            "magnitude": "depends only on beta times delta and an independent portal scale",
            "rg_and_threshold": "positive rates retain a basin, but splitting changes alter the predicted bias",
            "instrument": "transition counts identify rate data, not beta, delta, portal scale, and gain separately",
        },
    }

    output = Path(__file__).parents[1] / "results" / "wp812_kms_detailed_balance_scale_fiber_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
