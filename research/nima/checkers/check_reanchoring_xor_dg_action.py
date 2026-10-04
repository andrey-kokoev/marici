"""All four state-block XOR torsors in the existing reanchoring DG model.

Tests current payloads, not equality of retained operation histories. The free
DG fragment is realized by substitution; no full-source automorphism or lattice
realization is inferred. Standard library only; imports execute the old audit.
"""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import hashlib
import json
import runpy
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with redirect_stdout(StringIO()) as baseline_log:
    M = runpy.run_path(str(HERE/'check_witnessed_reference_reanchoring.py'))
plus, minus, mul, delta, word = (M[k] for k in ('plus', 'minus', 'mul', 'delta', 'word'))
reanchor, payload, initial = (M[k] for k in ('reanchor', 'payload', 'initial'))
anchors, hs = M['anchors'], M['hs']


def images(frame):
    return {'d': frame.reference, 'return': word('return'),
            'unitA': frame.unitA, 'unitB': frame.unitB,
            'triangle': frame.triangle, 'idA': word('idA'), 'idB': word('idB')}


def substitute(chain, assignment):
    result = {}
    for path, coefficient in chain.items():
        value = assignment[path[0]]
        for name in path[1:]: value = mul(assignment[name], value)
        result = plus(result, M['scale'](coefficient, value))
    return result


def main():
    counts = {'translations': 0, 'compositions': 0, 'generator_differentials': 0,
              'products': 0, 'round_trips': 0, 'omitted_quadratic_term_rejected': 0}
    per_q = []
    for q in range(4):
        labels = [f's:{o}:{o ^ q}' for o in range(4)]
        frames = [reanchor(initial, label) for label in labels]
        def kappa(o, g): return plus(hs[labels[o ^ g]], minus(hs[labels[o]]))
        for o in range(4):
            assert kappa(o, 0) == {}
            for g in range(4):
                k = kappa(o, g)
                old = frames[o]
                new = reanchor(old, labels[o ^ g])
                assert old.witnesses[labels[o ^ g]] == k
                assert delta(k) == plus(anchors[labels[o ^ g]], minus(anchors[labels[o]]))
                assert payload(new) == payload(frames[o ^ g])
                assert plus(k, kappa(o ^ g, g)) == {}
                assert payload(reanchor(new, labels[o])) == payload(old)
                assert new.parents == (old,)  # History remains, even for equal current payloads.
                counts['translations'] += 1
                counts['round_trips'] += 1
                assignment = images(new)
                if g:
                    assert plus(k, k)  # A base-independent additive V-action would fail.
                    quadratic = mul(mul(k, word('return')), k)
                    bad_triangle = plus(new.triangle, minus(quadratic))
                    expected_boundary = plus(mul(new.reference, new.unitA),
                                             minus(mul(new.unitB, new.reference)))
                    assert delta(bad_triangle) != expected_boundary
                    counts['omitted_quadratic_term_rejected'] += 1
                for name, value in assignment.items():
                    assert M['signature'](next(iter(value))) == M['arrows'][name]
                    assert delta(value) == substitute(delta(word(name)), assignment)
                    counts['generator_differentials'] += 1
                for a in assignment:
                    for b in assignment:
                        # Chronological product b then a, when typed.
                        if M['arrows'][b][1] != M['arrows'][a][0]: continue
                        source_product = mul(word(a), word(b))
                        realized = substitute(source_product, assignment)
                        assert realized == mul(assignment[a], assignment[b])
                        assert delta(realized) == substitute(delta(source_product), assignment)
                        counts['products'] += 1
                for h in range(4):
                    assert plus(k, kappa(o ^ g, h)) == kappa(o, g ^ h)
                    staged = reanchor(new, labels[o ^ g ^ h])
                    direct = reanchor(old, labels[o ^ g ^ h])
                    assert payload(staged) == payload(direct)
                    assert staged.parents == (new,) and direct.parents == (old,)
                    counts['compositions'] += 1
        per_q.append({'q': q, 'passed': True, 'strict_on_current_payload': True})
    report = {
        'schema': 'marici.nima.reanchoring-xor-dg-action.v1', 'status': 'passed',
        'torsors': per_q, 'counts': counts,
        'scope': 'Typed free DG fragment d,r,u,v,W and identities realized inside existing ambient DG algebra; reference changes compose strictly on current payloads.',
        'histories_identified': False,
        'full_source_dg_automorphism_proved': False,
        'lattice_adapter_extended_to_products_or_higher_witnesses': False,
        'q_selected_by_this_test': False,
        'baseline_audit_rerun': True,
        'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in
                          (Path(__file__).resolve(), HERE/'check_witnessed_reference_reanchoring.py',
                           HERE/'check_shared_leg_dg_realization.py')},
    }
    out = HERE.parent/'results'/'reanchoring-xor-dg-action.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print('PASS: all four torsors; '+str(counts))
    print('Strict current-payload composition; retained histories remain distinct.')
    print('No q-selection, full-source automorphism, or higher lattice adapter inferred.')


if __name__ == '__main__': main()
