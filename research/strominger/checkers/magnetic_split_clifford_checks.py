#!/usr/bin/env python3
"""Exact split-Clifford model for magnetic parity and its kernel taxonomy."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BOUNDARY = ROOT / "research/strominger/contracts/parity-port-executability-boundary.v1.json"
RESULT = ROOT / "research/strominger/results/magnetic_split_clifford_checks.json"
boundary = json.loads(BOUNDARY.read_text(encoding="utf-8"))

def mm(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))

def ma(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(len(a[0])))
                 for i in range(len(a)))

def ms(c, a):
    return tuple(tuple(c * x for x in row) for row in a)

def kron(a, b):
    return tuple(tuple(a[i // len(b)][j // len(b[0])] * b[i % len(b)][j % len(b[0])]
                       for j in range(len(a[0]) * len(b[0])))
                 for i in range(len(a) * len(b)))

def act(a, v):
    return tuple(sum(a[i][j] * v[j] for j in range(len(v))) for i in range(len(a)))

I2 = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
Z2 = ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(0)))
X = ((Fraction(0), Fraction(1)), (Fraction(1), Fraction(0)))
EP = ms(Fraction(1, 2), ma(I2, X))
EM = ms(Fraction(1, 2), ma(I2, ms(-1, X)))

# Split-Clifford multiplication for a+b epsilon, epsilon^2=1.
def split_mul(x, y):
    a, b = x
    c, d = y
    return (a*c + b*d, a*d + b*c)

ep = (Fraction(1, 2), Fraction(1, 2))
em = (Fraction(1, 2), Fraction(-1, 2))

P = kron(X, I2)
S = kron(I2, X)
Q = mm(P, S)
I4 = kron(I2, I2)
QEP = ms(Fraction(1, 2), ma(I4, Q))
QEM = ms(Fraction(1, 2), ma(I4, ms(-1, Q)))
four_idempotents = []
for rp in (1, -1):
    for rs in (1, -1):
        four_idempotents.append(
            ms(Fraction(1, 4), mm(ma(I4, ms(rp, P)), ma(I4, ms(rs, S))))
        )

fixed_q = ((Fraction(1),),)
fixed_i = ((Fraction(1),),)
fixed_m = ms(Fraction(1, 2), ma(fixed_i, ms(-1, fixed_q)))
free_m_rank_nonzero = EM != Z2
collision_vector = (Fraction(1), Fraction(1))
electric_kernel_vector = (Fraction(1), Fraction(-1))
electric_row = ((Fraction(1), Fraction(1)),)
magnetic_row = ((Fraction(1), Fraction(-1)),)

gates = {
    "split_clifford_generator_squares_to_one": mm(X, X) == I2,
    "primitive_idempotents": split_mul(ep, ep) == ep and split_mul(em, em) == em,
    "orthogonal_zero_divisors": split_mul(ep, em) == (0, 0),
    "resolution_of_identity": ma(EP, EM) == I2,
    "sheet_encoding_yields_sum_and_difference":
        split_mul(ep, (3, 5)) == (4, 4)
        and split_mul(em, (3, 5)) == (-1, 1),
    "source_involutions_commute": mm(P, S) == mm(S, P),
    "source_involutions_are_not_clifford_anticommuting_generators":
        ma(mm(P, S), mm(S, P)) != tuple(tuple(Fraction(0) for _ in range(4)) for _ in range(4)),
    "klein_four_has_four_primitive_sectors":
        ma(ma(four_idempotents[0], four_idempotents[1]),
           ma(four_idempotents[2], four_idempotents[3])) == I4,
    "physical_q_has_two_rank_two_ideals":
        ma(QEP, QEM) == I4 and mm(QEP, QEM) == tuple(tuple(Fraction(0) for _ in range(4)) for _ in range(4)),
    "fixed_orbit_structurally_lacks_magnetic_ideal": fixed_m == ((0,),),
    "free_orbit_has_magnetic_ideal_but_collision_can_avoid_it":
        free_m_rank_nonzero and act(EM, collision_vector) == (0, 0),
    "electric_port_detects_the_magnetic_kernel_line":
        act(magnetic_row, collision_vector) == (0,)
        and act(electric_row, collision_vector) == (2,),
    "magnetic_port_detects_the_electric_kernel_line":
        act(electric_row, electric_kernel_vector) == (0,)
        and act(magnetic_row, electric_kernel_vector) == (2,),
    "characteristic_zero_makes_complementary_detection_invertible":
        Fraction(1, 2) * 2 == 1,
    "clifford_splitting_does_not_authorize_joint_instrument":
        not boundary["joint_executability_model"]["atomic_joint_refinement_authorized"],
}
payload = {
    "schema": "marici.strominger.magnetic_split_clifford_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
    "algebra": {
        "parity": "Cl_1_0 = R[epsilon]/(epsilon^2-1) = R direct_sum R",
        "full_commuting_source_symmetry": "Cl_1_0 tensor Cl_1_0 = R[Z2 x Z2] = R^4",
        "warning": "P and sigma commute, so they are not the two anticommuting generators of Cl_2_0"
    },
    "kernel_taxonomy": {
        "tower": "selected Clifford ideal is absent on a fixed orbit",
        "collision_circuit": "selected ideal exists, but the transported combination lands in its complementary annihilator ideal",
        "transport_loss": "excluded by the injective transport theorem"
    },
    "universal_kernel_detection_theorem": "Assuming injective one-sheet transport A and characteristic not two, E restricts injectively to ker(M), and M restricts injectively to ker(E).",
    "operational_boundary": "A complementary port suffices to separate states already known to lie in the opposite kernel. Full arbitrary-state reconstruction still requires a provenance-correct jointly executable refinement."
}
RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["status"] == "passed" else 1)
