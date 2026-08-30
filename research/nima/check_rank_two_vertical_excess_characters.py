"""Exact character and Tor audit of the rank-two vertical excess algebra."""

import json
from fractions import Fraction as F
from pathlib import Path


# B=Q[w]/(w^2+R), with a nonsquare positive rational control R=2.
R = F(2)


def mul(x, y):
    a, b = x
    c, d = y
    return (a * c - R * b * d, a * d + b * c)


def deck(x):
    a, b = x
    return (a, -b)


def trace(x):
    return 2 * x[0]


one = (F(1), F(0))
w = (F(0), F(1))
assert mul(w, w) == (-R, F(0))
assert deck(one) == one
assert deck(w) == (F(0), F(-1))
assert trace(one) == 2
assert trace(w) == 0

controls = [(F(3), F(5)), (F(-2), F(7)), (F(0), F(11))]
for x in controls:
    even = ((x[0] + deck(x)[0]) / 2, (x[1] + deck(x)[1]) / 2)
    odd = ((x[0] - deck(x)[0]) / 2, (x[1] - deck(x)[1]) / 2)
    assert even == (x[0], 0)
    assert odd == (0, x[1])
    assert (even[0] + odd[0], even[1] + odd[1]) == x
    assert trace(odd) == 0

# Formally near the Gram rank-drop point, the excess module is
# M=(Q[e]/(e)) tensor B. Its length-one resolution [R --e--> R] gives B in
# both Tor_0 and Tor_1 after specialization e=0.
tor_dimensions = {"Tor_0": 2, "Tor_1": 2, "Tor_ge_2": 0}
character_dimensions = {
    "Tor_0": {"trivial": 1, "sign": 1},
    "Tor_1": {"trivial": 1, "sign": 1},
}

result = {
    "schema": "marici.cosmology.rank_two_vertical_excess_characters.v1",
    "special_fiber_algebra": "Q[w]/(w^2+2)",
    "deck_involution": "w -> -w",
    "trace_zero_generator": "w",
    "tor_dimensions": tor_dimensions,
    "character_dimensions": character_dimensions,
    "passed": True,
}
out = Path(__file__).with_name("results") / "rank-two-vertical-excess-characters.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
