import json
from pathlib import Path


def inverse(permutation):
    out = [0] * len(permutation)
    for source, target in enumerate(permutation):
        out[target] = source
    return tuple(out)


identity = (0, 1, 2, 3)
hidden_swap = (0, 1, 3, 2)
source = 0
visible_domain = (0, 1)
recovery_domain = (0, 1, 2, 3)

assert identity != hidden_swap
assert identity[source] == hidden_swap[source]
assert all(identity[x] == hidden_swap[x] for x in visible_domain)
assert inverse(identity) != inverse(hidden_swap)
assert any(inverse(identity)[x] != inverse(hidden_swap)[x] for x in recovery_domain)

# No endpoint-indexed inverse selector can choose both different inverse maps
# from their common endpoint value.
common_endpoint = identity[source]
candidate_from_endpoint = inverse(identity)
assert candidate_from_endpoint[common_endpoint] == source
assert candidate_from_endpoint != inverse(hidden_swap)

# A one-bit process tag separates exactly the two inverse-action classes.
process_tags = {identity: 0, hidden_swap: 1}
assert len(set(process_tags.values())) == 2

# Erasing that tag is a many-to-one map and has no inverse as a function.
erased = {tag: 0 for tag in process_tags.values()}
assert len(set(erased.values())) == 1

result = {
    "schema": "marici.inversion-descent-through-readout.v1",
    "processes_distinct": True,
    "source_endpoint_equal": True,
    "visible_subspace_action_equal": True,
    "inverse_actions_distinct": True,
    "endpoint_only_inverse_selector_exists": False,
    "minimum_process_tag_bits_for_fixture": 1,
    "tag_erasure_is_many_to_one": True,
    "claim_boundary": "complete reversal authority does not descend through nonfaithful endpoint readout",
    "status": "pass",
}

output = Path(__file__).resolve().parents[1] / "results" / "inversion-descent-through-readout.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
