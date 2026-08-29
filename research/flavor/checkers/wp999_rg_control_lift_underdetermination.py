import json
from pathlib import Path

import sympy as sp

x, Q, R = sp.symbols("x Q R")
coords = (x, Q, R)


def bracket(a, b):
    return tuple(
        sp.expand(sum(a[j] * sp.diff(b[i], coords[j]) - b[j] * sp.diff(a[i], coords[j]) for j in range(3)))
        for i in range(3)
    )


# x is a placeholder physical16 direction. Both lifts project to the same
# arbitrary nonzero physical vector field x*d_x.
f0 = (x, sp.Integer(0), sp.Integer(0))
f1 = (x, sp.Integer(0), Q)
u = (sp.Integer(0), sp.Integer(1), sp.Integer(0))

assert f0[0] == f1[0]
assert bracket(f0, u) == (0, 0, 0)
assert bracket(f1, u) == (0, 0, -1)

rank0 = sp.Matrix.hstack(sp.Matrix(u), sp.Matrix(bracket(f0, u))).rank()
rank1 = sp.Matrix.hstack(sp.Matrix(u), sp.Matrix(bracket(f1, u))).rank()
assert rank0 == 1
assert rank1 == 2

# Deliberate-failure test: equal physical projections must not be mistaken for
# equal coefficient brackets.
assert bracket(f0, u) != bracket(f1, u)

result = {
    "schema": "marici.flavor.wp999.v1",
    "status": "PASS",
    "physical_projection": "x partial_x for both lifts",
    "zero_coefficient_lift": {"coefficient_drift": [0, 0], "bracket_rank": rank0},
    "transverse_coefficient_lift": {"coefficient_drift": [0, "Q"], "bracket_rank": rank1},
    "conclusion": "physical16 RG projection does not determine coefficient-plane accessibility",
    "first_missing_arrow": "source-derived common-substrate RG-to-(Q,R) lift",
    "instrument": "absent",
}

out = Path(__file__).parents[1] / "results" / "wp999_rg_control_lift_underdetermination.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("WP999 PASS: identical physical RG projections admit rank-one and rank-two coefficient lifts")

