#!/usr/bin/env python3
"""Clear the exact CM twist and labelled wall poles in the native six-term jet."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / ".tmp_sympy"))
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research/benincasa/results/cleared-relative-shape-jet.json"

a, b, c, t, w = sp.symbols("a b c t w")
E = sp.Integer(3)
P1, P2, P3 = 1 + t, 1 - t, sp.Integer(1)
cm = sp.Matrix([
    [0, 1, 1, 1, 1],
    [1, 0, c**2, a**2, b**2],
    [1, c**2, 0, P2**2, P1**2],
    [1, a**2, P2**2, 0, P3**2],
    [1, b**2, P1**2, P3**2, 0],
])
K = sp.expand(-cm.det() / 2)
K0 = sp.factor(K.subs(t, 0))
K1 = sp.factor(sp.diff(K, t).subs(t, 0))
K2 = sp.factor(sp.diff(K, t, 2).subs(t, 0))

g1, g2, g3 = b + c + 1, c + a + 1, a + b + 1
B12, B23, B31 = c + 3, a + 3, b + 3
s12, s23, s31 = a + b + 2, b + c + 2, c + a + 2

dg = {"g1": 1, "g2": -1, "g3": 0}
terms = [
    ("G12_g23", B12, s23, -1),
    ("G12_g31", B12, s31, 1),
    ("G23_g31", B23, s31, 1),
    ("G23_g12", B23, s12, 0),
    ("G31_g12", B31, s12, 0),
    ("G31_g23", B31, s23, -1),
]


def cleared_second(big, small, dsmall):
    # T'' = T * (L'' + (L')^2), with w^2=K0 and a uniform declared
    # clearing factor w*K0^2*E*big*g1^3*g2^3*g3*small^3.
    k1 = K1 / K0
    k2 = K2 / K0
    log_first = -k1 / 2 - 1 / g1 + 1 / g2 - sp.Rational(dsmall, 1) / small
    log_second = -(k2 - k1**2) / 2 + 1 / g1**2 + 1 / g2**2 + sp.Rational(dsmall**2, 1) / small**2
    # Cancel the declared monomial factors structurally before polynomial
    # arithmetic; factoring the resulting large polynomial is unnecessary.
    cleared = K0**2 * g1**2 * g2**2 * small**2 * (log_second + log_first**2)
    numerator, denominator = sp.together(cleared).as_numer_denom()
    assert not denominator.has(a, b, c), denominator
    return sp.Poly(sp.expand(numerator / denominator), a, b, c).as_expr()


numerators = {name: cleared_second(big, small, dsmall) for name, big, small, dsmall in terms}
common_gcd = list(numerators.values())[0]
for numerator in list(numerators.values())[1:]:
    common_gcd = sp.gcd(common_gcd, numerator)
partner = {
    "G12_g23": "G12_g31", "G12_g31": "G12_g23",
    "G23_g31": "G31_g23", "G31_g23": "G23_g31",
    "G23_g12": "G31_g12", "G31_g12": "G23_g12",
}
swap = {a: b, b: a}
checks = {}
for name, mate in partner.items():
    checks[f"{name}_polynomial"] = sp.denom(numerators[name]) == 1
    checks[f"{name}_exchange"] = sp.expand(numerators[name].xreplace(swap) - numerators[mate]) == 0
checks["common_numerator_gcd_is_one"] = common_gcd == 1

assert all(checks.values()), {k: v for k, v in checks.items() if not v}
packet = {
    "schema": "marici.cleared-relative-shape-jet.v1",
    "clearing_convention": "w*K0^2*E*B*g1^3*g2^3*g3*s^3, with w^2=K0",
    "K0": sp.sstr(K0),
    "K1": sp.sstr(K1),
    "K2": sp.sstr(K2),
    "terms": {
        name: {
            "cleared_numerator": sp.sstr(numerators[name]),
            "total_degree": sp.Poly(numerators[name], a, b, c).total_degree(),
            "monomial_count": len(sp.Poly(numerators[name], a, b, c).terms()),
        }
        for name, *_ in terms
    },
    "site_exchange_partners": partner,
    "common_numerator_gcd": sp.sstr(common_gcd),
    "all_checks_pass": True,
    "ibp_reduction_applied": False,
    "proper_face_residues_constructed": False,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print(OUT)
for name, numerator in numerators.items():
    print(name, "degree", sp.Poly(numerator, a, b, c).total_degree())
