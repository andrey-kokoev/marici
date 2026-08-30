"""WP11: transport the one-loop phase line through the exact tree-face carrier groupoid.

The exact 33-edge spanning tree (wp10_exact_tree_face_spanning_groupoid)
connects all 34 sparse-fiber components.  Every remaining exact tree-face
arrow closes a fundamental cycle in the carrier incidence graph.  This
checker transports the oriented one-loop phase line (the unique signed
fundamental cycle of each nine-link support, oriented so the fitted phase
edge has coefficient +1) around every fundamental cycle and records the
Z2 monodromy.  All arithmetic is exact (permutations and integer signs
only; no fitted values are used).

Convention: cycle vectors are true incidence-kernel elements (divergence
free), with the distinguished edge (phase edge at a vertex, deleted normal
on a face) at coefficient +1.  This differs from the WP10 kernel checker's
labelled occurrence vector, which pinned the normal to +1 but walked the
tree path Q -> column; that vector is not in the cycle space and cannot be
compared across different normals.  WP11 compares cycles across normals,
so it needs genuine cycle-space elements.  Part C below re-audits the
WP10 kernel connectivity under the corrected vectors.

Structure:
  A. per-vertex oriented cycles and per-occurrence transport signs;
  B. vertex-level carrier multigraph: spanning tree, fundamental cycles,
     Z2 monodromy (trivial / twist / ambiguous) at occurrence granularity;
  C. WP10 kernel re-audit with true cycle vectors.
"""
from collections import defaultdict, deque
import itertools, json
from pathlib import Path

from wp10_exact_tree_face_spanning_groupoid import (
    ATLAS, INC, PERMS, graph_cc, slots, transport)

OUT = Path("research/flavor/results/wp11_phase_line_transport.json")

a = json.loads(ATLAS.read_text())
inc = json.loads(INC.read_text())
vertices = {v["id"]: v for v in inc["vertices"]}
vc = {v: i for i, c in enumerate(inc["components"]) for v in c["vertices"]}
ncomp = len(inc["components"])


def endpoints(edge):
    s, i, j = edge
    return i, (3 if s == "u" else 6) + j


def face_edges(pair):
    return [("u", i, j) for i, j in slots(pair[0])] + [("d", i, j) for i, j in slots(pair[1])]


def cycle(pair, normal):
    """True incidence-kernel fundamental cycle of T+{normal}; normal coeff +1.

    Walk the tree path from the normal's column endpoint back to its Q
    endpoint, +1 on Q -> column crossings (divergence-free signed cycle).
    """
    adjacency = defaultdict(list)
    for edge in face_edges(pair):
        x, y = endpoints(edge)
        adjacency[x].append((y, edge))
        adjacency[y].append((x, edge))
    start, end = endpoints(normal)
    queue = deque([end])
    previous = {end: None}
    while queue:
        x = queue.popleft()
        if x == start:
            break
        for y, e in adjacency[x]:
            if y not in previous:
                previous[y] = (x, e)
                queue.append(y)
    assert start in previous
    vector = {normal: 1}
    x = start
    while x != end:
        px, e = previous[x]
        q, col = endpoints(e)
        # previous chains run start -> end; flip to record the closed walk
        vector[e] = -1 if (x, px) == (q, col) else 1
        x = px
    return vector


def act(edge, p):
    s, i, j = edge
    q, u, d = p
    return (s, q[i], (u if s == "u" else d)[j])


def inv_act(edge, p):
    s, i, j = edge
    q, u, d = p
    qi = [q.index(k) for k in range(3)]
    ui = [u.index(k) for k in range(3)]
    di = [d.index(k) for k in range(3)]
    return (s, qi[i], (ui if s == "u" else di)[j])


def all_witnesses(pair, canon):
    return [(q, u, d) for q, u, d in itertools.product(PERMS, repeat=3)
            if (transport(pair[0], q, u), transport(pair[1], q, d)) == canon]


def reduced(member, edge):
    mu, md = member
    s, i, j = edge
    bit = 1 << (3 * i + j)
    return (mu & ~bit, md) if s == "u" else (mu, md & ~bit)


def sign_of(vec, target):
    if all(vec.get(e, 0) == c for e, c in target.items()):
        return 1
    if all(vec.get(e, 0) == -c for e, c in target.items()):
        return -1
    return 0


# ---- A. vertex cycles and occurrence signs -----------------------------------
vertex_cycle = {}
exceptions = []
for vid, v in vertices.items():
    member = tuple(v["member"])
    phase = tuple(v["phase_edge"])
    red = reduced(member, phase)
    if graph_cc(red) != (1, 8):
        exceptions.append({"vertex": vid, "reason": "phase edge not on the unique cycle"})
        continue
    vertex_cycle[vid] = cycle(red, phase)

tree_faces = {f["canonical_face"]: tuple(f["canonical_masks"])
              for f in a["faces"] if graph_cc(f["canonical_masks"]) == (1, 8)}

# occ_signs[(vid, sector, row, column, face)] = set of signs over witnesses
occ_signs = defaultdict(set)
occurrences = defaultdict(list)  # face -> list of occurrence keys
for vs, faces in a["vertex_faces"].items():
    vid = int(vs)
    if vid not in vertex_cycle:
        continue
    member = tuple(vertices[vid]["member"])
    for x in faces:
        cf = x["canonical_face"]
        if cf not in tree_faces:
            continue
        edge = (x["sector"], x["row"], x["column"])
        key = (vid, edge[0], edge[1], edge[2], cf)
        for p in all_witnesses(reduced(member, edge), cf and tree_faces[cf]):
            pulled = {}
            for e, coeff in cycle(tree_faces[cf], act(edge, p)).items():
                pulled[inv_act(e, p)] = coeff
            sgn = sign_of(pulled, vertex_cycle[vid])
            if sgn == 0:
                exceptions.append({"vertex": vid, "face": cf,
                                   "reason": "face cycle pullback is not +- the vertex cycle"})
                continue
            occ_signs[key].add(sgn)
        if key in occ_signs:
            occurrences[cf].append(key)

occ_ambiguous = sum(1 for s in occ_signs.values() if len(s) > 1)

# internal component transports (S3^3 witnesses between vertex supports)
internal = {}

def internal_signs(v0, v1):
    if v0 == v1:
        return {1}
    key = (min(v0, v1), max(v0, v1))
    if key not in internal:
        m0 = tuple(vertices[key[0]]["member"])
        m1 = tuple(vertices[key[1]]["member"])
        signs = set()
        for p in itertools.product(PERMS, repeat=3):
            q, u, d = p
            if transport(m0[0], q, u) == m1[0] and transport(m0[1], q, d) == m1[1]:
                pushed = {act(e, p): c for e, c in vertex_cycle[key[0]].items()}
                sgn = sign_of(pushed, vertex_cycle[key[1]])
                if sgn:
                    signs.add(sgn)
        internal[key] = signs
    return internal[key]

internal_adj = defaultdict(set)
for c in inc["components"]:
    for v0, v1 in itertools.combinations(sorted(c["vertices"]), 2):
        if internal_signs(v0, v1):
            internal_adj[v0].add(v1)
            internal_adj[v1].add(v0)
internal_ambiguous = sum(1 for k in internal if len(internal[k]) > 1)

# ---- B. vertex-level carrier multigraph --------------------------------------
# arrows: occurrence pairs sharing a canonical tree face (any components)
arrows = []
for cf, keys in sorted(occurrences.items()):
    for o0, o1 in itertools.combinations(sorted(set(keys)), 2):
        arrows.append((cf, o0, o1))

def arrow_sign_set(o0, o1):
    return {s0 * s1 for s0 in occ_signs[o0] for s1 in occ_signs[o1]}

# spanning tree over 61 vertices: internal S3^3 adjacency + face arrows
parent = list(range(61))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

tree_edges = []
internal_tree = set()
for v0 in sorted(internal_adj):
    for v1 in sorted(internal_adj[v0]):
        if v0 < v1:
            x, y = find(v0), find(v1)
            if x != y:
                parent[y] = x
                tree_edges.append(("internal", v0, v1))
                internal_tree.add((v0, v1))
face_tree = set()
for cf, o0, o1 in arrows:
    x, y = find(o0[0]), find(o1[0])
    if x != y:
        parent[y] = x
        tree_edges.append(("face", cf, o0, o1))
        face_tree.add((cf, o0, o1))
vertex_components = len({find(i) for i in range(61)})

# adjacency for tree paths
tr_adj = defaultdict(list)
for e in tree_edges:
    if e[0] == "internal":
        _, v0, v1 = e
        tr_adj[v0].append((v1, e))
        tr_adj[v1].append((v0, e))
    else:
        _, cf, o0, o1 = e
        tr_adj[o0[0]].append((o1[0], e))
        tr_adj[o1[0]].append((o0[0], e))

def tree_path(v0, v1):
    prev = {v0: None}
    dq = deque([v0])
    while dq:
        x = dq.popleft()
        if x == v1:
            break
        for y, e in tr_adj[x]:
            if y not in prev:
                prev[y] = (x, e)
                dq.append(y)
    path = []
    node = v1
    while prev[node] is not None:
        px, e = prev[node]
        path.append(e)
        node = px
    return path[::-1]

def edge_sign_set(e, from_vertex):
    """Signs for crossing tree edge e starting at from_vertex."""
    if e[0] == "internal":
        _, v0, v1 = e
        assert from_vertex in (v0, v1)
        return internal_signs(v0, v1)
    _, cf, o0, o1 = e
    if from_vertex == o0[0]:
        return arrow_sign_set(o0, o1)
    return arrow_sign_set(o1, o0)

def path_sign_set(v0, v1):
    signs = {1}
    cur = v0
    for e in tree_path(v0, v1):
        signs = {a * b for a in signs for b in edge_sign_set(e, cur)}
        if e[0] == "internal":
            cur = e[2] if e[1] == cur else e[1]
        else:
            _, cf, o0, o1 = e
            cur = o1[0] if cur == o0[0] else o0[0]
    return signs

# fundamental cycles: every arrow or internal edge not in the spanning tree
fundamental = []
for cf, o0, o1 in arrows:
    if (cf, o0, o1) in face_tree:
        continue
    signs = {a * b for a in path_sign_set(o0[0], o1[0]) for b in arrow_sign_set(o0, o1)}
    fundamental.append({"kind": "face_arrow", "canonical_face": cf,
                        "vertices": [o0[0], o1[0]],
                        "components": sorted({vc[o0[0]], vc[o1[0]]}),
                        "signs": sorted(signs)})
for v0 in sorted(internal_adj):
    for v1 in sorted(internal_adj[v0]):
        if v0 < v1 and (v0, v1) not in internal_tree:
            signs = {a * b for a in path_sign_set(v0, v1) for b in internal_signs(v0, v1)}
            fundamental.append({"kind": "internal", "vertices": [v0, v1],
                                "components": [vc[v0]], "signs": sorted(signs)})

def verdict(signs):
    if signs == [1]:
        return "trivial"
    if signs == [-1]:
        return "twist"
    return "ambiguous"

# independent cross-check: the Z2 monodromy is a coboundary iff the definite
# signed graph (definite arrows + definite internal edges) admits a global
# signing o(v) with o(v) = s*o(u) on every definite edge.  BFS over the
# definite signed graph; any violated edge witnesses nontriviality.
definite_edges = []
for cf, o0, o1 in arrows:
    s = arrow_sign_set(o0, o1)
    if len(s) == 1:
        definite_edges.append((o0[0], o1[0], next(iter(s)), ("face", cf)))
for (v0, v1), signs in sorted(internal.items()):
    if len(signs) == 1:
        definite_edges.append((v0, v1, next(iter(signs)), ("internal",)))
orient = {}
conflicts = []
dad = defaultdict(list)
for v0, v1, s, tag in definite_edges:
    dad[v0].append((v1, s, tag))
    dad[v1].append((v0, s, tag))
for seed in range(61):
    if seed in orient or seed not in dad:
        continue
    orient[seed] = 1
    dq = deque([seed])
    while dq:
        x = dq.popleft()
        for y, s, tag in dad[x]:
            want = s * orient[x]
            if y not in orient:
                orient[y] = want
                dq.append(y)
            elif orient[y] != want:
                conflicts.append({"between": sorted((x, y)), "sign": s,
                                  "tag": tag[0]})
conflict_edges = {(tuple(c["between"]), c["sign"]) for c in conflicts}

summary = defaultdict(int)
for r in fundamental:
    summary[verdict(r["signs"])] += 1
by_kind = defaultdict(lambda: defaultdict(int))
for r in fundamental:
    by_kind[r["kind"]][verdict(r["signs"])] += 1
twists = [r for r in fundamental if verdict(r["signs"]) == "twist"]

# ---- C. WP10 kernel re-audit with true cycle vectors -------------------------
def autos(pair):
    return [g for g in itertools.product(PERMS, repeat=3)
            if transport(pair[0], g[0], g[1]) == pair[0]
            and transport(pair[1], g[0], g[2]) == pair[1]]

def dot(v, w):
    return sum(v.get(e, 0) * w.get(e, 0) for e in set(v) | set(w))

kernel_pairs = set()
kernel_overlap = defaultdict(int)
for cf, keys in sorted(occurrences.items()):
    canon = tree_faces[cf]
    aa = autos(canon)
    comps = sorted({vc[k[0]] for k in keys})
    for cx, cy in itertools.combinations(comps, 2):
        hit = None
        for o0 in [k for k in keys if vc[k[0]] == cx]:
            edge0 = (o0[1], o0[2], o0[3])
            m0 = tuple(vertices[o0[0]]["member"])
            for p0 in all_witnesses(reduced(m0, edge0), canon):
                c0 = cycle(canon, act(edge0, p0))
                for o1 in [k for k in keys if vc[k[0]] == cy]:
                    edge1 = (o1[1], o1[2], o1[3])
                    m1 = tuple(vertices[o1[0]]["member"])
                    for p1 in all_witnesses(reduced(m1, edge1), canon):
                        n1 = act(edge1, p1)
                        for g in aa:
                            value = dot(c0, cycle(canon, act(n1, g)))
                            if value:
                                hit = abs(value)
                                break
                        if hit:
                            break
                    if hit:
                        break
                if hit:
                    break
            if hit:
                break
        if hit:
            kernel_pairs.add((cx, cy))
            kernel_overlap[hit] += 1

kparent = list(range(ncomp))
def kfind(x):
    while kparent[x] != x:
        kparent[x] = kparent[kparent[x]]
        x = kparent[x]
    return x
for x, y in sorted(kernel_pairs):
    fx, fy = kfind(x), kfind(y)
    if fx != fy:
        kparent[fy] = fx
kernel_components = len({kfind(i) for i in range(ncomp)})

out = {
    "schema": "marici.flavor.phase_line_transport.v1",
    "vertex_count": 61,
    "vertices_with_cycle": len(vertex_cycle),
    "cycle_exceptions": exceptions,
    "occurrence_count": len(occ_signs),
    "occurrence_sign_ambiguous_count": occ_ambiguous,
    "internal_pair_count": len(internal),
    "internal_sign_ambiguous_count": internal_ambiguous,
    "coboundary_check": {
        "definite_edge_count": len(definite_edges),
        "oriented_vertex_count": len(orient),
        "signing_conflict_count": len(conflict_edges),
        "cocycle_nontrivial": bool(conflict_edges),
    },
    "vertex_level": {
        "arrow_count": len(arrows),
        "spanning_tree_edge_count": len(tree_edges),
        "connected_components": vertex_components,
        "fundamental_cycles_tested": len(fundamental),
        "monodromy_summary": dict(sorted(summary.items())),
        "by_kind": {k: dict(sorted(v.items())) for k, v in sorted(by_kind.items())},
        "twist_cycle_count": len(twists),
        "twist_examples": twists[:25],
    },
    "wp10_kernel_reaudit_true_vectors": {
        "compatible_component_pair_count": len(kernel_pairs),
        "kernel_components": kernel_components,
        "absolute_overlap_histogram": dict(sorted(kernel_overlap.items())),
        "wp10_committed_values": {"compatible_component_pair_count": 370, "component_count": 1},
    },
    "criterion": ("Oriented phase line (unique signed support cycle, phase edge at +1, "
                  "true incidence-kernel vectors) transported through exact tree-face "
                  "arrows; Z2 monodromy recorded per fundamental cycle of the "
                  "vertex-level carrier multigraph."),
    "scope": ("Exact support/permutation level only. A twist means the oriented loop "
              "holonomy is a Mobius (unoriented) line over the exact carrier groupoid; "
              "it says nothing by itself about descent to the physical quotient."),
}
OUT.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({k: v for k, v in out.items()
                  if k not in ("cycle_exceptions",)}, indent=2))
if exceptions:
    print("EXCEPTIONS:", json.dumps(exceptions[:10], indent=2))
