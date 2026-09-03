from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    a, b, c, d, e, f = sp.symbols("a b c d e f", nonzero=True)
    d1 = d - b**2 / a
    e1 = e - b * c / a
    f1 = f - c**2 / a
    successive = sp.factor(f1 - e1**2 / d1)
    direct = sp.factor(f - (d * c**2 - 2 * b * c * e + a * e**2) / (a * d - b**2))
    associativity_residual = sp.factor(successive - direct)
    assert associativity_residual == 0

    wrong = sp.factor(f1 - e**2 / d1)
    hostile_residual = sp.factor(wrong - direct)
    hostile_numerator, hostile_denominator = sp.fraction(hostile_residual)
    assert hostile_numerator != 0

    fixture = {a: 2, b: sp.Rational(1, 2), c: sp.Rational(1, 3), d: 1, e: sp.Rational(1, 4), f: 1}
    fixture_correct = sp.factor(successive.subs(fixture))
    fixture_direct = sp.factor(direct.subs(fixture))
    fixture_wrong = sp.factor(wrong.subs(fixture))
    assert fixture_correct == fixture_direct == sp.Rational(115, 126)
    assert fixture_wrong == sp.Rational(55, 63)

    result = {
        "schema": "marici.voevodsky.mixed-bridge-pasting-theorem.v1",
        "status": "finite_mixed_bridge_pasting_associative",
        "generic_associativity_residual": str(associativity_residual),
        "hostile_raw_cross_residual_numerator": str(sp.factor(hostile_numerator)),
        "hostile_raw_cross_residual_denominator": str(sp.factor(hostile_denominator)),
        "hostile_residual_is_nonzero_polynomial": True,
        "required_pivots": ["a != 0", "a*d - b**2 != 0"],
        "positive_definite_inputs_supply_pivots": True,
        "fixture_successive": str(fixture_correct),
        "fixture_direct": str(fixture_direct),
        "fixture_raw_cross": str(fixture_wrong),
        "finite_block_extension": "same identity by block inversion with invertible pivot certificates",
        "unbounded_completion_proved": False,
        "next_gate": "closed-form and common-core completion of mixed bridge certificates",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
