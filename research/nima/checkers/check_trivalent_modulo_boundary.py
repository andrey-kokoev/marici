"""Bounded normalization modulo external boundary permutations, with recovery.

Quotient ONLY external input/output order, retaining all local slots. Recovery
uses explicit symmetry transports and signed experimental reversible rewrites.
This is not a quotient-free normal form or a higher coherence theorem.
"""
from collections import defaultdict, deque
from itertools import permutations
from pathlib import Path
import hashlib
import json
import check_reversible_trivalent_census as C
import check_trivalent_contextual_overlaps as O
import check_trivalent_derived_completion as D
import check_trivalent_residual_completion as R
import check_trivalent_mixed_candidate as M

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'research/nima/results/trivalent-residual-completion.json'
RESULT = ROOT / 'research/nima/results/trivalent-modulo-boundary.json'


def inverse(p):
    out = [None] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def transport(g, w):
    return C.relabel(R.reorder(g, w['inputs'], w['outputs']), w['vertices'], True)


def untransport(g, w):
    return R.reorder(C.relabel(g, inverse(w['vertices']), True),
                     inverse(w['inputs']), inverse(w['outputs']))


def witness(g, target):
    for pi in permutations(range(len(g[2]))):
        for po in permutations(range(len(g[3]))):
            for pv in permutations(range(len(g[0]))):
                w = {'inputs': pi, 'outputs': po, 'vertices': pv}
                if transport(g, w) == target:
                    assert untransport(target, w) == g
                    return w
    raise AssertionError('not in the same declared boundary orbit')


def main():
    source = json.loads(SOURCE.read_text(encoding='utf-8'))
    assert source['checker_sha256'] == hashlib.sha256(Path(R.__file__).read_bytes()).hexdigest()
    prior = ROOT / 'research/nima/results/trivalent-derived-completion.json'
    assert source['source_report_sha256'] == hashlib.sha256(prior.read_bytes()).hexdigest()
    prior_data = json.loads(prior.read_text(encoding='utf-8'))
    assert prior_data['checker_sha256'] == hashlib.sha256(Path(D.__file__).read_bytes()).hexdigest()
    for name, expected in prior_data['dependency_hashes'].items():
        assert hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() == expected
    gs = [R.tuple_tree(row['graph']) for row in source['diagrams']]
    qs = sorted({C.canonical(g, False) for g in gs})
    qids = {g: i for i, g in enumerate(qs)}
    orbit = [qids[C.canonical(g, False)] for g in gs]
    selected = set(source['chosen_orientation'])
    definitions = {n: (l, r) for n, l, r in O.rules()}
    definitions.update({'inverse_' + n: (r, l) for n, l, r in O.rules()})
    all_steps = source['placement_steps']
    lifts = defaultdict(list)
    trivial_base = []
    for e in all_steps:
        if e['rule'] in selected:
            a, b = orbit[e['source']], orbit[e['target']]
            if a == b:
                trivial_base.append(e['id'])
            else:
                lifts[a, b].append(e['id'])
    outgoing, incoming = defaultdict(set), defaultdict(set)
    for a, b in lifts:
        outgoing[a].add(b); incoming[b].add(a)
    indegree = {i: len(incoming[i]) for i in range(len(qs))}
    todo = deque(sorted(i for i in indegree if not indegree[i])); order = []
    while todo:
        i = todo.popleft(); order.append(i)
        for j in sorted(outgoing[i]):
            indegree[j] -= 1
            if not indegree[j]:
                todo.append(j)
    assert len(order) == len(qs), 'quotient has a directed cycle'
    terminals = {}
    for i in reversed(order):
        terminals[i] = set().union(*(terminals[j] for j in outgoing[i])) if outgoing[i] else {i}
    assert all(len(t) == 1 for t in terminals.values()), 'quotient is not uniquely normalizing'
    normal = {i: next(iter(t)) for i, t in terminals.items()}
    # Residual macro steps should be pure symmetry in this quotient, not extra
    # reductions added to make it appear convergent.
    macros = [e for e in all_steps if e['rule'].startswith('residual_')]
    assert macros and all(orbit[e['source']] == orbit[e['target']] for e in macros)

    def recover(end, ledger):
        current = untransport(qs[end], ledger['final_symmetry'])
        for item in reversed(ledger['steps']):
            e = all_steps[item['placement']]
            lhs, rhs = definitions[e['rule']]
            raw = C.relabel(current, inverse(item['target_canonicalization']), True)
            before = O.replace(raw, rhs, lhs, tuple(e['embedding']))
            assert before is not None
            current = untransport(before, item['source_symmetry'])
        return current

    ledgers = []
    for start, g in enumerate(gs):
        current = g; q = orbit[start]; ledger = {'ordered_source_id': start, 'steps': []}
        while outgoing[q]:
            nxt = min(outgoing[q])  # explicitly chosen finite normalization strategy
            eid = min(lifts[q, nxt]); e = all_steps[eid]
            sym = witness(current, gs[e['source']])
            before = transport(current, sym)
            lhs, rhs = definitions[e['rule']]
            raw = O.replace(before, lhs, rhs, tuple(e['embedding']))
            assert raw is not None
            target = gs[e['target']]
            pv = next(p for p in permutations(range(len(raw[0]))) if C.relabel(raw, p, True) == target)
            ledger['steps'].append({'placement': eid, 'source_symmetry': sym,
                                    'target_canonicalization': pv})
            current = target; q = nxt
        ledger['normal_orbit'] = q
        ledger['final_symmetry'] = witness(current, qs[q])
        assert q == normal[orbit[start]]
        assert recover(q, ledger) == g
        ledgers.append(ledger)

    # Check normalization is invariant under every boundary action in the
    # finite census. This does not make the chosen paths/witnesses canonical.
    gid = {g: i for i, g in enumerate(gs)}
    action_checks = 0
    for i, g in enumerate(gs):
        for pi in permutations(range(len(g[2]))):
            for po in permutations(range(len(g[3]))):
                h = C.canonical(R.reorder(g, pi, po), True)
                j = gid[h]
                assert orbit[i] == orbit[j] and ledgers[i]['normal_orbit'] == ledgers[j]['normal_orbit']
                action_checks += 1
    # Negative control: a terminal diagram with reordered boundary cannot be
    # recovered by simply discarding its nontrivial final witness.
    erased_witness_failures = []
    for i, ledger in enumerate(ledgers):
        if not ledger['steps'] and qs[ledger['normal_orbit']] != gs[i]:
            erased_witness_failures.append(i)
    assert erased_witness_failures
    # Noncommutative Frobenius countercontrol: 2x2 integer matrix units.
    # E_ij E_jk = E_ik; split is transpose multiplication in this basis.
    mu = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                mu[2*i+k][2*i+j][2*j+k] = 1
    split = M.transpose_mu(mu)
    ev = lambda g: M.evaluate(g, mu, split)
    rr = O.rules()
    for _, lhs, rhs in rr:
        assert ev(lhs) == ev(rhs)
    merge = C.graph((0,), ())
    swapped = R.reorder(merge, (1, 0), (0,))
    original_map, swapped_map = ev(merge), ev(swapped)
    assert C.canonical(merge, False) == C.canonical(swapped, False)
    assert original_map[1][1] == 1 and swapped_map[1][1] == 0
    semantic_control = {'model': '2x2 integer matrix algebra; transpose split',
                        'primitive_equations_checked': [n for n, _, _ in rr],
                        'same_boundary_orbit': True,
                        'original_merge_matrix': original_map, 'swapped_merge_matrix': swapped_map,
                        'witness': 'E00*E01=E01 but E01*E00=0',
                        'conclusion': 'Full boundary quotient is not equality of ordered linear maps, even in a Frobenius model.'}
    fibers = defaultdict(list)
    for i, q in enumerate(orbit):
        fibers[q].append(i)
    report = {
        'schema': 'marici.nima.trivalent-modulo-boundary.v1',
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'source_report_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'scope': 'Ordered connected DAG census, 1-3 vertices; quotient full external S_m x S_n, NOT local slots',
        'assumptions': ['Experimental reversible associativity/Frobenius comparisons.',
                        'Full external boundary quotient is an explicit representation choice, not an equality of ordered operations.',
                        'Finite representative choices select replay paths; no higher-path canonicity is claimed.'],
        'ordered_diagrams': source['diagrams'],
        'quotient_diagrams': [{'id': i, 'graph': q, 'ordered_members': fibers[i], 'normal_form': normal[i]} for i, q in enumerate(qs)],
        'quotient_edges': [{'source': a, 'target': b, 'ordered_lifts': es} for (a, b), es in sorted(lifts.items())],
        'base_symmetry_only_steps': trivial_base,
        'residual_steps_collapsed_to_symmetry': [e['id'] for e in macros],
        'normalization_ledgers': ledgers,
        'topological_order': order,
        'semantic_countercontrol': semantic_control,
        'checks': {'acyclic_quotient': True, 'unique_terminal_per_orbit': True,
                   'ordered_round_trips': len(ledgers), 'boundary_action_checks': action_checks,
                   'erased_witness_failure_examples': erased_witness_failures[:10]},
        'counts': {'ordered_diagrams': len(gs), 'boundary_orbits': len(qs),
                   'quotient_edges': len(lifts), 'normal_forms': len(set(normal.values())),
                   'max_normalization_steps': max(len(x['steps']) for x in ledgers)},
        'limitations': ['No arbitrary-arity termination or coherence theorem.',
                        'Quotient normal form alone does not recover the input; the retained ledger does.',
                        'Recovery uses inverses of experimental cells; it is not a forward reduction proof.',
                        'No compatibility with gluing arbitrary ordered contexts has been established.']}
    RESULT.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(report['counts'])
    print(report['checks'])
    print('residual macro placements trivial in quotient:', len(macros))
    print(semantic_control['witness'])


if __name__ == '__main__':
    main()
