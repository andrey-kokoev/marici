from fractions import Fraction
import json
from pathlib import Path


def record_gate(c, epsilon, fragment_size):
    overlap_squared = c ** (2 * fragment_size)
    threshold = 4 * epsilon * (1 - epsilon)
    return overlap_squared <= threshold


def first_passing_size(c, epsilon, maximum=100):
    for size in range(1, maximum + 1):
        if record_gate(c, epsilon, size):
            return size
    raise AssertionError("no fragment passed within the declared finite range")


def first_coherence_size(c, tolerance, maximum=100):
    for size in range(1, maximum + 1):
        if c ** size <= tolerance:
            return size
    raise AssertionError("no coherence cutoff passed within the declared finite range")


c = Fraction(3, 5)
epsilon = Fraction(1, 20)
fragment_size = first_passing_size(c, epsilon)
assert fragment_size == 2
assert not record_gate(c, epsilon, 1)
assert record_gate(c, epsilon, 2)

total_carriers = 8
redundancy = total_carriers // fragment_size
assert redundancy == 4

coherence_tolerance = Fraction(1, 100)
coherence_size = first_coherence_size(c, coherence_tolerance)
assert coherence_size == 10
assert c ** 9 > coherence_tolerance
assert c ** 10 <= coherence_tolerance

# Independent conditional carriers multiply their overlaps. Repeated labels on
# one shared carrier do not. The hostile shared-carrier model remains at c.
independent_overlap = c ** fragment_size
shared_carrier_overlap = c
assert independent_overlap < shared_carrier_overlap

# A finite permutation model supplies the exact reversibility witness already
# used by the previous DPC: controlled fanout is its own inverse.
def fanout(index):
    source = (index >> 2) & 1
    e1 = ((index >> 1) & 1) ^ source
    e2 = (index & 1) ^ source
    return (source << 2) | (e1 << 1) | e2


assert all(fanout(fanout(index)) == index for index in range(8))

result = {
    "schema": "marici.source-overlap-objective-record-scale.v1",
    "source_overlap": "3/5",
    "record_tolerance": "1/20",
    "minimum_fragment_size": fragment_size,
    "total_carriers": total_carriers,
    "disjoint_readable_fragments": redundancy,
    "coherence_tolerance": "1/100",
    "minimum_coherence_suppression_size": coherence_size,
    "independent_overlap_at_fragment_size": f"{independent_overlap.numerator}/{independent_overlap.denominator}",
    "shared_carrier_overlap": f"{shared_carrier_overlap.numerator}/{shared_carrier_overlap.denominator}",
    "global_inverse_exists": True,
    "claim_boundary": "one source overlap derives static information scales but not persistence or irreversibility",
    "status": "pass",
}

output = Path(__file__).resolve().parents[1] / "results" / "source-overlap-objective-record-scale.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
