"""Exact Möbius-order audit for quadratic Born readouts."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/born-mobius-interference-order.json"


def subsets(items: tuple[int, ...]):
    for size in range(len(items) + 1):
        yield from combinations(items, size)


def mobius_coefficient(values: dict[tuple[int, ...], sp.Expr], full: tuple[int, ...]):
    return sp.expand(
        sum(
            (-1) ** (len(full) - len(part)) * values[part]
            for part in subsets(full)
        )
    )


max_order = 7
x = sp.symbols(f"x0:{max_order}")
y = sp.symbols(f"y0:{max_order}")
mobius = {}
for order in range(1, max_order + 1):
    full = tuple(range(order))
    values = {}
    for part in subsets(full):
        amplitude = sum((x[i] for i in part), sp.Integer(0))
        conjugate = sum((y[i] for i in part), sp.Integer(0))
        values[part] = sp.expand(amplitude * conjugate)
    mobius[order] = sp.simplify(mobius_coefficient(values, full))

# A hostile readout: normalize each subset separately by an accepted-rate
# denominator 2+p.  With three unit amplitudes this creates a nonzero I3 even
# though the underlying common quadratic measure has I3=0.
full3 = (0, 1, 2)
raw_cardinality_values = {
    part: sp.Integer(len(part) ** 2) for part in subsets(full3)
}
raw_i3 = mobius_coefficient(raw_cardinality_values, full3)
conditioned_values = {
    part: (
        sp.Rational(raw_cardinality_values[part], 2 + raw_cardinality_values[part])
        if part
        else sp.Integer(0)
    )
    for part in subsets(full3)
}
conditioned_i3 = sp.simplify(mobius_coefficient(conditioned_values, full3))

gates = {
    "first_order_is_nonzero": mobius[1] != 0,
    "second_order_is_pair_coherence": mobius[2] == x[0] * y[1] + x[1] * y[0],
    "all_orders_three_through_seven_vanish": all(
        mobius[order] == 0 for order in range(3, max_order + 1)
    ),
    "raw_three_path_statistic_vanishes": raw_i3 == 0,
    "subset_dependent_conditioning_fakes_nonzero_i3": conditioned_i3 != 0,
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.born-mobius-interference-order.v1",
    "mobius_coefficients": {str(order): str(value) for order, value in mobius.items()},
    "raw_three_unit_path_i3": str(raw_i3),
    "conditioned_three_unit_path_i3": str(conditioned_i3),
    "conditioned_subset_values": {
        str(part): str(value) for part, value in conditioned_values.items()
    },
    "gates": gates,
    "conclusion": (
        "A common quadratic Born measure has Möbius interference order at "
        "most two. The rank-three exterior port constrains the pairwise "
        "coherence packet but is not a cubic screen term. Independent "
        "subset normalization can create a spurious nonzero I3."
    ),
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))

