from fractions import Fraction
from itertools import product
import json
from pathlib import Path


primes = (2, 3, 5, 7)
# Rational upper surrogates for 1 + log p; only positivity and increasing
# translation cost matter in the finite exact fixture.
position_cost = (2, 3, 4, 5)
delta_weight = tuple(p * p for p in primes)


def square(x):
    return x * x


def weighted_norm2(vector):
    return sum(Fraction(delta_weight[i] * square(vector[i])) for i in range(len(primes)))


dual_derivative_constant = sum(Fraction(1, delta_weight[i]) for i in range(len(primes)))
dual_position_constant = sum(
    Fraction(square(position_cost[i]), delta_weight[i]) for i in range(len(primes))
)

checked = 0
strict_position_gain = False
for vector in product(range(-2, 3), repeat=len(primes)):
    if not any(vector):
        continue
    q2 = weighted_norm2(vector)
    derivative_row = sum(vector)
    position_row = sum(position_cost[i] * vector[i] for i in range(len(primes)))
    assert Fraction(square(derivative_row)) <= q2 * dual_derivative_constant
    assert Fraction(square(position_row)) <= q2 * dual_position_constant
    if vector == (0, 0, 0, 1):
        assert square(position_row) > square(derivative_row)
        strict_position_gain = True
    checked += 1

assert strict_position_gain

result = {
    "schema": "marici.nima.smooth-prime-synthesis-graph-bound.v1",
    "prime_labels": list(primes),
    "vectors_checked": checked,
    "derivative_dual_constant": str(dual_derivative_constant),
    "position_dual_constant": str(dual_position_constant),
    "logarithmic_position_cost_detected": strict_position_gain,
    "verdict": "weighted prime test packets continuously control both synthesis graph rows",
}

out = Path(__file__).parents[1] / "results" / "smooth-prime-synthesis-graph-bound.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

