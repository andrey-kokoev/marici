import json
from pathlib import Path

import sympy as sp


L, z, f, e = sp.symbols("L z f e", real=True)
a = sp.Rational(1, 2) + z
b = sp.Rational(1, 2) - z
D = sp.diag(sp.exp(-a * L), sp.exp(-b * L))
r = sp.Matrix([
    f * (1 - sp.exp(-a * L)) / a,
    f * (1 - sp.exp(-b * L)) / b,
])
h = sp.Matrix([[1, -1]])
C = h * D
B = -r
Dinv = D.inv()

S = sp.simplify(e - (C * Dinv * B)[0])
S_direct = sp.simplify(e + (h * r)[0])

Dp = D.diff(L)
rp = r.diff(L)
Cp = C.diff(L)
Bp = B.diff(L)
jet_terms = {
    "return_derivative": sp.simplify(-(Cp * Dinv * B)[0]),
    "retained_transport": sp.simplify((C * Dinv * Dp * Dinv * B)[0]),
    "outgoing_derivative": sp.simplify(-(C * Dinv * Bp)[0]),
}
Sprime_complete = sp.simplify(sum(jet_terms.values()))
Q = 2 * f * sp.exp(-L / 2) * sp.sinh(z * L)
frozen_return_jet = sp.simplify(
    jet_terms["retained_transport"] + jet_terms["outgoing_derivative"]
)
swap = sp.Matrix([[0, 1], [1, 0]])

checks = {
    "schur_complement_reduces_to_odd_reservoir_pairing": sp.simplify(S - S_direct) == 0,
    "return_and_transport_terms_cancel": sp.simplify(
        jet_terms["return_derivative"] + jet_terms["retained_transport"]
    ) == 0,
    "complete_schur_first_jet_is_negative_endpoint_current": sp.simplify(
        (Sprime_complete + Q).rewrite(sp.exp)
    ) == 0,
    "complete_jet_equals_direct_schur_derivative": sp.simplify(
        (Sprime_complete - sp.diff(S, L)).rewrite(sp.exp)
    ) == 0,
    "frozen_return_erases_endpoint_current": sp.simplify(frozen_return_jet) == 0,
    "return_row_has_deck_odd_covariance": (C.subs(z, -z) + C * swap).applyfunc(sp.simplify) == sp.zeros(1, 2),
}

result = {
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "schur_complement": str(S),
    "complete_first_jet": str(Sprime_complete),
    "endpoint_current": str(Q),
    "jet_terms": {name: str(value) for name, value in jet_terms.items()},
    "frozen_return_jet": str(frozen_return_jet),
}
out = Path(__file__).resolve().parents[1] / "results" / "co_moving_odd_schur_first_jet.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
