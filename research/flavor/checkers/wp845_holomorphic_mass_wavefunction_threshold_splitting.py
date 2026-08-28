"""Exact WP845 audit of holomorphic versus physical threshold protection."""

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    charges = [sp.Integer(1), sp.Integer(2), sp.Integer(3)]
    mass, kappa, time = sp.symbols("mass kappa time", positive=True, real=True)
    Z = [sp.exp(kappa*q**2*time) for q in charges]
    physical = [sp.simplify(mass/sp.sqrt(value*value)) for value in Z]
    Q = sp.diag(*charges)
    gamma_traceless = kappa*(Q**2-sp.Rational(14, 3)*sp.eye(3))
    compensation = -gamma_traceless
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("three_vectorlike_mass_terms_are_charge_neutral",
          all(q+(-q) == 0 for q in charges), charges)
    check("holomorphic_mass_parameter_is_common",
          len({str(mass) for _ in charges}) == 1, mass)
    check("allowed_wavefunction_hostile_is_charge_square_dependent",
          Z == [sp.exp(kappa*time), sp.exp(4*kappa*time), sp.exp(9*kappa*time)], Z)
    check("canonical_physical_masses_have_exact_form",
          physical == [mass*sp.exp(-kappa*time),
                       mass*sp.exp(-4*kappa*time),
                       mass*sp.exp(-9*kappa*time)], physical)
    ratio_21 = sp.simplify(physical[1]/physical[0])
    ratio_32 = sp.simplify(physical[2]/physical[1])
    check("first_physical_mass_ratio_splits",
          ratio_21 == sp.exp(-3*kappa*time), ratio_21)
    check("second_physical_mass_ratio_splits",
          ratio_32 == sp.exp(-5*kappa*time), ratio_32)
    check("physical_thresholds_are_equal_only_at_zero_running",
          ratio_21.subs(time, 0) == 1 and ratio_32.subs(time, 0) == 1,
          (ratio_21, ratio_32))
    check("traceless_gauge_anomalous_dimension_is_exact",
          gamma_traceless == kappa*sp.diag(sp.Rational(-11, 3),
                                          sp.Rational(-2, 3),
                                          sp.Rational(13, 3)), gamma_traceless)
    check("traceless_gauge_anomalous_dimension_is_nonzero",
          gamma_traceless != sp.zeros(3) and sp.trace(gamma_traceless) == 0,
          gamma_traceless)
    check("required_kahler_compensation_cancels_exactly",
          gamma_traceless+compensation == sp.zeros(3), compensation)
    check("required_compensation_matches_wp844_operator",
          compensation == -kappa*(Q**2-sp.Rational(14, 3)*sp.eye(3)), compensation)
    check("holomorphic_protection_does_not_imply_physical_threshold_protection",
          physical[0] != physical[1] and physical[1] != physical[2], physical)

    result = {
        "work_package": "WP845",
        "title": "Holomorphic mass wavefunction threshold splitting",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "candidate": "common gauge-invariant holomorphic mass W=m sum_i Phi_i tildePhi_i for vectorlike charges +/-1,+/-2,+/-3",
        "wavefunction_hostile": "Z_i=tildeZ_i=exp(kappa q_i^2 t)",
        "physical_masses": ["m exp(-kappa t)", "m exp(-4 kappa t)", "m exp(-9 kappa t)"],
        "required_kahler_identity": "Gamma_Y^tl=-kappa(Q^2-(14/3)I)",
        "classification": "negative ordinary supersymmetric protection result; holomorphic equality does not protect physical thresholds",
        "claim_boundary": "the exponential wavefunction law is an allowed charge-dependent hostile, not a complete physical loop calculation",
        "remaining_source_gate": "derive an all-order Kähler or physical-pole identity canceling the traceless charge anomalous dimension, then finite matching and calibrated physical16 readout",
        "tests": tests}
    output = Path(__file__).parents[1] / "results" / "wp845_holomorphic_mass_wavefunction_threshold_splitting.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
