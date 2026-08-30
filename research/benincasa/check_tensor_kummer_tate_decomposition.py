#!/usr/bin/env python3
"""Exact deck decomposition of the CM-compiled tensor helicity forms."""

import json
from pathlib import Path

import sympy as sp


p, r, s, d0, d1, d2, K = sp.symbols("p r s d0 d1 d2 K", nonzero=True)
sK, sL = sp.symbols("sK sL", nonzero=True)
i = sp.I

lam = sp.factor((p - r - s) * (p - r + s) * (p + r - s) * (p + r + s))
N = sp.expand(
    2 * p**2 * (d0**2 + r**2 - d2**2)
    - (d0**2 + p**2 - d1**2) * (p**2 + r**2 - s**2)
)

# Oriented coordinates with sL^2=-Lambda and sK^2=K.  The factor i is
# forced by Z^2=K/Lambda.
Y = N / (2 * p * sL)
Z = i * sK / sL
omega = 1 / sK
raw_plus = sp.together((Y + i * Z) ** 2 * omega)
raw_minus = sp.together((Y - i * Z) ** 2 * omega)

kummer = -(N**2 + 4 * p**2 * K) / (4 * p**2 * lam * sK)
tate = N / (p * lam)


def quotient_remainder(expression):
    numerator = sp.together(expression).as_numer_denom()[0]
    _, remainder = sp.reduced(
        sp.Poly(numerator, sK, sL, domain="EX"),
        [
            sp.Poly(sK**2 - K, sK, sL, domain="EX"),
            sp.Poly(sL**2 + lam, sK, sL, domain="EX"),
        ],
    )
    return sp.factor(remainder.as_expr())


assert quotient_remainder(raw_plus - (kummer + tate)) == 0
assert quotient_remainder(raw_minus - (kummer - tate)) == 0

# The K deck changes both the scalar Kummer form and the normal coordinate.
deck_plus = sp.factor(raw_plus.subs(sK, -sK, simultaneous=True))
deck_minus = sp.factor(raw_minus.subs(sK, -sK, simultaneous=True))
assert quotient_remainder(deck_plus + raw_minus) == 0
assert quotient_remainder(deck_minus + raw_plus) == 0

# Reversing the oriented external base changes Y and Z simultaneously and
# leaves each spin-two helicity form invariant.
assert sp.factor(raw_plus.subs(sL, -sL, simultaneous=True) - raw_plus) == 0
assert sp.factor(raw_minus.subs(sL, -sL, simultaneous=True) - raw_minus) == 0

trace = sp.factor((kummer + tate + kummer - tate) / 2)
anti_trace = sp.factor((kummer + tate - kummer + tate) / 2)
assert sp.factor(trace - kummer) == 0
assert sp.factor(anti_trace - tate) == 0
assert sp.factor(trace.subs(sK, -sK, simultaneous=True) + trace) == 0
assert sp.factor(anti_trace.subs(sK, -sK, simultaneous=True) - anti_trace) == 0

packet = {
    "schema": "marici.benincasa.tensor-kummer-tate-decomposition.v1",
    "status": "passed",
    "relations": ["sK^2=K_CM", "sL^2=-Lambda_ext"],
    "oriented_coordinates": {"Y": str(Y), "Z": str(Z), "N": str(N)},
    "helicity_forms": {
        "Omega_plus": "Kummer+Tate",
        "Omega_minus": "Kummer-Tate",
        "Kummer": str(kummer),
        "Tate": str(tate),
    },
    "deck_action": {
        "Omega_plus": "-Omega_minus",
        "Omega_minus": "-Omega_plus",
        "trace_character": -1,
        "anti_trace_character": 1,
    },
    "external_orientation_action": "trivial on both spin-two helicity forms",
    "intrinsic_denominators": ["p", "Lambda_ext", "sqrt(K_CM) on the inherited Kummer summand"],
    "support_classification": {
        "p=0": "existing soft support",
        "Lambda_ext=0": "existing external Gram support",
        "K_CM=0": "existing Cayley-Menger branch support",
        "new_support": False,
    },
    "coefficient_object": "deck-odd Kummer line plus deck-even rational/Tate line",
    "scope_warning": (
        "This is a local coefficient decomposition before twisted-cohomology "
        "reduction and before the Ward-correlated channel/contact totalization."
    ),
}

output = Path(__file__).with_name("tensor-kummer-tate-decomposition.json")
output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2, sort_keys=True))
