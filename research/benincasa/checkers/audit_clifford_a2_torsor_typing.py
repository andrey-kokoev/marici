#!/usr/bin/env python3
"""Type the cyclic e6 torsor as an A2 logarithmic cocycle, not an intertwiner."""

import json
from pathlib import Path

import sympy as sp


P = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
augmentation = sp.Matrix([[1, 1, 1]])

# Columns span the degree-zero soft-divisor lattice A2 in Q^3.
A2 = sp.Matrix([[1, 0], [-1, 1], [0, -1]])
assert augmentation * A2 == sp.zeros(1, 2)

# Induced cyclic action on the A2 basis.
R = (A2.T * A2).inv() * A2.T * P * A2
assert A2 * R == P * A2

# A row h:A2->Q_triv is equivariant when h R = h.
h1, h2 = sp.symbols("h1 h2")
h = sp.Matrix([[h1, h2]])
solutions = sp.linsolve(list(h * R - h), (h1, h2))

candidate_root = sp.Matrix([0, -1, 1])  # div(X3/X2)
orbit = sp.Matrix.hstack(candidate_root, P * candidate_root, P**2 * candidate_root)

checks = {
    "P_order_three": P**3 == sp.eye(3),
    "A2_preserved": A2 * R == P * A2,
    "A2_has_no_trivial_quotient_map": solutions == {(0, 0)},
    "candidate_is_degree_zero": (augmentation * candidate_root)[0] == 0,
    "candidate_is_primitive": sp.gcd_list(list(candidate_root)) == 1,
    "root_orbit_rank_two": orbit.rank() == 2,
    "root_orbit_closes": sum((P**i * candidate_root for i in range(3)), sp.zeros(3, 1)) == sp.zeros(3, 1),
}

packet = {
    "schema": "marici.benincasa.clifford_a2_torsor_typing.v1",
    "soft_divisor_basis": ["X1=0", "X2=0", "X3=0"],
    "degree_zero_lattice": "A2 = ker(sum: Z^3 -> Z)",
    "cyclic_matrix_ambient": [[int(value) for value in row] for row in P.tolist()],
    "cyclic_matrix_A2": [[int(value) for value in row] for row in R.tolist()],
    "candidate_root": [int(value) for value in candidate_root],
    "candidate_meaning": "div(X3/X2)",
    "equivariant_Hom_A2_to_trivial_dimension": 0,
    "root_orbit_rank": orbit.rank(),
    "checks": checks,
    "verdict": (
        "The candidate is a primitive A2 boundary root and logarithmic Cech "
        "cocycle, not an ordinary C3-equivariant map into a trivial e6 line."
    ),
    "generic_vs_boundary": {
        "generic_energy_torus": "dlog(X3/X2) is a change of rational frame",
        "soft_compactification": "its divisor (0,-1,1) obstructs removal by a boundary-regular gauge",
    },
    "next_gate": (
        "Test the rank-twelve extension as a logarithmic lattice descent "
        "problem across cyclic occurrence charts, not as Hom_C3(A2,e6)."
    ),
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[key for key, ok in checks.items() if not ok]}")

out = Path(__file__).resolve().parents[1] / "results" / "clifford_a2_torsor_typing.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
