import json
from fractions import Fraction
from pathlib import Path


def mul(z, w):
    a, b = z
    c, d = w
    return (a * c - b * d, a * d + b * c)


def conj(z):
    return (z[0], -z[1])


def norm2(z):
    return mul(z, conj(z))[0]


def reciprocal(z):
    n = norm2(z)
    assert n != 0
    a, b = conj(z)
    return (a / n, b / n)


def linear_exchange_compatible(z):
    return reciprocal(z) == z


def dagger_exchange_compatible(z):
    return reciprocal(z) == conj(z)


one = (Fraction(1), Fraction(0))
minus_one = (Fraction(-1), Fraction(0))
i = (Fraction(0), Fraction(1))
two = (Fraction(2), Fraction(0))

assert linear_exchange_compatible(one)
assert linear_exchange_compatible(minus_one)
assert not linear_exchange_compatible(i)
assert dagger_exchange_compatible(one)
assert dagger_exchange_compatible(minus_one)
assert dagger_exchange_compatible(i)
assert not dagger_exchange_compatible(two)

# Rational parametrization of the unit circle supplies arbitrarily many exact
# dagger-compatible phases, proving that the residual is not finite.
unit_phases = []
for t in (Fraction(-3, 2), Fraction(-1), Fraction(-1, 3), Fraction(0),
          Fraction(1, 4), Fraction(1), Fraction(2)):
    den = 1 + t * t
    z = ((1 - t * t) / den, (2 * t) / den)
    assert norm2(z) == 1
    assert dagger_exchange_compatible(z)
    unit_phases.append(z)

assert len(set(unit_phases)) == len(unit_phases)
common = [z for z in unit_phases if linear_exchange_compatible(z)]
assert set(common).issubset({one, minus_one})

result = {
    "schema": "marici.exchange-modality-residual-gauge.v1",
    "pairing_stabilizer": "C_star",
    "linear_exchange_stabilizer": "mu_2",
    "dagger_exchange_stabilizer": "U_1",
    "common_stabilizer": "mu_2",
    "hostile_phase": "i preserves pairing and dagger exchange but not linear exchange",
    "exact_unit_phase_samples": [
        [str(a), str(b)] for a, b in unit_phases
    ],
    "verdict": "exchange modality must be typed before augmentation",
}

output = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "exchange-modality-residual-gauge.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
