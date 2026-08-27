#!/usr/bin/env python3
"""Exact all-grade H1/H2 test of the closed mixed source circuit."""

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT = ROOT / "research/strominger/results/deutschean_closed_mixed_circuit.json"
T, k = s.symbols("T k")
primitive = s.exp(-T) - 1 + T
g = s.Rational(2, 3) * (1 - (1 + T) * s.exp(-T))
b = s.Rational(5, 4) + s.Rational(3, 2) * k
c = s.Rational(3, 2) + k
z = T*s.exp(-T) - k*T*s.diff(g,T)


def E(expression):
    return s.factor(z/s.diff(z,T)*s.diff(expression,T))


h = s.factor(T*s.diff(z,T)/z)
S0 = 1+s.log(T/z)+(s.exp(-T)-1+k*g)/z
S1 = -(b+1)*T+s.log(T/z)-s.log(h)/2
F3 = 2+T**3/z*(-s.exp(-T)+k*s.diff(g,T,3))
F4 = -6+T**4/z*(s.exp(-T)+k*s.diff(g,T,4))
A = b+1
S2 = s.factor(
    c*z*s.exp(T) + A**2*T**2/(2*h) - A*T*F3/(2*h**2)
    + F4/(8*h**2) + s.Rational(5,24)*F3**2/h**3 - s.Rational(1,12)
)
A0=s.factor(S0+E(S0)); A1=E(S1); A2=s.factor(E(S2)-S2)
Q0=s.factor(1+E(A0))
Q1=s.factor(-s.Rational(1,2)*(E(E(A0))-E(A0))+E(A1)-A1)
Q2=s.factor(
    s.Rational(1,3)*E(A0)-s.Rational(1,2)*E(E(A0))+s.Rational(1,6)*E(E(E(A0)))
    -A1+s.Rational(3,2)*E(A1)-s.Rational(1,2)*E(E(A1))+E(A2)-2*A2
)
V0=s.factor(1-1/Q0)
V1=s.factor(Q1/Q0**2)
V2=s.factor(Q2/Q0**2-Q1**2/Q0**3)


def dR(expression):
    return s.factor(s.diff(expression,T)/s.diff(V0,T))


W0=s.log(V0/z)
H1=s.factor(V1/V0-(V1-4*V0)*dR(W0))
d1=V1-4*V0; d2=V2-4*V1
H2=s.factor(
    V2/V0-s.Rational(1,2)*(V1/V0)**2-d2*dR(W0)
    -s.Rational(1,2)*d1**2*dR(dR(W0))-4*H1-d1*dR(H1)
)


def fixed_leading_variation(expression):
    return s.factor(
        s.diff(expression,k).subs(k,0)
        - s.diff(expression.subs(k,0),T)*s.diff(V0,k).subs(k,0)
    )


DH1 = fixed_leading_variation(H1)
DH2 = fixed_leading_variation(H2)
euler_form = s.factor(s.Rational(2,3)*(T*s.diff(primitive,T)-primitive))
checks = {
    "closed_jet_matches_primitive_circuit_series": s.simplify(
        s.series(g,T,0,10).removeO() - s.series(
        T**2/s.Integer(3)-2*T**3/s.Integer(9)+T**4/s.Integer(12)-T**5/s.Integer(45)
        +T**6/s.Integer(216)-T**7/s.Integer(1260)+T**8/s.Integer(8640)-T**9/s.Integer(68040),
        T,0,10).removeO()
    ) == 0,
    "mixed_phase_is_euler_primitive_variation": s.simplify(g-euler_form) == 0,
    "closed_mixed_circuit_annihilates_H1": DH1 == 0,
    "closed_mixed_circuit_has_exact_H2_obstruction": s.simplify(
        DH2 - 2*T**2*(T**2-2)
    ) == 0,
}
payload = {
    "artifact_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
    "checks": checks,
    "observed": {
        "phase_deformation": str(g),
        "delta_b": "3/2",
        "delta_c": "1",
        "DH1": str(DH1),
        "DH2": str(DH2),
        "primitive_euler_form": str(euler_form),
    },
    "passed": all(checks.values()),
    "semantic_boundary": (
        "Exact tangent theorem: the circuit annihilates H1 but H2 detects it as "
        "2*T^2*(T^2-2). Earlier H2 cancellation came from incorrectly freezing "
        "z*exp(T)=T under phase deformation."
    ),
}
RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,indent=2))
raise SystemExit(0 if payload["passed"] else 1)
