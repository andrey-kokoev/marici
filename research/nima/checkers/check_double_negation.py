"""Audit one frozen goal; an audited miss is not a proved law."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
from check_fresh_equations import verify
from fresh_equational_search import decode
from emit_fresh_equations import emit

BASE=Path(__file__).resolve().parents[1]
WORK=BASE/'milestones/double-negation'
RESULT=BASE/'results/double-negation-search.json'


def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def audit():
    packet=json.loads(RESULT.read_text())
    assert packet['schema']=='marici.ground-equational-milestone.v1'
    assert packet['target']=='involution' and packet['adequacy_constructed'] is False
    assert packet['limits']=={'seconds':60,'pool_cost':5,'instances':30000,'nodes':100000,'unions':60000}
    provenance=packet['provenance']
    assert provenance['cached_adequacy_used'] is False and provenance['cached_consequences_used'] is False
    assert (provenance['cost'],provenance['ordinal'])==(6,1488521)
    data=(BASE/'results/algebra-formula-search.json').read_bytes()
    assert hashlib.sha256(data).hexdigest()==provenance['input_sha256']
    expected_paths={str(BASE/'checkers'/name) for name in
        ['ground_equational_milestone.py','fresh_equational_search.py','check_fresh_equations.py']}
    assert set(provenance['source_sha256'])==expected_paths
    for path,digest in provenance['source_sha256'].items(): assert sha(path)==digest
    for key in ['instances','nodes','unions']:
        assert 0 <= packet['statistics'][key] <= packet['limits'][key]
    candidate=next(s for s in json.loads(data)['survivors'] if s['cost']==6 and s['ordinal']==1488521)
    expected=decode(candidate['left']),decode(candidate['right'])
    certificate=packet['certificate']
    replay=verify(certificate,expected)
    reached=replay['goals_checked']==['involution']
    assert set(replay['goals_checked'])<= {'involution'}
    assert packet['status']==('goal-derived' if reached else 'unresolved')
    assert replay['basis_complete'] is False
    return packet,replay


def positive_source(packet):
    return emit(packet['certificate']).replace('module FreshEquationalConsequences where','module DoubleNegation where')


def negative_source():
    return '''{-# OPTIONS --safe --cubical --guardedness #-}
module DoubleNegationWrongConclusion where
open import Cubical.Foundations.Prelude
import DoubleNegation as F
module Bad {ℓ : Level} (A : Type ℓ) (stroke : A → A → A)
  (hypothesis : (x0 x1 x2 : A) →
    stroke (stroke (stroke x0 x1) x2) (stroke x0 (stroke (stroke x0 x2) x0)) ≡ x2) where
  module D = F.Derived A stroke hypothesis
  bad : (x0 x1 : A) → stroke (stroke x0 x0) (stroke x0 x0) ≡ x1
  bad x0 x1 = D.involution x0
'''


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--emit',action='store_true')
    args=parser.parse_args()
    packet,replay=audit()
    reached=packet['status']=='goal-derived'
    if args.emit:
        if not reached: raise RuntimeError('unresolved: no goal theorem may be emitted')
        directory=WORK/'agda'; directory.mkdir(parents=True,exist_ok=True)
        (directory/'DoubleNegation.agda').write_text(positive_source(packet),encoding='utf-8')
        (directory/'DoubleNegationWrongConclusion.agda').write_text(negative_source(),encoding='utf-8')
        print(json.dumps({'emitted':True,'proof_records':replay['facts_checked']}))
        return
    checked=False
    if reached:
        assert (WORK/'agda/DoubleNegation.agda').read_text(encoding='utf-8')==positive_source(packet)
        assert (WORK/'agda/DoubleNegationWrongConclusion.agda').read_text(encoding='utf-8')==negative_source()
        kernel=json.loads((BASE/'results/double-negation-kernel.json').read_text(encoding='utf-8-sig'))
        assert kernel['passed'] is True and kernel['fresh'] is True and kernel['inputs_stable'] is True
        assert kernel['negative_rejected'] is True and kernel['negative_diagnostic']=='[UnequalTerms]'
        for path,digest in kernel['source_sha256'].items(): assert sha(path)==digest.lower()
        assert sha(kernel['compiler'])==kernel['compiler_sha256'].lower()
        assert sha(BASE/'checkers/check_double_negation_kernel.ps1')==kernel['checker_sha256'].lower()
        checked=True
    report={'schema':'marici.double-negation-audit.v1',
        'status':'one-law-kernel-checked' if checked else 'bounded-search-unresolved',
        'generated_at':datetime.now(timezone.utc).isoformat(),
        'search_status':packet['status'],
        'goal_kernel_checked':checked,'adequacy_constructed':False,'replay':replay,
        'search_sha256':sha(RESULT),'audit_sha256':sha(__file__),
        'residual':None if checked else 'No derivation of the prescribed law within the frozen search budget.'}
    (BASE/'results/double-negation-audit.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))


if __name__=='__main__':
    if not __debug__: raise RuntimeError('audit assertions must remain enabled')
    main()
