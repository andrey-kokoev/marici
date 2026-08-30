#!/usr/bin/env python3
"""Express the physical tensor trace in the frozen rank-seven source module."""

import json
from pathlib import Path

import sympy as sp


a, b, c = sp.symbols("a b c")
P1, P2, P3 = sp.symbols("P1 P2 P3", nonzero=True)

CM = sp.Matrix(
    [
        [0, 1, 1, 1, 1],
        [1, 0, c**2, a**2, b**2],
        [1, c**2, 0, P2**2, P1**2],
        [1, a**2, P2**2, 0, P3**2],
        [1, b**2, P1**2, P3**2, 0],
    ]
)
K = sp.factor(-CM.det() / 2)
Lambda = sp.factor(
    (P1 - P2 - P3) * (P1 - P2 + P3) * (P1 + P2 - P3) * (P1 + P2 + P3)
)

# Site-1 numerator from the exact CM trilateration of Entry 2443.
N = sp.expand(
    2 * P1**2 * (c**2 + P2**2 - a**2)
    - (c**2 + P1**2 - b**2) * (P1**2 + P2**2 - P3**2)
)
Q_even = sp.cancel(-(N**2 + 4 * P1**2 * K) / (4 * P1**2 * Lambda))

L1 = (
    2 * P1**2 * a**2
    + P2**2 * P3**2
    - P2**2 * a**2
    - P2**2 * b**2
    - P3**2 * a**2
    - P3**2 * c**2
    + a**4
    - a**2 * b**2
    - a**2 * c**2
    + b**2 * c**2
)
L2 = (
    P1**2 * P3**2
    - P1**2 * a**2
    - P1**2 * b**2
    + 2 * P2**2 * b**2
    - P3**2 * b**2
    - P3**2 * c**2
    - a**2 * b**2
    + a**2 * c**2
    + b**4
    - b**2 * c**2
)
L3 = (
    P1**2 * P2**2
    - P1**2 * a**2
    - P1**2 * c**2
    - P2**2 * b**2
    - P2**2 * c**2
    + 2 * P3**2 * c**2
    + a**2 * b**2
    - a**2 * c**2
    - b**2 * c**2
    + c**4
)
basis = [L1, L2, L3, a**2, b**2, c**2, sp.Integer(1)]
basis_labels = ["L1", "L2", "L3", "D1=a^2", "D2=b^2", "D3=c^2", "U=1"]

monomials = sorted(
    set().union(*(set(sp.Poly(poly, a, b, c).monoms()) for poly in basis + [Q_even]))
)
matrix = sp.Matrix(
    [[sp.Poly(poly, a, b, c).coeff_monomial(monomial) for poly in basis] for monomial in monomials]
)
target = sp.Matrix(
    [sp.Poly(Q_even, a, b, c).coeff_monomial(monomial) for monomial in monomials]
)
solution_set = sp.linsolve((matrix, target))
assert len(solution_set.args) == 1
coordinates = [sp.factor(value) for value in next(iter(solution_set))]
assert len(coordinates) == 7
assert sp.factor(sum(value * vector for value, vector in zip(coordinates, basis)) - Q_even) == 0
assert matrix.rank() == 7

# All coordinate denominators are supported on the already frozen soft/Gram
# divisor P1*Lambda=0.
for coordinate in coordinates:
    denominator = sp.factor(sp.denom(sp.cancel(coordinate)))
    residual = sp.cancel((P1**8 * Lambda**2) / denominator)
    # Every irreducible denominator factor must divide a sufficiently large
    # power of the declared support polynomial.
    assert sp.denom(residual) == 1

# Cyclic relabelling preserves the module and generates the other two traces.
cyclic = {a: b, b: c, c: a, P1: P2, P2: P3, P3: P1}
cyclic_basis = [sp.expand(poly.xreplace(cyclic)) for poly in basis]
assert sp.Matrix(
    [
        [sp.Poly(poly, a, b, c).coeff_monomial(monomial) for poly in cyclic_basis]
        for monomial in monomials
    ]
).rank() == 7

packet = {
    "schema": "marici.benincasa.parity-even-tensor-rank7-module.v1",
    "status": "passed",
    "source_basis": basis_labels,
    "source_module_rank": matrix.rank(),
    "site1_tensor_trace": str(sp.factor(Q_even)),
    "site1_coordinates": {
        label: str(value) for label, value in zip(basis_labels, coordinates)
    },
    "cyclic_closure": True,
    "coefficient_denominator_support": ["P_i=0", "Lambda(P1,P2,P3)=0"],
    "rank60_action": {
        "source": "Entry 2419",
        "rank": 7,
        "additional_tensor_source_dimension": 0,
        "additional_generic_action_kernel": 0,
    },
    "classification": "the physical parity-even tensor trace is an existing rank-seven interaction-module element",
    "new_carrier_support": False,
    "scope_warning": (
        "Module membership and Entry 2419 type the generic rank-60 action. "
        "They do not construct the Ward/contact total differential or the "
        "supported Gram specialization of the singular coordinate vector."
    ),
}

output = Path(__file__).with_name("parity-even-tensor-rank7-module.json")
output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2, sort_keys=True))
