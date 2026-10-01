"""Selected four-vertex overlapping contexts around the residual three-vertex forks.

Saturate explicit one-vertex extensions under the chosen elementary directions
and previously derived residual macros. No new generator or higher filler.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations
from pathlib import Path
import hashlib
import json
import check_reversible_trivalent_census as C
import check_trivalent_contextual_overlaps as O
import check_trivalent_residual_completion as R
import check_trivalent_retained_gluing as G
import check_trivalent_modulo_boundary as N
import check_trivalent_mixed_candidate as M

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'research/nima/results/trivalent-residual-completion.json'
RESULT = ROOT / 'research/nima/results/trivalent-four-vertex-overlaps.json'
canon = lru_cache(None)(lambda g: C.canonical(g, True))


def main():
    source = json.loads(SOURCE.read_text(encoding='utf-8'))
    assert source['checker_sha256'] == hashlib.sha256(Path(R.__file__).read_bytes()).hexdigest()
    prior_path = ROOT / 'research/nima/results/trivalent-derived-completion.json'
    assert source['source_report_sha256'] == hashlib.sha256(prior_path.read_bytes()).hexdigest()
    prior = json.loads(prior_path.read_text(encoding='utf-8'))
    import check_trivalent_derived_completion as D
    assert prior['checker_sha256'] == hashlib.sha256(Path(D.__file__).read_bytes()).hexdigest()
    for name, expected in prior['dependency_hashes'].items():
        assert hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() == expected
    small = [R.tuple_tree(x['graph']) for x in source['diagrams']]
    definitions = {n: (l, r) for n, l, r in O.rules()}
    definitions.update({'inverse_'+n: (r, l) for n, l, r in O.rules()})
    base_rules = [(n, *definitions[n]) for n in source['chosen_orientation']]
    # One displayed direction per family suffices: slot-preserving contextual
    # placements already include the boundary-swapped opposite direction.
    macros = [m for m in source['derived_macro_schemas'] if m['name'].endswith('_0')]
    macro_defs = {m['name']: (R.tuple_tree(m['lhs']), R.tuple_tree(m['rhs'])) for m in macros}
    macro_meta = {m['name']: m for m in macros}
    all_rules = base_rules + [(n, *lr) for n, lr in macro_defs.items()]
    primitives = sorted(C.ordered_graphs(C.skeletons(1)[0]))
    seed_sources = sorted({f['source'] for f in source['residual_forks']})
    seeds = set(); seed_provenance = defaultdict(list)
    for sid in seed_sources:
        for prim in primitives:
            for side in ('before', 'after'):
                a, b = (prim, small[sid]) if side == 'before' else (small[sid], prim)
                for matching in G.matchings(a, b):
                    g = G.glue(a, b, matching)
                    C.validate(g)
                    for pi in permutations(range(len(g[2]))):
                        for po in permutations(range(len(g[3]))):
                            h = canon(R.reorder(g, pi, po))
                            seeds.add(h)
                            seed_provenance[h].append({'residual_source': sid, 'primitive': prim,
                                                       'side': side, 'matching': matching,
                                                       'boundary_inputs': pi, 'boundary_outputs': po})
    graphs, ids, todo = [], {}, deque()
    def intern(g):
        g = canon(g)
        if g not in ids:
            ids[g] = len(graphs); graphs.append(g); todo.append(ids[g])
        return ids[g]
    for g in sorted(seeds):
        intern(g)
    seed_ids = sorted(ids[g] for g in seeds)
    steps, excluded = [], Counter()
    macro_checks = 0
    while todo:
        sid = todo.popleft(); g = graphs[sid]
        for name, lhs, rhs in all_rules:
            for p in permutations(range(4), len(lhs[0])):
                h = O.replace(g, lhs, rhs, p)
                if h is None:
                    continue
                if not O.convex_support(g, set(p)):
                    excluded[name] += 1
                    continue
                C.validate(h)
                assert O.replace(h, rhs, lhs, p) == g
                hid = intern(h)
                entry = {'id': len(steps), 'source': sid, 'target': hid, 'rule': name, 'embedding': p}
                if name in macro_meta:
                    # Replay the entire previously derived primitive path in
                    # this four-vertex context; do not accept macros on endpoints alone.
                    current = g; expansion = []
                    for t in macro_meta[name]['derivation']['signed_path']:
                        pe = source['placement_steps'][t['step']]
                        next_small = pe['target'] if t['direction'] == 1 else pe['source']
                        target = canon(O.replace(g, lhs, small[next_small], p))
                        pl, pr = definitions[pe['rule']]
                        if t['direction'] == -1:
                            pl, pr = pr, pl
                        match = None
                        for q in permutations(range(4), 2):
                            rr = O.replace(current, pl, pr, q)
                            if rr is not None and O.convex_support(current, set(q)) and canon(rr) == target:
                                C.validate(rr); match = q; break
                        assert match is not None, 'derived path failed in context'
                        expansion.append({'rule': pe['rule'], 'direction': t['direction'],
                                          'embedding': match, 'target_graph': target})
                        current = target
                    assert current == graphs[hid]
                    entry['primitive_expansion'] = expansion
                    macro_checks += 1
                steps.append(entry)
    base_names = set(source['chosen_orientation'])
    base_out, full_out, by_source = defaultdict(list), defaultdict(list), defaultdict(list)
    for e in steps:
        full_out[e['source']].append((e['id'], e['target']))
        if e['rule'] in base_names:
            base_out[e['source']].append((e['id'], e['target']))
            by_source[e['source']].append(e)
    @lru_cache(None)
    def reach(i):
        return O.reachable(i, base_out)
    @lru_cache(None)
    def full_reach(i):
        return O.reachable(i, full_out)
    forks = []
    for sid, es in sorted(by_source.items()):
        for a, b in combinations(es, 2):
            sa, sb = set(a['embedding']), set(b['embedding'])
            overlap = 'same_support' if sa == sb else 'shared_vertex' if sa & sb else 'disjoint'
            common = set(reach(a['target'])) & set(reach(b['target']))
            join = min(common) if common else None
            augmented = None
            if join is None:
                cc = set(full_reach(a['target'])) & set(full_reach(b['target']))
                augmented = min(cc) if cc else None
            forks.append({'source': sid, 'steps': [a['id'], b['id']], 'overlap': overlap,
                          'union_convex': O.convex_support(graphs[sid], sa | sb),
                          'base_join': join, 'base_left_path': reach(a['target'])[join] if join is not None else None,
                          'base_right_path': reach(b['target'])[join] if join is not None else None,
                          'macro_join': augmented,
                          'macro_left_path': full_reach(a['target'])[augmented] if augmented is not None else None,
                          'macro_right_path': full_reach(b['target'])[augmented] if augmented is not None else None,
                          'left_normal_forms': sorted(i for i in reach(a['target']) if not base_out[i]),
                          'right_normal_forms': sorted(i for i in reach(b['target']) if not base_out[i])})
    base_cycle_edges = [e['id'] for e in steps if e['rule'] in base_names and e['source'] in reach(e['target'])]
    unresolved = [f for f in forks if f['base_join'] is None and f['macro_join'] is None]
    # Ensure the selected saturated universe is also closed under the full
    # boundary action used by the quotient test.
    for g in graphs:
        for pi in permutations(range(len(g[2]))):
            for po in permutations(range(len(g[3]))):
                assert canon(R.reorder(g, pi, po)) in ids
    qgraphs = sorted({C.canonical(g, False) for g in graphs})
    qids = {g: i for i, g in enumerate(qgraphs)}
    quotient = [qids[C.canonical(g, False)] for g in graphs]
    qout = defaultdict(list)
    for e in steps:
        qout[quotient[e['source']]].append((e['id'], quotient[e['target']]))
    @lru_cache(None)
    def qreach(i):
        return O.reachable(i, qout)
    terminal_classes = defaultdict(list)
    for index, f in enumerate(unresolved):
        assert len(f['left_normal_forms']) == len(f['right_normal_forms']) == 1
        a, b = f['left_normal_forms'][0], f['right_normal_forms'][0]
        f['normalization_left_path'] = reach(steps[f['steps'][0]]['target'])[a]
        f['normalization_right_path'] = reach(steps[f['steps'][1]]['target'])[b]
        f['terminal_boundary_orbit_equal'] = quotient[a] == quotient[b]
        f['terminal_boundary_transport'] = N.witness(graphs[a], graphs[b]) if quotient[a] == quotient[b] else None
        common = set(qreach(quotient[a])) & set(qreach(quotient[b]))
        f['join_after_boundary_quotient_and_old_macros'] = min(common) if common else None
        def attachment(g):
            return {'inputs': sorted(g[0][v] for v, _ in g[2]),
                    'outputs': sorted(g[0][v] for v, _ in g[3])}
        f['terminal_attachment_signatures'] = [attachment(graphs[a]), attachment(graphs[b])]
        if quotient[a] != quotient[b]:
            assert f['terminal_attachment_signatures'][0] != f['terminal_attachment_signatures'][1]
        terminal_classes[R.orbit_key([graphs[f['source']], graphs[a], graphs[b]], True)].append(index)
    # The genuinely different boundary-orbit terminals still agree in a
    # noncommutative Frobenius model. They are a normalization obstruction,
    # not a countermodel to the experimental equations.
    mu = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    from itertools import product
    for i, j, k in product(range(2), repeat=3):
        mu[2*i+k][2*i+j][2*j+k] = 1
    split = M.transpose_mu(mu)
    for _, lhs, rhs in O.rules():
        assert M.evaluate(lhs, mu, split) == M.evaluate(rhs, mu, split)
    @lru_cache(None)
    def model(i):
        return M.evaluate(graphs[i], mu, split)
    for f in unresolved:
        if not f['terminal_boundary_orbit_equal']:
            assert model(f['left_normal_forms'][0]) == model(f['right_normal_forms'][0])
            assert any(any(row) for row in model(f['left_normal_forms'][0]))
            f['matrix_frobenius_terminals_agree'] = True
    assert all(not f['union_convex'] for f in unresolved)
    # A disjoint-support fork must commute; check rather than silently assuming it.
    assert all(f['base_join'] is not None for f in forks if f['overlap'] == 'disjoint')
    summary = Counter()
    for f in forks:
        outcome = 'base_joined' if f['base_join'] is not None else 'old_macro_joined' if f['macro_join'] is not None else 'unresolved'
        summary[f['overlap']+'_'+outcome] += 1
    histogram = Counter((len(g[2]), len(g[3]), len(g[1])-3) for g in graphs)
    report = {'schema': 'marici.nima.trivalent-four-vertex-overlaps.v1',
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'source_report_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'helper_hashes': {Path(m.__file__).name: hashlib.sha256(Path(m.__file__).read_bytes()).hexdigest() for m in (C, O, R, G, N, M)},
              'scope': 'One-vertex one-way gluing extensions of the four residual fork sources, closed under all external boundary orders and saturated by selected basic rules plus old residual macros; not the full four-vertex census',
              'selected_rules': source['chosen_orientation'],
              'macro_schemas': macros,
              'seed_ids': seed_ids,
              'seeds': [{'id': ids[g], 'provenance': seed_provenance[g]} for g in sorted(seeds)],
              'diagrams': [{'id': i, 'graph': g} for i, g in enumerate(graphs)],
              'steps': steps, 'forks': forks,
              'base_steps_on_directed_cycles': base_cycle_edges,
              'excluded_nonconvex_matches': dict(excluded),
              'counts': {'seed_diagrams': len(seeds), 'saturated_diagrams': len(graphs),
                         'basic_placements': sum(e['rule'] in base_names for e in steps),
                         'old_macro_placements': macro_checks, 'forks': len(forks),
                         'unresolved_after_old_macros': len(unresolved),
                         'terminal_pairs_related_by_boundary_permutation': sum(f['terminal_boundary_orbit_equal'] for f in unresolved),
                         'unjoined_even_modulo_boundary_and_old_macros': sum(f['join_after_boundary_quotient_and_old_macros'] is None for f in unresolved)},
              'unresolved_fork_orbits_under_boundary_and_reversal': list(terminal_classes.values()),
              'unresolved_fork_indexing': [{'source': f['source'], 'steps': f['steps']} for f in unresolved],
              'boundary_quotient_diagrams': qgraphs,
              'fork_summary': dict(summary),
              'boundary_cycle_rank_histogram': [{'boundary': [m,n], 'cycle_rank': r, 'diagrams': count} for (m,n,r),count in sorted(histogram.items())],
              'checks_passed': True,
              'limitations': ['Old macros are derived in the reversible experimental extension; no new generators or fillers are supplied.',
                              'Macro-assisted reachability need not terminate; it is not a normal-form claim.',
                              'Unresolved means unjoined under this chosen elementary orientation plus the two old macro schemas, not a proof of independence.',
                              'Saturation is finite in this selected boundary/incidence sector, not a global-arities theorem.']}
    RESULT.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(report['counts']); print(dict(summary))
    print('base cycle edges:', len(base_cycle_edges), 'nonconvex exclusions:', dict(excluded))
    print('boundaries:', report['boundary_cycle_rank_histogram'])
    print('unresolved examples:', unresolved[:1])


if __name__ == '__main__':
    main()
