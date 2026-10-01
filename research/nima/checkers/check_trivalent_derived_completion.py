"""Test derived slide shortcuts and orientation controls in the finite DAG sector.

Shortcuts use INVERSES of experimental Frobenius cells. They are derived in
that reversible/equational extension, not from the original trivalent syntax
or from the outward directed rewrite system alone.
"""
from collections import defaultdict
from itertools import permutations, product
from pathlib import Path
import hashlib
import json
import check_reversible_trivalent_census as C
import check_trivalent_contextual_overlaps as O
import check_trivalent_mixed_candidate as M
from check_trivalent_mixed_candidate import evaluate, transpose_mu

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / 'research/nima/results/trivalent-derived-completion.json'


def replay(g, expansion, definitions):
    for step in expansion:
        lhs, rhs = definitions[step['rule']]
        g = O.replace(g, lhs, rhs, tuple(step['embedding']))
        assert g is not None
        C.validate(g)
    return g


def main():
    base = set().union(*(C.skeletons(n)[0] for n in (1, 2, 3)))
    gs = sorted(C.ordered_graphs(base)); ids = {g: i for i, g in enumerate(gs)}
    basic = O.rules()
    inverse = [('inverse_' + n, rhs, lhs) for n, lhs, rhs in basic]
    k, fl, fr = basic[2][1], basic[2][2], basic[3][2]
    derived = [('slide_right_to_left', fr, fl), ('slide_left_to_right', fl, fr)]
    expansion_rules = {'slide_right_to_left': ['inverse_frobenius_right', 'frobenius_left'],
                       'slide_left_to_right': ['inverse_frobenius_left', 'frobenius_right']}
    rr = basic + inverse + derived
    definitions = {n: (lhs, rhs) for n, lhs, rhs in rr}
    steps, excluded = [], []
    for i, g in enumerate(gs):
        for name, lhs, rhs in rr:
            for p in permutations(range(len(g[0])), 2):
                h = O.replace(g, lhs, rhs, p)
                if h is None:
                    continue
                if not O.convex_support(g, set(p)) or not C.connected_dag(len(h[0]), h[1]):
                    excluded.append({'source': i, 'rule': name, 'embedding': p})
                    continue
                C.validate(h)
                assert O.replace(h, rhs, lhs, p) == g
                hc = C.canonical(h, True)
                assert hc in ids
                step = {'id': len(steps), 'source': i, 'target': ids[hc], 'rule': name, 'embedding': p}
                if name in expansion_rules:
                    expansion = [{'rule': n, 'embedding': p} for n in expansion_rules[name]]
                    assert replay(g, expansion, definitions) == h
                    middle = replay(g, expansion[:1], definitions)
                    assert C.canonical(middle, True) in ids
                    step['expansion'] = expansion
                    step['intermediate_graph'] = middle
                    # This guards against accepting a wrong-direction shortcut.
                    bad = [{'rule': 'frobenius_right' if name == 'slide_right_to_left' else 'frobenius_left',
                            'embedding': p}]
                    bl, br = definitions[bad[0]['rule']]
                    assert O.replace(g, bl, br, p) is None
                steps.append(step)
    scaled = [[[2, 0], [0, 0]], [[0, 0], [0, 2]]]
    split = transpose_mu(scaled)
    values = [evaluate(g, scaled, split) for g in gs]
    assert all(values[e['source']] == values[e['target']] for e in steps)

    names = [n for n, _, _ in basic]
    orientation_controls = []
    for bits in product((False, True), repeat=len(names)):
        chosen = {('inverse_' if b else '') + n for n, b in zip(names, bits)}
        s = O.summarize(gs, steps, chosen)
        orientation_controls.append({'rules': sorted(chosen),
                                     'fork_counts': s['fork_counts'],
                                     'unjoined_forks': sum(f['join'] is None for f in s['forks']),
                                     'steps_on_directed_cycles': len(s['steps_on_directed_cycles']),
                                     'placement_steps': s['placement_steps']})
    experiments = {}
    for title, chosen in [
            ('outward', set(names)),
            ('outward_plus_right_to_left', set(names) | {'slide_right_to_left'}),
            ('outward_plus_left_to_right', set(names) | {'slide_left_to_right'}),
            ('outward_plus_both_shortcuts', set(names) | {n for n, _, _ in derived})]:
        experiments[title] = O.summarize(gs, steps, chosen)
    # Both shortcuts must expose a loop, rather than treating joinability as
    # sufficient for a terminating normalization procedure.
    assert experiments['outward_plus_both_shortcuts']['steps_on_directed_cycles']
    for title in ('outward_plus_right_to_left', 'outward_plus_left_to_right'):
        e = experiments[title]
        two_vertex = [f for f in e['forks'] if len(gs[f['source']][0]) == 2]
        assert two_vertex and all(f['join'] is not None for f in two_vertex)
    acyclic = [r for r in orientation_controls if not r['steps_on_directed_cycles']]
    best_unjoined = min(r['unjoined_forks'] for r in acyclic)
    best_controls = [O.summarize(gs, steps, set(r['rules'])) for r in acyclic
                     if r['unjoined_forks'] == best_unjoined]
    for e in best_controls:
        e['unjoined_source_boundaries'] = [[len(gs[f['source']][2]), len(gs[f['source']][3])]
                                           for f in e['forks'] if f['join'] is None]
    for e in experiments.values():
        chosen_steps = [s for s in steps if s['rule'] in e['rules']]
        outgoing = defaultdict(list)
        for s in chosen_steps:
            outgoing[s['source']].append((s['id'], s['target']))
        if e['steps_on_directed_cycles']:
            first = steps[e['steps_on_directed_cycles'][0]]
            back = O.reachable(first['target'], outgoing)[first['source']]
            e['example_directed_cycle'] = [first['id']] + back
        else:
            e['example_directed_cycle'] = None
    # All equational edges remain those already generated by reversible basic
    # cells: every derived edge has its two-step, same-boundary witness above.
    report = {
        'schema': 'marici.nima.trivalent-derived-completion.v1',
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependency_hashes': {Path(m.__file__).name: hashlib.sha256(Path(m.__file__).read_bytes()).hexdigest()
                              for m in (C, O, M)},
        'scope': 'Ordered-boundary connected DAGs with 1-3 vertices, fixed local slots, convex induced two-vertex replacements',
        'assumptions': ['Associativity and reversed associativity comparisons are experimental rewrite inputs.',
                        'Frobenius comparisons are treated as reversible for deriving the shortcuts.',
                        'No higher fillers or global convergence theorem are introduced.'],
        'derived_rules': {n: {'lhs': lhs, 'rhs': rhs, 'expansion_rules': expansion_rules[n]}
                          for n, lhs, rhs in derived},
        'diagrams': [{'id': i, 'graph': g} for i, g in enumerate(gs)],
        'placement_steps': steps, 'excluded_placements': excluded,
        'orientation_controls': orientation_controls, 'best_acyclic_controls': best_controls,
        'experiments': experiments,
        'checks_passed': True,
        'limitations': ['Finite closed-sector tests; rule placements are counted, not symmetry-quotiented critical types.',
                        'Joinability and termination are separate properties.',
                        'Reversibility of candidate cells is additional to orientation reversal of vertices.']}
    RESULT.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print('diagrams:', len(gs), 'rule placements:', len(steps), 'excluded:', len(excluded))
    print('orientation controls:', len(orientation_controls))
    for row in orientation_controls:
        print(row)
    for title, e in experiments.items():
        print(title, 'forks:', e['fork_counts'], 'cycle steps:', len(e['steps_on_directed_cycles']))


if __name__ == '__main__':
    main()
