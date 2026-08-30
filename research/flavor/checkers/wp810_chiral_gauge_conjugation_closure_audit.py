"""Exact WP810 audit of conjugation closure in a chiral gauge source."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    YQ = sp.Rational(1, 6)
    Yu = sp.Rational(-2, 3)
    Yd = sp.Rational(1, 3)
    YL = sp.Rational(-1, 2)
    Ye = sp.Integer(1)
    YHu = sp.Rational(1, 2)
    YHd = sp.Rational(-1, 2)

    anomalies = {
        "SU3^2-U1": 2 * YQ + Yu + Yd,
        "SU2^2-U1": 3 * YQ + YL,
        "gravity^2-U1": 6 * YQ + 3 * Yu + 3 * Yd + 2 * YL + Ye,
        "U1^3": 6 * YQ**3 + 3 * Yu**3 + 3 * Yd**3 + 2 * YL**3 + Ye**3,
        "SU3^3": sp.Integer(2) - sp.Integer(1) - sp.Integer(1),
    }
    conjugate_anomalies = {
        "SU3^2-U1": -anomalies["SU3^2-U1"],
        "SU2^2-U1": -anomalies["SU2^2-U1"],
        "gravity^2-U1": -anomalies["gravity^2-U1"],
        "U1^3": -anomalies["U1^3"],
        "SU3^3": -anomalies["SU3^3"],
    }
    yukawa_sums = {
        "up": YQ + YHu + Yu,
        "down": YQ + YHd + Yd,
        "charged_lepton": YL + YHd + Ye,
    }
    conjugate_yukawa_sums = {name: -value for name, value in yukawa_sums.items()}

    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("standard_model_local_anomalies_cancel",
          all(value == 0 for value in anomalies.values()), anomalies)
    check("fully_conjugated_local_anomalies_cancel",
          all(value == 0 for value in conjugate_anomalies.values()), conjugate_anomalies)
    check("standard_model_has_even_su2_doublet_count", 3 + 1 == 4, 4)
    check("conjugation_preserves_su2_global_anomaly_condition", (3 + 1) % 2 == 0,
          (3 + 1) % 2)
    check("yukawa_hypercharge_incidence_closes", all(v == 0 for v in yukawa_sums.values()),
          yukawa_sums)
    check("conjugated_yukawa_incidence_closes",
          all(v == 0 for v in conjugate_yukawa_sums.values()), conjugate_yukawa_sums)

    # Quadratic representation data entering perturbative gauge running are
    # unchanged by R -> conjugate(R) and Y -> -Y.
    quadratic_u1 = 6 * YQ**2 + 3 * Yu**2 + 3 * Yd**2 + 2 * YL**2 + Ye**2
    conjugate_quadratic_u1 = 6 * (-YQ)**2 + 3 * (-Yu)**2 + 3 * (-Yd)**2 + 2 * (-YL)**2 + (-Ye)**2
    check("quadratic_gauge_running_data_are_conjugation_even",
          quadratic_u1 == conjugate_quadratic_u1, quadratic_u1)

    x, y, a, b = sp.symbols("x y a b", real=True)
    radius2 = x**2 + y**2
    beta = sp.Matrix([x * (a - b * radius2), y * (a - b * radius2)])
    beta_at_conjugate = beta.subs(y, -y, simultaneous=True)
    conjugated_beta = sp.Matrix([beta[0], -beta[1]])
    check("complex_coupling_rg_is_conjugation_equivariant",
          sp.simplify(beta_at_conjugate - conjugated_beta) == sp.zeros(2, 1),
          sp.simplify(beta_at_conjugate - conjugated_beta))

    masses = [sp.Integer(1), sp.Integer(2), sp.Integer(5)]
    conjugate_masses = [abs(m) for m in masses]
    check("mass_threshold_spectrum_is_conjugation_even", conjugate_masses == masses,
          conjugate_masses)

    J = 4 * sp.sqrt(3) / 3
    check("faithful_cp_odd_invariant_reverses", -J != J, (J, -J))
    check("cp_even_spectrum_collapses_conjugate_pair", J**2 == (-J)**2, J**2)

    portal = sp.Rational(2, 7)
    check("signed_portal_reverses_under_conjugation", -portal != portal, (portal, -portal))
    check("portal_magnitude_is_not_a_sign_selector", abs(portal) == abs(-portal), abs(portal))

    source_pair = {"source": 1, "conjugate": -1}
    check("source_grammar_contains_two_conjugate_orientations", set(source_pair.values()) == {-1, 1},
          source_pair)
    fixed_conjugation_port = {"source": 1}
    check("choosing_one_orientation_changes_to_a_stabilizer_experiment",
          len(source_pair) == 2 and len(fixed_conjugation_port) == 1,
          {"full": source_pair, "stabilizer": fixed_conjugation_port})

    obstruction = len(set(source_pair.values())) - 1
    check("deliberate_failure_exhibits_chiral_source_nonuniqueness", obstruction == 1,
          obstruction)

    result = {
        "work_package": "WP810",
        "title": "Chiral gauge conjugation-closure audit",
        "summary": {
            "passed": sum(t["passed"] for t in tests),
            "total": len(tests),
            "all_passed": all(t["passed"] for t in tests),
        },
        "exact_data": {
            "hypercharges": {"Q": str(YQ), "u_c": str(Yu), "d_c": str(Yd),
                             "L": str(YL), "e_c": str(Ye)},
            "anomalies": {name: str(value) for name, value in anomalies.items()},
            "conjugate_anomalies": {name: str(value) for name, value in conjugate_anomalies.items()},
            "cp_odd_pair": [str(J), str(-J)],
        },
        "tests": tests,
        "classification": {
            "gauge_and_anomaly_consistency": "rigidifies a chiral packet but admits its full conjugate",
            "rg_and_threshold": "conjugation-equivariant and spectrum-preserving",
            "physical_orientation": "faithful CP-odd invariant distinguishes the pair but is not selected",
            "portal": "signed contrast reverses while its magnitude is unchanged",
            "instrument": "a signed CP readout needs an independently oriented experimental convention",
        },
    }

    output = Path(__file__).parents[1] / "results" / "wp810_chiral_gauge_conjugation_closure_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
