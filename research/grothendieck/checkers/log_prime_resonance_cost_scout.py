"""Discovery scout for log-prime phase alignment versus logarithmic frequency cost."""

import json
import math
from pathlib import Path


def terms_for(L):
    limit = int(math.exp(2 * L))
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    values = {}
    for p in range(2, limit + 1):
        if not sieve[p]:
            continue
        power = p
        while power <= limit:
            values[power] = math.log(p)
            if power > limit // p:
                break
            power *= p
        if p * p <= limit:
            sieve[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    return [(math.log(n), lam / math.sqrt(n)) for n, lam in values.items()]


def symbol(terms, xi):
    return sum(weight * math.cos(xi * logn) for logn, weight in terms)


step = 0.02
maximum_xi = 1000.0
floors = (1.0, 10.0, 100.0)
rows = []
for L in (1, 2, 3):
    terms = terms_for(L)
    mass = sum(weight for _, weight in terms)
    records = {}
    for floor in floors:
        best_value = -math.inf
        best_xi = None
        index0 = math.ceil(floor / step)
        index1 = math.floor(maximum_xi / step)
        for index in range(index0, index1 + 1):
            xi = index * step
            value = symbol(terms, xi) - math.log1p(xi)
            if value > best_value:
                best_value = value
                best_xi = xi
        records[str(floor)] = {
            "max_symbol_minus_log1p": best_value,
            "argmax_xi": best_xi,
            "absolute_mass": mass,
        }
    rows.append({"L": L, "term_count": len(terms), "floors": records})

result = {
    "schema": "marici.grothendieck.log-prime-resonance-cost-scout.v1",
    "grid_step": step,
    "maximum_xi": maximum_xi,
    "rows": rows,
    "claim_boundary": "Coarse finite grid; cannot certify a supremum or exclude narrow resonances.",
}
output = Path(__file__).parents[1] / "results" / "log-prime-resonance-cost-scout.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
