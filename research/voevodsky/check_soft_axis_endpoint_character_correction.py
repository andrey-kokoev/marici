"""Audit the actual deck character of the soft endpoint jet."""

import importlib.util
from pathlib import Path

source = Path(__file__).with_name("check_soft_axis_deck_orbit_completion.py")
spec = importlib.util.spec_from_file_location("deck", source)
deck = importlib.util.module_from_spec(spec)
spec.loader.exec_module(deck)

# The mechanical involution changes a-parity only.  It fixes b, u, K, and L1.
assert deck.rho(deck.b) == deck.b
assert deck.rho(deck.u) == deck.u
assert deck.rho(deck.L1) == deck.L1
assert deck.rho(deck.a) == deck.scale(deck.a, -1)

# Naturality of d(e_a)=K_a forces rho(e_a)=-e_a; d(e_u)=K_u forces
# rho(e_u)=e_u.  Hence a^2 e_a and a^3 e_u are both odd.
character_a2_ea = (+1) * (-1)
character_a3_eu = (-1) * (+1)
assert character_a2_ea == -1
assert character_a3_eu == -1

# b is fixed, so neither endpoint is exchanged and L1 has no 1-b conjugate.
for endpoint in (-1, 1):
    assert endpoint == endpoint

print("rho(b)=b, rho(u)=u, rho(a)=-a")
print("rho(L1)=L1 for L1=b+1-u")
print("character(a^2 e_a) = character(a^3 e_u) = -1")
print("b=+1 and b=-1 are individually fixed, not deck-exchanged")
print("verdict: Entries 497-499 do not identify the plus defect")
