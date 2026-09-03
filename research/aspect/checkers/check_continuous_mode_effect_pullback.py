#!/usr/bin/env python3
"""Exact finite compression of continuous-mode effect pullback and loss obstruction."""

import json
from fractions import Fraction
from pathlib import Path

Z = Fraction(0)
O = Fraction(1)
H = Fraction(1, 2)


def transpose(a):
    return tuple(zip(*a))


def multiply(a, b):
    bt = transpose(b)
    return tuple(tuple(sum(x * y for x, y in zip(row, column)) for column in bt) for row in a)


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(row_a, row_b)) for row_a, row_b in zip(a, b))


def subtract(a, b):
    return tuple(tuple(x - y for x, y in zip(row_a, row_b)) for row_a, row_b in zip(a, b))


def pullback(v, effect):
    return multiply(transpose(v), multiply(effect, v))


def psd_2x2(a):
    return a[0][0] >= 0 and a[1][1] >= 0 and a[0][0] * a[1][1] - a[0][1] * a[1][0] >= 0 and a[0][1] == a[1][0]


def serializable(a):
    return [[str(value) for value in row] for row in a]


I = ((O, Z), (Z, O))
E_H = ((O, Z), (Z, Z))
E_V = ((Z, Z), (Z, O))
LOSS = ((O, Z), (Z, H))
SWAP = ((Z, O), (O, Z))

pull_h = pullback(LOSS, E_H)
pull_v = pullback(LOSS, E_V)
pulled_sum = add(pull_h, pull_v)
loss_effect = subtract(I, multiply(transpose(LOSS), LOSS))
swap_sum = add(pullback(SWAP, E_H), pullback(SWAP, E_V))

# Direct pullback through SWAP after LOSS versus iterated pullback.
composite = multiply(SWAP, LOSS)
direct = pullback(composite, E_H)
iterated = pullback(LOSS, pullback(SWAP, E_H))

checks = {
    "target_detector_family_is_normalized": add(E_H, E_V) == I,
    "loss_map_is_contractive": psd_2x2(subtract(I, multiply(transpose(LOSS), LOSS))),
    "individual_effects_remain_positive": psd_2x2(pull_h) and psd_2x2(pull_v),
    "pulled_sum_equals_v_star_v": pulled_sum == multiply(transpose(LOSS), LOSS),
    "loss_breaks_detector_normalization": pulled_sum != I,
    "loss_effect_is_positive": psd_2x2(loss_effect),
    "loss_effect_restores_normalization": add(pulled_sum, loss_effect) == I,
    "isometric_swap_preserves_normalization": swap_sum == I,
    "direct_and_iterated_conjugation_agree": direct == iterated,
    "attenuated_vertical_effect_has_exact_quarter_weight": pull_v == ((Z, Z), (Z, Fraction(1, 4))),
    "missing_vertical_weight_is_exact_three_quarters": loss_effect == ((Z, Z), (Z, Fraction(3, 4))),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.continuous-mode-effect-pullback.v1", "status": "passed", "checks": checks, "pulled_horizontal": serializable(pull_h), "pulled_vertical": serializable(pull_v), "pulled_sum": serializable(pulled_sum), "loss_effect": serializable(loss_effect), "claim_boundary": "Exact two-mode compression of bounded-operator identities; not a continuous-spectrum or laboratory realization certificate."}
output = Path(__file__).parents[1] / "results" / "continuous_mode_effect_pullback.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "loss_effect": serializable(loss_effect)}, sort_keys=True))
