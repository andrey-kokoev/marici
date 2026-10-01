"""Retained loops from direct/staged gluing discrepancies.

Replays primitive paths and boundary transports. Tests their return
permutations, not higher-cell triviality or a fundamental-group presentation.
"""
from collections import Counter, defaultdict
from itertools import permutations, product
from pathlib import Path
import hashlib
import json
import check_reversible_trivalent_census as C
import check_trivalent_contextual_overlaps as O
import check_trivalent_modulo_boundary as N
import check_trivalent_residual_completion as R
import check_trivalent_retained_gluing as G
import check_trivalent_four_vertex_interchange as F
import check_trivalent_mixed_candidate as M

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'research/nima/results/trivalent-retained-gluing.json'
RESULT = ROOT / 'research/nima/results/trivalent-transport-loops.json'


def reduce_path(path):
    out = []
    for e, direction in path:
        if out and out[-1] == (e, -direction):
            out.pop()
        else:
            out.append((e, direction))
    return out


def compose_permutations(first, second):
    # reorder(reorder(labels, first), second)
    return tuple(first[i] for i in second)


def main():
    gluing = json.loads(SOURCE.read_text(encoding='utf-8'))
    assert gluing['checker_sha256'] == hashlib.sha256(Path(G.__file__).read_bytes()).hexdigest()
    norm_path = ROOT / 'research/nima/results/trivalent-modulo-boundary.json'
    assert gluing['normalization_report_sha256'] == hashlib.sha256(norm_path.read_bytes()).hexdigest()
    norm = json.loads(norm_path.read_text(encoding='utf-8'))
    assert norm['checker_sha256'] == hashlib.sha256(Path(N.__file__).read_bytes()).hexdigest()
    residual_path = ROOT / 'research/nima/results/trivalent-residual-completion.json'
    assert norm['source_report_sha256'] == hashlib.sha256(residual_path.read_bytes()).hexdigest()
    residual = json.loads(residual_path.read_text(encoding='utf-8'))
    assert residual['checker_sha256'] == hashlib.sha256(Path(R.__file__).read_bytes()).hexdigest()
    prior_path = ROOT / 'research/nima/results/trivalent-derived-completion.json'
    assert residual['source_report_sha256'] == hashlib.sha256(prior_path.read_bytes()).hexdigest()
    prior = json.loads(prior_path.read_text(encoding='utf-8'))
    import check_trivalent_derived_completion as D
    assert prior['checker_sha256'] == hashlib.sha256(Path(D.__file__).read_bytes()).hexdigest()
    for name, expected in prior['dependency_hashes'].items():
        assert hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() == expected
    gs = [R.tuple_tree(x['graph']) for x in norm['ordered_diagrams']]
    gid = {g: i for i, g in enumerate(gs)}
    qs = [R.tuple_tree(x['graph']) for x in norm['quotient_diagrams']]
    ledgers, steps = norm['normalization_ledgers'], residual['placement_steps']
    definitions = {n: (l, r) for n, l, r in O.rules()}
    definitions.update({'inverse_'+n: (r, l) for n, l, r in O.rules()})
    selected = set(residual['chosen_orientation'])
    edge_ids = defaultdict(list)
    for e in steps:
        if e['rule'] in selected:
            edge_ids[e['source'], e['target'], e['rule']].append(e['id'])
    traces = [F.normalize_trace(g, ledgers[i], steps, definitions, qs) for i, g in enumerate(gs)]
    paths = []
    for trace in traces:
        path = []
        for a, b, rule in zip(trace['states'], trace['states'][1:], trace['rules']):
            path.append(min(edge_ids[gid[a], gid[b], rule]))
        paths.append(path)

    def replay(start, program):
        at = start
        it = tuple(range(len(gs[at][2]))); ot = tuple(range(len(gs[at][3])))
        for item in program:
            assert item['source'] == at
            if item['kind'] == 'rewrite':
                at, _ = R.replay_signed(at, [{'step': item['step'], 'direction': item['direction']}],
                                        gs, steps, definitions)
            else:
                w = item['witness']
                g = N.transport(gs[at], w)
                at = gid[g]
                it = tuple(it[i] for i in w['inputs']); ot = tuple(ot[i] for i in w['outputs'])
            assert at == item['target']
        return at, it, ot

    def sym_event(a, b):
        return {'kind': 'symmetry', 'source': a, 'target': b,
                'witness': N.witness(gs[a], gs[b])}

    def invert_program(program):
        result = []
        for e in reversed(program):
            r = dict(e, source=e['target'], target=e['source'])
            if e['kind'] == 'rewrite':
                r['direction'] = -e['direction']
            else:
                r['witness'] = {k: N.inverse(v) for k, v in e['witness'].items()}
            result.append(r)
        return result

    loops = []
    for ci, case in enumerate(gluing['cases']):
        direct, staged = case['direct_gluing'], case['transported_gluing']
        td = gid[traces[direct]['states'][-1]]; ts = gid[traces[staged]['states'][-1]]
        if td == ts:
            continue
        # td -> original composite -> staged composite -> ts.
        path = ([(e, -1) for e in reversed(paths[direct])] +
                [(e, 1) for e in case['contextual_primitive_path']] +
                [(e, 1) for e in paths[staged]])
        reduced = reduce_path(path)
        assert R.replay_signed(td, [{'step': e, 'direction': d} for e, d in path], gs, steps, definitions)[0] == ts
        assert R.replay_signed(td, [{'step': e, 'direction': d} for e, d in reduced], gs, steps, definitions)[0] == ts
        base = min(td, ts)
        program = [sym_event(base, td)] if base != td else []
        at = td
        for eid, direction in reduced:
            e = steps[eid]
            target = e['target'] if direction == 1 else e['source']
            program.append({'kind': 'rewrite', 'source': at, 'target': target,
                            'step': eid, 'direction': direction})
            at = target
        program.append(sym_event(ts, td))
        if base != td:
            program.append(sym_event(td, base))
        end, ip, op = replay(base, program)
        assert end == base
        identities = (tuple(range(len(ip))), tuple(range(len(op))))
        assert (ip, op) != identities
        twice = replay(base, program + program)
        assert twice == (base, *identities)
        inverse_program = invert_program(program)
        assert replay(base, program + inverse_program) == (base, *identities)
        assert replay(base, inverse_program + program) == (base, *identities)
        loops.append({'id': len(loops), 'gluing_case': ci, 'left_operand': case['left'],
                      'right_operand': case['right'], 'matching': case['matching'],
                      'direct_terminal': td, 'staged_terminal': ts, 'base': base,
                      'unreduced_primitive_path': path, 'reduced_primitive_path': reduced,
                      'program': program, 'inverse_program': inverse_program,
                      'return_inputs': ip, 'return_outputs': op})
    assert len(loops) == gluing['different_final_ordered_normal_representatives']

    # Classify open primitive paths under simultaneous boundary action and path
    # inversion. No global reversal or higher-cell relation is silently used.
    def path_orbit(loop):
        alternatives = []
        for pi in permutations(range(len(gs[loop['direct_terminal']][2]))):
            for po in permutations(range(len(gs[loop['direct_terminal']][3]))):
                def act(g):
                    return C.canonical(R.reorder(g, pi, po), True)
                mapped = []
                for eid, direction in loop['reduced_primitive_path']:
                    e = steps[eid]
                    a, b = gid[act(gs[e['source']])], gid[act(gs[e['target']])]
                    raw_source = R.reorder(gs[e['source']], pi, po)
                    pv = next(p for p in permutations(range(len(raw_source[0])))
                              if C.relabel(raw_source, p, True) == gs[a])
                    emb = tuple(pv[v] for v in e['embedding'])
                    candidates = [x for x in edge_ids[a, b, e['rule']] if tuple(steps[x]['embedding']) == emb]
                    assert candidates
                    mapped.append((min(candidates), direction))
                a = gid[act(gs[loop['direct_terminal']])]; b = gid[act(gs[loop['staged_terminal']])]
                alternatives.extend([(a, b, tuple(mapped)), (b, a, tuple((e, -d) for e, d in reversed(mapped)))])
        return min(alternatives)
    classes = defaultdict(list)
    for loop in loops:
        classes[path_orbit(loop)].append(loop['id'])

    residual_classes = {path_orbit({'direct_terminal': f['left_terminal'],
                                   'staged_terminal': f['right_terminal'],
                                   'reduced_primitive_path': [(s['step'], s['direction']) for s in f['derived_left_to_right']]})
                        for f in residual['residual_forks']}
    assert residual_classes == set(classes)

    # In a noncommutative matrix Frobenius model the input-side terminal
    # realizes H(x,y)=trace(x*y) I. Test this formula, not just equality of
    # numerical orbit IDs. Primitive multiplication itself is not symmetric.
    mu = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for i, j, k in product(range(2), repeat=3):
        mu[2*i+k][2*i+j][2*j+k] = 1
    split = M.transpose_mu(mu)
    ev = lambda g: M.evaluate(g, mu, split)
    for _, lhs, rhs in O.rules():
        assert ev(lhs) == ev(rhs)
    semantic = []
    for base in sorted({x['base'] for x in loops}):
        sample = next(x for x in loops if x['base'] == base)
        original = ev(gs[base])
        swapped = ev(R.reorder(gs[base], sample['return_inputs'], sample['return_outputs']))
        assert original == swapped and any(any(row) for row in original)
        semantic.append({'base': base, 'matrix': original, 'boundary_swap_invariant': True})
    input_base = next(x['base'] for x in loops if len(x['return_inputs']) == 2)
    expected = [[int(row in (0, 3) and a == d and b == c)
                 for a, b, c, d in product(range(2), repeat=4)] for row in range(4)]
    assert ev(gs[input_base]) == expected

    # Test every compatible pair of based programs, keeping the actual paths.
    # Return permutations alone have exponent two; no loop contraction follows.
    pairs = []
    by_base = defaultdict(list)
    for loop in loops:
        by_base[loop['base']].append(loop)
    triple_checks = 0
    for base, family in by_base.items():
        for a, b in product(family, repeat=2):
            end, ip, op = replay(base, a['program'] + b['program'])
            assert end == base
            assert ip == compose_permutations(a['return_inputs'], b['return_inputs'])
            assert op == compose_permutations(a['return_outputs'], b['return_outputs'])
            assert ip == tuple(range(len(ip))) and op == tuple(range(len(op)))
            pairs.append({'first': a['id'], 'second': b['id'], 'base': base,
                          'inputs': ip, 'outputs': op})
        for a, b, c in product(family, repeat=3):
            for key in ('return_inputs', 'return_outputs'):
                assert compose_permutations(compose_permutations(a[key], b[key]), c[key]) == compose_permutations(a[key], compose_permutations(b[key], c[key]))
            triple_checks += 1
    report = {'schema': 'marici.nima.trivalent-transport-loops.v1',
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'gluing_report_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'helper_hashes': {Path(m.__file__).name: hashlib.sha256(Path(m.__file__).read_bytes()).hexdigest()
                                for m in (C, O, N, R, G, F, M)},
              'scope': '20 recorded direct/staged discrepancies; reversible experimental comparison paths, explicit external symmetry closures',
              'diagrams': norm['ordered_diagrams'], 'loops': loops,
              'path_orbits_under_boundary_action_and_inversion': list(classes.values()),
              'same_path_orbits_as_previous_residual_forks': True,
              'matrix_frobenius_control': {'terminals': semantic, 'input_side_formula': 'H(x,y)=trace(x*y) I in 2x2 integer matrices'},
              'compatible_pair_transports': pairs,
              'counts': {'loops': len(loops), 'based_families': {base: len(xs) for base, xs in by_base.items()},
                         'open_path_orbits': len(classes), 'pair_replays': len(pairs),
                         'triple_permutation_associativity_checks': triple_checks,
                         'primitive_lengths_before_cancellation': dict(Counter(len(x['unreduced_primitive_path']) for x in loops)),
                         'primitive_lengths_after_cancellation': dict(Counter(len(x['reduced_primitive_path']) for x in loops))},
              'checks_passed': True,
              'limitations': ['Diagram loops close only after an explicit symmetry; the decorated port state has a nonidentity return permutation.',
                              'Squaring gives identity boundary transport, NOT a proof that the retained comparison path is trivial.',
                              'Path orbits use boundary action and inversion only, not higher coherence or a global reversal quotient.',
                              'No fundamental-group, homotopy-order or seven-grade theorem is claimed.']}
    RESULT.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(report['counts'])
    print('path orbits:', list(classes.values()))
    print('return transports:', sorted({(tuple(x['return_inputs']), tuple(x['return_outputs'])) for x in loops}))


if __name__ == '__main__':
    main()
