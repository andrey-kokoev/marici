"""Finite CDFG root-image correctability checks."""

from itertools import combinations

blocks = frozenset({"C", "D", "F", "G"})
independent = {
    "rC": frozenset({"C"}),
    "rD": frozenset({"D"}),
    "rF": frozenset({"F"}),
    "rG": frozenset({"G"}),
}
shared = {"rShared": blocks}


def audit(root_images, budget, correctable):
    roots = list(root_images)
    failures = []
    for count in range(1, budget + 1):
        for chosen in combinations(roots, count):
            support = frozenset().union(*(root_images[root] for root in chosen))
            if support not in correctable:
                failures.append({"roots": chosen, "support": sorted(support)})
    return failures


singleton_correctable = {
    frozenset(),
    frozenset({"C"}),
    frozenset({"D"}),
    frozenset({"F"}),
    frozenset({"G"}),
}

assert audit(independent, 1, singleton_correctable) == []
shared_failures = audit(shared, 1, singleton_correctable)
assert shared_failures == [{"roots": ("rShared",), "support": ["C", "D", "F", "G"]}]

product_correctable = singleton_correctable | {blocks}
assert audit(shared, 1, product_correctable) == []

failure = {
    "code": "fault_image_outside_correctable_family",
    **shared_failures[0],
    "root_fault_count": 1,
    "affected_block_count": 4,
}

print("independent one-root audit:", "safe")
print("shared-root singleton-family witness:", failure)
print("shared-root product-family audit:", "conditionally safe")
print("PASS: root count and physical fault-image support are distinct")
