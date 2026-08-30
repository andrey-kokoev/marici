#!/usr/bin/env python3
"""Test the canonical H1 phase-null jet against the second connected port."""

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT = ROOT / "research/strominger/results/deutschean_h2_phase_null_probe.json"
T, k = s.symbols("T k")
N = 5
b = s.Rational(5, 4)
c = s.Rational(3, 2)


def tr(expression):
    expression = s.series(expression, k, 0, 2).removeO()
    return s.series(expression, T, 0, N).removeO().expand()


g = (
    33*T**2 - 31*T**3 + s.Rational(273,16)*T**4
    - s.Rational(731,104)*T**5 + s.Rational(61429,24960)*T**6
)
z = tr(T*s.exp(-T) - k*T*s.diff(g,T))
zprime = tr(s.diff(z,T))


def E(expression):
    return tr(tr(z/zprime)*s.diff(expression,T))


h = tr(T*zprime/z)
S0 = tr(1+s.log(T/z)+(s.exp(-T)-1+k*g)/z)
S1 = tr(-(b+1)*T+s.log(T/z)-s.log(h)/2)
F3 = tr(2 + T**3/z*(-s.exp(-T)+k*s.diff(g,T,3)))
F4 = tr(-6 + T**4/z*(s.exp(-T)+k*s.diff(g,T,4)))
A = b+1
S2 = tr(
    c*z*s.exp(T) + A**2*T**2/(2*h) - A*T*F3/(2*h**2)
    + F4/(8*h**2) + 5*F3**2/(24*h**3) - s.Rational(1,12)
)
A0=tr(S0+E(S0)); A1=E(S1); A2=tr(E(S2)-S2)
Q0=tr(1+E(A0))
Q1=tr(-s.Rational(1,2)*(E(E(A0))-E(A0))+E(A1)-A1)
Q2=tr(
    s.Rational(1,3)*E(A0)-s.Rational(1,2)*E(E(A0))+s.Rational(1,6)*E(E(E(A0)))
    -A1+s.Rational(3,2)*E(A1)-s.Rational(1,2)*E(E(A1))+E(A2)-2*A2
)
V0=tr(1-1/Q0); V1=tr(Q1/Q0**2); V2=tr(Q2/Q0**2-Q1**2/Q0**3)


def dR(expression):
    return tr(s.diff(expression,T)/s.diff(V0,T))


W0=tr(s.log(V0/z))
H1=tr(V1/V0-(V1-4*V0)*dR(W0))
d1=tr(V1-4*V0); d2=tr(V2-4*V1)
H2=tr(
    V2/V0-s.Rational(1,2)*(V1/V0)**2-d2*dR(W0)
    -s.Rational(1,2)*d1**2*dR(dR(W0))-4*H1-d1*dR(H1)
)
variation=tr(
    s.diff(H2,k).subs(k,0)
    - s.diff(H2.subs(k,0),T)*s.diff(V0,k).subs(k,0)
)

baseline = s.expand(H2.subs(k, 0))
checks = {
    "baseline_H2_T2_matches_exact_source": baseline.coeff(T,2) == s.Rational(391,48),
    "H1_null_jet_is_detected_by_H2": variation != 0,
    "leading_H2_obstruction_is_minus_1065_over_2": variation.coeff(T,2) == -s.Rational(1065,2),
}
payload = {
    "artifact_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
    "checks": checks,
    "observed": {
        "phase_null_jet": str(g),
        "H2_first_variation_at_fixed_leading_coordinate": str(variation),
        "leading_obstruction_grade": 2,
        "leading_obstruction": "-1065/2",
    },
    "passed": all(checks.values()),
    "semantic_boundary": (
        "Finite exact jet test at the leading T^2 obstruction. It proves that the canonical H1-null "
        "direction is not in the H2 kernel; it does not classify the full joint "
        "kernel away from this one-dimensional H1 phase-null line."
    ),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)
