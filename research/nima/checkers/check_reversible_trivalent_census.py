"""Finite reversible trivalent census; explicit DAG conventions, no seven input."""
import argparse
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
import hashlib
import json
from math import factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / 'research/nima/results/reversible-trivalent-census.json'
# Graph = (vertex orientations: 0 merge, 1 split; internal edges; input/output ports).
# Edge = (source vertex, output slot, target vertex, input slot).


def ports(types):
    ins = tuple((v, s) for v, t in enumerate(types) for s in range(2 if t == 0 else 1))
    outs = tuple((v, s) for v, t in enumerate(types) for s in range(1 if t == 0 else 2))
    return ins, outs


def graph(types, edges):
    edges = tuple(sorted(edges))
    ins, outs = ports(types)
    used_i = {(c, d) for a, b, c, d in edges}
    used_o = {(a, b) for a, b, c, d in edges}
    return (tuple(types), edges, tuple(p for p in ins if p not in used_i),
            tuple(p for p in outs if p not in used_o))


def relabel(g, p, ordered):
    ts, es, ins, outs = g
    nt = [None] * len(ts)
    for v, t in enumerate(ts):
        nt[p[v]] = t
    ni = tuple((p[v], s) for v, s in ins)
    no = tuple((p[v], s) for v, s in outs)
    return (tuple(nt), tuple(sorted((p[a], b, p[c], d) for a, b, c, d in es)),
            ni if ordered else tuple(sorted(ni)), no if ordered else tuple(sorted(no)))


def canonical(g, ordered):
    return min(relabel(g, p, ordered) for p in permutations(range(len(g[0]))))


def reverse(g):
    ts, es, ins, outs = g
    return (tuple(1-t for t in ts), tuple(sorted((c, d, a, b) for a, b, c, d in es)), outs, ins)


def connected_dag(n, edges):
    adj = [set() for _ in range(n)]
    nxt = [set() for _ in range(n)]
    for a, _, c, _ in edges:
        if a == c:
            return False
        adj[a].add(c); adj[c].add(a); nxt[a].add(c)
    seen, todo = set(), [0]
    while todo:
        v = todo.pop()
        if v not in seen:
            seen.add(v); todo.extend(adj[v] - seen)
    if len(seen) != n:
        return False
    def cycle(v, active, done):
        if v in active:
            return True
        if v in done:
            return False
        active.add(v)
        if any(cycle(w, active, done) for w in nxt[v]):
            return True
        active.remove(v); done.add(v)
        return False
    done = set()
    return not any(cycle(v, set(), done) for v in range(n))


def skeletons(n):
    result = set()
    labelled = ordered_labelled = 0
    for ts in product((0, 1), repeat=n):
        ins, outs = ports(ts)
        for k in range(n-1, min(len(ins), len(outs))+1):
            for os in combinations(outs, k):
                for ii in combinations(ins, k):
                    for js in permutations(ii):
                        es = tuple((a, b, c, d) for (a, b), (c, d) in zip(os, js))
                        if connected_dag(n, es):
                            g = graph(ts, es)
                            labelled += 1
                            ordered_labelled += factorial(len(g[2])) * factorial(len(g[3]))
                            result.add(canonical(g, False))
    return result, labelled, ordered_labelled


def ordered_graphs(base):
    return {canonical((g[0], g[1], ii, oo), True) for g in base
            for ii in permutations(g[2]) for oo in permutations(g[3])}


def merge_rotations(g):
    ts, es, ins, outs = g
    for child, slot, parent, target in es:
        if ts[child] != 0 or ts[parent] != 0 or target != 0:
            continue
        # ((a b) c) -> (a (b c)); child remains the lower merge vertex.
        mapping = {(child, 0): (parent, 0), (child, 1): (child, 0),
                   (parent, 1): (child, 1)}
        ne = []
        for a, b, c, d in es:
            if (a, b, c, d) == (child, slot, parent, target):
                ne.append((child, 0, parent, 1))
            else:
                x, y = mapping.get((c, d), (c, d))
                ne.append((a, b, x, y))
        yield (ts, tuple(sorted(ne)), tuple(mapping.get(p, p) for p in ins), outs)


def rewrites(g):
    yield from merge_rotations(g)
    for h in merge_rotations(reverse(g)):
        yield reverse(h)


def validate(g):
    ts, es, ins, outs = g
    all_i, all_o = ports(ts)
    wired_i = [(c, d) for a, b, c, d in es]
    wired_o = [(a, b) for a, b, c, d in es]
    assert sorted(wired_i + list(ins)) == sorted(all_i)
    assert sorted(wired_o + list(outs)) == sorted(all_o)
    assert connected_dag(len(ts), es)
    v, e, b = len(ts), len(es), len(ins)+len(outs)
    rank = e-v+1
    assert 3*v == 2*e+b and b == v+2-2*rank
    assert len(outs)-len(ins) == ts.count(1)-ts.count(0)
    assert reverse(reverse(g)) == g


def analyze(gs, ordered):
    gs = sorted(gs)
    ids = {g: i for i, g in enumerate(gs)}
    edges = set()
    for g in gs:
        validate(g)
        assert canonical(reverse(g), ordered) in ids
        for h in rewrites(g):
            validate(h)
            h = canonical(h, ordered)
            assert h in ids
            assert (len(g[2]), len(g[3])) == (len(h[2]), len(h[3]))
            edges.add(tuple(sorted((ids[g], ids[h]))))
    for a, b in edges:
        ra = ids[canonical(reverse(gs[a]), ordered)]
        rb = ids[canonical(reverse(gs[b]), ordered)]
        assert tuple(sorted((ra, rb))) in edges
    # This is the simple undirected adjacency graph, not a rewrite multigraph
    # or a higher-cell presentation. Multiple placements can share an edge.
    adj = [set() for _ in gs]
    for a, b in edges:
        adj[a].add(b); adj[b].add(a)
    groups = defaultdict(list)
    for i, g in enumerate(gs):
        groups[(len(g[0]), len(g[2]), len(g[3]))].append(i)
    summaries = []
    for (v, m, n), members in sorted(groups.items()):
        unseen = set(members); sizes = []; ranks = []
        while unseen:
            component, todo = set(), [min(unseen)]
            while todo:
                x = todo.pop()
                if x not in component:
                    component.add(x); todo.extend(adj[x]-component)
            unseen -= component
            ec = sum(a in component and b in component for a, b in edges)
            sizes.append(len(component)); ranks.append(ec-len(component)+1)
        summaries.append({'vertices': v, 'boundary': [m, n], 'diagrams': len(members),
                          'rewrite_edges': sum(a in members and b in members for a, b in edges),
                          'component_sizes': dict(sorted(Counter(sizes).items())),
                          'cycle_rank_distribution': dict(sorted(Counter(ranks).items()))})
    records = []
    for i, g in enumerate(gs):
        autos = [p for p in permutations(range(len(g[0]))) if relabel(g, p, ordered) == g]
        assert tuple(range(len(g[0]))) in autos
        assert all(tuple(p[q[v]] for v in range(len(p))) in autos for p in autos for q in autos)
        records.append({'id': i, 'orientations': g[0], 'internal_wires': g[1],
                        'input_order': g[2], 'output_order': g[3],
                        'underlying_cycle_rank': len(g[1])-len(g[0])+1,
                        'automorphisms_on_vertices': autos,
                        'automorphisms_on_inputs': [tuple(g[2].index((p[v], s)) for v, s in g[2]) for p in autos],
                        'automorphisms_on_outputs': [tuple(g[3].index((p[v], s)) for v, s in g[3]) for p in autos],
                        'rewrite_degree': len(adj[i]),
                        'reversed_id': ids[canonical(reverse(g), ordered)]})
    return {'boundary_ordered': ordered, 'summaries': summaries,
            'diagrams': records, 'simple_undirected_rewrite_edges': sorted(edges)}


def self_test():
    assert not connected_dag(1, ((0, 0, 0, 0),))
    assert not connected_dag(2, ((0, 0, 1, 0), (1, 0, 0, 0)))
    assert not connected_dag(2, ())
    assert connected_dag(2, ((0, 0, 1, 0), (0, 1, 1, 1)))
    left = graph((0, 0), ((0, 0, 1, 0),))
    right, = merge_rotations(left)
    assert right != left
    validate(right)
    for g in (left, right, reverse(left), reverse(right)):
        validate(g)
        assert canonical(g, True) == canonical(relabel(g, (1, 0), True), True)
    # Directed rotations become undirected comparisons only in analyze().
    assert not list(merge_rotations(right))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    self_test()
    enumerations = {n: skeletons(n) for n in (1, 2, 3)}
    base = set().union(*(row[0] for row in enumerations.values()))
    quotient = analyze(base, False)
    ordered = analyze(ordered_graphs(base), True)
    for sector in (quotient, ordered):
        for n in (1, 2, 3):
            orbit_mass = sum(factorial(n) // len(g['automorphisms_on_vertices'])
                             for g in sector['diagrams'] if len(g['orientations']) == n)
            assert orbit_mass == enumerations[n][2 if sector['boundary_ordered'] else 1]
        pure = next(s for s in sector['summaries'] if s['vertices'] == 3 and s['boundary'] == [4, 1])
        assert pure['component_sizes'] == {5: 24 if sector['boundary_ordered'] else 1}
        assert pure['cycle_rank_distribution'] == {1: 24 if sector['boundary_ordered'] else 1}
        assert all(g['rewrite_degree'] == 2 for g in sector['diagrams']
                   if len(g['orientations']) == 3 and len(g['input_order']) == 4)
    report = {'schema': 'marici.nima.trivalent-census.v1',
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'conventions': {'vertices': [1, 2, 3], 'connected': 'underlying undirected',
                              'directed_cycles': False, 'self_loops': False, 'parallel_wires': True,
                              'local_slots': 'distinguishable', 'isomorphism': 'vertex relabelling preserving orientations and local slots',
                              'reversal': 'reverse all wires, swap merge/split and ordered boundaries, keep slot numbers',
                              'rewrite_cells': 'merge associativity and its reversal only; adjacency is undirected',
                              'excluded': 'zero-vertex wires, cyclic sectors, mixed generating cells, higher fillers'},
              'tests': {'passed': True, 'checks': ['port incidence and uniqueness', 'connectedness and acyclicity',
                         'boundary balance and cycle-rank identities', 'reversal involution and rewrite equivariance',
                         'vertex relabelling invariance fixture', 'automorphism group identity and closure',
                         'orbit-stabilizer counts against labelled enumeration', 'pure four-input pentagons']},
              'labelled_counts': {n: {'boundary_quotient': row[1], 'boundary_ordered': row[2]}
                                  for n, row in enumerations.items()},
              'ordered': ordered, 'boundary_permutation_quotient': quotient,
              'limitations': ['Simple graph cycle rank is not a classification of higher coherence cells.',
                              'Same-boundary disconnected components do not require a mixed comparison without a target semantics.',
                              'No definition of essential grade or cell has been supplied; seven-grade conjecture remains unassessed.']}
    if args.write:
        RESULT.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    for title, sector in [('ordered', ordered), ('boundary quotient', quotient)]:
        print(title, 'diagrams:', len(sector['diagrams']))
        for s in sector['summaries']:
            print(s)


if __name__ == '__main__':
    main()
