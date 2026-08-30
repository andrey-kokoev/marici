import json
from itertools import combinations
from pathlib import Path


def partition(states, visible_bits):
    classes = {}
    for state in states:
        signature = tuple((state >> bit) & 1 for bit in visible_bits)
        classes.setdefault(signature, []).append(state)
    return tuple(tuple(values) for _, values in sorted(classes.items()))


def class_index(parts):
    return {state: i for i, block in enumerate(parts) for state in block}


def ambiguous_pairs(parts):
    return sum(len(block) * (len(block) - 1) // 2 for block in parts)


bit_count = 5
states = tuple(range(2 ** bit_count))
levels = []
previous = None

for version in range(bit_count + 1):
    parts = partition(states, range(version))
    index = class_index(parts)
    ambiguity = ambiguous_pairs(parts)
    total_pairs = len(states) * (len(states) - 1) // 2
    entry = {
        "version": version,
        "context_generators": version,
        "quotient_classes": len(parts),
        "ambiguous_pairs": ambiguity,
        "distinguished_pairs": total_pairs - ambiguity,
    }
    if previous is not None:
        old_index = class_index(previous)
        # Every new class lies in exactly one old class: canonical forgetting map.
        downgrade = {new_i: old_index[block[0]] for new_i, block in enumerate(parts)}
        assert all(old_index[state] == downgrade[index[state]] for state in states)
        # Every old class splits in two in this independent-bit fixture.
        fibers = {old_i: [] for old_i in range(len(previous))}
        for new_i, old_i in downgrade.items():
            fibers[old_i].append(new_i)
        assert all(len(fiber) == 2 for fiber in fibers.values())
        entry["canonical_downgrade"] = True
        entry["forward_sections"] = 2 ** len(previous)
        entry["canonical_upgrade"] = False
        assert entry["forward_sections"] > 1
    levels.append(entry)
    previous = parts

assert [level["quotient_classes"] for level in levels] == [1, 2, 4, 8, 16, 32]
assert all(a["ambiguous_pairs"] > b["ambiguous_pairs"] for a, b in zip(levels, levels[1:]))
assert all(a["distinguished_pairs"] < b["distinguished_pairs"] for a, b in zip(levels, levels[1:]))

# A redundant context is admitted but induces no refinement.
full = partition(states, range(bit_count))
redundant = partition(states, list(range(bit_count)) + [0])
assert full == redundant

result = {
    "schema": "marici.nima.protocol-context-refinement.v1",
    "state_count": len(states),
    "levels": levels,
    "redundant_context_changes_partition": False,
    "verdict": "Protocol enrichment is canonically contravariant on behavioral quotients: richer context forgets to poorer context, while a forward upgrade requires noncanonical splitting data."
}

out = Path(__file__).parents[1] / "results" / "protocol-context-refinement.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
