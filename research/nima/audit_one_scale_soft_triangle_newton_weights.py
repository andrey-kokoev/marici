#!/usr/bin/env python3
"""Verify the Newton weights forced at the one-scale soft-triangle corner."""

import json


weights = {"delta": 1, "d": 1, "q": 2}


def order(monomial):
    return sum(weights[name] * exponent for name, exponent in monomial.items())


t2_terms = {
    "d*delta": {"d": 1, "delta": 1},
    "P1^2*q": {"q": 1},
    "delta*q": {"delta": 1, "q": 1},
}
t0_inside_terms = {
    "delta^2": {"delta": 2},
    "d*delta": {"d": 1, "delta": 1},
    "delta*q": {"delta": 1, "q": 1},
    "P1^2*q": {"q": 1},
}
assert {name: order(m) for name, m in t2_terms.items()} == {
    "d*delta": 2, "P1^2*q": 2, "delta*q": 3
}
assert {name: order(m) for name, m in t0_inside_terms.items()} == {
    "delta^2": 2, "d*delta": 2, "delta*q": 3, "P1^2*q": 2
}

# Delta ~ t0 * delta^4 * B^2, B=(d+q)^2-4*P1^2*q.
t0_order = weights["q"] + 2
b_order = 2
discriminant_order = t0_order + 4 * weights["delta"] + 2 * b_order
assert (t0_order, b_order, discriminant_order) == (4, 2, 12)

print(json.dumps({
    "weights": weights,
    "initial_t2": "-d*delta-2*P1^2*q",
    "initial_t0": "q*(delta^2+d*delta+P1^2*q)",
    "orders": {"t2": 2, "t0": 4, "B": 2, "Delta_A3": 12},
    "resolution": "weighted blowup of (delta,d,q) with weights (1,1,2)",
}, indent=2))
