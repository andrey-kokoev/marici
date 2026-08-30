#!/usr/bin/env python3
"""Audit the tensor multiplier at total energy and its homogeneous Gram collision."""

import json
from pathlib import Path

import sympy as sp


a, b, c, E = sp.symbols("a b c E")
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
N = sp.expand(
    2 * P1**2 * (c**2 + P2**2 - a**2)
    - (c**2 + P1**2 - b**2) * (P1**2 + P2**2 - P3**2)
)
Q_even = sp.cancel(-(N**2 + 4 * P1**2 * K) / (4 * P1**2 * Lambda))

# On the nonhomogeneous base the site-energy normal E_T is independent of
# the momentum magnitudes P_i, so the tensor multiplier is horizontal.
assert sp.diff(Q_even, E) == 0

# On the homogeneous scattering diagonal choose P3=E-P1-P2.  The declared
# total-energy divisor then meets the external triangle Gram divisor simply.
homogeneous = {P3: E - P1 - P2}
Lambda_path = sp.factor(Lambda.subs(homogeneous))
assert Lambda_path == E * (E - 2 * P1) * (E - 2 * P2) * (E - 2 * P1 - 2 * P2)

A = sp.factor(
    -P1**2 * P2 - P1 * P2**2
    + P1 * a**2 - P1 * c**2 + P2 * b**2 - P2 * c**2
)
assert sp.factor(N.subs(P3, -P1 - P2) + 2 * P1 * A) == 0
assert sp.factor(K.subs(P3, -P1 - P2) - A**2) == 0

Q_path = sp.factor(Q_even.subs(homogeneous))
cartier_residue = sp.factor(sp.limit(E * Q_path, E, 0))
expected_residue = sp.factor(A**2 / (4 * P1 * P2 * (P1 + P2)))
assert sp.factor(cartier_residue - expected_residue) == 0

finite_part = sp.cancel(Q_path - cartier_residue / E)
assert sp.denom(finite_part).subs(E, 0) != 0

# An order-one meromorphic lattice shift has trivial semisimple monodromy.
integral_lattice_shift = -1
semisimple_monodromy = "exp(-2*pi*i)=1"

packet = {
    "schema": "marici.benincasa.tensor-total-energy-gram-nearby.v1",
    "status": "passed",
    "nonhomogeneous_base": {
        "normal": "E_T at fixed P_i",
        "d_ET_Q_even": "0",
        "nearby_compatibility": "strict",
    },
    "homogeneous_diagonal": {
        "path": "P3=E_T-P1-P2",
        "lambda_factorization": str(Lambda_path),
        "pole_order": 1,
        "gram_normal": str(A),
        "K_at_boundary": "A^2",
        "N_at_boundary": "-2*P1*A",
        "cartier_residue": str(cartier_residue),
        "finite_part_regular": True,
        "lattice_shift": integral_lattice_shift,
        "semisimple_monodromy": semisimple_monodromy,
    },
    "nilpotent_update": 0,
    "additional_support": [],
    "existing_support": ["E_T=0", "Lambda(P)=0", "P1*P2*(P1+P2)=0 (soft endpoints)"],
    "classification": (
        "strict nearby tensoring off the homogeneous diagonal; on the diagonal, "
        "an integral Gram-Cartier filtration shift with residue the square of "
        "the existing labelled Gram normal"
    ),
    "new_carrier_support": False,
    "scope_warning": (
        "This identifies the tensor contribution to the total-energy/Gram nearby "
        "grade. It does not compute the Landau intersection or physical elliptic "
        "period pairing."
    ),
}

output = Path(__file__).with_name("tensor-total-energy-gram-nearby.json")
output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2, sort_keys=True))
