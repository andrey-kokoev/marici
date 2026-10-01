"""Four-vertex selected-sector test: two nontrivially normalized operands.

Checks all one-way nonempty injective gluings of two-vertex operands whose
saved normalization paths contain primitive steps. No global four-vertex
normal form or higher filler is claimed.
"""
from collections import Counter
from functools import lru_cache
from itertools import permutations
from pathlib import Path
import hashlib
import json
import check_reversible_trivalent_census as C
import check_trivalent_contextual_overlaps as O
import check_trivalent_modulo_boundary as N
import check_trivalent_residual_completion as R
import check_trivalent_retained_gluing as G
import check_trivalent_mixed_candidate as M

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'research/nima/results/trivalent-modulo-boundary.json'
RESULT = ROOT / 'research/nima/results/trivalent-four-vertex-interchange.json'


def normalize_trace(g, ledger, steps, definitions, qs):
    current = g
    ins, outs = tuple(range(len(g[2]))), tuple(range(len(g[3])))
    states, rules = [g], []
    for item in ledger['steps']:
        e = steps[item['placement']]; w = item['source_symmetry']
        current = N.transport(current, w)
        ins = tuple(ins[j] for j in w['inputs']); outs = tuple(outs[j] for j in w['outputs'])
        lhs, rhs = definitions[e['rule']]
        current = O.replace(current, lhs, rhs, tuple(e['embedding']))
        assert current is not None
        current = C.relabel(current, tuple(item['target_canonicalization']), True)
        states.append(C.canonical(G.restore_order(current, ins, outs), True))
        rules.append(e['rule'])
    w = ledger['final_symmetry']
    current = N.transport(current, w)
    ins = tuple(ins[j] for j in w['inputs']); outs = tuple(outs[j] for j in w['outputs'])
    assert current == qs[ledger['normal_orbit']]
    assert C.canonical(G.restore_order(current, ins, outs), True) == states[-1]
    return {'states': states, 'rules': rules, 'normal': current, 'inputs': ins, 'outputs': outs}


def apply_witness(g, w, definitions):
    lhs, rhs = definitions[w['rule']]
    h = O.replace(g, lhs, rhs, tuple(w['embedding']))
    assert h is not None
    return C.relabel(h, tuple(w['renaming']), True)


def undo_witness(g, w, definitions):
    lhs, rhs = definitions[w['rule']]
    raw = C.relabel(g, N.inverse(w['renaming']), True)
    result = O.replace(raw, rhs, lhs, tuple(w['embedding']))
    assert result is not None
    return result


def lift_witness(g, target, rule, support, definitions):
    lhs, rhs = definitions[rule]
    assert O.convex_support(g, set(support))
    for p in permutations(support):
        raw = O.replace(g, lhs, rhs, p)
        if raw is None:
            continue
        for q in permutations(support):
            renaming = list(range(len(g[0])))
            for a, b in zip(support, q):
                renaming[a] = b
            if C.relabel(raw, tuple(renaming), True) == target:
                w = {'rule': rule, 'embedding': p, 'renaming': tuple(renaming)}
                assert apply_witness(g, w, definitions) == target
                assert undo_witness(target, w, definitions) == g
                return w
    raise AssertionError('primitive step did not lift through the declared gluing')


def main():
    data = json.loads(SOURCE.read_text(encoding='utf-8'))
    assert data['checker_sha256'] == hashlib.sha256(Path(N.__file__).read_bytes()).hexdigest()
    residual_path = ROOT / 'research/nima/results/trivalent-residual-completion.json'
    assert data['source_report_sha256'] == hashlib.sha256(residual_path.read_bytes()).hexdigest()
    residual = json.loads(residual_path.read_text(encoding='utf-8'))
    assert residual['checker_sha256'] == hashlib.sha256(Path(R.__file__).read_bytes()).hexdigest()
    derived_path = ROOT / 'research/nima/results/trivalent-derived-completion.json'
    assert residual['source_report_sha256'] == hashlib.sha256(derived_path.read_bytes()).hexdigest()
    derived = json.loads(derived_path.read_text(encoding='utf-8'))
    import check_trivalent_derived_completion as D
    assert derived['checker_sha256'] == hashlib.sha256(Path(D.__file__).read_bytes()).hexdigest()
    for name, expected in derived['dependency_hashes'].items():
        assert hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() == expected
    gs = [R.tuple_tree(x['graph']) for x in data['ordered_diagrams']]
    qs = [R.tuple_tree(x['graph']) for x in data['quotient_diagrams']]
    steps, ledgers = residual['placement_steps'], data['normalization_ledgers']
    definitions = {n: (l, r) for n, l, r in O.rules()}
    definitions.update({'inverse_'+n: (r, l) for n, l, r in O.rules()})
    traces = {i: normalize_trace(g, ledgers[i], steps, definitions, qs)
              for i, g in enumerate(gs) if len(g[0]) == 2 and ledgers[i]['steps']}
    mu = [[[1, 1], [0, 0]], [[0, 0], [1, 1]]]
    split = M.transpose_mu(mu)
    for _, lhs, rhs in O.rules():
        assert M.evaluate(lhs, mu, split) == M.evaluate(rhs, mu, split)

    @lru_cache(None)
    def value(g):
        return M.evaluate(C.canonical(g, True), mu, split)

    # Intern labelled four-vertex graphs. Blocks 0,1 and 2,3 remain distinguishable
    # here, so interchange is tested before quotienting by vertex isomorphism.
    graphs, graph_ids = [], {}
    def intern(g):
        if g not in graph_ids:
            graph_ids[g] = len(graphs); graphs.append(g)
        return graph_ids[g]

    cases = []; counts = Counter(); comparisons = 0; negative_examples = []
    for ai, a in traces.items():
        for bi, b in traces.items():
            for matching in G.matchings(gs[ai], gs[bi]):
                na, nb = len(a['rules']), len(b['rules'])
                grid = [[G.glue(x, y, matching) for y in b['states']] for x in a['states']]
                for row in grid:
                    for g in row:
                        C.validate(g)
                horizontal, vertical = {}, {}
                for i in range(na):
                    for j in range(nb+1):
                        horizontal[i, j] = lift_witness(grid[i][j], grid[i+1][j], a['rules'][i], (0, 1), definitions)
                for i in range(na+1):
                    for j in range(nb):
                        vertical[i, j] = lift_witness(grid[i][j], grid[i][j+1], b['rules'][j], (2, 3), definitions)
                for i in range(na):
                    for j in range(nb):
                        h, v = horizontal[i, j], vertical[i, j]
                        assert set(h['embedding']).isdisjoint(v['embedding'])
                        # Reuse exactly the same placements/renamings on either
                        # route, not separate witnesses chosen after the first step.
                        hv = apply_witness(apply_witness(grid[i][j], h, definitions), v, definitions)
                        vh = apply_witness(apply_witness(grid[i][j], v, definitions), h, definitions)
                        assert hv == vh == grid[i+1][j+1]
                        comparisons += 1
                # Recover the original labelled composite along BOTH routes.
                left_then_right = [horizontal[i, 0] for i in range(na)] + [vertical[na, j] for j in range(nb)]
                right_then_left = [vertical[0, j] for j in range(nb)] + [horizontal[i, nb] for i in range(na)]
                for route in (left_then_right, right_then_left):
                    x = grid[0][0]
                    for w in route:
                        x = apply_witness(x, w, definitions)
                    assert x == grid[-1][-1]
                    for w in reversed(route):
                        x = undo_witness(x, w, definitions)
                    assert x == grid[0][0]
                assert value(grid[0][0]) == value(grid[-1][-1])
                # Also perform gluing directly on raw quotient representatives
                # using transported joining indices and restored external order.
                moved = tuple((a['outputs'].index(o), b['inputs'].index(i)) for o, i in matching)
                raw = G.glue(a['normal'], b['normal'], moved)
                used_o, used_i = {o for o, _ in matching}, {i for _, i in matching}
                actual_i = [('A', i) for i in a['inputs']] + [('B', i) for i in b['inputs'] if i not in used_i]
                actual_o = [('A', o) for o in a['outputs'] if o not in used_o] + [('B', o) for o in b['outputs']]
                want_i = [('A', i) for i in range(len(gs[ai][2]))] + [('B', i) for i in range(len(gs[bi][2])) if i not in used_i]
                want_o = [('A', o) for o in range(len(gs[ai][3])) if o not in used_o] + [('B', o) for o in range(len(gs[bi][3]))]
                pi = tuple(actual_i.index(t) for t in want_i); po = tuple(actual_o.index(t) for t in want_o)
                assert C.canonical(R.reorder(raw, pi, po), True) == C.canonical(grid[-1][-1], True)
                naive = G.glue(a['normal'], b['normal'], matching)
                bad = value(naive) != value(grid[0][0])
                counts['naive_semantic_failures'] += bad
                counts[f'wires_{len(matching)}'] += 1
                if bad and len(negative_examples) < 3:
                    negative_examples.append({'left': ai, 'right': bi, 'matching': matching,
                                              'direct_graph': intern(grid[0][0]), 'naive_graph': intern(naive),
                                              'difference': M.first_difference(value(grid[0][0]), value(naive))})
                cases.append({'left': ai, 'right': bi, 'matching': matching, 'transported_matching': moved,
                              'external_inputs': pi, 'external_outputs': po,
                              'grid': [[intern(g) for g in row] for row in grid],
                              'horizontal': [{'at': key, 'witness': w} for key, w in sorted(horizontal.items())],
                              'vertical': [{'at': key, 'witness': w} for key, w in sorted(vertical.items())]})
    assert negative_examples
    report = {'schema': 'marici.nima.trivalent-four-vertex-interchange.v1',
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'source_report_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'helper_hashes': {Path(m.__file__).name: hashlib.sha256(Path(m.__file__).read_bytes()).hexdigest() for m in (C, O, R, N, G, M)},
              'scope': 'All nonempty injective one-way matchings between two-vertex operands with nonempty saved normalization paths; exactly four total vertices',
              'operand_traces': {i: t for i, t in traces.items()},
              'labelled_graphs': graphs, 'cases': cases,
              'counts': dict(counts, operands=len(traces), gluing_cases=len(cases),
                             elementary_interchange_squares=comparisons, exact_two_route_round_trips=2*len(cases)),
              'negative_examples': negative_examples, 'checks_passed': True,
              'limitations': ['Selected four-vertex sector, not an exhaustive four-vertex rewrite census.',
                              'No composite four-vertex normal form, termination or confluence claim.',
                              'Equality of final port graphs for disjoint rewrites is not a supplied higher cell between paths.',
                              'No overlapping-support, feedback or arbitrary-arity coherence theorem.']}
    RESULT.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(report['counts'])
    print('interned labelled graphs:', len(graphs))
    print('negative example:', negative_examples[0])


if __name__ == '__main__':
    main()
