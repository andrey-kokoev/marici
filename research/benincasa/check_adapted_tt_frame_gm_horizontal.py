#!/usr/bin/env python3
"""Projected Gauss-Manin transport of the external-triangle TT frame."""

import json
from pathlib import Path

import sympy as sp


theta = sp.symbols("theta", real=True)
qhat = sp.Matrix([sp.cos(theta), sp.sin(theta), 0])
n = sp.Matrix([0, 0, 1])
t = n.cross(qhat)

assert sp.simplify(qhat.dot(qhat)) == 1
assert sp.simplify(n.dot(n)) == 1
assert sp.simplify(t.dot(t)) == 1
assert sp.simplify(qhat.dot(n)) == 0
assert sp.simplify(qhat.dot(t)) == 0
assert sp.simplify(n.dot(t)) == 0

pi = sp.simplify(sp.eye(3) - qhat * qhat.T)


def tt_project(matrix):
    transverse = sp.simplify(pi * matrix * pi)
    transverse_trace = sp.simplify(sp.trace(pi * matrix))
    return sp.simplify(transverse - pi * transverse_trace / 2)


plus = sp.simplify(t * t.T - n * n.T)
cross = sp.simplify(t * n.T + n * t.T)
assert sp.simplify(tt_project(plus) - plus) == sp.zeros(3)
assert sp.simplify(tt_project(cross) - cross) == sp.zeros(3)

d_plus = plus.diff(theta)
d_cross = cross.diff(theta)
assert sp.simplify(tt_project(d_plus)) == sp.zeros(3)
assert sp.simplify(tt_project(d_cross)) == sp.zeros(3)

# The frame therefore has zero induced 2x2 connection in the source-adapted
# basis, even though its ambient Cartesian representatives vary.
gram = sp.Matrix(
    [
        [sp.trace(plus.T * plus), sp.trace(plus.T * cross)],
        [sp.trace(cross.T * plus), sp.trace(cross.T * cross)],
    ]
)
connection_numerators = sp.Matrix(
    [
        [sp.trace(plus.T * tt_project(d_plus)), sp.trace(plus.T * tt_project(d_cross))],
        [sp.trace(cross.T * tt_project(d_plus)), sp.trace(cross.T * tt_project(d_cross))],
    ]
)
assert sp.simplify(gram - 2 * sp.eye(2)) == sp.zeros(2)
assert sp.simplify(connection_numerators) == sp.zeros(2)

# Reversing the external-plane orientation flips n and t together and fixes
# both spin-two tensors.
plus_reversed = (-t) * (-t).T - (-n) * (-n).T
cross_reversed = (-t) * (-n).T + (-n) * (-t).T
assert sp.simplify(plus_reversed - plus) == sp.zeros(3)
assert sp.simplify(cross_reversed - cross) == sp.zeros(3)

# One full angular turn has identity spin-two transport.
assert sp.simplify(plus.subs(theta, theta + 2 * sp.pi) - plus) == sp.zeros(3)
assert sp.simplify(cross.subs(theta, theta + 2 * sp.pi) - cross) == sp.zeros(3)

packet = {
    "schema": "marici.benincasa.adapted-tt-frame-gm-horizontal.v1",
    "status": "passed",
    "frame": {
        "qhat": [str(value) for value in qhat],
        "external_normal": [str(value) for value in n],
        "in_plane_transverse": [str(value) for value in t],
        "plus": [[str(value) for value in row] for row in plus.tolist()],
        "cross": [[str(value) for value in row] for row in cross.tolist()],
    },
    "induced_connection": {
        "basis_gram": [[str(sp.simplify(value)) for value in row] for row in gram.tolist()],
        "matrix": [[0, 0], [0, 0]],
        "reason": "ambient frame derivatives are longitudinal and vanish after TT projection",
    },
    "orientation_descent": {
        "external_normal_reversal": "identity on plus and cross",
        "full_turn_monodromy": "identity",
    },
    "compatibility": {
        "scalar_GM": "acts on the rank-seven coefficient module",
        "TT_GM": "trivial in the adapted frame",
        "tensor_product_connection": "strict on the generic non-Gram locus",
    },
    "failure_support": "external Gram wall where the plane normal is undefined",
    "new_carrier_support": False,
    "scope_warning": (
        "This is the rotational-invariant unequal-magnitude base with its "
        "source-adapted external-triangle frame. Arbitrary independent motion "
        "of tensor directions would require the full spin-two polarization connection."
    ),
}

output = Path(__file__).with_name("adapted-tt-frame-gm-horizontal.json")
output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2, sort_keys=True))
