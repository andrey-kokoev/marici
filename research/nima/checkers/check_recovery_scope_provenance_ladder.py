from collections import defaultdict
from itertools import permutations
import json
from pathlib import Path


processes = tuple(permutations(range(4)))
assert len(processes) == 24


def signature(process, domain):
    return tuple(process[index] for index in domain)


def partition(domain):
    classes = defaultdict(list)
    for process in processes:
        classes[signature(process, domain)].append(process)
    return classes


point_domain = (0,)
visible_domain = (0, 1)
global_domain = (0, 1, 2, 3)

point = partition(point_domain)
visible = partition(visible_domain)
global_classes = partition(global_domain)

assert len(point) == 4
assert set(map(len, point.values())) == {6}
assert len(visible) == 12
assert set(map(len, visible.values())) == {2}
assert len(global_classes) == 24
assert set(map(len, global_classes.values())) == {1}

# Restriction maps are well defined and surjective.
visible_to_point = {sig: (sig[0],) for sig in visible}
global_to_visible = {sig: sig[:2] for sig in global_classes}
assert set(visible_to_point.values()) == set(point)
assert set(global_to_visible.values()) == set(visible)

# Each coarse class has several finer lifts, so no lift is selected by the
# coarse signature alone.
point_lift_counts = {
    point_sig: sum(1 for target in visible_to_point.values() if target == point_sig)
    for point_sig in point
}
visible_lift_counts = {
    visible_sig: sum(1 for target in global_to_visible.values() if target == visible_sig)
    for visible_sig in visible
}
assert set(point_lift_counts.values()) == {3}
assert set(visible_lift_counts.values()) == {2}

# Explicit hostiles for the two failed promotions.
same_point = next(group for group in point.values() if len({signature(p, visible_domain) for p in group}) > 1)
assert len({signature(p, point_domain) for p in same_point}) == 1
assert len({signature(p, visible_domain) for p in same_point}) > 1

same_visible = next(group for group in visible.values() if len(group) == 2)
assert signature(same_visible[0], visible_domain) == signature(same_visible[1], visible_domain)
assert signature(same_visible[0], global_domain) != signature(same_visible[1], global_domain)

result = {
    "schema": "marici.recovery-scope-provenance-ladder.v1",
    "process_count": len(processes),
    "point_recovery": {"class_count": len(point), "class_size": 6},
    "visible_domain_recovery": {"class_count": len(visible), "class_size": 2},
    "global_uncomputation": {"class_count": len(global_classes), "class_size": 1},
    "point_to_visible_lifts_per_class": 3,
    "visible_to_global_lifts_per_class": 2,
    "canonical_reverse_lifts": False,
    "authority_gates": ["existence", "synthesis", "execution"],
    "claim_boundary": "minimal process provenance is indexed by declared recovery scope",
    "status": "pass",
}

output = Path(__file__).resolve().parents[1] / "results" / "recovery-scope-provenance-ladder.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
