"""Exact WP842 charge-moment mismatch with the diameter-normalized flow."""

import json
from pathlib import Path
import sympy as sp


def packet(charges):
    values = [sp.Integer(value) for value in charges]
    s2 = sum(value**2 for value in values)
    s4 = sum(value**4 for value in values)
    delta = max(values)-min(values)
    required_screening = s4-delta*s2
    return {"delta": delta, "s2": s2, "s4": s4,
            "moment_fixed": sp.Rational(s2, s4),
            "diameter_fixed": sp.Rational(1, delta),
            "required_screening": required_screening}


def main() -> None:
    base = packet([1, 2, 3])
    shifted = packet([2, 3, 4])
    active = packet([2, 3])
    x, screening = sp.symbols("x screening", real=True)
    beta_screened = x**2*(base["s2"]-(base["s4"]-screening)*x)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("primitive_second_moment_is_fourteen", base["s2"] == 14, base["s2"])
    check("primitive_fourth_moment_is_ninety_eight", base["s4"] == 98, base["s4"])
    check("primitive_diameter_is_two", base["delta"] == 2, base["delta"])
    check("charge_moment_flow_selects_one_seventh",
          base["moment_fixed"] == sp.Rational(1, 7), base["moment_fixed"])
    check("moment_flow_disagrees_with_diameter_flow",
          base["moment_fixed"] != base["diameter_fixed"]
          and base["diameter_fixed"] == sp.Rational(1, 2),
          (base["moment_fixed"], base["diameter_fixed"]))
    check("required_screening_is_seventy",
          base["required_screening"] == 70, base["required_screening"])
    check("screening_seventy_restores_diameter_fixed_point",
          sp.simplify(beta_screened.subs({screening: 70, x: sp.Rational(1, 2)})) == 0,
          beta_screened.subs(screening, 70))
    check("unscreened_flow_rejects_diameter_fixed_point",
          beta_screened.subs({screening: 0, x: sp.Rational(1, 2)}) != 0,
          beta_screened.subs({screening: 0, x: sp.Rational(1, 2)}))
    check("same_diameter_shift_changes_both_moments",
          shifted["delta"] == base["delta"]
          and shifted["s2"] == 29 and shifted["s4"] == 353,
          shifted)
    check("same_diameter_shift_changes_required_screening",
          shifted["required_screening"] == 295
          and shifted["required_screening"] != base["required_screening"],
          shifted["required_screening"])
    check("threshold_active_packet_has_exact_moments",
          active["delta"] == 1 and active["s2"] == 13 and active["s4"] == 97,
          active)
    check("threshold_changes_required_screening_to_eighty_four",
          active["required_screening"] == 84
          and active["required_screening"] != base["required_screening"],
          active["required_screening"])

    result = {
        "work_package": "WP842",
        "title": "Charge-moment loop mismatch with diameter flow",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "base_packet": {key: str(value) for key, value in base.items()},
        "shifted_same_diameter_packet": {key: str(value) for key, value in shifted.items()},
        "threshold_active_packet": {key: str(value) for key, value in active.items()},
        "hostile_loop_grammar": "beta_x=x^2(S2-S4 x) selects S2/S4=1/7, not 1/Delta_Q=1/2",
        "required_interaction": "a source-derived tensor contribution Y=70 is required so S4-Y=Delta_Q S2",
        "classification": "negative charge-only microscopic derivation; exact target for a unique interaction tensor",
        "claim_boundary": "the unit-coefficient moment beta is a structural hostile, not a claimed physical scheme",
        "remaining_source_gate": "derive one interaction tensor with loop contraction 70 and threshold-matched contraction 84, then physical16 realization",
        "tests": tests}
    output = Path(__file__).parents[1] / "results" / "wp842_charge_moment_loop_mismatch.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
