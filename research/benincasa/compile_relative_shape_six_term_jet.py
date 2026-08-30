#!/usr/bin/env python3
"""Compile the native six-term second-shape source insertion before IBP."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / ".tmp_sympy"))
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research/benincasa/results/relative-shape-six-term-jet.json"

E, K, k1, k2 = sp.symbols("E K k1 k2", nonzero=True)
g1, g2, g3 = sp.symbols("g1 g2 g3", nonzero=True)
B12, B23, B31 = sp.symbols("B12 B23 B31", nonzero=True)
s12, s23, s31 = sp.symbols("s12 s23 s31", nonzero=True)

dg = {g1: 1, g2: -1, g3: 0}
terms = [
    ("G12_g23", B12, s23, -1),
    ("G12_g31", B12, s31, 1),
    ("G23_g31", B23, s31, 1),
    ("G23_g12", B23, s12, 0),
    ("G31_g12", B31, s12, 0),
    ("G31_g23", B31, s23, -1),
]


def compile_term(big, small, dsmall):
    value = 1 / (sp.sqrt(K) * E * g1 * g2 * g3 * big * small)
    log_first = -k1 / 2 - sum(sp.Rational(dg[g], 1) / g for g in (g1, g2, g3)) - sp.Rational(dsmall, 1) / small
    log_second = -sp.Rational(1, 2) * (k2 - k1**2) + sum(sp.Rational(dg[g] ** 2, 1) / g**2 for g in (g1, g2, g3)) + sp.Rational(dsmall**2, 1) / small**2
    first = sp.factor(value * log_first)
    second = sp.factor(value * (log_second + log_first**2))
    return value, first, second


compiled = {}
for name, big, small, dsmall in terms:
    value, first, second = compile_term(big, small, dsmall)
    compiled[name] = {"value": sp.sstr(value), "first": sp.sstr(first), "second": sp.sstr(second)}

swap = {
    g1: g2, g2: g1, g3: g3,
    B12: B12, B23: B31, B31: B23,
    s12: s12, s23: s31, s31: s23,
    k1: -k1, k2: k2,
}
partner = {
    "G12_g23": "G12_g31", "G12_g31": "G12_g23",
    "G23_g31": "G31_g23", "G31_g23": "G23_g31",
    "G23_g12": "G31_g12", "G31_g12": "G23_g12",
}

symbolic = {name: compile_term(big, small, dsmall) for name, big, small, dsmall in terms}
checks = {}
for name, mate in partner.items():
    checks[f"{name}_value_swap"] = sp.factor(symbolic[name][0].xreplace(swap) - symbolic[mate][0]) == 0
    checks[f"{name}_first_odd"] = sp.factor(symbolic[name][1].xreplace(swap) + symbolic[mate][1]) == 0
    checks[f"{name}_second_even"] = sp.factor(symbolic[name][2].xreplace(swap) - symbolic[mate][2]) == 0

assert all(checks.values()), checks
packet = {
    "schema": "marici.relative-shape-six-term-jet.v1",
    "native_arity": 6,
    "terms": compiled,
    "site_exchange_partners": partner,
    "all_exchange_checks_pass": True,
    "k1": "K'/K",
    "k2": "K''/K",
    "maximum_individual_source_pole_power": 3,
    "ibp_reduction_applied": False,
    "quotient_applied": False,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print(OUT)
