"""Exact WP830 test of process-relative physical effective charges."""

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    u = sp.symbols("u", real=True)
    rate = sp.symbols("rate", positive=True, real=True)
    beta = rate*u*(1-u)
    charge_a = u
    charge_b = sp.expand(u + sp.Rational(1, 2)*u**2*(1-u))
    derivative_b = sp.diff(charge_b, u)
    beta_b = sp.factor(derivative_b*beta)
    acceleration_b = sp.factor(beta*sp.diff(beta_b, u))
    anchor_b = 60*u**4-108*u**3+45*u**2+4*u-2
    old_lower = (3-sp.sqrt(3))/6
    old_upper = (3+sp.sqrt(3))/6
    reflected_b = sp.expand(anchor_b.subs(u, 1-u))
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("two_effective_charges_share_tree_normalization",
          charge_a.subs(u, 0) == charge_b.subs(u, 0) == 0
          and sp.diff(charge_a, u).subs(u, 0) == 1
          and derivative_b.subs(u, 0) == 1,
          (charge_a, charge_b))
    check("channels_differ_first_at_quadratic_order",
          sp.simplify(charge_b-charge_a-sp.Rational(1, 2)*u**2*(1-u)) == 0,
          charge_b-charge_a)
    check("second_channel_is_monotone_on_physical_interval",
          derivative_b.subs(u, 0) > 0 and derivative_b.subs(u, 1) > 0
          and sp.diff(derivative_b, u, 2) < 0,
          derivative_b)
    check("both_channels_fix_endpoint_values",
          charge_b.subs(u, 0) == 0 and charge_b.subs(u, 1) == 1,
          (charge_b.subs(u, 0), charge_b.subs(u, 1)))
    check("same_portal_has_process_relative_effective_charge",
          charge_a.subs(u, sp.Rational(1, 2)) == sp.Rational(1, 2)
          and charge_b.subs(u, sp.Rational(1, 2)) == sp.Rational(9, 16),
          (charge_a.subs(u, sp.Rational(1, 2)),
           charge_b.subs(u, sp.Rational(1, 2))))

    linearized_b = sp.cancel(sp.diff(beta_b, u)/derivative_b)
    check("physical_critical_exponents_agree",
          sp.simplify(linearized_b.subs(u, 0)-rate) == 0
          and sp.simplify(linearized_b.subs(u, 1)+rate) == 0,
          (linearized_b.subs(u, 0), linearized_b.subs(u, 1)))
    check("second_channel_curvature_anchor_equation_is_quartic",
          sp.simplify(sp.diff(acceleration_b, u)+rate**2*anchor_b/2) == 0,
          sp.diff(acceleration_b, u))
    check("old_channel_anchors_are_not_second_channel_anchors",
          sp.simplify(anchor_b.subs(u, old_lower)
                      -(-sp.Rational(1, 3)+sp.sqrt(3)/6)) == 0
          and sp.simplify(anchor_b.subs(u, old_upper)
                          -(-sp.Rational(1, 3)-sp.sqrt(3)/6)) == 0,
          (anchor_b.subs(u, old_lower), anchor_b.subs(u, old_upper)))
    check("second_channel_has_exactly_two_internal_curvature_anchors",
          sp.count_roots(anchor_b, 0, 1) == 2,
          sp.count_roots(anchor_b, 0, 1))
    check("second_channel_anchors_are_not_reflection_paired",
          sp.resultant(anchor_b, reflected_b, u) == 53084160
          and sp.gcd(anchor_b, reflected_b) == 1,
          sp.resultant(anchor_b, reflected_b, u))

    result = {
        "work_package": "WP830",
        "title": "Process-relative effective-charge no-go",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "admitted_channel_model": {
            "underlying_physical_orbit": str(beta),
            "effective_charge_A": str(charge_a),
            "effective_charge_B": str(charge_b),
            "common_tree_normalization": True,
            "portal_records": ["1/2", "9/16"],
            "channel_B_anchor_polynomial": str(anchor_b),
        },
        "contextual_partition": {
            "each_channel": "monotone and individually faithful to the one-dimensional orbit",
            "joint_family": "faithful but supplies no canonical scalar channel",
            "curvature_events": "channel-relative despite common tree normalization and common critical exponents",
        },
        "classification": {
            "physical_instrument": "conditional: pole, width, rate, and interference channels exist as typed source-derived probes, but their completed calibrations remain open",
            "selector": False,
            "rigidifier": "each chosen effective-charge channel rigidifies its own running-coordinate presentation",
            "first_nonfaithful_arrow": "source probe family to an unnamed canonical effective charge",
            "smallest_exact_falsifier": "A(u)=u versus B(u)=u+u^2(1-u)/2; same tree normalization and orbit, different portal value and curvature anchors",
            "required_source_principle": "derive a unique conserved-current channel or a channel-natural invariant relation before using effective-charge geometry for selection",
        },
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp830_process_relative_effective_charge_no_go.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
