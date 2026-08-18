"""Exact lift-independence gate for the weighted physical extension pairing."""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

OUT = Path(__file__).with_name("weighted-extension-chain-pairing-gate.json")


def u_chart(t: Fraction) -> tuple[Fraction, ...]:
    q = Fraction(1, 2) / (t*t - 1)
    return (0*q, -q, 0*q, 3*q)


def stack_chart(s: Fraction) -> tuple[Fraction, ...]:
    q = Fraction(1, 2) / (s**4 - 1)
    return (0*q, q, 0*q, -3*s*s*q)


def transition_u_to_stack(value: tuple[Fraction, ...], s: Fraction):
    # Bottom-row shear inherited from diag(1,1,s^-4,s^-2).
    return (value[0], value[1]/s**4, value[2], value[3]/s**2)


def traced_bd_lift(c: Fraction) -> tuple[Fraction, ...]:
    # t=i*c, hence t^2=-c^2.  The unnormalized mu_2 trace doubles the
    # even coefficient vector.
    q = Fraction(-1, 1) / (c*c + 1)
    direction = (Fraction(0), Fraction(-1), Fraction(0), Fraction(3))
    return tuple(q*x for x in direction)


def show(v): return [str(x) for x in v]


def main() -> None:
    overlap_samples = []
    for s in map(Fraction, (2, 3, 4, 5, 7)):
        source = u_chart(1/(s*s))
        transported = transition_u_to_stack(source, s)
        target = stack_chart(s)
        assert transported == target
        overlap_samples.append({"s": str(s), "transported": show(transported)})

    lift_1 = traced_bd_lift(Fraction(1))
    lift_2 = traced_bd_lift(Fraction(2))
    assert lift_1 != lift_2
    difference = tuple(x-y for x,y in zip(lift_1,lift_2))
    assert any(difference)

    result = {
        "schema": "marici.weighted-extension-chain-pairing-gate.v1",
        "extension_class": "the rationally nonsplit cyclic Hom cocycle of Entry 774",
        "u_chart_exceptional_extension": "(0,-1,0,3)/(2*(t^2-1))",
        "stack_chart_exceptional_extension": "(0,1,0,-3*s^2)/(2*(s^4-1))",
        "overlap_relation": "t=s^-2",
        "overlap_transition": "diag on extension target rows: (s^-4,s^-2)",
        "overlap_homotopy": "zero; the two displayed restrictions agree exactly",
        "overlap_exact_samples": overlap_samples,
        "mu2_character": "even",
        "mu2_trace": "unnormalized trace doubles the section",
        "admissible_bd_lift_family": "u=-i*epsilon, y=-i*c*epsilon^2, t=i*c, c>0",
        "traced_lift_formula": "(0,1,0,-3)/(1+c^2)",
        "c_1_value": show(lift_1),
        "c_2_value": show(lift_2),
        "difference": show(difference),
        "lift_independent": False,
        "physical_relative_chain_current_present": False,
        "typed_pairing_status": "undefined: coefficient restriction and descent are explicit, but no source-derived chain specialization/current compensates the lift dependence",
        "vanishing_claim_authorized": False,
        "nonvanishing_claim_authorized": False,
        "supported_comparison_cone_authorized": False,
        "Q_test_authorized": False,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "overlap_samples": len(overlap_samples),
        "mu2_even": True,
        "lift_independent": result["lift_independent"],
        "pairing_status": result["typed_pairing_status"],
    }))


if __name__ == "__main__":
    main()
