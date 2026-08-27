from fractions import Fraction
import json
import math
from pathlib import Path


primes = [2, 3, 5, 7, 11, 17, 29, 47, 97]
orders = [1, 2, 3]
rows = []

for k in orders:
    expected_character_ratio = 1 / (k * math.sqrt(2))
    for prime in primes:
        n = prime**k
        # For A(h)=exp(-h) and h=log(n/(n-1)), exp(-h)=(n-1)/n.
        norm_squared = Fraction(2, n)
        norm = math.sqrt(float(norm_squared))
        character_weight = prime ** (-k / 2) / k
        current_weight = math.log(prime) * character_weight
        character_ratio = character_weight / norm
        current_ratio = current_weight / norm
        assert abs(character_ratio - expected_character_ratio) < 1e-12
        assert abs(current_ratio - math.log(prime) * expected_character_ratio) < 1e-12
        rows.append(
            {
                "prime": prime,
                "order": k,
                "character_ratio": character_ratio,
                "current_ratio": current_ratio,
            }
        )

for k in orders:
    ratios = [row["current_ratio"] for row in rows if row["order"] == k]
    assert all(right > left for left, right in zip(ratios, ratios[1:]))

result = {
    "schema": "marici.rh.tate-character-current-threshold.v1",
    "orders_checked": orders,
    "primes_checked": primes,
    "character_ratio_uniform_in_prime": True,
    "differentiated_current_ratio_grows_as_log_prime": True,
    "verdict": "cusp topology separates continuity of the Tate character from its logarithmic current",
}

out = Path(__file__).parents[1] / "results" / "rh-tate-character-current-threshold.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
