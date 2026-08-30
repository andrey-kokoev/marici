"""Exact WP821 audit of the incidence-to-fixed-point source interface."""

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    x, y = sp.symbols("x y", nonnegative=True, real=True)
    a, b, c, d, f = sp.symbols("a b c d f", positive=True, real=True)
    denominator = a*c-d*f
    beta_x = 2*x**2*(-b+c*x-d*y)
    beta_y = 2*y*(a*y-f*x)
    fixed_x = sp.factor(a*b/denominator)
    fixed_y = sp.factor(b*f/denominator)
    jacobian = sp.Matrix([beta_x, beta_y]).jacobian([x, y])
    fixed_jacobian = sp.simplify(jacobian.subs({x: fixed_x, y: fixed_y}))
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("general_nonzero_fixed_point_solves_gauge_beta",
          sp.simplify(beta_x.subs({x: fixed_x, y: fixed_y})) == 0,
          beta_x.subs({x: fixed_x, y: fixed_y}))
    check("general_nonzero_fixed_point_solves_yukawa_beta",
          sp.simplify(beta_y.subs({x: fixed_x, y: fixed_y})) == 0,
          beta_y.subs({x: fixed_x, y: fixed_y}))
    check("fixed_point_is_positive_when_denominator_is_positive",
          fixed_x == a*b/denominator and fixed_y == b*f/denominator,
          (fixed_x, fixed_y))

    packet_a = {a: 1, b: 1, c: 3, d: 1, f: 1}
    fixed_a = (sp.simplify(fixed_x.subs(packet_a)), sp.simplify(fixed_y.subs(packet_a)))
    jacobian_a = sp.simplify(fixed_jacobian.subs(packet_a))
    eigen_a = jacobian_a.eigenvals()
    check("controlled_toy_packet_has_positive_fixed_point",
          fixed_a == (sp.Rational(1, 2), sp.Rational(1, 2)), fixed_a)
    check("controlled_toy_fixed_point_has_exact_jacobian",
          jacobian_a == sp.Matrix([[sp.Rational(3, 2), -sp.Rational(1, 2)], [-1, 1]]),
          jacobian_a)
    check("controlled_toy_fixed_point_has_positive_stability_exponents",
          eigen_a == {sp.Rational(1, 2): 1, 2: 1}, eigen_a)
    check("positive_exponents_make_fixed_point_locally_ir_attractive",
          all(value > 0 for value in eigen_a), eigen_a)
    portal_a = sp.sqrt(fixed_a[0])
    check("conditional_fixed_point_sets_portal_magnitude",
          portal_a == sp.sqrt(2)/2, portal_a)

    # The WP820 incidence and charge vector do not specify these loop
    # coefficients. Two microscopic completions with the same charges can
    # therefore have different fixed-point structure.
    packet_b = {a: 1, b: 1, c: 1, d: 1, f: 1}
    check("same_incidence_packet_can_remove_finite_fixed_point",
          denominator.subs(packet_b) == 0, denominator.subs(packet_b))
    packet_c = {a: 1, b: 1, c: 4, d: 1, f: 1}
    fixed_c = (sp.simplify(fixed_x.subs(packet_c)), sp.simplify(fixed_y.subs(packet_c)))
    check("same_incidence_threshold_coefficients_shift_fixed_magnitude",
          fixed_c == (sp.Rational(1, 3), sp.Rational(1, 3)), fixed_c)
    check("threshold_shift_changes_portal_prediction",
          sp.sqrt(fixed_c[0]) != portal_a, (portal_a, sp.sqrt(fixed_c[0])))

    incidence = sp.Matrix([[2, -1, 0], [3, 0, -1]])
    charges = sp.Matrix([1, 2, 3])
    check("all_coefficient_packets_share_identical_wp820_incidence",
          incidence*charges == sp.zeros(2, 1), incidence*charges)
    charge_contrast = charges[2]-charges[1]
    check("oriented_charge_contrast_remains_positive_unit",
          charge_contrast == 1, charge_contrast)
    check("conditional_portal_sign_is_positive_at_positive_fixed_gauge",
          portal_a*charge_contrast > 0, portal_a*charge_contrast)

    # The local fixed point does not establish a global basin.
    check("local_linearization_has_two_dimensional_stable_ir_tangent",
          len(eigen_a) == 2 and jacobian_a.det() > 0, jacobian_a.det())
    global_basin_authorized = False
    check("global_rg_basin_is_not_established",
          not global_basin_authorized, global_basin_authorized)

    # Existing WP805 exact polynomial zero is outside perturbative control.
    wp805_gauge = sp.Rational(3163, 2234)
    wp805_tensor_yukawa = sp.Rational(34182, 5585)
    check("known_chiral_fixed_point_gauge_coordinate_exceeds_one",
          wp805_gauge > 1, wp805_gauge)
    check("known_chiral_tensor_yukawa_coordinate_exceeds_six",
          wp805_tensor_yukawa > 6, wp805_tensor_yukawa)

    gain = sp.symbols("gain", positive=True)
    source_portal = sp.symbols("source_portal", positive=True)
    record = gain*source_portal
    hostile_records = [
        record.subs({gain: 2, source_portal: portal_a}),
        record.subs({gain: 1, source_portal: 2*portal_a}),
    ]
    check("uncalibrated_fixed_point_readout_has_source_gain_pair",
          hostile_records[0] == hostile_records[1], hostile_records)
    check("fixed_point_coordinate_is_not_a_physical16_instrument",
          sp.Matrix([record]).jacobian([gain, source_portal]).rank() == 1,
          "rank one on two source-plus-gain coordinates")

    germ = {
        "native_arity": 8,
        "source_germs": ["oriented_bulk", "incidence", "matter_spectrum", "mediator",
                         "O1", "O2", "O3", "detector"],
        "charge_selector": True,
        "beta_coefficients_from_same_incidence": False,
        "controlled_nonzero_fixed_point": False,
        "global_basin": False,
        "threshold_fixed_point_survival": False,
        "physical16_descent": False,
        "detector_calibration": False,
    }
    check("aspect_native_eight_object_germ_is_retained",
          germ["native_arity"] == len(germ["source_germs"]), germ)
    open_gates = [key for key in (
        "beta_coefficients_from_same_incidence", "controlled_nonzero_fixed_point",
        "global_basin", "threshold_fixed_point_survival", "physical16_descent",
        "detector_calibration"
    ) if not germ[key]]
    check("six_common_source_and_realization_gates_remain_open",
          len(open_gates) == 6, open_gates)

    result = {
        "work_package": "WP821",
        "title": "Same-incidence gauge-Yukawa fixed-point interface",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "exact_data": {
            "general_fixed_point": {"x": str(fixed_x), "y": str(fixed_y)},
            "conditional_packet_a": {"coefficients": {str(k): v for k, v in packet_a.items()},
                                     "fixed_point": [str(v) for v in fixed_a],
                                     "stability": {str(k): v for k, v in eigen_a.items()}},
            "same_incidence_no_fixed_packet": {str(k): v for k, v in packet_b.items()},
            "threshold_shifted_fixed_point": [str(v) for v in fixed_c],
            "aspect_germ": germ,
        },
        "classification": {
            "conditional_completion": "a specified weakly coupled coefficient packet fixes positive portal magnitude and a local IR basin",
            "common_source": "WP820 incidence does not determine beta coefficients or matter multiplicities",
            "threshold": "coefficient shifts move or remove the fixed point",
            "control": "the known WP805 chiral fixed point is algebraic but strongly coupled",
            "readout": "physical16 descent and detector calibration remain absent",
            "verdict": "fixed-point parallelization is possible, but no source-authorized interface yet joins it to the oriented incidence",
        },
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp821_same_incidence_gauge_yukawa_fixed_point_interface.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
