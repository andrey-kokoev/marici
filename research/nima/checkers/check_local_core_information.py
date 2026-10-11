"""Dependency-aware information analysis, not a scientific outcome update.

Boolean worlds are a classical planning abstraction, not constructive witnesses.
The only loaded probability is the explicitly historical parent marginal.
"""
from pathlib import Path
import hashlib
import itertools
import json
import math

ROOT=Path(__file__).resolve().parents[1]
CONTRACT=ROOT/'contracts/current-problem-conjecture-net.v1.json'

def entropy(p):
    return 0.0 if p in (0.0,1.0) else -p*math.log2(p)-(1-p)*math.log2(1-p)

def distribution(p,q):
    # q=P(A | not P), not a new elicited estimate.
    if not (0<=p<=1 and 0<=q<=1):
        raise ValueError('Probabilities outside [0,1]')
    return [(1-p)*(1-q),(1-p)*q,p]

def information(p,q):
    a=p+(1-p)*q
    posterior=p/a if a else 0.0
    gain=entropy(p)-a*entropy(posterior)
    return {'Pr_A':a,'Pr_parent_given_A':posterior if a else None,
            'Pr_parent_given_not_A':0.0 if a<1 else None,
            'joint_entropy_bits':entropy(p)+(1-p)*entropy(q),
            'perfect_A_test_information_about_parent_bits':max(0.0,gain)}

def main():
    net=json.loads(CONTRACT.read_text(encoding='utf-8'))
    nodes={n['id']:n for n in net['conjectures']}
    parent='source-derived-intermediate-locality-preserving-lift'
    core='source-derived-local-core-exists'
    assert net['lift_outcome_split']['standalone_local_core']==core
    assert nodes[core]['scope_id']==nodes[parent]['scope_id']
    assert nodes[core]['outcome']=='++' and nodes[parent]['outcome']=='++'
    receipt=json.loads((ROOT/'results/uniform-local-core.json').read_text(encoding='utf-8'))
    assert receipt['status']=='pass' and receipt['outcome']=='++'
    assert net['source_derivation_policy']['meaning']=='uniform-construction-existence-not-source-uniqueness'
    edges={e['id']:e for e in net['proof_relations']}
    assert edges['full-lift-proof-entails-standalone-local-core']['conclusion']==core
    assert edges['local-core-rejection-refutes-full-lift']['conclusion']==parent
    worlds=[{'local_core_exists':a,'full_lift_exists':p,'universal_return_obstruction':not p}
            for a,p in itertools.product((False,True),repeat=2) if not p or a]
    assert len(worlds)==3
    # Check formulas against explicit world probabilities over a grid, not new observations.
    for p,q in itertools.product((0,.1,.5,.9,1),repeat=2):
        weights=distribution(p,q)
        assert abs(sum(weights)-1)<1e-12
        actual=-sum(w*math.log2(w) for w in weights if w)
        r=information(p,q)
        assert abs(actual-r['joint_entropy_bits'])<1e-12
        assert -1e-12<=r['perfect_A_test_information_about_parent_bits']<=entropy(p)+1e-12
    historical_p=net['cost_model']['probabilities']['claim_prior_probability']
    assert abs(information(historical_p,0)['perfect_A_test_information_about_parent_bits']-entropy(historical_p))<1e-12
    assert information(historical_p,1)['perfect_A_test_information_about_parent_bits']<1e-12
    result={
        'status':'pass',
        'scope':'P implies A; comparison concerns the same candidate class and source-derived predicate.',
        'prior_logical_worlds':worlds,
        'possible_worlds':[w for w in worlds if w['local_core_exists'] and w['full_lift_exists']],
        'observed_local_core_outcome':'++','observed_full_lift_outcome':'++',
        'current_proved_pair_entropy_bits':0,
        'current_scope':'standard complex semantics with external whole-record return paths',
        'posterior_boundary':'Under the clarified meaning both A and P are proved. The old prior calculations below are historical, not a numerical Bayesian update. The now-decided mathematical pair has one consistent world; no claim about unresolved completion or physical semantics follows.',
        'free_parameter':{'name':'q = Pr(A | not P)','value':None,'status':'not_elicited'},
        'probability_model':'Pr(not A,not P)=(1-p)(1-q); Pr(A,not P)=(1-p)q; Pr(A,P)=p',
        'formulas':{'joint_entropy':'H(P,A)=h(p)+(1-p)h(q)',
                    'perfect_local_core_test_information':'I(P;A)=h(p)-[p+(1-p)q]*h(p/[p+(1-p)q])'},
        'historical_parent_marginal':{'p':historical_p,'status':'historical_subjective_not_reelicited','entropy_bits':entropy(historical_p)},
        'bounds_at_historical_parent_marginal':{
            'joint_entropy_bits':[entropy(historical_p),entropy(historical_p)+(1-historical_p)],
            'perfect_local_core_test_information_bits':[0.0,entropy(historical_p)]},
        'illustrations_not_estimates':[{'q':q,**information(historical_p,q)} for q in (0,.5,1)],
        'net_entropy_identified':True,'observational_update':True,
        'readiness':nodes[core]['test_readiness'],
        'limitations':['No probability assigned to q; no numerical ranking follows.',
                       'Perfect resolution of A is an information benchmark, not an attempt-success forecast.',
                       'Existence of an extendable lift does not imply that an arbitrary local witness extends.',
                       'Implication schemas and universal return obstruction are not independent random bits.',
                       'Extra joint entropy describes a finer question, not uncertainty created by adding a node.'],
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (CONTRACT,ROOT/'results/uniform-local-core.json',ROOT/'results/spectral-whole-return.json',Path(__file__).resolve())}}
    (ROOT/'results/local-core-information.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
