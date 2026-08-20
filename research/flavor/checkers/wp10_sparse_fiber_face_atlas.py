"""Codimension-one carrier gate for the sparse flavor-fiber groupoid.

Every nonzero Yukawa entry of every fiber representative is deleted in turn.
The resulting pair of eight-link supports is canonicalized under the
sector-preserving S3_Q x S3_u x S3_d action. Sharing a canonical face is only
necessary for a boundary incidence arrow; no coefficient/readout equality is
inferred here.
"""
from collections import defaultdict
import itertools
import json

INCIDENCE = "research/flavor/results/wp10_sparse_fiber_incidence_graph.json"
OUTPUT = "research/flavor/results/wp10_sparse_fiber_face_atlas.json"
PERMS = list(itertools.permutations(range(3)))


def slots(mask):
    return [(i, j) for i in range(3) for j in range(3)
            if mask & (1 << (3*i+j))]


def mask_of(entries):
    return sum(1 << (3*i+j) for i, j in entries)


def transport(mask, rows, columns):
    return mask_of((rows[i], columns[j]) for i, j in slots(mask))


def canonical_pair(mask_u, mask_d):
    return min(
        (transport(mask_u, q, u), transport(mask_d, q, d))
        for q, u, d in itertools.product(PERMS, repeat=3))


def union_find(n, edges):
    parent = list(range(n))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for a, b in edges:
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a
    groups = {}
    for i in range(n):
        groups.setdefault(find(i), []).append(i)
    return sorted(groups.values(), key=lambda x: (len(x), x), reverse=True)


def main():
    packet = json.load(open(INCIDENCE))
    vertices = packet["vertices"]
    vertex_component = {}
    for component_id, component in enumerate(packet["components"]):
        for vertex in component["vertices"]:
            vertex_component[vertex] = component_id

    faces = {}
    vertex_faces = {}
    for vertex in vertices:
        vid = vertex["id"]
        mu, md = vertex["member"]
        local = []
        for sector, mask in (("u", mu), ("d", md)):
            for i, j in slots(mask):
                reduced = mask & ~(1 << (3*i+j))
                key = canonical_pair(reduced, md) if sector == "u" \
                    else canonical_pair(mu, reduced)
                key_text = f"{key[0]}:{key[1]}"
                local.append({"sector": sector, "row": i, "column": j,
                              "canonical_face": key_text})
                faces.setdefault(key_text, {
                    "canonical_masks": list(key),
                    "vertices": set(),
                    "components": set(),
                    "occurrences": 0,
                })
                faces[key_text]["vertices"].add(vid)
                faces[key_text]["components"].add(vertex_component[vid])
                faces[key_text]["occurrences"] += 1
        vertex_faces[str(vid)] = local

    eligible_component_edges = set()
    pair_faces = defaultdict(list)
    for key, face in faces.items():
        components = sorted(face["components"])
        for a, b in itertools.combinations(components, 2):
            eligible_component_edges.add((a, b))
            pair_faces[(a, b)].append(key)
    carrier_components = union_find(
        len(packet["components"]), sorted(eligible_component_edges))

    # A deterministic maximum-support spanning tree bounds the expensive
    # readout continuations at 33. Prefer witnesses shared by more vertices
    # and components, then break ties lexicographically.
    candidates = []
    for edge, keys in pair_faces.items():
        key = max(keys, key=lambda k: (
            len(faces[k]["vertices"]), len(faces[k]["components"]), k))
        candidates.append((
            -len(faces[key]["vertices"]),
            -len(faces[key]["components"]), edge, key))
    candidates.sort()
    tree_parent = list(range(len(packet["components"])))
    def tree_find(a):
        while tree_parent[a] != a:
            tree_parent[a] = tree_parent[tree_parent[a]]
            a = tree_parent[a]
        return a
    spanning_tree = []
    for _, _, (a, b), key in candidates:
        ra, rb = tree_find(a), tree_find(b)
        if ra == rb:
            continue
        tree_parent[rb] = ra
        spanning_tree.append({
            "source_component": a,
            "target_component": b,
            "canonical_face": key,
            "face_vertex_count": len(faces[key]["vertices"]),
            "face_component_count": len(faces[key]["components"]),
        })

    serialized_faces = []
    for key, face in sorted(faces.items()):
        serialized_faces.append({
            "canonical_face": key,
            "canonical_masks": face["canonical_masks"],
            "occurrences": face["occurrences"],
            "vertex_count": len(face["vertices"]),
            "component_count": len(face["components"]),
            "vertices": sorted(face["vertices"]),
            "components": sorted(face["components"]),
        })

    out = {
        "schema": "marici.flavor.sparse_fiber_face_atlas.v1",
        "strength": "finite_combinatorial_carrier_gate",
        "source": INCIDENCE,
        "vertex_count": len(vertices),
        "input_component_count": len(packet["components"]),
        "face_occurrence_count": sum(
            face["occurrences"] for face in faces.values()),
        "canonical_face_type_count": len(faces),
        "shared_face_type_count": sum(
            len(face["components"]) > 1 for face in faces.values()),
        "carrier_eligible_component_pair_count":
            len(eligible_component_edges),
        "carrier_gate_component_count": len(carrier_components),
        "carrier_gate_component_sizes":
            [len(c) for c in carrier_components],
        "minimum_readout_compatible_edges_if_gate_connects": (
            len(packet["components"])-len(carrier_components)),
        "carrier_gate_spanning_tree_edge_count": len(spanning_tree),
        "carrier_gate_spanning_tree": spanning_tree,
        "scope": (
            "a common canonical support face is necessary but not sufficient; "
            "normalized boundary readout, phase/deck data, and continuation "
            "must still be matched before admitting an incidence arrow"),
        "carrier_eligible_component_edges": [
            list(edge) for edge in sorted(eligible_component_edges)],
        "faces": serialized_faces,
        "vertex_faces": vertex_faces,
    }
    with open(OUTPUT, "w", encoding="utf-8") as handle:
        json.dump(out, handle, indent=2)
        handle.write("\n")
    print(json.dumps({key: out[key] for key in (
        "vertex_count", "input_component_count", "face_occurrence_count",
        "canonical_face_type_count", "shared_face_type_count",
        "carrier_eligible_component_pair_count",
        "carrier_gate_component_count", "carrier_gate_component_sizes",
        "minimum_readout_compatible_edges_if_gate_connects",
        "carrier_gate_spanning_tree_edge_count")}, indent=2))


if __name__ == "__main__":
    main()
