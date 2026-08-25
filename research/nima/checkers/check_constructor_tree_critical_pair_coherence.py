"""Finite critical-pair checker for constructor-tree rewrites."""


def normal_forms(start, rules):
    frontier = [start]
    seen = set()
    normals = set()
    while frontier:
        node = frontier.pop()
        if node in seen:
            continue
        seen.add(node)
        targets = rules.get(node, ())
        if not targets:
            normals.add(node)
        else:
            frontier.extend(targets)
    return normals


def critical_pair(start, rules):
    branches = rules.get(start, ())
    if len(branches) < 2:
        return None
    left, right = branches[:2]
    left_nf = normal_forms(left, rules)
    right_nf = normal_forms(right, rules)
    joins = left_nf & right_nf
    if joins:
        return {"status": "joined", "normal_forms": sorted(joins)}
    return {
        "code": "constructor_tree_coherence_failure",
        "node": start,
        "branches": [left, right],
        "left_normal_forms": sorted(left_nf),
        "right_normal_forms": sorted(right_nf),
        "missing_cell": f"{right}->{next(iter(left_nf))}",
    }


unfilled = {"T": ("L", "R"), "L": ("N",)}
filled = {"T": ("L", "R"), "L": ("N",), "R": ("N",)}
same_bytes = {"L": b"authority", "R": b"authority", "N": b"authority"}

failure = critical_pair("T", unfilled)
success = critical_pair("T", filled)

assert same_bytes["L"] == same_bytes["R"] == same_bytes["N"]
assert failure["code"] == "constructor_tree_coherence_failure"
assert failure["left_normal_forms"] == ["N"]
assert failure["right_normal_forms"] == ["R"]
assert success == {"status": "joined", "normal_forms": ["N"]}

print("equal evaluator bytes:", same_bytes["L"])
print("unfilled critical pair:", failure)
print("filled critical pair:", success)
print("PASS: joinability, not output equality, establishes tree coherence")
