"""Exact WP820 audit of integer incidence plus oriented anomaly inflow."""

import itertools
import json
import math
from pathlib import Path
import sympy as sp


def main() -> None:
    incidence = sp.Matrix([[2, -1, 0], [3, 0, -1]])
    primitive = sp.Matrix([1, 2, 3])
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("integer_incidence_has_rank_two", incidence.rank() == 2, incidence.rank())
    check("integer_incidence_kernel_is_one_dimensional",
          len(incidence.nullspace()) == 1, incidence.nullspace())
    check("primitive_charge_vector_spans_kernel",
          incidence*primitive == sp.zeros(2, 1)
          and incidence.nullspace()[0].cross(primitive) == sp.zeros(3, 1),
          incidence*primitive)
    check("charge_vector_is_primitive",
          math.gcd(*[abs(int(value)) for value in primitive]) == 1, primitive)

    primitive_solutions = []
    for values in itertools.product(range(-3, 4), repeat=3):
        if values == (0, 0, 0):
            continue
        vector = sp.Matrix(values)
        if incidence*vector == sp.zeros(2, 1) and math.gcd(*[abs(v) for v in values]) == 1:
            primitive_solutions.append(values)
    check("bounded_primitive_kernel_has_only_orientation_pair",
          primitive_solutions == [(-1, -2, -3), (1, 2, 3)], primitive_solutions)

    scale = sp.symbols("scale", real=True)
    charges = scale*primitive
    cubic_anomaly = sp.expand(sum(value**3 for value in charges))
    check("cubic_anomaly_on_kernel_is_36_scale_cubed",
          cubic_anomaly == 36*scale**3, cubic_anomaly)
    check("oriented_inflow_36_selects_positive_unit_scale",
          sp.solve(sp.Eq(cubic_anomaly, 36), scale) == [1],
          sp.solve(sp.Eq(cubic_anomaly, 36), scale))
    check("reversed_inflow_selects_mirror_orientation",
          sp.solve(sp.Eq(cubic_anomaly, -36), scale) == [-1],
          sp.solve(sp.Eq(cubic_anomaly, -36), scale))
    selected_charges = charges.subs(scale, 1)
    check("selected_integer_contrast_is_positive_unit",
          selected_charges[2]-selected_charges[1] == 1,
          selected_charges[2]-selected_charges[1])

    gauge = sp.symbols("gauge", positive=True)
    portal = sp.simplify(gauge*(selected_charges[2]-selected_charges[1]))
    check("physical_linear_portal_retains_gauge_coupling",
          portal == gauge, portal)
    gauge_a, gauge_b = sp.Rational(1, 5), sp.Rational(2, 5)
    check("same_selected_charge_packet_allows_distinct_portal_magnitudes",
          portal.subs(gauge, gauge_a) != portal.subs(gauge, gauge_b),
          (portal.subs(gauge, gauge_a), portal.subs(gauge, gauge_b)))

    beta_coefficient, initial, time = sp.symbols(
        "beta_coefficient initial time", positive=True)
    running = initial/sp.sqrt(1-2*beta_coefficient*initial**2*time)
    check("abelian_one_loop_solution_satisfies_beta_equation",
          sp.simplify(sp.diff(running, time)-beta_coefficient*running**3) == 0,
          sp.diff(running, time))
    running_symbol = sp.symbols("running_symbol", real=True)
    check("positive_one_loop_coefficient_has_only_gaussian_fixed_point",
          sp.solve(sp.Eq(beta_coefficient*running_symbol**3, 0), running_symbol) == [0],
          sp.solve(sp.Eq(beta_coefficient*running_symbol**3, 0), running_symbol))
    initial_two = sp.symbols("initial_two", positive=True)
    running_two = initial_two/sp.sqrt(1-2*beta_coefficient*initial_two**2*time)
    check("finite_scale_rg_retains_initial_coupling_fiber",
          sp.simplify(running-running_two).subs(initial_two, 2*initial) != 0,
          sp.simplify((running-running_two).subs(initial_two, 2*initial)))

    light_anomaly, inflow = sp.symbols("light_anomaly inflow", real=True)
    wz_term = inflow-light_anomaly
    check("wess_zumino_matching_preserves_total_anomaly",
          sp.simplify(light_anomaly+wz_term) == inflow, light_anomaly+wz_term)
    check("anomaly_matching_allows_continuous_threshold_partition",
          sp.diff(wz_term, light_anomaly) == -1, wz_term)

    gain = sp.symbols("gain", positive=True)
    record = gain*portal
    hostile_records = [
        record.subs({gauge: sp.Rational(1, 5), gain: 2}),
        record.subs({gauge: sp.Rational(2, 5), gain: 1}),
    ]
    check("uncalibrated_detector_has_exact_gauge_gain_pair",
          hostile_records[0] == hostile_records[1], hostile_records)
    detector_jacobian = sp.Matrix([record]).jacobian([gauge, gain])
    check("detector_record_has_rank_one_on_gauge_gain_domain",
          detector_jacobian.rank() == 1, detector_jacobian.rank())

    # The same target can still be compiled into integer relations. Authority
    # requires a topology/action deriving this incidence before the target.
    alternative_incidence = sp.Matrix([[3, -1, 0], [4, 0, -1]])
    alternative_target = sp.Matrix([1, 3, 4])
    check("different_integer_incidence_selects_different_primitive_ray",
          alternative_incidence*alternative_target == sp.zeros(2, 1),
          alternative_incidence*alternative_target)

    germ = {
        "native_arity": 7,
        "source_germs": ["oriented_bulk", "incidence", "mediator", "O1", "O2", "O3",
                         "detector"],
        "incidence_authority": False,
        "oriented_inflow_authority": False,
        "primitive_charge_selection": True,
        "gauge_normalization_authority": False,
        "nonzero_rg_basin": False,
        "threshold_amplitude_protection": False,
        "physical16_descent": False,
        "detector_calibration": False,
    }
    check("aspect_native_seven_object_germ_is_retained",
          germ["native_arity"] == len(germ["source_germs"]), germ)
    check("conditional_charge_selector_gate_passes",
          germ["primitive_charge_selection"], germ)
    open_gates = [key for key in (
        "incidence_authority", "oriented_inflow_authority",
        "gauge_normalization_authority", "nonzero_rg_basin",
        "threshold_amplitude_protection", "physical16_descent",
        "detector_calibration"
    ) if not germ[key]]
    check("seven_source_and_realization_gates_remain_open",
          len(open_gates) == 7, open_gates)

    result = {
        "work_package": "WP820",
        "title": "Integer incidence and anomaly-inflow selector",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "exact_data": {
            "incidence": str(incidence),
            "primitive_kernel_pair": primitive_solutions,
            "cubic_anomaly": str(cubic_anomaly),
            "selected_charges": [int(value) for value in selected_charges],
            "selected_charge_contrast": 1,
            "aspect_germ": germ,
        },
        "classification": {
            "conditional_source_principle": "rank-two integer incidence plus oriented quantized cubic inflow",
            "sign_and_charge_scale": "inflow 36 selects the positive primitive charge vector (1,2,3)",
            "portal_magnitude": "the physical linear portal still equals the continuous gauge coupling",
            "rg": "positive one-loop Abelian flow has no nonzero fixed point and retains initial data",
            "threshold": "anomaly matching survives through a Wess-Zumino term but does not freeze amplitudes",
            "readout": "physical16 descent is absent and detector gain remains confounded with gauge coupling",
            "authority": "incidence and oriented inflow must be derived independently; reversing the bulk gives the mirror",
            "verdict": "conditional topological charge selector, not a complete asymmetric-portal selector",
        },
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp820_integer_incidence_anomaly_inflow_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
