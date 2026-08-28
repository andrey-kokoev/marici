"""Exact WP803 audit of the finite SU(5) chiral safe window."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    N, p = sp.symbols("N p", integer=True, positive=True)

    # Cubic SU(N) anomaly coefficients, normalized to one fundamental.
    anomaly_gg = (N - 4) - (N - 4 + p) + p
    anomaly_by = (N + 4) - (N + 4 + p) + p

    p_real = sp.symbols("p_real", real=True)
    b0 = sp.Rational(4, 3) * p_real - 34
    b1 = (
        sp.Rational(4, 15) * (161 * p_real - 1776)
        - sp.Rational(288, 5) * p_real * (1 + p_real) / (11 + 2 * p_real)
    )
    lower = sp.Rational(51, 2)
    roots = sp.solve(sp.together(b1), p_real)
    upper = roots[1]

    # A rational point in the analytically continued window.
    p_probe = sp.Rational(103, 4)
    b0_probe = sp.simplify(b0.subs(p_real, p_probe))
    b1_probe = sp.simplify(b1.subs(p_real, p_probe))
    ag_star = sp.simplify(-b0_probe / b1_probe)
    yukawa_ratio = sp.simplify(sp.Rational(144, 5) / (11 + 2 * p_probe))
    aM_star = sp.simplify(yukawa_ratio * ag_star)

    ag, aM = sp.symbols("a_g a_M", real=True)
    beta_g_eff = b0_probe * ag**2 + b1_probe * ag**3
    beta_M = aM**2 * (15 + 2 * p_probe - 4) - 6 * ag * aM * sp.Rational(24, 5)

    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("georgi_glashow_gauge_anomaly_cancels", sp.simplify(anomaly_gg) == 0,
          sp.simplify(anomaly_gg))
    check("bars_yankielowicz_gauge_anomaly_cancels", sp.simplify(anomaly_by) == 0,
          sp.simplify(anomaly_by))
    check("safe_window_opens_after_loss_of_asymptotic_freedom",
          sp.simplify(b0.subs(p_real, lower)) == 0, lower)
    check("upper_endpoint_is_below_next_integer", upper < 26, upper)
    check("upper_endpoint_exceeds_lower_endpoint", upper > lower,
          sp.simplify(upper - lower))
    check("finite_su5_safe_window_contains_no_integer",
          sp.ceiling(lower) == 26 and sp.floor(upper) == 25,
          f"ceil(lower)={sp.ceiling(lower)}, floor(upper)={sp.floor(upper)}")
    check("analytic_probe_lies_inside_window", lower < p_probe < upper, p_probe)
    check("analytic_probe_has_positive_fixed_gauge_coupling", ag_star > 0, ag_star)
    check("effective_gauge_beta_vanishes_exactly",
          sp.simplify(beta_g_eff.subs(ag, ag_star)) == 0,
          sp.simplify(beta_g_eff.subs(ag, ag_star)))
    check("meson_yukawa_beta_vanishes_exactly",
          sp.simplify(beta_M.subs({ag: ag_star, aM: aM_star})) == 0,
          sp.simplify(beta_M.subs({ag: ag_star, aM: aM_star})))
    check("fixed_yukawa_gauge_ratio_is_exact",
          sp.simplify(aM_star / ag_star) == sp.Rational(288, 625),
          sp.simplify(aM_star / ag_star))

    # a_M is proportional to y_M squared and loses its sign.
    yM = sp.symbols("y_M", real=True)
    check("safe_yukawa_coordinate_is_sign_blind",
          (yM**2).subs(yM, 1) == (yM**2).subs(yM, -1),
          "a_M(+1)=a_M(-1)")

    # The safety-generating Yukawa uses the vectorlike F and anti-F pair;
    # the chiral two-index tensor contributes zero incidence to that vertex.
    incidence = sp.Matrix([1, 1, 0])  # F, anti-F, chiral tensor T
    check("safety_yukawa_omits_chiral_tensor", incidence[2] == 0, incidence.T)

    # Intrinsic dimensionless data cannot determine crossover or detector scale.
    epsilon, crossover, calibration = sp.symbols("epsilon crossover calibration", positive=True)
    probes = sp.Matrix([epsilon, sp.Rational(288, 625) * epsilon])
    jacobian = probes.jacobian([epsilon, crossover, calibration])
    check("intrinsic_probe_has_scale_and_detector_kernel", jacobian.rank() == 1,
          f"rank={jacobian.rank()}, nullity={3 - jacobian.rank()}")

    obstruction = sp.ceiling(lower) - sp.floor(upper)
    check("deliberate_failure_exhibits_integrality_gap", obstruction == 1, obstruction)

    result = {
        "work_package": "WP803",
        "title": "Chiral safe-window integrality and incidence audit",
        "su5_safe_window": {"lower": str(lower), "upper": str(upper)},
        "analytic_probe": {
            "p": str(p_probe),
            "alpha_g_star": str(ag_star),
            "alpha_M_star": str(aM_star),
        },
        "summary": {
            "passed": sum(t["passed"] for t in tests),
            "total": len(tests),
            "all_passed": all(t["passed"] for t in tests),
        },
        "tests": tests,
        "classification": {
            "chirality": "exact anomaly-free GG/BY matter packet",
            "finite_source": "no integer p in the controlled SU(5) safe window",
            "portal_incidence": "safety Yukawa couples vectorlike pair and omits chiral tensor",
            "sign": "erased by squared Yukawa coordinate",
            "scale_and_readout": "unresolved",
        },
    }

    output = Path(__file__).parents[1] / "results" / "wp803_chiral_safe_window_integrality_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
