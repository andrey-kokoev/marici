"""Exact WP840 audit of reciprocal spectral self-duality and its normalization fiber."""

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    z, m, scale, lam, x, eta = sp.symbols(
        "z m scale lam x eta", positive=True, real=True)
    reciprocal = z+1/z
    mass_coordinate = m**2/scale**2
    mass_action = sp.simplify(reciprocal.subs(z, mass_coordinate))
    coupling_action = eta*x+1/(eta*x)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("reciprocal_action_is_inversion_invariant",
          sp.simplify(reciprocal.subs(z, 1/z)-reciprocal) == 0,
          sp.simplify(reciprocal.subs(z, 1/z)))
    check("reciprocal_action_has_self_dual_stationary_point",
          sp.diff(reciprocal, z).subs(z, 1) == 0, sp.diff(reciprocal, z))
    check("self_dual_stationary_point_is_strict_minimum",
          sp.diff(reciprocal, z, 2).subs(z, 1) == 2,
          sp.diff(reciprocal, z, 2).subs(z, 1))
    check("am_gm_lower_bound_is_saturated_at_self_dual_point",
          reciprocal.subs(z, 1) == 2, reciprocal.subs(z, 1))
    check("mass_action_is_invariant_under_common_rescaling",
          sp.simplify(mass_action.subs({m: lam*m, scale: lam*scale})-mass_action) == 0,
          mass_action)
    check("mass_inversion_contains_comparison_scale",
          sp.simplify(mass_coordinate.subs(m, scale**2/m)-1/mass_coordinate) == 0,
          scale**2/m)
    check("self_duality_selects_only_mass_to_scale_ratio",
          mass_coordinate.subs(m, scale) == 1,
          mass_coordinate.subs(m, scale))
    check("coupling_reciprocity_has_normalized_inversion",
          sp.simplify(coupling_action.subs(x, 1/(eta**2*x))-coupling_action) == 0,
          1/(eta**2*x))
    check("coupling_self_dual_point_depends_on_normalization",
          sp.diff(coupling_action, x).subs(x, 1/eta) == 0,
          1/eta)
    check("eta_two_selects_wp821_coordinate",
          sp.Rational(1, 2) == (1/eta).subs(eta, 2), (1/eta).subs(eta, 2))
    check("eta_three_selects_hostile_coordinate",
          sp.Rational(1, 3) == (1/eta).subs(eta, 3), (1/eta).subs(eta, 3))
    portals = [sp.sqrt(sp.Rational(1, 2)), sp.sqrt(sp.Rational(1, 3))]
    check("same_reciprocal_form_predicts_distinct_portals",
          portals[0] != portals[1], portals)

    result = {
        "work_package": "WP840",
        "title": "Reciprocal spectral self-duality normalization fiber",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "reciprocal_action": "R(z)=z+z^(-1), invariant under z->z^(-1), unique positive minimum z=1",
        "mass_coordinate": "z=m^2/L^2; self-duality selects m=L but not L",
        "coupling_coordinate": "z=eta x; self-duality selects x=1/eta",
        "hostile_pair": {"eta_2": {"x_star": "1/2", "portal": "1/sqrt(2)"},
                         "eta_3": {"x_star": "1/3", "portal": "1/sqrt(3)"}},
        "classification": "conditional relative-scale selector; absolute scale and coupling normalization remain unselected",
        "first_nonfaithful_arrow": "physical spectral or coupling coordinate -> normalized reciprocal coordinate",
        "remaining_source_gate": "derive the reciprocal variable, invariant pairing, normalization, and beta-system map from the same primitive source before testing basin, thresholds, and physical16 realization",
        "tests": tests}
    output = Path(__file__).parents[1] / "results" / "wp840_reciprocal_spectral_self_duality_normalization_fiber.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
