"""Exact WP839 transport of spectral-action coefficient freedom to portal magnitude."""

import json
from pathlib import Path
import sympy as sp


def spectral_shape(matrix: sp.Matrix):
    gram = matrix.T*matrix
    return sp.simplify(sp.trace(gram)/gram.det()**sp.Rational(1, matrix.rows))


def main() -> None:
    q = sp.Matrix([1, 2, 3])
    H = sp.eye(3)-2*q*q.T/q.dot(q)
    m = sp.symbols("m", positive=True, real=True)
    alpha, beta = sp.symbols("alpha beta", real=True)
    D = m*H
    gram = D.T*D
    action = sp.expand(alpha*sp.trace(gram)+beta*sp.trace(gram**2))
    derivative = sp.diff(action, m)
    second = sp.diff(action, m, 2)
    packets = {"A": {alpha: -2, beta: 1}, "B": {alpha: -4, beta: 1}}
    stationary_m2 = {
        name: sp.Rational(-values[alpha], 2*values[beta])
        for name, values in packets.items()
    }
    c_values = {name: 2+value for name, value in stationary_m2.items()}
    x_values = {name: sp.simplify(1/(value-1)) for name, value in c_values.items()}
    portals = {name: sp.sqrt(value) for name, value in x_values.items()}
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("primitive_reflection_is_fixed", H*q == -q and H.T == H and H*H == sp.eye(3), H)
    check("scale_free_shape_is_three_for_entire_mass_fiber", spectral_shape(D) == 3, spectral_shape(D))
    check("polynomial_action_has_exact_two_moment_form", action == 3*alpha*m**2+3*beta*m**4, action)
    check("stationary_equation_factors_exactly", sp.factor(derivative) == 6*m*(alpha+2*beta*m**2), sp.factor(derivative))
    check("packet_a_selects_unit_squared_scale", stationary_m2["A"] == 1, stationary_m2["A"])
    check("packet_b_selects_squared_scale_two", stationary_m2["B"] == 2, stationary_m2["B"])
    check("both_nonzero_stationary_points_are_strict_minima",
          all(sp.simplify(second.subs(values).subs(m**2, stationary_m2[name])) == -12*values[alpha]
                  and -12*values[alpha] > 0 for name, values in packets.items()),
          {name: -12*values[alpha] for name, values in packets.items()})
    check("source_interface_transports_spectral_choice_to_c", c_values == {"A": 3, "B": 4}, c_values)
    check("fixed_point_magnitude_splits_exactly",
          x_values == {"A": sp.Rational(1, 2), "B": sp.Rational(1, 3)}, x_values)
    check("positive_portal_magnitudes_are_distinct",
          portals["A"] == 1/sp.sqrt(2) and portals["B"] == 1/sp.sqrt(3)
          and portals["A"] != portals["B"], portals)
    check("upstream_current_and_mixing_data_are_identical",
          q.dot(q) == 14 and H == sp.eye(3)-2*q*q.T/q.dot(q), (q.dot(q), H))
    check("action_coefficient_ratio_is_first_nonfaithful_arrow",
          stationary_m2["A"] != stationary_m2["B"] and spectral_shape(H) == spectral_shape(2*H) == 3,
          stationary_m2)

    result = {
        "work_package": "WP839",
        "title": "Spectral-action coefficient fiber transports to the portal",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "fixed_upstream_packet": "q=(1,2,3), H_q=I-2qq^T/(q^Tq), R_3(mH_q)=3",
        "action_family": "S=3 alpha m^2+3 beta m^4",
        "stationary_law": "m_*^2=-alpha/(2 beta), alpha<0, beta>0",
        "hostile_packets": {
            "A": {"alpha": -2, "beta": 1, "m_squared": "1", "c": "3", "x_star": "1/2", "portal": "1/sqrt(2)"},
            "B": {"alpha": -4, "beta": 1, "m_squared": "2", "c": "4", "x_star": "1/3", "portal": "1/sqrt(3)"}},
        "first_nonfaithful_arrow": "fixed finite spectral packet -> choice of spectral-action profile and moment ratio",
        "classification": "negative source-map theorem; geometry and normalized reflection do not determine interacting dynamics",
        "claim_boundary": "c=2+m^2 is an exact hostile interface, not a proposed physical matching law",
        "remaining_source_gate": "derive the action profile, its normalization, and beta coefficients from the same primitive source; then prove global basin, threshold survival, and calibrated physical16 realization",
        "tests": tests}
    output = Path(__file__).parents[1] / "results" / "wp839_spectral_action_coefficient_fiber.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
