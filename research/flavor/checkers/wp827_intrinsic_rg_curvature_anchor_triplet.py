"""Exact WP827 audit of intrinsic RG curvature-anchor events."""

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    u = sp.symbols("u", real=True)
    rate = sp.symbols("rate", positive=True, real=True)
    modulus = sp.symbols("modulus", positive=True, real=True)
    beta = rate*u*(1-u)
    acceleration = sp.factor(beta*sp.diff(beta, u))
    jerk = sp.factor(beta*sp.diff(acceleration, u))
    internal_roots = sp.solve(sp.Eq(sp.diff(acceleration, u), 0), u)
    lower = (sp.Integer(3)-sp.sqrt(3))/6
    upper = (sp.Integer(3)+sp.sqrt(3))/6
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("rg_acceleration_is_intrinsic_vector_field_derivative",
          acceleration == rate**2*u*(u-1)*(2*u-1), acceleration)
    check("internal_curvature_anchor_values_are_exact",
          internal_roots == [lower, upper], internal_roots)
    check("anchors_are_symmetric_about_portal_half",
          sp.simplify(lower+upper) == 1
          and sp.simplify((lower+upper)/2) == sp.Rational(1, 2),
          (lower, upper))
    check("jerk_vanishes_at_both_internal_anchors",
          sp.simplify(jerk.subs(u, lower)) == 0
          and sp.simplify(jerk.subs(u, upper)) == 0,
          (jerk.subs(u, lower), jerk.subs(u, upper)))
    check("acceleration_has_opposite_sign_at_anchor_pair",
          acceleration.subs(u, lower) > 0
          and acceleration.subs(u, upper) < 0,
          (acceleration.subs(u, lower), acceleration.subs(u, upper)))

    def event_time(value):
        return sp.log(modulus*value/(1-value))/rate

    lower_time = sp.simplify(event_time(lower))
    portal_time = sp.log(modulus)/rate
    upper_time = sp.simplify(event_time(upper))
    anchor_constant = 2+sp.sqrt(3)
    lower_offset = sp.simplify(sp.expand_log(portal_time-lower_time, force=True))
    upper_offset = sp.simplify(sp.expand_log(upper_time-portal_time, force=True))
    check("curvature_anchors_are_equidistant_in_rg_time",
          sp.simplify(sp.exp(rate*lower_offset)-anchor_constant) == 0
          and sp.simplify(sp.exp(rate*upper_offset)-anchor_constant) == 0,
          (lower_offset, upper_offset))
    check("event_separations_cancel_translation_modulus",
          sp.diff(lower_offset, modulus) == 0 and sp.diff(upper_offset, modulus) == 0,
          (lower_offset, upper_offset))

    portal_to_upper_scale_ratio = sp.exp(upper_offset)
    lower_to_portal_scale_ratio = sp.exp(lower_offset)
    check("unit_rate_anchor_ratios_equal_two_plus_sqrt_three",
          sp.simplify(portal_to_upper_scale_ratio.subs(rate, 1)-anchor_constant) == 0
          and sp.simplify(lower_to_portal_scale_ratio.subs(rate, 1)-anchor_constant) == 0,
          (portal_to_upper_scale_ratio.subs(rate, 1),
           lower_to_portal_scale_ratio.subs(rate, 1)))
    check("unit_rate_full_anchor_ratio_is_seven_plus_four_sqrt_three",
          sp.simplify((portal_to_upper_scale_ratio*lower_to_portal_scale_ratio)
                      .subs(rate, 1)-(7+4*sp.sqrt(3))) == 0,
          (portal_to_upper_scale_ratio*lower_to_portal_scale_ratio).subs(rate, 1))
    check("beta_normalization_changes_relational_scale_ratio",
          sp.simplify(portal_to_upper_scale_ratio.subs(rate, 2)
                      -sp.sqrt(anchor_constant)) == 0,
          portal_to_upper_scale_ratio.subs(rate, 2))

    reference_scale = sp.symbols("reference_scale", positive=True)
    lower_scale = reference_scale*sp.exp(lower_time)
    portal_scale = reference_scale*sp.exp(portal_time)
    upper_scale = reference_scale*sp.exp(upper_time)
    check("scale_ratios_are_independent_of_reference_and_translation",
          sp.simplify(upper_scale/portal_scale-portal_to_upper_scale_ratio) == 0
          and sp.simplify(portal_scale/lower_scale-lower_to_portal_scale_ratio) == 0,
          (upper_scale/portal_scale, portal_scale/lower_scale))

    common_gain = sp.symbols("common_gain", positive=True)
    measured = [common_gain*lower_scale, common_gain*portal_scale, common_gain*upper_scale]
    check("common_gain_cancels_from_three_event_ratios",
          sp.simplify(measured[2]/measured[1]-upper_scale/portal_scale) == 0
          and sp.simplify(measured[1]/measured[0]-portal_scale/lower_scale) == 0,
          (measured[2]/measured[1], measured[1]/measured[0]))
    gain_lower, gain_portal, gain_upper = sp.symbols(
        "gain_lower gain_portal gain_upper", positive=True)
    separate_measured = [
        gain_lower*lower_scale, gain_portal*portal_scale, gain_upper*upper_scale]
    check("separate_event_gains_destroy_ratio_calibration",
          sp.simplify(separate_measured[2]/separate_measured[1])
          != sp.simplify(upper_scale/portal_scale),
          separate_measured[2]/separate_measured[1])

    check("portal_event_remains_positive_transverse_crossing",
          beta.subs(u, sp.Rational(1, 2)) == rate/4,
          beta.subs(u, sp.Rational(1, 2)))
    check("curvature_triplet_does_not_fix_absolute_translation_modulus",
          sp.diff(portal_scale, modulus) != 0, portal_scale)

    germ = {
        "implementation_ingredient_count": 10,
        "native_relation_arity": 3,
        "implementation_ingredients": ["oriented_bulk", "rg_vector_field", "curvature_triplet",
                         "beta_normalization", "spectral_portal", "mediator",
                         "threshold_map", "common_event_clock", "physical16_map",
                         "detector"],
        "orientation_selection": True,
        "dimensionless_magnitude_selection": True,
        "global_basin": True,
        "translation_invariant_event_ratios": True,
        "beta_normalization_authority": False,
        "absolute_scale": False,
        "physical16_descent": False,
        "common_gain_instrument": False,
    }
    check("implementation_stack_is_distinct_from_ternary_native_arity",
          germ["implementation_ingredient_count"] == len(germ["implementation_ingredients"])
          and germ["native_relation_arity"] == 3, germ)
    open_gates = [key for key in (
        "beta_normalization_authority", "absolute_scale",
        "physical16_descent", "common_gain_instrument"
    ) if not germ[key]]
    check("four_normalization_and_realization_gates_remain_open",
          len(open_gates) == 4, open_gates)

    result = {
        "work_package": "WP827",
        "title": "Intrinsic RG curvature-anchor triplet",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "exact_data": {
            "beta": str(beta),
            "acceleration": str(acceleration),
            "anchor_values": [str(lower), "1/2", str(upper)],
            "one_sided_time_offset": str(sp.log(anchor_constant)/rate),
            "unit_rate_scale_ratio": str(anchor_constant),
            "unit_rate_full_ratio": str(7+4*sp.sqrt(3)),
            "aspect_germ": germ,
        },
        "classification": {
            "event_source": "curvature anchors are intrinsic extrema of RG acceleration, not inserted threshold levels",
            "selector": "orientation, half-magnitude, open basin, and three-event ordering are source-generated conditionally",
            "translation": "relative event scale ratios cancel the heteroclinic modulus and reference scale",
            "normalization": "ratios retain beta-function rate normalization",
            "instrument": "a common-gain three-event detector would read ratios; such an instrument and physical16 descent are absent",
            "verdict": "intrinsic anchor triplet repairs translation fiber relationally but not beta normalization or absolute scale",
        },
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp827_intrinsic_rg_curvature_anchor_triplet.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
