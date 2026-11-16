"""Generate Ramsey(3,6,17) witnesses from Clebsch, with no target graph input.

Requires networkx. Run:
    python ramsey36_generate_square_births.py

Moves are degree-preserving square switches on 16-node 5-regular carriers,
followed by 2, 3 or 4 half-square moves and one four-port birth.
Only no-A-triangle/no-B-six conditions filter states. Isomorphisms deduplicate
states; no catalogue is used. The output JSON records each construction.
"""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json
import argparse
import networkx as nx


def bitgraph(n, E):
    a = [0] * n
    for u, v in E:
        a[u] |= 1 << v
        a[v] |= 1 << u
    return tuple(a)


def independent6(a):
    def visit(mask, left):
        if left == 0:
            return True
        while mask.bit_count() >= left:
            bit = mask & -mask
            mask ^= bit
            u = bit.bit_length() - 1
            if visit(mask & ~a[u], left - 1):
                return True
        return False
    return visit((1 << len(a)) - 1, 6)


def admissible(n, E):
    a = bitgraph(n, E)
    return not any(a[u] & a[v] for u, v in E) and not independent6(a)


def graph(n, E):
    g = nx.Graph()
    g.add_nodes_from(range(n))
    g.add_edges_from(E)
    return g


def fingerprint(n, E):
    a = bitgraph(n, E)
    common = Counter((a[u] & a[v]).bit_count()
                     for u, v in combinations(range(n), 2) if (u, v) not in E)
    return (len(E), tuple(sorted(x.bit_count() for x in a)),
            tuple(sorted(common.items())))


class Classes:
    def __init__(self, n):
        self.n = n
        self.items = []
        self.graphs = []
        self.buckets = {}

    def add(self, E, history):
        """Return whether E is a new isomorphism class."""
        key = fingerprint(self.n, E)
        bucket = self.buckets.get(key, [])
        g = graph(self.n, E)
        if any(nx.is_isomorphic(g, self.graphs[j]) for j in bucket):
            return False
        self.buckets.setdefault(key, []).append(len(self.items))
        self.items.append((E, history))
        self.graphs.append(g)
        return True


def moves(E, kind):
    assert kind in ("half", "switch")
    for S in combinations(range(16), 4):
        allpairs = set(combinations(S, 2))
        present = allpairs & E
        if len(present) != 4:
            continue
        deg = Counter(x for p in present for x in p)
        if any(deg[x] != 2 for x in S):
            continue
        diagonals = allpairs - present
        for removed in combinations(sorted(present), 2):
            if not set(removed[0]).isdisjoint(removed[1]):
                continue
            additions = [tuple(sorted(diagonals))] if kind == "switch" else \
                        [(d,) for d in sorted(diagonals)]
            for added in additions:
                H = E.difference(removed).union(added)
                description = {"kind": kind, "vertices": list(S),
                               "remove": [list(p) for p in removed],
                               "add": [list(p) for p in added]}
                yield H, description


def births(E):
    a = bitgraph(16, E)
    # A-degree <=5 follows directly because any A-neighborhood is a B-group.
    eligible = [v for v in range(16) if a[v].bit_count() < 5]
    for P in combinations(eligible, 4):
        if any(a[u] >> v & 1 for u, v in combinations(P, 2)):
            continue
        H = E.union((v, 16) for v in P)
        if admissible(17, H):
            yield H, list(P)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path("ramsey36_forward_generated.json"))
    args = parser.parse_args()

    C = frozenset((i, j) for i, j in combinations(range(16), 2)
                  if (i ^ j).bit_count() in (1, 4))
    assert admissible(16, C)
    regular = Classes(16)
    regular.add(C, [])
    index = 0
    while index < len(regular.items):
        E, history = regular.items[index]
        for H, operation in moves(E, "switch"):
            if admissible(16, H):
                regular.add(H, history + [operation])
        index += 1
    print("Regular switch closure:", len(regular.items), flush=True)

    output = Classes(17)
    previous = regular
    layer_sizes = [len(regular.items)]
    accepted = {}
    for depth in range(1, 4):
        current = Classes(16)
        for E, history in previous.items:
            for H, operation in moves(E, "half"):
                if admissible(16, H):
                    current.add(H, history + [operation])
        previous = current
        layer_sizes.append(len(current.items))
        print("Half-square layer", depth, "classes", len(current.items), flush=True)
        if depth >= 2:
            count = 0
            for E, history in current.items:
                for H, P in births(E):
                    count += 1
                    output.add(H, {"moves": history, "birth_ports": P})
            accepted[depth] = count

    # Fuse the final half move with birth testing. A valid born graph implies
    # that its preceding 16-node induced graph is admissible as well.
    fourth_candidates = count = 0
    for E, history in previous.items:
        for H16, operation in moves(E, "half"):
            fourth_candidates += 1
            for H17, P in births(H16):
                count += 1
                output.add(H17, {"moves": history + [operation], "birth_ports": P})
    accepted[4] = count
    payload = {
        "carrier_generators_xor": [1, 2, 4, 8, 15],
        "regular_and_half_layer_class_counts": layer_sizes,
        "accepted_births_by_half_move_count": accepted,
        "fourth_half_candidates": fourth_candidates,
        "generated_type_count": len(output.items),
        "outputs": [{**history, "edges": sorted(E)} for E, history in output.items],
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print("Nonisomorphic 17-node outputs:", len(output.items))
    print("Accepted births by half-square depth:", accepted)
    print("Saved", args.output)


if __name__ == "__main__":
    main()
