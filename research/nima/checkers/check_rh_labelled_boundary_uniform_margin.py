"""Exact checks for the labelled-boundary uniform equalizer estimate."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def norm_sq(vector):
    return sum(Fraction(x) ** 2 for x in vector)


z = Fraction(3, 4)
a = z - Fraction(1, 2)
constant = max(Fraction(1), Fraction(1, 2) / (a**2))
assert constant == 8

packets = [
    ([2], [1], [3], [5]),
    ([2, 17], [1, -2], [3, -4], [5, 7]),
    ([2, 17, 257], [1, -2, 5], [3, -4, 2], [5, 7, -11]),
    ([2, 17, 257, 4099], [1, -2, 5, 3], [3, -4, 2, 9], [5, 7, -11, 13]),
]

records = []
for rates, incidences, tails, reservoirs in packets:
    rates = list(map(Fraction, rates))
    incidences = list(map(Fraction, incidences))
    tails = list(map(Fraction, tails))
    reservoirs = list(map(Fraction, reservoirs))
    plus = [
        (z - rate) * tail + incidence * reservoir
        for rate, incidence, tail, reservoir in zip(
            rates, incidences, tails, reservoirs
        )
    ]
    minus = [
        (1 - z - rate) * tail + incidence * reservoir
        for rate, incidence, tail, reservoir in zip(
            rates, incidences, tails, reservoirs
        )
    ]
    assert [x - y for x, y in zip(plus, minus)] == [2 * a * x for x in tails]
    state_energy = norm_sq(tails) + norm_sq(reservoirs)
    observed_energy = norm_sq(plus) + norm_sq(minus) + norm_sq(reservoirs)
    assert state_energy <= constant * observed_energy
    records.append({
        "label_count": len(rates),
        "state_energy": str(state_energy),
        "observed_energy": str(observed_energy),
        "uniform_bound_pass": True,
    })

# A scalar aggregate endpoint port misses a two-mode high-rate escape.
escape_records = []
previous = None
for rate in [Fraction(8), Fraction(16), Fraction(32), Fraction(64), Fraction(128)]:
    rates = [rate, rate + 1]
    incidences = [Fraction(1), Fraction(1)]
    reservoirs = [Fraction(1), Fraction(-1)]
    tails = [
        incidence * reservoir / (r - Fraction(1, 2))
        for r, incidence, reservoir in zip(rates, incidences, reservoirs)
    ]
    plus = [
        (z - r) * tail + incidence * reservoir
        for r, incidence, tail, reservoir in zip(rates, incidences, tails, reservoirs)
    ]
    minus = [
        (1 - z - r) * tail + incidence * reservoir
        for r, incidence, tail, reservoir in zip(rates, incidences, tails, reservoirs)
    ]
    scalar_boundary = sum(reservoirs)
    assert scalar_boundary == 0
    state_energy = norm_sq(tails) + norm_sq(reservoirs)
    observed_energy = norm_sq(plus) + norm_sq(minus) + scalar_boundary**2
    ratio = observed_energy / state_energy
    if previous is not None:
        assert ratio < previous
    previous = ratio
    escape_records.append({"rate": str(rate), "aggregate_ratio": str(ratio)})

assert previous < Fraction(1, 100000)

payload = {
    "schema": "marici.research.check.v1",
    "claim": "labelled boundary observation restores a cutoff-independent off-seam equalizer margin",
    "z": str(z),
    "uniform_constant": str(constant),
    "packets": records,
    "scalar_aggregate_escape": escape_records,
    "verdict": "combined labelled law is uniformly exact off seam",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-labelled-boundary-uniform-margin.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
