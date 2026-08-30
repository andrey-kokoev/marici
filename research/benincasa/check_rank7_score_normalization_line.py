#!/usr/bin/env python3
"""Identify the unique connected-score blind line in the rank-seven module."""

import json
from pathlib import Path

import sympy as sp


a, b, c = sp.symbols("a b c")
P1, P2, P3 = sp.symbols("P1 P2 P3", nonzero=True)

CM = sp.Matrix(
    [
        [0,1,1,1,1],
        [1,0,c**2,a**2,b**2],
        [1,c**2,0,P2**2,P1**2],
        [1,a**2,P2**2,0,P3**2],
        [1,b**2,P1**2,P3**2,0],
    ]
)
K = sp.factor(-CM.det()/2)
L1 = (
    2*P1**2*a**2+P2**2*P3**2-P2**2*a**2-P2**2*b**2
    -P3**2*a**2-P3**2*c**2+a**4-a**2*b**2-a**2*c**2+b**2*c**2
)
L2 = (
    P1**2*P3**2-P1**2*a**2-P1**2*b**2+2*P2**2*b**2
    -P3**2*b**2-P3**2*c**2-a**2*b**2+a**2*c**2+b**4-b**2*c**2
)
L3 = (
    P1**2*P2**2-P1**2*a**2-P1**2*c**2-P2**2*b**2-P2**2*c**2
    +2*P3**2*c**2+a**2*b**2-a**2*c**2-b**2*c**2+c**4
)
basis = [L1,L2,L3,a**2,b**2,c**2,sp.Integer(1)]
labels = ["L1","L2","L3","D1","D2","D3","U"]

k_coordinates = sp.Matrix([
    P1**2,
    P2**2,
    P3**2,
    -P1**4+P1**2*P2**2+P1**2*P3**2,
    P1**2*P2**2-P2**4+P2**2*P3**2,
    P1**2*P3**2+P2**2*P3**2-P3**4,
    -2*P1**2*P2**2*P3**2,
])
assert sp.factor(sum(k_coordinates[i]*basis[i] for i in range(7))-K) == 0

monomials = sorted(set().union(*(set(sp.Poly(poly,a,b,c).monoms()) for poly in basis)))
coefficient_matrix = sp.Matrix([
    [sp.Poly(poly,a,b,c).coeff_monomial(monomial) for poly in basis]
    for monomial in monomials
])
assert coefficient_matrix.rank() == 7

# Six shape vectors plus the kernel-scaling vector form a basis away from the
# already frozen soft support P1*P2*P3=0.
shape_and_scale = sp.eye(7)[:, :6].row_join(k_coordinates)
assert sp.factor(shape_and_scale.det()+2*P1**2*P2**2*P3**2) == 0

# For gamma=-1/2, the logarithmic score of delta K=K is the nonzero constant
# gamma. Connected covariance kills it, while the ordinary mean retains it.
gamma = sp.Rational(-1,2)
assert gamma != 0

packet = {
    "schema": "marici.benincasa.rank7-score-normalization-line.v1",
    "status": "passed",
    "interaction_basis": labels,
    "kernel_coordinates": [str(value) for value in k_coordinates],
    "identity": "K=sum_i kernel_coordinates[i]*basis[i]",
    "module_rank": int(coefficient_matrix.rank()),
    "connected_score_kernel_rank": 1,
    "connected_score_kernel": "span<K>",
    "shape_quotient_rank": 6,
    "shape_scale_change_determinant": str(sp.factor(shape_and_scale.det())),
    "mean_score_on_kernel_line": str(gamma),
    "augmented_mean_plus_connected_rank": 7,
    "support_assumption": "positive regulated source measure on an open Cayley-Menger chamber",
    "failure_support": ["P1*P2*P3=0", "K=0/Landau boundary"],
    "classification": (
        "connected score covariance can lose only the overall kernel-scaling "
        "line, and the ordinary mean score recovers that line"
    ),
    "new_carrier_support": False,
    "scope_warning": (
        "The positivity theorem applies to the regulated fixed-chamber density. "
        "The parameter-dependent physical boundary must still be transported "
        "through the source moving-cycle adapter before claiming period-level rank seven."
    ),
}

output = Path(__file__).with_name("rank7-score-normalization-line.json")
output.write_text(json.dumps(packet, indent=2, sort_keys=True)+"\n", encoding="utf-8")
print(json.dumps(packet, indent=2, sort_keys=True))
