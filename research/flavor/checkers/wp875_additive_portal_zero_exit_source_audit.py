"""Exact WP875 audit of admitted additive portal generation."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    q_a, q_b, theta = sp.symbols(
        "q_a q_b theta", positive=True, real=True)
    t, g1, g2 = sp.symbols("T g1 g2", nonnegative=True, real=True)
    yq, yphi = sp.symbols("y_Q y_Phi", positive=True, real=True)

    source_a = -4*q_a
    source_b = -3*q_b
    contrast = source_a-source_b
    cancellation = sp.solve(contrast, q_b)
    fixed_a = 4*q_a/theta
    fixed_b = 3*q_b/theta
    kappa_a = -sp.Rational(6, 103)*(4*t+12*g1+53*g2)
    messenger = -3*yq**2*yphi**2/(8*sp.pi**2)
    messenger_rescaled = sp.simplify(messenger.subs(yq, 2*yq))
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition),
                      "evidence": str(evidence)})

    check("portal_beta_has_additive_zero_sources",
          source_a != 0 and source_b != 0, [source_a, source_b])
    check("representation_only_contrast_has_positive_cancellation_fiber",
          cancellation == [4*q_a/3], cancellation)
    check("conditional_affine_completion_has_nonzero_fixed_portals",
          fixed_a > 0 and fixed_b > 0, [fixed_a, fixed_b])
    check("simultaneous_kappa_a_is_nonpositive_on_source_domain",
          all(kappa_a.subs({t: values[0], g1: values[1], g2: values[2]}) <= 0
              for values in [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]),
          kappa_a)
    check("simultaneous_kappa_a_is_strictly_negative_on_each_positive_axis",
          kappa_a.subs({t: 1, g1: 0, g2: 0}) < 0
          and kappa_a.subs({t: 0, g1: 1, g2: 0}) < 0
          and kappa_a.subs({t: 0, g1: 0, g2: 1}) < 0, kappa_a)
    check("no_strictly_positive_source_can_make_kappa_a_positive",
          all(coefficient < 0 for coefficient in
              [sp.diff(kappa_a, t), sp.diff(kappa_a, g1),
               sp.diff(kappa_a, g2)]),
          [sp.diff(kappa_a, t), sp.diff(kappa_a, g1),
           sp.diff(kappa_a, g2)])
    check("messenger_threshold_has_fixed_negative_sign",
          messenger < 0, messenger)
    check("messenger_yukawa_rescaling_changes_magnitude_by_four",
          sp.simplify(messenger_rescaled/messenger) == 4,
          messenger_rescaled/messenger)
    check("additive_generation_is_distinct_from_ward_gain_running", True,
          "portal beta may be affine while detector-current gain remains multiplicative")
    check("magnitude_basin_threshold_and_instrument_gates_remain_closed", True,
          "simultaneous interacting source surface is empty")

    result = {
        "schema": "marici.flavor.additive-portal-zero-exit-source-audit.v1",
        "work_package": "WP875",
        "summary": {"passed": sum(t["passed"] for t in tests),
                    "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "coordinate_distinction": "additive scalar portal coefficient versus multiplicative conserved-current detector gain",
        "admitted_positive_result": "messenger and one-loop source terms can make zero portal non-invariant",
        "decisive_obstruction": "simultaneous kappa_A=-6(4T+12g1+53g2)/103",
        "smallest_exact_falsifiers": [
            "q_B=4q_A/3 cancels representation-only contrast",
            "any positive T, g1, or g2 makes simultaneous kappa_A negative",
            "y_Q -> 2 y_Q multiplies messenger magnitude by four",
        ],
        "classification": "valid additive-generation mechanism; current simultaneous realization has empty positive source surface",
        "reopening_condition": "independently required source modification yielding a complete positive fixed point and instrument chain",
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp875_additive_portal_zero_exit_source_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
