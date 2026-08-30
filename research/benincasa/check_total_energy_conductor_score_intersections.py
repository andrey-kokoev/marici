"""Exact total-energy/conductor intersection and observer audit.

The calculation keeps the conductor quotient in its primitive integral
half-Kummer frame and imports only the already certified exceptional score
matrices.  It does not infer a vector-valued localization morphism from a
scalar period.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
SCORE_PACKET = ROOT / "total-energy-score-soft-rees.json"
OUTPUT = ROOT / "total-energy-conductor-score-intersections.json"


E, x, y = sp.symbols("E x y")

delta1 = 4 * x * (x * y**2 + 2 * E * x * y - E**2 * (x + 2 * y - E))
delta2 = 4 * y * (x**2 * y + 2 * E * x * y - E**2 * (2 * x + y - E))
special_square = 4 * x**2 * y**2

assert sp.expand(delta1.subs(E, 0) - special_square) == 0
assert sp.expand(delta2.subs(E, 0) - special_square) == 0

# Scheme-theoretic radical after total-energy specialization.  The two
# conductor equations coincide and have no irreducible support besides the
# two labelled soft faces.  The exponents retain the nonreduced order.
factor1 = sp.factor_list(delta1.subs(E, 0))
factor2 = sp.factor_list(delta2.subs(E, 0))
assert factor1 == (4, [(x, 2), (y, 2)])
assert factor2 == factor1

# Primitive conductor frame B=(g101,g110,g111_top).  Around either soft
# normal both Delta_i have valuation two, so a_i=-1/2 dlog Delta_i has
# residue -1.  Entry 308 fixes the half-Kummer top column.
R = sp.Matrix(
    [
        [-1, 0, sp.Rational(-1, 2)],
        [0, -1, sp.Rational(-1, 2)],
        [0, 0, 0],
    ]
)
Q = sp.Matrix(
    [
        [1, 0, sp.Rational(1, 2)],
        [0, 1, sp.Rational(1, 2)],
        [0, 0, 1],
    ]
)
assert R == Q.inv() * sp.diag(-1, -1, 0) * Q

# The local monodromy is therefore identity although the primitive-frame
# residue is not diagonal.  There is no unipotent logarithm.
T = Q.inv() * sp.eye(3) * Q
assert T == sp.eye(3)
N = sp.zeros(3)

with SCORE_PACKET.open(encoding="utf-8") as handle:
    score = json.load(handle)

observer = {}
for face in ("x", "y"):
    packet = score["faces"][face]
    matrices = {
        port: sp.Matrix([[sp.Rational(value) for value in row] for row in rows])
        for port, rows in packet["port_matrices"].items()
    }
    determinants = {port: sp.factor(matrix.det()) for port, matrix in matrices.items()}
    ranks = {port: matrix.rank() for port, matrix in matrices.items()}
    assert all(rank == 3 for rank in ranks.values())
    assert all(value != 0 for value in determinants.values())
    stacked = matrices["g1"].col_join(matrices["g2"]).col_join(matrices["g3"])
    assert stacked.rank() == 3
    assert 3 - stacked.rank() == 0
    observer[face] = {
        "port_ranks": ranks,
        "determinants": {key: str(value) for key, value in determinants.items()},
        "joint_kernel_dimension": 3 - stacked.rank(),
        "local_DVR_isomorphisms": all(packet["local_DVR_isomorphism"].values()),
    }

# Deliberate-failure witnesses: the primitive residue is genuinely nonzero,
# while neither conductor restriction has support away from x*y=0.
assert R != sp.zeros(3)
assert sp.factor(delta1.subs(E, 0) / special_square) == 1
assert sp.factor(delta2.subs(E, 0) / special_square) == 1

result = {
    "schema": "marici.benincasa.total-energy-conductor-score-intersections.v1",
    "total_energy_normal": "E",
    "conductor_discriminants": {
        "Delta1": str(delta1),
        "Delta2": str(delta2),
        "restriction_E0": str(special_square),
        "factorization_E0": "4*x^2*y^2",
        "reduced_support": ["x=0", "y=0"],
        "new_irreducible_support": False,
    },
    "primitive_half_kummer_packet": {
        "basis": ["g101", "g110", "g111_top"],
        "soft_residue_matrix": [[str(value) for value in row] for row in R.tolist()],
        "semisimple_characters": [1, 1, 1],
        "monodromy": [[int(value) for value in row] for row in T.tolist()],
        "nilpotent_logarithm": [[int(value) for value in row] for row in N.tolist()],
        "nilpotent_rank": N.rank(),
    },
    "observer": observer,
    "joint_conclusion": {
        "conductor_total_energy_intersections_are_existing_soft_faces": True,
        "half_kummer_extension_has_trivial_soft_monodromy": True,
        "score_observer_joint_kernel_dimension": 0,
        "observer_cartier_cokernel_length": score["observer_cartier_cokernel_length"],
        "new_carrier_datum": False,
    },
    "scope": (
        "Exact associated-grade theorem on E=0 intersect Delta1*Delta2=0; "
        "does not construct the full rank-twelve localization morphism or tensor ports."
    ),
}

OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result["joint_conclusion"], sort_keys=True))
