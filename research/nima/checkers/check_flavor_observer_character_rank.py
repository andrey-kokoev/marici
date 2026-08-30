from collections import defaultdict
import json
from pathlib import Path


states = tuple((family_sign, volume_sign) for family_sign in (-1, 1) for volume_sign in (-1, 1))


def unsigned_record(_state):
    return (1,)


def first_signed_record(state):
    family_sign, volume_sign = state
    return family_sign * volume_sign


def second_signed_record(state):
    family_sign, _ = state
    return family_sign


def fibers(record):
    grouped = defaultdict(set)
    for state in states:
        grouped[record(state)].add(state)
    return grouped


unsigned_fibers = fibers(unsigned_record)
one_signed_fibers = fibers(lambda state: (unsigned_record(state), first_signed_record(state)))
two_signed_fibers = fibers(
    lambda state: (unsigned_record(state), first_signed_record(state), second_signed_record(state))
)

assert len(unsigned_fibers) == 1
assert {len(fiber) for fiber in one_signed_fibers.values()} == {2}
assert {len(fiber) for fiber in two_signed_fibers.values()} == {1}

# A source coherence relation fixing one torsor reduces the reachable locus to
# two states. On that restricted locus, one signed observer is sufficient.
coherent_states = tuple(state for state in states if state[1] == 1)
coherent_records = {first_signed_record(state): state for state in coherent_states}
assert len(coherent_records) == len(coherent_states) == 2

result = {
    "schema": "marici.nima.flavor-observer-character-rank.v1",
    "independent_sign_torsors": 2,
    "raw_sign_states": len(states),
    "unsigned_record_classes": len(unsigned_fibers),
    "one_signed_record_classes": len(one_signed_fibers),
    "one_signed_maximum_fiber": max(len(fiber) for fiber in one_signed_fibers.values()),
    "two_signed_record_classes": len(two_signed_fibers),
    "two_signed_maximum_fiber": max(len(fiber) for fiber in two_signed_fibers.values()),
    "one_signed_faithful_after_source_coherence": True,
    "verdict": (
        "Observer count is the rank of signed characters on the surviving "
        "torsor group. One unsigned plus one signed observer suffices only when "
        "source coherence has reduced the sign rank to one; two independent "
        "sign torsors require two independent signed characters."
    ),
}

output = Path(__file__).parents[1] / "results" / "flavor-observer-character-rank.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
