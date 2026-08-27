import json
from pathlib import Path


def bracketings(items):
    if len(items) == 1:
        return {items[0]}
    out = set()
    for split in range(1, len(items)):
        for left in bracketings(items[:split]):
            for right in bracketings(items[split:]):
                out.add((left, right))
    return out


def rotations(tree):
    if isinstance(tree, str):
        return set()
    left, right = tree
    out = set()
    if isinstance(left, tuple):
        a, b = left
        out.add((a, (b, right)))
    if isinstance(right, tuple):
        b, c = right
        out.add(((left, b), c))
    for moved in rotations(left):
        out.add((moved, right))
    for moved in rotations(right):
        out.add((left, moved))
    return out


def leaves(tree):
    if isinstance(tree, str):
        return (tree,)
    return leaves(tree[0]) + leaves(tree[1])


arrows = ("eta", "J", "K", "epsilon")
vertices = bracketings(arrows)
assert len(vertices) == 5
assert all(leaves(v) == arrows for v in vertices)

edges = set()
for source in vertices:
    for target in rotations(source):
        if target in vertices and source != target:
            edges.add(frozenset((source, target)))
assert len(edges) == 5

degree = {v: 0 for v in vertices}
for edge in edges:
    for v in edge:
        degree[v] += 1
assert set(degree.values()) == {2}

seen = set()
frontier = [next(iter(vertices))]
while frontier:
    v = frontier.pop()
    if v in seen:
        continue
    seen.add(v)
    for edge in edges:
        if v in edge:
            frontier.extend(x for x in edge if x != v and x not in seen)
assert seen == vertices


def render(tree):
    if isinstance(tree, str):
        return tree
    return f"({render(tree[0])} {render(tree[1])})"


result = {
    "ordered_arrows": list(arrows),
    "parenthesization_count": len(vertices),
    "associator_edge_count": len(edges),
    "vertex_degrees": sorted(degree.values()),
    "connected": True,
    "rotation_graph": "five-cycle associahedron K4",
    "unlabelled_graph_automorphism_group": "D5",
    "typed_state_port_rotation_inferred": False,
    "theta_smoothing_correspondence_constructed": False,
    "parenthesizations": sorted(render(v) for v in vertices),
    "verdict": "five counts coherent presentations of a four-stage composite, not five state channels",
}

out = Path(__file__).parents[1] / "results" / "rh-four-stage-associahedron.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
