"""Low-energy source-operation preflight and exact conditional witness ambiguity."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
HOME=ROOT/'research/scattering/low-energy'
CONTRACT=HOME/'contracts/retained-operation-inventory.v1.json'
NOTE=HOME/'RETAINED-OPERATION-INVENTORY.md'
RESULT=HOME/'results/retained-operation-inventory.v1.json'
PERMS=list(itertools.permutations(range(4)))
IDENTITY=tuple(range(4))


def compose(p,q):return tuple(p[q[i]] for i in range(4))
def inverse(p):return tuple(p.index(i) for i in range(4))
def conjugate(p,q):return compose(compose(p,q),inverse(p))


def swap(a,b):
    p=list(IDENTITY);p[a],p[b]=p[b],p[a];return tuple(p)


def policy(a,b,spectators):
    result=swap(a,b)
    if spectators:
        c,d=[i for i in range(4) if i not in (a,b)]
        result=compose(result,swap(c,d))
    return result


def valid_policy(rule):
    for a,b in itertools.permutations(range(4),2):
        if rule(a,b)[a]!=b:return False
        for p in PERMS:
            if rule(p[a],p[b])!=conjugate(p,rule(a,b)):return False
    return True


def generated_group(generators):
    group={IDENTITY};todo=[IDENTITY]
    while todo:
        p=todo.pop()
        for g in generators:
            q=compose(g,p)
            if q not in group:group.add(q);todo.append(q)
    return group


def audit():
    model=json.loads(CONTRACT.read_text(encoding='utf-8'))
    assert model['schema']=='marici.scattering.low-energy-retained-operations.v1'
    operations=model['operations'];assert len({o['id'] for o in operations})==len(operations)
    allowed={'source_defined','source_defined_conditional','mathematical_convention','fixed_supplied_model','requires_explicit_input','conditional_adapter','missing_source_attachment','imported_model_structure'}
    for op in operations:assert op['availability'] in allowed and op['input'] and op['retains'] and op['boundary']
    gate=model['candidate_gate']
    assert gate['status']=='preflight_completed_missing_source_attachment' and len(gate['missing_inputs'])==3
    for key in ('source_construction_refuted','physical_output_identified','new_conjecture_admitted'):assert gate[key] is False
    spec=model['conditional_witness_test']
    assert spec['not_admitted_as_C12'] is True
    assert spec['labels']==['A','B','C','D'] and spec['base_edge']==['A','B']
    assert spec['distinguishing_route']==['B','C','A','B'],'unreviewed witness-test dictionary'
    pointed=[p for p in PERMS if p[0]==1]
    stabilizer=[p for p in PERMS if p[0]==0 and p[1]==1]
    commuting=[g for g in pointed if all(conjugate(p,g)==g for p in stabilizer)]
    assert len(pointed)==6 and len(stabilizer)==2
    assert set(commuting)=={policy(0,1,False),policy(0,1,True)}
    results=[]
    for spectator in (False,True):
        rule=lambda a,b:policy(a,b,spectator)
        assert valid_policy(rule)
        for a,b in itertools.permutations(range(4),2):assert rule(b,a)==inverse(rule(a,b))
        # Traversal B->C->A->B; later arrows compose on the left.
        loop=compose(rule(0,1),compose(rule(2,0),rule(1,2)))
        assert loop[1]==1
        expected=IDENTITY if spectator else swap(0,2)
        assert loop==expected
        group=generated_group([rule(a,b) for a,b in itertools.permutations(range(4),2)])
        assert len(group)==(4 if spectator else 24)
        results.append({'spectators_swapped':spectator,'loop_permutation':[chr(65+i) for i in loop],
                        'generated_group_order':len(group),'loop_fixes_anchor_B':True})
    assert results[0]['loop_permutation']!=results[1]['loop_permutation']
    # Endpoint compatibility alone is too weak, and choosing spectator policy
    # independently on one edge destroys full relabelling equivariance.
    mixed=lambda a,b:policy(a,b,(a,b)==(0,1))
    assert not valid_policy(mixed)
    assert results[0]['loop_fixes_anchor_B'] and results[1]['loop_fixes_anchor_B']
    paths={CONTRACT,NOTE,Path(__file__)}|{ROOT/p for p in model['sources']}
    for p in paths:assert p.is_file()
    return {'schema':'marici.scattering.retained-operation-inventory-receipt.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
            'operations_inventoried':len(operations),'pointed_base_witnesses':6,'equivariant_policies':2,
            'conditional_policy_tests':results,
            'hostiles_refused':['edgewise-fitted-policy','anchor-return-implies-full-return'],
            'missing_actual_comparison_assignment':True,'joint_phase_transport_verified':False,
            'all_source_authorized_constructions_classified':False,'new_conjecture_admitted':False,
            'source_constructor_refuted':False,'scientific_solver_replayed':False}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=audit()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale operation preflight receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','operations_inventoried','equivariant_policies','missing_actual_comparison_assignment','new_conjecture_admitted')}))


if __name__=='__main__':main()
