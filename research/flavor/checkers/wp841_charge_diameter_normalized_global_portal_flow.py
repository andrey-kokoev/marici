"""Exact WP841 audit of the charge-diameter normalized global portal flow."""

import json
from pathlib import Path
import sympy as sp


def diameter(matrix: sp.Matrix):
    eigenvalues = list(matrix.eigenvals().keys())
    return sp.simplify(max(eigenvalues)-min(eigenvalues))


def main() -> None:
    Q = sp.diag(1, 2, 3)
    delta = diameter(Q)
    x, kappa, shift = sp.symbols("x kappa shift", positive=True, real=True)
    beta = kappa*x**2*(1-delta*x)
    fixed = 1/delta
    V = (x-fixed)**2
    Vdot = sp.factor(sp.diff(V, x)*beta)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("primitive_charge_diameter_is_two", delta == 2, delta)
    permutation = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    check("diameter_is_basis_conjugation_invariant",
          diameter(permutation*Q*permutation.T) == delta,
          diameter(permutation*Q*permutation.T))
    check("diameter_is_common_shift_invariant",
          diameter(Q+shift*sp.eye(3)) == delta, diameter(Q+shift*sp.eye(3)))
    check("primitive_integer_normalization_blocks_nontrivial_rescaling",
          sp.gcd_list([1, 2, 3]) == 1 and diameter(2*Q) == 2*delta,
          (sp.gcd_list([1, 2, 3]), diameter(2*Q)))
    check("diameter_flow_has_selected_nonzero_fixed_point",
          sp.simplify(beta.subs(x, fixed)) == 0 and fixed == sp.Rational(1, 2),
          fixed)
    check("positive_prefactor_does_not_move_fixed_point",
          sp.solve(sp.factor(beta/x**2), x) == [fixed], sp.solve(sp.factor(beta/x**2), x))
    check("local_stability_exponent_is_negative",
          sp.diff(beta, x).subs(x, fixed) == -kappa/delta,
          sp.diff(beta, x).subs(x, fixed))
    check("global_positive_basin_has_exact_lyapunov_identity",
          sp.simplify(Vdot+2*kappa*delta*x**2*(x-fixed)**2) == 0, Vdot)
    check("flow_points_toward_fixed_point_on_both_sides",
          beta.subs(x, sp.Rational(1, 4)) > 0
          and beta.subs(x, 1) < 0,
          (beta.subs(x, sp.Rational(1, 4)), beta.subs(x, 1)))
    portal = sp.sqrt(fixed)
    check("primitive_adjacent_contrast_selects_positive_portal",
          Q[2, 2]-Q[1, 1] == 1 and portal == 1/sp.sqrt(2), portal)
    active_Q = sp.diag(2, 3)
    active_delta = diameter(active_Q)
    active_fixed = 1/active_delta
    check("extremal_threshold_deletion_changes_diameter",
          active_delta == 1, active_delta)
    check("threshold_hostile_moves_selected_portal_coordinate",
          active_fixed == 1 and active_fixed != fixed, (fixed, active_fixed))

    result = {
        "work_package": "WP841",
        "title": "Charge-diameter normalized global portal flow",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "source_invariant": "Delta_Q=lambda_max(Q)-lambda_min(Q)=2 for primitive Q=diag(1,2,3)",
        "candidate_beta": "beta_x=kappa x^2(1-Delta_Q x), kappa>0",
        "prediction": {"x_star": "1/2", "portal": "1/sqrt(2)",
                       "sign": "positive from q_3-q_2=1",
                       "basin": "entire positive x half-line",
                       "local_exponent": "-kappa/2"},
        "lyapunov_identity": "d(x-x_*)^2/dt=-2 kappa Delta_Q x^2 (x-x_*)^2",
        "classification": "progressive invariant sign-magnitude-global-basin selector; microscopic beta authority, threshold survival, and instrument remain open",
        "smallest_threshold_falsifier": "decouple charge 1: active diameter 2->1 and selected x 1/2->1",
        "remaining_source_gate": "derive the diameter-normalized beta ratio from one microscopic action, prove extremal-sector threshold support or matching, and realize labelled calibrated physical16 response",
        "tests": tests}
    output = Path(__file__).parents[1] / "results" / "wp841_charge_diameter_normalized_global_portal_flow.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
