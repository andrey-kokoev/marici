import json
import math
from pathlib import Path


def gaussian_atom_distance(n):
    shift = math.log(n / (n - 1))
    # Normalized smooth autocorrelation A(h)=exp(-h^2/4).
    return math.sqrt(2 * (1 - math.exp(-(shift * shift) / 4)))


primes = [3, 5, 7, 11, 17, 29, 47, 97, 193]
orders = [1, 2, 3]
rows = []

for order in orders:
    character_ratios = []
    current_ratios = []
    for prime in primes:
        n = prime**order
        norm = gaussian_atom_distance(n)
        character_weight = prime ** (-order / 2) / order
        character_ratio = character_weight / norm
        current_ratio = math.log(prime) * character_ratio
        character_ratios.append(character_ratio)
        current_ratios.append(current_ratio)
        rows.append(
            {
                "prime": prime,
                "order": order,
                "character_ratio": character_ratio,
                "current_ratio": current_ratio,
            }
        )
    assert all(right > left for left, right in zip(character_ratios, character_ratios[1:]))
    assert all(right > left for left, right in zip(current_ratios, current_ratios[1:]))
    expected_growth = (primes[-1] / primes[0]) ** (order / 2)
    observed_growth = character_ratios[-1] / character_ratios[0]
    assert observed_growth > expected_growth * 0.8

result = {
    "schema": "marici.rh.smooth-gram-tate-character-no-go.v1",
    "kernel": "A(h)=exp(-h^2/4)",
    "orders_checked": orders,
    "primes_checked": primes,
    "undifferentiated_character_ratio_diverges": True,
    "differentiated_current_ratio_diverges": True,
    "verdict": "smooth analytic Gram completion cannot carry the typed Tate anomaly traces",
}

out = Path(__file__).parents[1] / "results" / "rh-smooth-gram-tate-character-no-go.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
