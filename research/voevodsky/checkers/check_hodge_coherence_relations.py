"""Exact abstract relation controls and graph validation, not Hodge evidence."""
import json
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = 'research/conjecture_net/contracts/hodge-coherence-relations.v1.json'


def validate(c, lead):
    ids = {n['id'] for n in lead['leads'] + lead['conjectures']}
    assert len(c['relations']) == len({r['id'] for r in c['relations']}) == 6
    assert not c['Hodge_proved'] and not c['Hodge_refuted']
    for r in c['relations']:
        assert set(r['endpoints']) <= ids
        assert r['hodge_implication_admitted'] is False
        assert r['status'] in ('proved_abstract_only', 'countermodel_checked_abstract_only', 'open_blocked')
        assert all(r[k] for k in ('premises', 'claim', 'proof_or_test', 'hodge_bridge', 'falsifier'))
    assert c['execution']['Hodge_source_tasks'] == []


def controls():
    # P keeps the first two coordinates; B keeps only the first.
    p = lambda v: v[:2]
    b = lambda w: w[0]
    q = lambda v: b(p(v))**2
    for v in product((-1, 0, 1), repeat=3):
        if p(v) == (0, 0):
            assert q(v) == 0
    assert p((0, 1, 0)) != (0, 0) and q((0, 1, 0)) == 0
    # A nonzero dark state exists in a fully admitted identity-realization source.
    v = (0, 1)
    assert v != (0, 0) and v[0]**2 == 0
    # Surjectivity and a lost witness coexist: s(x,y)=x, F(x,y)=y.
    for h in (-2, -1, 0, 1, 2):
        assert (h, 0)[0] == h
    assert (0, 1)[0] == (0, 0)[0] and (0, 1)[1] != (0, 0)[1]
    # An indefinite form's zero locus is not the matrix kernel.
    assert 1**2 - 1**2 == 0 and (1, -1) != (0, 0)
    cases = 0
    for source_size in range(3):
        for mu in product(range(2), repeat=source_size):
            image = set(mu)
            for rho in product(range(2), repeat=2):
                saturated = all(rho[x] != rho[y] or ((x in image) == (y in image))
                                for x in range(2) for y in range(2))
                reflects = all(rho[m] not in {rho[a] for a in image} or m in image
                               for m in range(2))
                assert saturated == reflects
                cases += 1
    # Filled boundary 0 and empty boundary 1 become indistinguishable.
    image, rho = {0}, (0, 0)
    assert 1 not in image and rho[1] in {rho[a] for a in image}
    return cases


if __name__ == '__main__':
    c = json.loads((ROOT/CONTRACT).read_text(encoding='utf-8'))
    lead = json.loads((ROOT/c['lead_contract']).read_text(encoding='utf-8'))
    validate(c, lead)
    cases = controls()
    bad = json.loads(json.dumps(c)); bad['relations'][0]['hodge_implication_admitted'] = True
    try:
        validate(bad, lead)
    except AssertionError:
        pass
    else:
        raise AssertionError('unsupported Hodge implication accepted')
    result = {'passed': True, 'relations': 6, 'finite_existence_reflection_cases': cases,
              'classification': 'abstract_conditional_relations_and_countermodels_only',
              'Hodge_proved': False, 'Hodge_refuted': False,
              'residuals': ['common source-derived Hodge realization diagram missing']}
    (ROOT/'research/voevodsky/results/hodge-coherence-relations-v1.json').write_text(
        json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result))
