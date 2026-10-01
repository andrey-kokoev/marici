"""Exhaustive bounded gluing of retained boundary-modulo normalizations.

Glue nonempty matchings from left outputs to right inputs, with total vertices
at most three. Retain original external order and contextual rewrite paths.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from pathlib import Path
import hashlib
import json
import check_reversible_trivalent_census as C
import check_trivalent_contextual_overlaps as O
import check_trivalent_residual_completion as R
import check_trivalent_modulo_boundary as N
import check_trivalent_mixed_candidate as M

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'research/nima/results/trivalent-modulo-boundary.json'
RESULT = ROOT / 'research/nima/results/trivalent-retained-gluing.json'


def glue(a, b, matching):
    """Boundary indices: remaining inputs A then B; remaining outputs A then B."""
    if not matching:
        raise ValueError('nonempty connection required')
    oo, ii = zip(*matching)
    if len(set(oo)) != len(oo) or len(set(ii)) != len(ii):
        raise ValueError('port used twice')
    if any(not 0 <= x < len(a[3]) for x in oo) or any(not 0 <= x < len(b[2]) for x in ii):
        raise ValueError('port index out of range')
    offset = len(a[0])
    shift = lambda p: (p[0]+offset, p[1])
    es = list(a[1]) + [(x+offset, s, y+offset, t) for x, s, y, t in b[1]]
    for out, inp in matching:
        x, s = a[3][out]; y, t = shift(b[2][inp])
        es.append((x, s, y, t))
    return (a[0]+b[0], tuple(sorted(es)),
            a[2]+tuple(shift(p) for j, p in enumerate(b[2]) if j not in ii),
            tuple(p for j, p in enumerate(a[3]) if j not in oo)+tuple(shift(p) for p in b[3]))


def matchings(a, b):
    for k in range(1, min(len(a[3]), len(b[2]))+1):
        for os in combinations(range(len(a[3])), k):
            for ins in combinations(range(len(b[2])), k):
                for js in permutations(ins):
                    yield tuple(zip(os, js))


def restore_order(g, ins, outs):
    # ins[j] identifies the original boundary input carried by current slot j.
    return R.reorder(g, N.inverse(ins), N.inverse(outs))


def main():
    data = json.loads(SOURCE.read_text(encoding='utf-8'))
    assert data['checker_sha256'] == hashlib.sha256(Path(N.__file__).read_bytes()).hexdigest()
    residual_path = ROOT / 'research/nima/results/trivalent-residual-completion.json'
    assert data['source_report_sha256'] == hashlib.sha256(residual_path.read_bytes()).hexdigest()
    residual = json.loads(residual_path.read_text(encoding='utf-8'))
    assert residual['checker_sha256'] == hashlib.sha256(Path(R.__file__).read_bytes()).hexdigest()
    prior_path = ROOT / 'research/nima/results/trivalent-derived-completion.json'
    assert residual['source_report_sha256'] == hashlib.sha256(prior_path.read_bytes()).hexdigest()
    prior = json.loads(prior_path.read_text(encoding='utf-8'))
    import check_trivalent_derived_completion as D
    assert prior['checker_sha256'] == hashlib.sha256(Path(D.__file__).read_bytes()).hexdigest()
    for name, expected in prior['dependency_hashes'].items():
        assert hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() == expected
    gs = [R.tuple_tree(x['graph']) for x in data['ordered_diagrams']]
    gid = {g: i for i, g in enumerate(gs)}
    qs = [R.tuple_tree(x['graph']) for x in data['quotient_diagrams']]
    ledgers = data['normalization_ledgers']
    steps = residual['placement_steps']
    selected = set(residual['chosen_orientation'])
    definitions = {n: (l, r) for n, l, r in O.rules()}
    definitions.update({'inverse_'+n: (r, l) for n, l, r in O.rules()})
    edge_ids = defaultdict(list)
    for e in steps:
        if e['rule'] in selected:
            edge_ids[e['source'], e['target'], e['rule']].append(e['id'])

    def operand(i):
        current = gs[i]; tags_i = tuple(range(len(current[2]))); tags_o = tuple(range(len(current[3])))
        route = []
        for item in ledgers[i]['steps']:
            w = item['source_symmetry']; e = steps[item['placement']]
            current = N.transport(current, w)
            tags_i = tuple(tags_i[j] for j in w['inputs'])
            tags_o = tuple(tags_o[j] for j in w['outputs'])
            lhs, rhs = definitions[e['rule']]
            current = O.replace(current, lhs, rhs, tuple(e['embedding']))
            current = C.relabel(current, tuple(item['target_canonicalization']), True)
            route.append((C.canonical(restore_order(current, tags_i, tags_o), True), e['rule']))
        w = ledgers[i]['final_symmetry']
        current = N.transport(current, w)
        tags_i = tuple(tags_i[j] for j in w['inputs'])
        tags_o = tuple(tags_o[j] for j in w['outputs'])
        assert current == qs[ledgers[i]['normal_orbit']]
        restored = C.canonical(restore_order(current, tags_i, tags_o), True)
        assert restored == (route[-1][0] if route else gs[i])
        return {'normal': current, 'input_tags': tags_i, 'output_tags': tags_o,
                'restored': restored, 'route': route}

    operands = [operand(i) for i in range(len(gs))]

    def recover_normalized(i):
        ledger = ledgers[i]
        current = N.untransport(qs[ledger['normal_orbit']], ledger['final_symmetry'])
        for item in reversed(ledger['steps']):
            e = steps[item['placement']]
            lhs, rhs = definitions[e['rule']]
            raw = C.relabel(current, N.inverse(item['target_canonicalization']), True)
            before = O.replace(raw, rhs, lhs, tuple(e['embedding']))
            assert before is not None
            current = N.untransport(before, item['source_symmetry'])
        return current

    recovered = [recover_normalized(i) for i in range(len(gs))]
    assert recovered == gs
    # Noncommutative left-zero semigroup algebra, with transpose split.
    # e_i * e_j = e_i. All four experimental equations are checked below.
    mu = [[[1, 1], [0, 0]], [[0, 0], [1, 1]]]
    split = M.transpose_mu(mu)
    for _, lhs, rhs in O.rules():
        assert M.evaluate(lhs, mu, split) == M.evaluate(rhs, mu, split)
    matrices = [M.evaluate(g, mu, split) for g in gs]
    cases = []; counts = Counter(); naive_examples = []; different_final_representatives = 0
    final_representative_examples = []
    final_pair_counts = Counter()
    for ai, a in enumerate(gs):
        for bi, b in enumerate(gs):
            if len(a[0])+len(b[0]) > 3:
                continue
            aa, bb = operands[ai], operands[bi]
            for matching in matchings(a, b):
                direct = C.canonical(glue(a, b, matching), True); C.validate(direct)
                di = gid[direct]
                transported = tuple((aa['output_tags'].index(o), bb['input_tags'].index(i)) for o, i in matching)
                raw = glue(aa['normal'], bb['normal'], transported)
                used_o, used_i = {o for o, _ in matching}, {i for _, i in matching}
                actual_i = [('A', i) for i in aa['input_tags']] + [('B', i) for i in bb['input_tags'] if i not in used_i]
                actual_o = [('A', o) for o in aa['output_tags'] if o not in used_o] + [('B', o) for o in bb['output_tags']]
                wanted_i = [('A', i) for i in range(len(a[2]))] + [('B', i) for i in range(len(b[2])) if i not in used_i]
                wanted_o = [('A', o) for o in range(len(a[3])) if o not in used_o] + [('B', o) for o in range(len(b[3]))]
                pi = tuple(actual_i.index(t) for t in wanted_i)
                po = tuple(actual_o.index(t) for t in wanted_o)
                computed = C.canonical(R.reorder(raw, pi, po), True); C.validate(computed)
                ci = gid[computed]
                assert computed == C.canonical(glue(aa['restored'], bb['restored'], matching), True)
                assert ledgers[di]['normal_orbit'] == ledgers[ci]['normal_orbit']
                assert matrices[di] == matrices[ci]
                # Explicitly lift every operand rewrite through this gluing.
                # Symmetry stages cancel on restoring the original boundary.
                at = di; contextual_path = []; ca, cb = a, b
                for side, route in [('A', aa['route']), ('B', bb['route'])]:
                    for nxt, rule in route:
                        if side == 'A':
                            ca = nxt
                        else:
                            cb = nxt
                        target = gid[C.canonical(glue(ca, cb, matching), True)]
                        assert (at, target, rule) in edge_ids
                        contextual_path.append(min(edge_ids[at, target, rule])); at = target
                assert at == ci
                # Recover from the normalized transported composite, then undo
                # the contextual operand paths. This checks the composite
                # readback, not just equality of quotient IDs.
                assert recovered[ci] == computed
                back = [{'step': e, 'direction': -1} for e in reversed(contextual_path)]
                restored_id, _ = R.replay_signed(ci, back, gs, steps, definitions)
                assert restored_id == di
                final_direct = gid[operands[di]['restored']]
                final_staged = gid[operands[ci]['restored']]
                assert matrices[final_direct] == matrices[final_staged] == matrices[di]
                if final_direct != final_staged:
                    different_final_representatives += 1
                    final_pair_counts[tuple(sorted((final_direct, final_staged)))] += 1
                    if len(final_representative_examples) < 5:
                        final_representative_examples.append({'left': ai, 'right': bi, 'matching': matching,
                                                             'direct_terminal': final_direct,
                                                             'staged_terminal': final_staged,
                                                             'common_normal_orbit': ledgers[di]['normal_orbit']})
                naive = C.canonical(glue(aa['normal'], bb['normal'], matching), True)
                ni = gid[naive]
                naive_bad = matrices[di] != matrices[ni]
                counts['naive_semantic_failures'] += naive_bad
                counts['naive_syntax_differences'] += naive != computed
                counts[f'vertices_{len(direct[0])}_wires_{len(matching)}'] += 1
                if naive_bad and len(naive_examples) < 5:
                    naive_examples.append({'left': ai, 'right': bi, 'matching': matching,
                                           'direct': di, 'transported': ci, 'naive': ni,
                                           'matrix_difference': M.first_difference(matrices[di], matrices[ni])})
                cases.append({'left': ai, 'right': bi, 'matching': matching,
                              'normalized_matching': transported,
                              'external_input_restore': pi, 'external_output_restore': po,
                              'direct_gluing': di, 'transported_gluing': ci,
                              'normal_orbit': ledgers[di]['normal_orbit'],
                              'contextual_primitive_path': contextual_path})
    assert naive_examples
    # Rejection controls for the gluing interface itself.
    a = C.graph((1,), ()); b = C.graph((0,), ())
    for bad in ((), ((0, 0), (0, 1)), ((0, 0), (1, 0)), ((2, 0),), ((0, -1),)):
        try:
            glue(a, b, bad)
        except ValueError:
            pass
        else:
            raise AssertionError('invalid gluing accepted')
    report = {'schema': 'marici.nima.trivalent-retained-gluing.v1',
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'normalization_report_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'scope': 'All nonempty injective one-way output/input matchings between connected nonempty operands with at most three total vertices; ordered boundary restored',
              'model': 'rank-two left-zero semigroup algebra over integers, transpose split; noncommutative Frobenius equations verified',
              'operand_transports': [{'source': i, 'input_tags': o['input_tags'], 'output_tags': o['output_tags'],
                                      'normal_orbit': ledgers[i]['normal_orbit']} for i, o in enumerate(operands)],
              'cases': cases, 'counts': dict(counts), 'total_cases': len(cases),
              'different_final_ordered_normal_representatives': different_final_representatives,
              'negative_examples': naive_examples,
              'different_ordered_terminal_examples': final_representative_examples,
              'different_ordered_terminal_pairs': [{'pair': p, 'cases': n} for p, n in sorted(final_pair_counts.items())],
              'composite_round_trips': len(cases), 'checks_passed': True,
              'limitations': ['At most one operand can have two vertices; does not test two nontrivial two-vertex normalizations together.',
                              'One-way cross-operand gluing only; no feedback, self-gluing or arbitrary multi-stage associativity theorem.',
                              'Matching quotient normal forms and contextual paths do not identify higher proof paths.',
                              'No general-arities compositionality or semantics-faithfulness theorem.']}
    RESULT.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print('gluing cases:', len(cases)); print(dict(counts))
    print('different final ordered normal representatives:', different_final_representatives)
    print('naive counterexamples:', naive_examples[:1])


if __name__ == '__main__':
    main()
