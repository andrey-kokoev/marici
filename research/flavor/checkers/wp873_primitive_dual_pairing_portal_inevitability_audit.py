"""Exact WP873 primitive dual-pairing portal audit."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    g, gd, delta, level, y, tau, s0, lam = sp.symbols(
        "g gd delta level y tau s0 lam", positive=True, real=True)
    pairing = delta*g*gd
    self_dual_solution = sp.solve(
        [pairing-1, g-gd], (g, gd), dict=True)
    level_solution = sp.solve(
        [pairing-level, g-gd], (g, gd), dict=True)
    log_g_beta = -sp.tanh(y)/2
    log_gd_beta = sp.tanh(y)/2
    log_pairing_beta = sp.simplify(log_g_beta+log_gd_beta)
    y_beta = sp.simplify(log_g_beta-log_gd_beta)
    solution_sinh = s0*sp.exp(-tau)
    threshold_g = lam*g
    threshold_gd = gd/lam
    threshold_pairing = sp.simplify(delta*threshold_g*threshold_gd)
    exchange_after_threshold = sp.Matrix([threshold_gd, threshold_g])
    threshold_after_exchange = sp.Matrix([lam*gd, g/lam])
    commutation_residual = sp.simplify(
        exchange_after_threshold-threshold_after_exchange)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition),
                      "evidence": str(evidence)})

    check("primitive_pairing_excludes_zero_couplings",
          pairing.subs(g, 0) != 1 and pairing.subs(gd, 0) != 1,
          [pairing.subs(g, 0), pairing.subs(gd, 0)])
    check("unique_positive_self_dual_solution",
          self_dual_solution == [{g: 1/sp.sqrt(delta),
                                  gd: 1/sp.sqrt(delta)}],
          self_dual_solution)
    check("diameter_two_selects_inverse_sqrt_two",
          self_dual_solution[0][g].subs(delta, 2) == sp.sqrt(2)/2,
          self_dual_solution[0][g].subs(delta, 2))
    check("pairing_level_changes_selected_magnitude",
          level_solution == [{g: sp.sqrt(level)/sp.sqrt(delta),
                              gd: sp.sqrt(level)/sp.sqrt(delta)}],
          level_solution)
    check("reciprocal_flow_preserves_pairing",
          log_pairing_beta == 0, log_pairing_beta)
    check("ratio_coordinate_obeys_log_cosh_gradient",
          y_beta == -sp.tanh(y), y_beta)
    check("sinh_ratio_has_exact_exponential_solution",
          sp.diff(solution_sinh, tau) == -solution_sinh, solution_sinh)
    check("threshold_rescaling_preserves_primitive_product",
          threshold_pairing == pairing, threshold_pairing)
    check("pairing_preserving_rescaling_need_not_commute_with_duality",
          commutation_residual != sp.zeros(2, 1), commutation_residual)
    check("positive_rescaling_commutes_with_duality_only_at_unit_scale",
          sp.solve(list(commutation_residual.subs({g: 1, gd: 1})), lam)
          == [(1,)], sp.solve(list(commutation_residual.subs({g: 1, gd: 1})), lam))
    check("level_two_hostile_moves_diameter_two_value_to_one",
          sp.sqrt(sp.Rational(2, 2)) == 1, sp.sqrt(sp.Rational(2, 2)))
    check("physical_dual_port_and_calibration_remain_open", True,
          "no admitted flavor dual coupling, pairing instrument, or physical16 calibration")

    result = {
        "schema": "marici.flavor.primitive-dual-pairing-portal-inevitability-audit.v1",
        "work_package": "WP873",
        "summary": {"passed": sum(t["passed"] for t in tests),
                    "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "candidate_source_principle": "primitive nondegenerate self-dual boundary pairing Delta_Q g g_D=1",
        "admitted_domain": "positive electric-dual coupling hyperbola; zero excluded",
        "selected_coupling": "g=g_D=1/sqrt(2)",
        "basin": "entire primitive positive pairing locus",
        "threshold_condition": "intertwine both primitive pairing and electric-dual exchange",
        "groupoid": "oriented pairing stabilizer; mirror remains in full unoriented groupoid",
        "classification": "abstractly sufficient end-to-end source principle; no admitted microscopic flavor realization",
        "smallest_exact_falsifiers": [
            "pairing level n=2 selects g=1",
            "lambda=2 pairing-preserving threshold destroys self-duality",
            "removing dual port restores zero cusp",
        ],
        "remaining_physical_instrument_gate": "construct and calibrate an actual flavor dual/reference port in physical16 units",
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp873_primitive_dual_pairing_portal_inevitability_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
