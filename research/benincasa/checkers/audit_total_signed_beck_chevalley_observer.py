#!/usr/bin/env python3
"""Audit the total-energy/signed-energy Beck--Chevalley observer identity."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa" / ".tmp_sympy"))

import sympy as sp


u, v = sp.symbols("u v")
SOURCE = ROOT / "research" / "benincasa" / "marked-wall-quotient-connection.json"
RESULT = ROOT / "research" / "benincasa" / "results" / "total_signed_beck_chevalley_observer.json"


def matrix(packet: dict, axis: str) -> sp.Matrix:
    D = sp.sympify(packet["D"])
    H = sp.sympify(packet["H"])
    repl = {sp.Symbol("D"): D, sp.Symbol("H"): H}
    a = {k: sp.sympify(value).subs(repl) for k, value in packet[axis].items()}
    return sp.Matrix(
        [
            [a["alpha"], 0, 0],
            [a["beta1"], a["gamma1"], 0],
            [a["beta2"], 0, a["gamma2"]],
        ]
    )


def strings(m: sp.Matrix) -> list[list[str]]:
    return [[str(sp.factor(x)) for x in row] for row in m.tolist()]


def main() -> None:
    packet = json.loads(SOURCE.read_text(encoding="utf-8"))
    Au = matrix(packet, "u")
    Av = matrix(packet, "v")
    curvature = Au.diff(v) * 0  # preserve shape
    curvature = Av.diff(u) - Au.diff(v) + Au * Av - Av * Au
    assert all(sp.cancel(x) == 0 for x in curvature)

    R = Au.applyfunc(lambda x: sp.factor(sp.limit(u * x, u, 0)))
    S = Av.subs(u, 0).applyfunc(sp.factor)
    bc = R.diff(v) - (R * S - S * R)
    assert all(sp.cancel(x) == 0 for x in bc)

    mu = sp.Matrix([[1, 0, 0]])
    hidden = sp.Matrix([0, 1, 1])
    derivative_route = mu * R.diff(v).T
    commutator_route = mu * (S.T * R.T - R.T * S.T)
    observer_defect = (derivative_route - commutator_route).applyfunc(sp.cancel)
    assert observer_defect == sp.zeros(1, 3)

    at_corner = derivative_route.subs(v, 0).applyfunc(sp.factor)
    assert at_corner == sp.Matrix([[0, sp.Rational(-1, 4), 0]])
    assert (at_corner * hidden)[0] == -sp.Rational(1, 4)

    R0 = R.subs(v, 0).applyfunc(sp.factor)
    S0 = S.subs(v, 0).applyfunc(sp.factor)
    left = (mu * S0.T * R0.T).applyfunc(sp.factor)
    right = (mu * R0.T * S0.T).applyfunc(sp.factor)
    assert (left - right) == at_corner

    output = {
        "schema": "marici.benincasa.total_signed_beck_chevalley_observer.v1",
        "status": "pass",
        "connection_convention": "F_uv=d_u A_v-d_v A_u+[A_u,A_v]",
        "full_flatness": True,
        "u_residue_R_at_v0": strings(R0),
        "v_tangential_connection_S_at_corner": strings(S0),
        "route_specialize_then_transport": strings(left),
        "route_transport_then_specialize": strings(right),
        "route_commutator": strings(left - right),
        "direct_conormal_derivative": strings(at_corner),
        "beck_chevalley_defect": strings(observer_defect),
        "value_on_hidden_generator": str((at_corner * hidden)[0]),
        "identity": "d_v R=[R,S], equivalently mu*d_v(R^T)=mu*(S^T*R^T-R^T*S^T)",
        "classification": {
            "conormal_symbol": "source-derived mixed-flatness commutator",
            "order_dependence": "controlled exactly by the Beck-Chevalley commutator",
            "unexplained_coherence_cell": False,
            "new_carrier_datum": False,
        },
    }
    RESULT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
