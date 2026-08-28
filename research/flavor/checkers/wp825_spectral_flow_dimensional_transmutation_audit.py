"""Exact WP825 audit of spectral-flow and dimensional-transmutation selection."""

import json
from pathlib import Path
import sympy as sp


def spectral_flow_linear(crossing, bound=sp.Integer(1)):
    left = -bound-crossing
    right = bound-crossing
    if left < 0 < right:
        return 1
    if right < 0 < left:
        return -1
    return 0


def main() -> None:
    crossing = sp.symbols("crossing", real=True)
    t = sp.symbols("t", real=True)
    path = t-crossing
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("linear_path_crosses_at_its_mass_coordinate",
          sp.solve(sp.Eq(path, 0), t) == [crossing],
          sp.solve(sp.Eq(path, 0), t))
    check("two_distinct_crossings_have_same_unit_spectral_flow",
          spectral_flow_linear(sp.Rational(1, 4)) == 1
          and spectral_flow_linear(sp.Rational(3, 4)) == 1,
          (spectral_flow_linear(sp.Rational(1, 4)),
           spectral_flow_linear(sp.Rational(3, 4))))
    check("same_index_pair_has_distinct_crossing_locations",
          sp.Rational(1, 4) != sp.Rational(3, 4),
          (sp.Rational(1, 4), sp.Rational(3, 4)))
    check("index_is_stable_under_small_crossing_displacement",
          all(spectral_flow_linear(value) == 1
              for value in [sp.Rational(-3, 4), 0, sp.Rational(3, 4)]),
          "spectral flow one throughout the open interval")
    check("index_changes_only_at_endpoint_wall",
          spectral_flow_linear(sp.Rational(5, 4)) == 0,
          spectral_flow_linear(sp.Rational(5, 4)))

    reverse_path = crossing-t
    reverse_left = reverse_path.subs({t: -1, crossing: 0})
    reverse_right = reverse_path.subs({t: 1, crossing: 0})
    check("reversing_parameter_orientation_reverses_spectral_flow",
          reverse_left > 0 > reverse_right,
          (reverse_left, reverse_right))
    check("spectral_flow_orients_crossing_but_not_location",
          spectral_flow_linear(sp.Rational(1, 4))
          == spectral_flow_linear(sp.Rational(3, 4)) == 1,
          "orientation fixed; location fiber remains")

    mu, gauge, beta_coefficient = sp.symbols(
        "mu gauge beta_coefficient", positive=True, real=True)
    beta_gauge = -beta_coefficient*gauge**3
    transmutation = mu*sp.exp(-1/(2*beta_coefficient*gauge**2))
    log_transmutation = sp.log(mu)-1/(2*beta_coefficient*gauge**2)
    rg_derivative = sp.simplify(
        mu*sp.diff(log_transmutation, mu)
        +beta_gauge*sp.diff(log_transmutation, gauge))
    check("transmutation_scale_is_one_loop_rg_invariant",
          rg_derivative == 0, rg_derivative)

    target_scale = sp.symbols("target_scale", positive=True, real=True)
    inverse_gauge = sp.sqrt(1/(2*beta_coefficient*sp.log(mu/target_scale)))
    check("every_subtraction_scale_below_mu_corresponds_to_boundary_coupling",
          sp.simplify(transmutation.subs(gauge, inverse_gauge)-target_scale) == 0,
          transmutation.subs(gauge, inverse_gauge))
    target_a, target_b = mu/sp.E, mu/sp.E**2
    gauge_a = sp.simplify(inverse_gauge.subs(target_scale, target_a))
    gauge_b = sp.simplify(inverse_gauge.subs(target_scale, target_b))
    check("distinct_transmutation_scales_are_selected_by_distinct_boundary_couplings",
          gauge_a != gauge_b, (gauge_a, gauge_b))

    scale = sp.symbols("scale", positive=True)
    check("transmutation_formula_is_covariant_under_common_unit_rescaling",
          sp.simplify(
              transmutation.subs(mu, scale*mu)-scale*transmutation) == 0,
          transmutation.subs(mu, scale*mu))

    ratio = sp.symbols("ratio", real=True)
    spectral_mass = ratio*transmutation
    check("spectral_flow_leaves_continuum_of_mass_to_transmutation_ratios",
          spectral_flow_linear(sp.Rational(1, 4)) == spectral_flow_linear(sp.Rational(3, 4))
          and spectral_mass.subs(ratio, sp.Rational(1, 4))
          != spectral_mass.subs(ratio, sp.Rational(3, 4)),
          (spectral_mass.subs(ratio, sp.Rational(1, 4)),
           spectral_mass.subs(ratio, sp.Rational(3, 4))))
    check("threshold_displacement_preserves_index_before_endpoint_collision",
          spectral_flow_linear(sp.Rational(1, 2)) == spectral_flow_linear(sp.Rational(3, 4)) == 1,
          "threshold moved crossing without changing index")

    clock_gain = sp.symbols("clock_gain", positive=True)
    crossing_record = clock_gain*crossing
    hostile_clock = [
        crossing_record.subs({clock_gain: 2, crossing: sp.Rational(1, 4)}),
        crossing_record.subs({clock_gain: 1, crossing: sp.Rational(1, 2)}),
    ]
    check("uncalibrated_crossing_clock_has_exact_source_gain_pair",
          hostile_clock[0] == hostile_clock[1], hostile_clock)
    check("crossing_record_is_rank_one_on_location_clock_domain",
          sp.Matrix([crossing_record]).jacobian([crossing, clock_gain]).rank() == 1,
          "rank one")

    germ = {
        "native_arity": 9,
        "source_germs": ["oriented_bulk", "spectral_path", "index_pairing",
                         "gauge_yukawa_action", "renormalization_clock", "mediator",
                         "threshold_map", "physical16_map", "detector"],
        "orientation_selection": True,
        "crossing_location_selection": False,
        "boundary_coupling_selection": False,
        "absolute_scale_selection": False,
        "threshold_location_protection": False,
        "physical16_descent": False,
        "detector_calibration": False,
    }
    check("aspect_native_nine_object_parallelization_germ_is_retained",
          germ["native_arity"] == len(germ["source_germs"]), germ)
    open_gates = [key for key in (
        "crossing_location_selection", "boundary_coupling_selection",
        "absolute_scale_selection", "threshold_location_protection",
        "physical16_descent", "detector_calibration"
    ) if not germ[key]]
    check("six_scale_location_and_realization_gates_remain_open",
          len(open_gates) == 6, open_gates)

    result = {
        "work_package": "WP825",
        "title": "Spectral-flow and dimensional-transmutation audit",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "exact_data": {
            "spectral_path": str(path),
            "hostile_same_index_crossings": ["1/4", "3/4"],
            "transmutation_scale": str(transmutation),
            "inverse_boundary_coupling": str(inverse_gauge),
            "aspect_germ": germ,
        },
        "classification": {
            "spectral_flow": "selects oriented crossing count but not crossing location or eigenvalue ratio",
            "dimensional_transmutation": "produces an RG invariant but trades boundary coupling for scale",
            "parallelization": "index and transmutation leave an independent mass/scale ratio",
            "threshold": "crossing location moves continuously while index is protected",
            "readout": "location requires a calibrated path clock; physical16 descent and detector remain absent",
            "verdict": "quantized index plus transmutation does not yet make portal magnitude unavoidable",
        },
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp825_spectral_flow_dimensional_transmutation_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
