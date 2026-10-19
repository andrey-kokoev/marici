"""Reflection covariance of supplied controller masks, events and predictive quotient."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import mm, rank, eye, apply, encode
from check_graded_boundary_transport import add, scale
from check_segmented_copy_transport import audit as transport_audit
from check_controller_preparation_audit import audit as preparation_audit
from check_controller_memory import audit as memory_audit
from check_symmetry_orbit_adapter import audit as orbit_audit

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/controller-reflection.v1.json'


def zero(n,m=None):return [[F(0)]*(n if m is None else m) for _ in range(n)]
def minus(a,b):return add(a,scale(b,-1))
def permutation_matrix(p):return [[F(i==p[j]) for j in range(len(p))] for i in range(len(p))]
def parity(J):return scale(add(eye(len(J)),J),F(1,2)),scale(minus(eye(len(J)),J),F(1,2))


def audit():
    previous=orbit_audit();transport=transport_audit();prep=preparation_audit();memory=memory_audit()
    primitive_perm=prep['symmetry']['primitive_permutations'][1]
    boundary_perm=[9,10,11,6,7,8,3,4,5,0,1,2]
    long=transport['segmented_automaton']['length_two_macro_ids']
    context_perm=boundary_perm+[12+long.index(boundary_perm[e]) for e in long]
    J=permutation_matrix(context_perm);R=permutation_matrix(primitive_perm)
    assert mm(J,J)==eye(18)
    contexts=prep['controller']['contexts'];P=transport['matrices']['micro_P']
    assert mm(J,P)==mm(P,J)
    rp,rm=parity(R);jp,jm=parity(J)
    mask_rows=[]
    for c in contexts:
        reflected=contexts[context_perm[c['state']]]
        assert reflected['expected_primitive']==primitive_perm[c['expected_primitive']]
        assert set(reflected['available_primitives'])=={primitive_perm[p] for p in c['available_primitives']}
        chosen=c['expected_primitive'];M=[[F(i==j==chosen) for j in range(10)] for i in range(10)]
        leakage=mm(rp,mm(M,rm))
        assert rank(minus(mm(R,M),mm(M,R)))==2 and rank(leakage)==1
        mask_rows.append({'context':c['state'],'reflected_context':context_perm[c['state']],
                          'primitive':chosen,'reflected_primitive':primitive_perm[chosen],
                          'global_primitive_mask_commutator_rank':2,'odd_to_even_rank':1,
                          'endpoint_forced':len(c['available_primitives'])==1})
    # Retain context together with eligible primitive slots. Reflection acts on
    # both indices, so accepted/rejected masks are jointly invariant.
    eligible=[(c['state'],p) for c in contexts for p in c['available_primitives']]
    eligible_perm=[eligible.index((context_perm[c],primitive_perm[p])) for c,p in eligible]
    G=permutation_matrix(eligible_perm);gp,gm=parity(G)
    accept=[[F(i==j and eligible[i][1]==contexts[eligible[i][0]]['expected_primitive'])
             for j in range(len(eligible))] for i in range(len(eligible))]
    reject=minus(eye(len(eligible)),accept)
    assert len(eligible)==32
    assert mm(G,accept)==mm(accept,G) and mm(G,reject)==mm(reject,G)
    assert [rank(accept),rank(reject)]==[18,14]
    assert [rank(mm(gp,accept)),rank(mm(gm,accept)),rank(mm(gp,reject)),rank(mm(gm,reject))]==[9,9,7,7]
    assert mm(gp,mm(accept,gm))==zero(32)
    assert add(accept,reject)==eye(32) and mm(accept,reject)==zero(32)
    # Explicit hostile: a fixed primitive selector destroys anti-correlation.
    witness=[F(i==0)-F(i==primitive_perm[0]) for i in range(10)]
    M=[[F(i==j==0) for j in range(10)] for i in range(10)]
    assert apply(rm,witness)==witness and any(apply(rp,apply(M,witness)))

    transitions=transport['segmented_automaton']['transition_labels']
    matrices=[zero(18) for _ in range(10)]
    for a,b,p in transitions:matrices[p][b][a]+=1
    label_rows=[]
    for p,T in enumerate(matrices):
        assert mm(J,mm(T,J))==matrices[primitive_perm[p]]
        leak=mm(jp,mm(T,jm))
        orbit_sum=add(T,matrices[primitive_perm[p]])
        assert mm(jp,mm(orbit_sum,jm))==zero(18)
        label_rows.append({'primitive':p,'reflected_primitive':primitive_perm[p],
                           'arcs':int(sum(map(sum,T))),'odd_to_even_rank':rank(leak),
                           'reflection_orbit_sum_preserves_parity':True})
    assert all(row['odd_to_even_rank']>0 for row in label_rows)
    assert mm(jp,mm(P,jm))==zero(18)
    # Preserve event identity: a reflected event-word has the reflected pair,
    # primitive and same completion flag, not the identical event label.
    finishes=[i not in long for i in range(12)]+[True]*6
    pairs=[i//6 for i in range(12)]+[e//6 for e in long]
    arcs=set(transitions)
    assert all((context_perm[a],context_perm[b],primitive_perm[p]) in arcs for a,b,p in arcs)
    assert all(pairs[context_perm[c]]==1-pairs[c] and finishes[context_perm[c]]==finishes[c] for c in range(18))

    groups=memory['quotient']['classes'];Q=memory['quotient']['state_sum_Q']
    group_perm=[next(i for i,h in enumerate(groups) if set(h)=={context_perm[s] for s in g}) for g in groups]
    Jq=permutation_matrix(group_perm)
    assert mm(Q,J)==mm(Jq,Q) and mm(Jq,Jq)==eye(16)
    qplus,qminus=parity(Jq)
    assert rank(qplus)==rank(qminus)==8
    residual=[[F(i==a)-F(i==b) for i in range(18)] for a,b in [(1,14),(10,16)]]
    residual_action=[[F(0),F(1)],[F(1),F(0)]]
    assert mm(residual,J)==mm(residual_action,residual)

    dependencies=list(previous['source_sha256'])+['research/scattering/seed-composition/check_controller_reflection.py']
    return {
        'schema':'marici.scattering.controller-reflection.v1',
        'status':'retained_joint_controller_is_reflection_covariant_fixed_primitive_postselection_leaks_parity',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'context_permutation':context_perm,'primitive_permutation':primitive_perm,
        'isolated_masks':mask_rows,
        'joint_eligible_controller':{'dimension':32,'accepted_rank':18,'rejected_rank':14,
                                     'accepted_even_odd_ranks':[9,9],'rejected_even_odd_ranks':[7,7],
                                     'joint_reflection':'(context,primitive) -> (J_context context,J_primitive primitive)',
                                     'accepted_and_rejected_preserve_joint_parity':True,
                                     'original_slots_recovered_by_sum':True},
        'event_dynamics':{'labelled_matrices':label_rows,'aggregate_micro_P_commutes_with_reflection':True,
                          'event_label_reflection':'(pair,primitive,completion) -> (1-pair,J_primitive primitive,completion)',
                          'fixed_label_branch_preserves_parity':False,
                          'orbit_summing_retains_primitive_label':False,
                          'paired_label_covariance_is_physical_coherent_erasure':False},
        'predictive_quotient':{'classes':16,'reflection_permutation':group_perm,
                               'even_odd_ranks':[8,8],'Q_J_equals_Jq_Q':True,
                               'retained_difference_records_reflection':'swap the two residuals'},
        'hostile_fixed_mask_witness':{'odd_input':witness,'selected_output':apply(M,witness),
                                     'leaked_even_component':apply(rp,apply(M,witness))},
        'boundary':{'controller_policy_source_derived':False,'parity_preparation_derived':False,
                    'primitive_label_discard_authorized':False,'physical_measurement_derived':False,
                    'formal_outcome_admitted':False},
        'next_gate':'Keep primitive event labels as an explicit output register and test joint system/register parity versus conditional boundary parity; identify the coherence or label-erasure operation needed before using aggregate covariance as odd preparation.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale controller-reflection receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: isolated masks leak parity; accepted/rejected joint-context masks preserve reflected parity (ranks 18+14).')
    print('PASS: labelled transitions are reflection covariant, aggregate transport preserves parity, and quotient symmetry descends.')
    print('Boundary: fixed event postselection is not parity preserving; supplied controller covariance is not derived preparation.')


if __name__=='__main__':main()
