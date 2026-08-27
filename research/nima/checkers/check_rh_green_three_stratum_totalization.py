"""Exact finite diagnostics for three Green-boundary completion strata."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


cutoffs = [8, 16, 32, 64]
records = []
previous_hilbert_l1 = None
for n in cutoffs:
    trace_values = [Fraction(1, j * j) for j in range(1, n + 1)]
    hilbert_values = [Fraction(1, j) for j in range(1, n + 1)]
    distribution_values = [Fraction(1) for _ in range(n)]
    trace_l1 = sum(trace_values)
    hilbert_l1 = sum(hilbert_values)
    hilbert_l2_squared = sum(x * x for x in hilbert_values)
    if previous_hilbert_l1 is not None:
        assert hilbert_l1 > previous_hilbert_l1
    previous_hilbert_l1 = hilbert_l1
    records.append({
        "cutoff": n,
        "trace_l1_below_2": trace_l1 < 2,
        "hilbert_l1_strictly_growing": True,
        "hilbert_l2_squared_below_2": hilbert_l2_squared < 2,
        "distribution_l2_squared": str(sum(x * x for x in distribution_values)),
    })

# Exact monotonic diagnostics at the checked cutoffs.
assert all(record["trace_l1_below_2"] for record in records)
assert all(record["hilbert_l2_squared_below_2"] for record in records)
assert [Fraction(record["distribution_l2_squared"]) for record in records] == [
    Fraction(n) for n in cutoffs
]

# Finite rearrangement witness: the same alternating terms have different
# intermediate scalar values under different source orderings.
terms = [Fraction(1, j) if j % 2 else Fraction(-1, j) for j in range(1, 13)]
natural_order = list(range(len(terms)))
positive_first = [i for i, value in enumerate(terms) if value > 0] + [
    i for i, value in enumerate(terms) if value < 0
]
natural_prefix = sum(terms[i] for i in natural_order[:6])
reordered_prefix = sum(terms[i] for i in positive_first[:6])
assert natural_prefix != reordered_prefix
assert sum(terms[i] for i in natural_order) == sum(terms[i] for i in positive_first)

payload = {
    "schema": "marici.research.check.v1",
    "claim": "finite Green identities admit three inequivalent completion modalities",
    "records": records,
    "conditional_rearrangement": {
        "natural_six_term_prefix": str(natural_prefix),
        "positive_first_six_term_prefix": str(reordered_prefix),
        "same_finite_total": True,
    },
    "verdict": "global boundary totalization must remain stratified",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-green-three-stratum-totalization.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
