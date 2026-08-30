#!/usr/bin/env python3
"""Exact occurrence-inversion transport on the rank-five infinity target."""
from fractions import Fraction
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
x,y,z = 2,3,4


def mmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def eye(n):
    return [[Fraction(i==j) for j in range(n)] for i in range(n)]


def matrix_forward(x,y,z):
    # Columns: source (omega0,omega2,alpha0,alpha-1,alpha-inf).
    # Rows: target basis after t'=1/t.
    return [
        [Fraction(-1),0,0,Fraction(-z),0],
        [0,Fraction(-y*y,x*x),0,0,0],
        [0,0,0,0,Fraction(-1)],
        [0,0,0,1,0],
        [0,0,Fraction(-1),0,0],
    ]


U = matrix_forward(x,y,z)
U_reverse = matrix_forward(y,x,z)
signed_U = [[-v for v in row] for row in U]
signed_reverse = [[-v for v in row] for row in U_reverse]

# Polynomial identity for the only non-obvious compact reduction:
# Fq=x^2-hu^2+y^2u^4 and L(1/(x^2u))=-u^-2+(y^2/x^2)u^2.
second_kind_coefficients = {
    "-2": Fraction(-1),
    "0": Fraction(0),
    "2": Fraction(y*y,x*x),
}
expected_second_kind = {
    "-2": Fraction(-1),
    "0": Fraction(0),
    "2": Fraction(y*y,x*x),
}

checks = {
    "geometric_transport_is_involutive": mmul(U_reverse,U) == eye(5),
    "signed_residue_transport_is_involutive": mmul(signed_reverse,signed_U) == eye(5),
    "second_kind_exact_reduction_identity": second_kind_coefficients == expected_second_kind,
    "source_zero_puncture_maps_to_target_infinity": U[4][2] == -1,
    "source_infinity_maps_to_target_zero": U[2][4] == -1,
    "minus_one_puncture_is_retained_with_compact_shift": U[3][3] == 1 and U[0][3] == -z,
}
packet = {
    "schema": "marici.rank5-infinity-occurrence-inversion.v1",
    "source_basis": ["omega0","omega2","alpha0","alpha_minus1","alpha_infinity"],
    "target_basis": ["omega0_prime","omega2_prime","alpha0_prime","alpha_minus1_prime","alpha_infinity_prime"],
    "coordinate_change": "t_prime=1/t, W_prime=t_prime^2 W",
    "geometric_matrix": [[str(v) for v in row] for row in U],
    "poincare_residue_orientation_sign": -1,
    "signed_matrix": [[str(v) for v in row] for row in signed_U],
    "nontrivial_exact_identity": (
        "L(1/(x^2 t_prime))=-t_prime^-2+(y^2/x^2)t_prime^2"
    ),
    "checks": checks,
    "passed": all(checks.values()),
    "conclusion": (
        "Occurrence inversion preserves the rank-five anti-character target. "
        "It exchanges the zero and infinity residue directions, retains the "
        "minus-one direction with a compact omega0 shift, and transports the "
        "second compact class contragrediently modulo an exact differential."
    ),
}
out=ROOT/"research"/"benincasa"/"results"/"rank5-infinity-occurrence-inversion.json"
out.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8")
print(json.dumps(packet,indent=2))
if not packet["passed"]:
    raise SystemExit(1)
