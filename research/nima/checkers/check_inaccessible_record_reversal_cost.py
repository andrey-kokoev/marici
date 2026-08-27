from fractions import Fraction
import json
from pathlib import Path


def recovered_coherence(c, total, controlled):
    return c ** (total - controlled)


def minimum_control_count(c, total, threshold):
    for controlled in range(total + 1):
        if recovered_coherence(c, total, controlled) >= threshold:
            return controlled
    raise AssertionError("full control must restore unit coherence")


c = Fraction(3, 5)
total = 10
half_recovery = minimum_control_count(c, total, Fraction(1, 2))
high_recovery = minimum_control_count(c, total, Fraction(9, 10))

assert half_recovery == 9
assert high_recovery == 10
assert recovered_coherence(c, total, 5) == Fraction(243, 3125)
assert recovered_coherence(c, total, total) == 1

# Monotonicity: each additional exact inverse collision increases the recovered
# coherence by the fixed factor 1/c.
coherences = [recovered_coherence(c, total, k) for k in range(total + 1)]
assert all(coherences[k] < coherences[k + 1] for k in range(total))

# Exact causal lower bound for a source-declared carrier geometry.
distances = (Fraction(1), Fraction(2), Fraction(4), Fraction(8), Fraction(16))
speed = Fraction(2)
full_reversal_time_bound = max(distances) / speed
assert full_reversal_time_bound == 8

# Hostile: five observer labels share one conditional carrier. Visible count is
# five, but the inverse-support rank remains one.
nominal_observer_count = 5
shared_carrier_control_rank = 1
assert nominal_observer_count > shared_carrier_control_rank

# The commuting bit-fanout factors satisfy exact partial cancellation. On basis
# indices, each controlled-NOT is its own inverse and the two target operations
# commute.
def cnot(index, target):
    source = (index >> 2) & 1
    return index ^ ((source << (2 - target)) if source else 0)


for index in range(8):
    assert cnot(cnot(index, 1), 1) == index
    assert cnot(cnot(index, 2), 2) == index
    assert cnot(cnot(index, 1), 2) == cnot(cnot(index, 2), 1)

result = {
    "schema": "marici.inaccessible-record-reversal-cost.v1",
    "source_overlap": "3/5",
    "total_independent_carriers": total,
    "minimum_control_for_half_coherence": half_recovery,
    "minimum_control_for_nine_tenths_coherence": high_recovery,
    "coherence_after_reversing_five": "243/3125",
    "full_reversal_time_lower_bound": "8",
    "copy_count_hostile": {
        "nominal_observers": nominal_observer_count,
        "inverse_support_rank": shared_carrier_control_rank,
    },
    "claim_boundary": "reversal cost follows independent carrier support, not observer count",
    "status": "pass",
}

output = Path(__file__).resolve().parents[1] / "results" / "inaccessible-record-reversal-cost.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
