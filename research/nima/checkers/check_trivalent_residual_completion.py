"""Extract residual three-vertex derived shortcuts and test contextual symmetry.

No independent relation is added: each shortcut has a signed path through the
reversible experimental Frobenius/associativity equations. Compare honest local
schema placement with a deliberately non-equivariant numbered-graph control.
"""
from collections import defaultdict
from itertools import permutations, product
from pathlib import Path
import hashlib
import json
import check_reversible_trivalent_census as C
import check_trivalent_contextual_overlaps as O
import check_trivalent_derived_completion as D
import check_trivalent_mixed_candidate as M

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'research/nima/results/trivalent-derived-completion.json'
RESULT = ROOT / 'research/nima/results/trivalent-residual-completion.json'


def tuple_tree(x):
    return tuple(tuple_tree(y) for y in x) if isinstance(x, list) else x


def reorder(g, pi, po):
    return (g[0], g[1], tuple(g[2][i] for i in pi), tuple(g[3][i] for i in po))


def orbit_key(diagrams, reversal=False):
    """Simultaneous boundary action, independent internal vertex relabelling.

    Diagram 0 is the fork source; remaining two are an unordered terminal pair.
    Optionally reverse all three. Local slots are never permuted.
    """
    variants = []
    for rev in ([False, True] if reversal else [False]):
        ds = [C.reverse(g) if rev else g for g in diagrams]
        for pi in permutations(range(len(ds[0][2]))):
            for po in permutations(range(len(ds[0][3]))):
                cc = [C.canonical(reorder(g, pi, po), True) for g in ds]
                variants.append((cc[0], tuple(sorted(cc[1:]))))
    return min(variants)


def replay_signed(start, trace, gs, steps, definitions):
    current = start
    evidence = []
    for signed in trace:
        e = steps[signed['step']]
        lhs, rhs = definitions[e['rule']]
        p = tuple(e['embedding'])
        raw = O.replace(gs[e['source']], lhs, rhs, p)
        assert raw is not None and C.canonical(raw, True) == gs[e['target']]
        if signed['direction'] == 1:
            assert current == e['source']
            current = e['target']
            evidence.append({'step': e['id'], 'direction': 1})
        else:
            assert signed['direction'] == -1 and current == e['target']
            # Exhibit the renaming needed to undo a step whose target was
            # canonicalized by the earlier checker.
            rename = next(q for q in permutations(range(len(raw[0])))
                          if C.relabel(gs[current], q, True) == raw)
            assert O.replace(C.relabel(gs[current], rename, True), rhs, lhs, p) == gs[e['source']]
            current = e['source']
            evidence.append({'step': e['id'], 'direction': -1, 'target_to_raw_renaming': rename})
    return current, evidence


def compact(summary):
    return {'rules': summary['rules'], 'placement_steps': summary['placement_steps'],
            'fork_counts': summary['fork_counts'],
            'unjoined_forks': sum(f['join'] is None for f in summary['forks']),
            'cycle_step_count': len(summary['steps_on_directed_cycles'])}


def main():
    source = json.loads(SOURCE.read_text(encoding='utf-8'))
    # Fail rather than silently testing stale graph IDs/provenance.
    assert source['checker_sha256'] == hashlib.sha256(Path(D.__file__).read_bytes()).hexdigest()
    for module in (C, O, M):
        assert source['dependency_hashes'][Path(module.__file__).name] == hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest()
    gs = [tuple_tree(row['graph']) for row in source['diagrams']]
    ids = {g: i for i, g in enumerate(gs)}
    steps = source['placement_steps']
    best = source['best_acyclic_controls'][0]
    chosen = set(best['rules'])
    definitions = {n: (l, r) for n, l, r in O.rules()}
    definitions.update({'inverse_' + n: (r, l) for n, l, r in O.rules()})
    outgoing = defaultdict(list)
    for e in steps:
        if e['rule'] in chosen:
            outgoing[e['source']].append((e['id'], e['target']))
    residual = []
    for f in best['forks']:
        if f['join'] is not None:
            continue
        assert len(f['left_normal_forms']) == len(f['right_normal_forms']) == 1
        a, b = f['left_normal_forms'][0], f['right_normal_forms'][0]
        ea, eb = (steps[i] for i in f['steps'])
        pa = [ea['id']] + O.reachable(ea['target'], outgoing)[a]
        pb = [eb['id']] + O.reachable(eb['target'], outgoing)[b]
        signed = ([{'step': e, 'direction': -1} for e in reversed(pa)] +
                  [{'step': e, 'direction': 1} for e in pb])
        end, proof = replay_signed(a, signed, gs, steps, definitions)
        assert end == b
        residual.append({'source': f['source'], 'left_terminal': a, 'right_terminal': b,
                         'left_forward_path': pa, 'right_forward_path': pb,
                         'derived_left_to_right': proof})
    assert len(residual) == 4
    boundary_orbits = defaultdict(list); reversal_orbits = defaultdict(list)
    for i, f in enumerate(residual):
        triple = [gs[f['source']], gs[f['left_terminal']], gs[f['right_terminal']]]
        boundary_orbits[orbit_key(triple)].append(i)
        reversal_orbits[orbit_key(triple, True)].append(i)

    # One proposed local schema per distinct terminal equation (up to endpoint
    # exchange, but NOT silently quotienting external boundary order).
    pairs = sorted({tuple(sorted((f['left_terminal'], f['right_terminal']))) for f in residual})
    macros = []
    macro_derivations = {}
    for j, (a, b) in enumerate(pairs):
        witness = next(f for f in residual if {f['left_terminal'], f['right_terminal']} == {a, b})
        for direction, (x, y) in enumerate(((a, b), (b, a))):
            name = f'residual_{j}_{direction}'
            macros.append((name, gs[x], gs[y]))
            trace = witness['derived_left_to_right']
            if witness['left_terminal'] != x:
                trace = [{'step': t['step'], 'direction': -t['direction']} for t in reversed(trace)]
            end, proof = replay_signed(x, trace, gs, steps, definitions)
            assert end == y
            macro_derivations[name] = {'start': x, 'end': y, 'signed_path': proof}
    extended_steps = list(steps)
    macro_records = []
    for name, lhs, rhs in macros:
        applications = []
        for i, g in enumerate(gs):
            if len(g[0]) < len(lhs[0]):
                continue
            for p in permutations(range(len(g[0])), len(lhs[0])):
                h = O.replace(g, lhs, rhs, p)
                if h is None or not O.convex_support(g, set(p)):
                    continue
                C.validate(h)
                target = ids[C.canonical(h, True)]
                # Lift the macro's signed primitive path through this actual
                # placement and find/replay each primitive embedding. This
                # checks boundary-permuted instances, not only the display rule.
                at = macro_derivations[name]['start']
                current = i
                expansion = []
                for t in macro_derivations[name]['signed_path']:
                    primitive = steps[t['step']]
                    at = primitive['target'] if t['direction'] == 1 else primitive['source']
                    lifted = O.replace(g, lhs, gs[at], p)
                    expected = ids[C.canonical(lifted, True)]
                    pl, pr = definitions[primitive['rule']]
                    if t['direction'] == -1:
                        pl, pr = pr, pl
                    embedding = next(q for q in permutations(range(len(g[0])), 2)
                                     if (raw := O.replace(gs[current], pl, pr, q)) is not None
                                     and C.canonical(raw, True) == gs[expected])
                    expansion.append({'source': current, 'target': expected,
                                      'rule': primitive['rule'], 'direction': t['direction'],
                                      'embedding': embedding})
                    current = expected
                assert current == target
                e = {'id': len(extended_steps), 'source': i, 'target': target,
                     'rule': name, 'embedding': p, 'primitive_expansion': expansion}
                extended_steps.append(e); applications.append(e['id'])
        macro_records.append({'name': name, 'lhs': lhs, 'rhs': rhs, 'placement_ids': applications,
                              'derivation': macro_derivations[name]})
    # Exact tensor check includes all derived macro placements, not only the
    # two nominal endpoints used to display a schema.
    mu = [[[2, 0], [0, 0]], [[0, 0], [0, 2]]]
    vals = [M.evaluate(g, mu, M.transpose_mu(mu)) for g in gs]
    assert all(vals[e['source']] == vals[e['target']] for e in extended_steps[len(steps):])

    tests = {}
    for bits in product((0, 1), repeat=len(pairs)):
        names = {f'residual_{j}_{b}' for j, b in enumerate(bits)}
        label = '_'.join(map(str, bits))
        tests[label] = O.summarize(gs, extended_steps, chosen | names)
    # Numbered-graph controls are intentionally NOT local rewrite schemas.
    anchored_tests = {}
    for bits in product((0, 1), repeat=len(pairs)):
        ss = list(steps); nn = set()
        for j, (a, b) in enumerate(pairs):
            x, y = (a, b) if bits[j] == 0 else (b, a)
            name = f'anchored_{j}'; nn.add(name)
            ss.append({'id': len(ss), 'source': x, 'target': y,
                       'rule': name, 'embedding': tuple(range(len(gs[x][0])))})
        label = '_'.join(map(str, bits))
        anchored_tests[label] = compact(O.summarize(gs, ss, chosen | nn))

    symmetry_witnesses = []
    for a, b in pairs:
        for pi in permutations(range(len(gs[a][2]))):
            for po in permutations(range(len(gs[a][3]))):
                if (C.canonical(reorder(gs[a], pi, po), True) == gs[b]
                        and C.canonical(reorder(gs[b], pi, po), True) == gs[a]):
                    symmetry_witnesses.append({'endpoints': [a, b], 'input_permutation': pi,
                                               'output_permutation': po})
    assert len(symmetry_witnesses) == len(pairs)
    assert all(t['steps_on_directed_cycles'] for t in tests.values())
    assert all(not t['cycle_step_count'] and not t['unjoined_forks'] for t in anchored_tests.values())
    report = {'schema': 'marici.nima.trivalent-residual-completion.v1',
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'source_report_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'scope': 'Same ordered DAG census, 1-3 vertices; experimental reversible equations; no higher fillers',
              'chosen_orientation': sorted(chosen), 'residual_forks': residual,
              'boundary_permutation_fork_orbits': list(boundary_orbits.values()),
              'boundary_and_reversal_fork_orbits': list(reversal_orbits.values()),
              'diagrams': source['diagrams'], 'placement_steps': extended_steps,
              'derived_macro_schemas': macro_records, 'local_schema_tests': tests,
              'non_equivariant_anchored_controls': anchored_tests,
              'endpoint_exchange_symmetries': symmetry_witnesses,
              'checks_passed': True,
              'conclusions': ['Derived local terminal-swap schemas inherit both directions under boundary symmetry and create two-cycles.',
                              'Orienting only a numbered graph pair can converge in this bound, but is not an equivariant local schema.',
                              'No independent primitive or higher coherence filler has been introduced.']}
    RESULT.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print('residual forks:', len(residual), 'terminal pairs:', pairs)
    print('fork orbits, boundary permutations:', list(boundary_orbits.values()))
    print('fork orbits, also reversal:', list(reversal_orbits.values()))
    print('exchange symmetries:', symmetry_witnesses)
    for label, t in tests.items():
        print('local schemas', label, compact(t))
    for label, t in anchored_tests.items():
        print('anchored control', label, t)


if __name__ == '__main__':
    main()
