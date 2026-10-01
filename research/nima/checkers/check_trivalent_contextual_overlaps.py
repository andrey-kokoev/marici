"""Experimental Frobenius extension: contextual placements and bounded forks.

Directed rules are chosen for this experiment, not claimed terminating or
confluent. Only induced, two-vertex, one-wire subdiagrams are replaced.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations
from pathlib import Path
import hashlib
import json
import check_reversible_trivalent_census as C
from check_trivalent_mixed_candidate import evaluate, transpose_mu

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / 'research/nima/results/trivalent-contextual-overlaps.json'


def rules():
    al = C.graph((0, 0), ((0, 0, 1, 0),))
    ar, = C.merge_rotations(al)
    k = ((0, 1), ((0, 0, 1, 0),), ((0, 0), (0, 1)), ((1, 0), (1, 1)))
    fl = ((0, 1), ((1, 0, 0, 1),), ((0, 0), (1, 0)), ((0, 0), (1, 1)))
    fr = ((0, 1), ((1, 1, 0, 0),), ((1, 0), (0, 1)), ((1, 0), (0, 0)))
    return [('alpha', al, ar), ('reverse_alpha', C.reverse(al), C.reverse(ar)),
            ('frobenius_left', k, fl), ('frobenius_right', k, fr)]


def replace(g, lhs, rhs, embedding):
    """Return None unless embedding is an exact induced subdiagram match."""
    ts, es, ins, outs = g
    support = set(embedding)
    if any(ts[embedding[i]] != t for i, t in enumerate(lhs[0])):
        return None
    def embed_edges(edges):
        return {(embedding[a], b, embedding[c], d) for a, b, c, d in edges}
    old = embed_edges(lhs[1])
    if {e for e in es if e[0] in support and e[2] in support} != old:
        return None
    imap = {(embedding[a], b): (embedding[c], d) for (a, b), (c, d) in zip(lhs[2], rhs[2])}
    omap = {(embedding[a], b): (embedding[c], d) for (a, b), (c, d) in zip(lhs[3], rhs[3])}
    edges = list(embed_edges(rhs[1]))
    for a, b, c, d in es:
        if (a, b, c, d) not in old:
            x, y = omap.get((a, b), (a, b))
            z, w = imap.get((c, d), (c, d))
            edges.append((x, y, z, w))
    types = list(ts)
    for i, t in enumerate(rhs[0]):
        types[embedding[i]] = t
    return (tuple(types), tuple(sorted(edges)), tuple(imap.get(p, p) for p in ins),
            tuple(omap.get(p, p) for p in outs))


def convex_support(g, support):
    # A proper DAG context cannot leave the matched support and then re-enter it.
    nxt = defaultdict(set)
    for a, _, b, _ in g[1]:
        nxt[a].add(b)
    todo = [b for a in support for b in nxt[a] if b not in support]
    seen = set()
    while todo:
        v = todo.pop()
        if v in support:
            return False
        if v not in seen:
            seen.add(v); todo.extend(nxt[v])
    return True


def reachable(start, outgoing):
    paths, todo = {start: []}, deque([start])
    while todo:
        x = todo.popleft()
        for eid, y in outgoing[x]:
            if y not in paths:
                paths[y] = paths[x] + [eid]
                todo.append(y)
    return paths


def summarize(gs, steps, active_rules):
    selected = [e for e in steps if e['rule'] in active_rules]
    outgoing, undirected = defaultdict(list), defaultdict(set)
    by_source = defaultdict(list)
    for e in selected:
        outgoing[e['source']].append((e['id'], e['target']))
        by_source[e['source']].append(e)
        undirected[e['source']].add(e['target'])
        undirected[e['target']].add(e['source'])
    reach = {i: reachable(i, outgoing) for i in range(len(gs))}
    forks = []
    for src, es in sorted(by_source.items()):
        for a, b in combinations(es, 2):
            intersection = set(a['embedding']) & set(b['embedding'])
            kind = ('same_support' if set(a['embedding']) == set(b['embedding']) else
                    'shared_vertex' if intersection else 'disjoint')
            common = set(reach[a['target']]) & set(reach[b['target']])
            join = min(common, key=lambda j: (len(reach[a['target']][j])+len(reach[b['target']][j]), j)) if common else None
            forks.append({'source': src, 'steps': [a['id'], b['id']], 'overlap': kind,
                          'same_target': a['target'] == b['target'], 'join': join,
                          'left_path': reach[a['target']][join] if join is not None else None,
                          'right_path': reach[b['target']][join] if join is not None else None,
                          'left_normal_forms': sorted(x for x in reach[a['target']] if not outgoing[x]),
                          'right_normal_forms': sorted(x for x in reach[b['target']] if not outgoing[x])})
    groups = defaultdict(list)
    for i, g in enumerate(gs):
        groups[(len(g[0]), len(g[2]), len(g[3]))].append(i)
    rows = []
    for (v, m, n), members in sorted(groups.items()):
        unseen = set(members); sizes = []
        while unseen:
            component, todo = set(), [min(unseen)]
            while todo:
                x = todo.pop()
                if x not in component:
                    component.add(x); todo.extend(undirected[x]-component)
            unseen -= component
            sizes.append(len(component))
        f = [f for f in forks if f['source'] in members]
        rows.append({'vertices': v, 'boundary': [m, n], 'components': dict(Counter(sizes)),
                     'placement_steps': sum(e['source'] in members for e in selected),
                     'forks': len(f), 'unjoined_forks': sum(x['join'] is None for x in f)})
    cycle_steps = [e['id'] for e in selected if e['source'] in reach[e['target']]]
    return {'rules': sorted(active_rules), 'placement_steps': len(selected),
            'summaries': rows, 'forks': forks,
            'fork_counts': dict(Counter((f['overlap'] + ('_unjoined' if f['join'] is None else '_joined')) for f in forks)),
            'steps_on_directed_cycles': cycle_steps}


def main():
    base = set().union(*(C.skeletons(n)[0] for n in (1, 2, 3)))
    gs = sorted(C.ordered_graphs(base)); ids = {g: i for i, g in enumerate(gs)}
    steps, excluded = [], []
    outward_rules = rules()
    inward_rules = [('collapse_left', outward_rules[2][2], outward_rules[2][1]),
                    ('collapse_right', outward_rules[3][2], outward_rules[3][1])]
    rr = outward_rules + inward_rules
    for name, lhs, rhs in rr:
        assert replace(lhs, lhs, rhs, (0, 1)) == rhs
        assert replace(rhs, rhs, lhs, (0, 1)) == lhs
    for i, g in enumerate(gs):
        for name, lhs, rhs in rr:
            for p in permutations(range(len(g[0])), 2):
                h = replace(g, lhs, rhs, p)
                if h is None:
                    continue
                if not C.connected_dag(len(h[0]), h[1]):
                    assert not convex_support(g, set(p))
                    excluded.append({'source': i, 'rule': name, 'embedding': p,
                                     'reason': 'nonconvex support; replacement leaves DAG sector'})
                    continue
                assert convex_support(g, set(p))
                C.validate(h)
                # Check the actual contextual replacement is invertible as a
                # syntax operation; this does not orient the reverse as a rule.
                assert replace(h, rhs, lhs, p) == g
                h = C.canonical(h, True)
                assert h in ids
                assert len(g[2]) == len(h[2]) and len(g[3]) == len(h[3])
                steps.append({'id': len(steps), 'source': i, 'target': ids[h], 'rule': name, 'embedding': p})
    # Every typed contextual rewrite must hold in a model of the experimental
    # laws. This catches boundary/slot mistakes beyond mere graph isomorphism.
    scaled = [[[2, 0], [0, 0]], [[0, 0], [0, 2]]]
    split = transpose_mu(scaled)
    values = [evaluate(g, scaled, split) for g in gs]
    assert all(values[e['source']] == values[e['target']] for e in steps)
    # Reversal preserves adjacency, though it may permute rule names/vertices.
    pairs = {(e['source'], e['target']) for e in steps}
    for a, b in pairs:
        assert (ids[C.canonical(C.reverse(gs[a]), True)],
                ids[C.canonical(C.reverse(gs[b]), True)]) in pairs
    original = summarize(gs, steps, {'alpha', 'reverse_alpha'})
    extended = summarize(gs, steps, {r[0] for r in outward_rules})
    inward = summarize(gs, steps, {'alpha', 'reverse_alpha', 'collapse_left', 'collapse_right'})
    for data in (original, extended, inward):
        pp = {(e['source'], e['target']) for e in steps if e['rule'] in data['rules']}
        for a, b in pp:
            assert (ids[C.canonical(C.reverse(gs[a]), True)],
                    ids[C.canonical(C.reverse(gs[b]), True)]) in pp
    outward_pairs = {tuple(sorted((e['source'], e['target']))) for e in steps if e['rule'] in extended['rules']}
    inward_pairs = {tuple(sorted((e['source'], e['target']))) for e in steps if e['rule'] in inward['rules']}
    assert outward_pairs == inward_pairs
    assert all(not d['steps_on_directed_cycles'] for d in (original, extended, inward))
    # The familiar pentagon fork is joinable using only directed rotations.
    pure_forks = [f for f in original['forks'] if gs[f['source']][0] == (0, 0, 0)]
    assert pure_forks and all(f['join'] is not None for f in pure_forks)
    # Two competing slides at K have distinct normal forms for this orientation.
    k_forks = [f for f in extended['forks'] if len(gs[f['source']][0]) == 2]
    assert k_forks and all(f['join'] is None for f in k_forks)
    report = {'schema': 'marici.nima.trivalent-contextual-overlaps.v1',
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependencies_sha256': {Path(C.__file__).name: hashlib.sha256(Path(C.__file__).read_bytes()).hexdigest(),
                                      'check_trivalent_mixed_candidate.py': hashlib.sha256(Path(__file__).with_name('check_trivalent_mixed_candidate.py').read_bytes()).hexdigest()},
              'status': 'experimental extra Frobenius rules; not admitted to base calculus',
              'conventions': 'Ordered-boundary connected DAGs, 1-3 vertices, slots distinguished, induced two-vertex matches; forward alpha and reversed-alpha; compare separate outward and inward orientations of Frobenius',
              'diagrams': [{'id': i, 'graph': g} for i, g in enumerate(gs)],
              'placement_steps': steps, 'excluded_non_DAG_or_disconnected_placements': excluded,
              'original': original, 'experimental_outward': extended, 'experimental_inward': inward,
              'checks_passed': True,
              'limitations': ['Forks are bounded representative contextual overlaps, not a complete polygraphic critical-pair classification.',
                              'No higher fillers or confluence completion are introduced.',
                              'Undirected connectivity and forward joinability are different tests.',
                              'No disjoint two-vertex supports can occur with at most three vertices.']}
    RESULT.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print('diagrams:', len(gs), 'placements:', len(steps), 'excluded:', len(excluded))
    for name, data in [('original', original), ('experimental_outward', extended), ('experimental_inward', inward)]:
        print(name, 'forks:', data['fork_counts'], 'cycle steps:', len(data['steps_on_directed_cycles']))
        for row in data['summaries']:
            if row['vertices'] >= 2:
                print(row)


if __name__ == '__main__':
    main()
