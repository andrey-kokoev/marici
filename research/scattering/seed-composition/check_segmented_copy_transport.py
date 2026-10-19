"""Conditional segmentation-aware unchanged-copy transport for the seed candidate.

Build the macro-boundary rule from the supplied dictionary and endpoint incidence.
Derive its invariant copy image before comparing with the reference photon plane.
No physical state preparation or common physical clock is inferred.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import audit as incidence_audit, mm, transpose, rank, eye, apply, encode
from check_retained_word_transport import RetainedSuccessorLedger

ROOT = Path(__file__).resolve().parents[3]
BASE = Path(__file__).resolve().parent
DEST = BASE / 'results/segmented-copy-transport.v1.json'


def zeros(n,m):
    return [[F(0)]*m for _ in range(n)]


def plus(a,b):
    return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]


def audit():
    prior=incidence_audit()
    primitive=prior['primitive_order']; displayed=prior['displayed_order']
    endpoints=[tuple(p['edge']) for p in primitive]
    packets=[(p['owner']+':'+''.join(p['edge']),*p['edge']) for p in primitive]
    words=[tuple(endpoints.index(e) for e in zip(d['path'],d['path'][1:])) for d in displayed]
    ledger=RetainedSuccessorLedger(packets)
    x=list(map(F,range(1,11)))
    leaves=[ledger.retain_path_payload((((a,b,label),),),(value,)) for (label,a,b),value in zip(packets,x)]
    neutral=[ledger.retain_path_payload((((a,b,label),),),(F(1),)) for label,a,b in packets]
    retained=[]
    for word in words:
        payload=leaves[word[0]]
        for index in word[1:]:
            previous=payload
            payload=ledger.compose_payloads(previous,neutral[index])
            parents,slots=ledger.deconstruct_payload(payload)
            assert parents==(previous,neutral[index]) and slots==((0,0),)
        assert payload.values==(x[word[0]],)
        retained.append(payload)
    Q=[[F(j==word[0]) for j in range(10)] for word in words]
    assert [p.values[0] for p in retained]==apply(Q,x)
    assert [word[0] for word in words]==[0,1,8,2,4,0,5,7,8,8,9,0]
    assert rank(Q)==8
    residuals=[[F(j==i) for j in range(10)] for i in [3,6]]
    assert rank(Q+residuals)==10

    # Full macro endpoint incidence, with the candidate's two output labels kept.
    K=[[F(i//6==j//6 and displayed[j]['edge'][1]==displayed[i]['edge'][0])
        for j in range(12)] for i in range(12)]
    assert sum(map(sum,K))==20
    C=[[F(j==a)-F(j==b) for j in range(12)] for a,b in [(5,0),(11,0),(8,2),(9,2)]]
    assert rank(C)==4 and mm(C,Q)==zeros(4,10)
    assert rank(mm(C,mm(K,Q)))==2  # Arbitrary source copies are not invariant.

    # Derive the maximal continuation-stable part of im(Q) by compatibility,
    # not by fitting a two-dimensional operator first. Unobserved d,g remain
    # two separate residual directions of the input carrier.
    compatibility=[]; current=Q
    ranks=[]
    for step in range(13):
        compatibility+=mm(C,current)
        ranks.append(rank(compatibility))
        current=mm(K,current)
    assert ranks[:4]==[0,2,4,4] and ranks[-1]==4
    # A four-dimensional stable image is explicit; the rank bound proves maximality.
    # Common source roles (a,b,i,e), with f=a,h=b,c=i,j=e.
    roles=[0,1,2,2,3,0,0,1,2,2,3,0]
    H=[[F(j==role) for j in range(4)] for role in roles]
    J4=[[F(j==role) if role is not None else F(0) for j in range(4)]
        for role in [0,1,2,None,3,0,None,1,2,3]]
    M=[[F(n) for n in row] for row in [[0,0,1,1],[1,0,0,0],[1,1,0,0],[0,0,1,0]]]
    assert rank(H)==4 and mm(Q,J4)==H and mm(K,H)==mm(H,M)

    # Only now compare the invariant source-role carrier with the independently
    # recorded reference mode frame and its actual endpoint-derived step.
    V=prior['matrices']['displayed_mode_frame_V']; T=prior['matrices']['reference_mode_step_T']
    T4=[[T[i%2][j%2] if i//2==j//2 else F(0) for j in range(4)] for i in range(4)]
    assert rank(mm(C,V))==1
    assert rank(mm(C,V)+mm(C,mm(V,T4)))==2
    diagonal=[[1,0],[0,1],[1,0],[0,1]]
    Vsync=mm(V,diagonal)
    Z=[[-1,0],[F(1,2),F(1,2)],[1,0],[-F(1,2),-F(1,2)]]
    assert mm(H,Z)==Vsync and mm(M,Z)==mm(Z,T)
    assert mm(K,Vsync)==mm(Vsync,T) and rank(Vsync)==2
    assert mm(K,mm(K,mm(K,Vsync)))==Vsync
    J=mm(J4,Z)
    assert mm(Q,J)==Vsync
    # Unrestricted endpoint continuation on the supplied glued primitive
    # registry is a DIFFERENT operator, not an identified physical dynamics.
    N=[[F(endpoints[j][1]==endpoints[i][0]) for j in range(10)] for i in range(10)]
    native_defect=[[a-b for a,b in zip(r,s)] for r,s in zip(mm(Q,mm(N,J)),mm(Vsync,T))]
    assert rank(native_defect)>0

    # An explicit graded automaton implements the supplied macro dictionary.
    # Its boundary states identify the next macro-edge to execute. Each length-2
    # word has one internal state retaining which composite is in progress.
    long=[i for i,w in enumerate(words) if len(w)==2]
    assert len(long)==6
    A=[[K[i][j] if len(words[j])==1 else F(0) for j in range(12)] for i in range(12)]
    B=[[K[i][j] for j in long] for i in range(12)]
    D=[[F(j==edge) for j in range(12)] for edge in long]
    P=[A[i]+B[i] for i in range(12)]+[row+[F(0)]*6 for row in D]
    assert plus(A,mm(B,D))==K
    assert mm(P,P)[:12]==[plus(mm(A,A),mm(B,D))[i]+mm(A,B)[i] for i in range(12)]
    transitions=[]
    for edge,word in enumerate(words):
        if len(word)==1:
            for target in range(12):
                if K[target][edge]:transitions.append((edge,target,word[0]))
        else:
            interior=12+long.index(edge)
            transitions.append((edge,interior,word[0]))
            for target in range(12):
                if K[target][edge]:transitions.append((interior,target,word[1]))
    assert len(transitions)==sum(map(sum,P))
    state_vertex=[d['edge'][0] for d in displayed]+[endpoints[words[e][0]][1] for e in long]
    for start,end,primitive_id in transitions:
        assert P[end][start]==1
        assert (state_vertex[start],state_vertex[end])==endpoints[primitive_id]
    # A three-MACRO-step mode return is not a three-primitive-step return for
    # this boundary-only initialization; do not turn event count into time.
    initial=Vsync+zeros(6,2)
    three_micro=mm(P,mm(P,mm(P,initial)))
    assert three_micro!=initial
    # The internal state blocks premature switching into another allowed
    # endpoint extension: after the first AB in composite AC, BA is not its BC.
    ac=5; interior=12+long.index(ac)
    assert endpoints[words[ac][0]][1]==endpoints[9][0]  # BA is globally composable
    assert all(primitive_id!=9 for start,_,primitive_id in transitions if start==interior)

    dependencies=list(prior['source_sha256'])+[
        'research/scattering/seed-composition/check_segmented_copy_transport.py',
        'research/scattering/seed-composition/check_retained_word_transport.py',
        'research/nima/checkers/retained_path_successor.py',
        'research/nima/checkers/check_indexed_path_synthesis.py',
        'research/nima/checkers/check_natural_tower_return.py',
        'research/nima/retained-path-family-composition-synthesis.md']
    return {
        'schema':'marici.scattering.segmented-copy-transport.v1',
        'status':'conditional_graded_copy_transport_with_synchronized_mode_plane',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'operation':'existing registered coefficient-copy extension using neutral right operands; dictionary/pair/segmentation supplied by candidate',
        'prefix_copy':{'pair_1':['a','b','i','c','e','a'],'pair_2':['f','h','i','i','j','a'],
                       'rank':8,'residuals':['d','g'],'residual_augmented_rank':10},
        'invariant_image':{'compatibility_ranks_through_step_12':ranks,'maximal_stable_dimension':4,
                           'constraints':['f=a','h=b','c=i','j=e'],
                           'common_roles':['a','b','i','e'],'derived_step_M':M},
        'mode_sector':{'instantaneous_pair_plane_intersection_dimension':3,
                       'maximal_reference_stable_pair_plane_dimension':2,
                       'synchronization':['u=s','v=t'],'macro_period_three':True,
                       'four_independent_mode_parameters':False,
                       'glued_primitive_endpoint_same_step_defect_rank':rank(native_defect)},
        'segmented_automaton':{'boundary_states':12,'internal_states':6,
                               'length_two_macro_ids':long,'transition_count':len(transitions),
                               'transition_labels':transitions,
                               'first_return_transfer':'z*A + z^2*B*D; A+B*D=K',
                               'three_micro_steps_return_boundary_initialized_mode':False,
                               'premature_internal_BA_extension_excluded':True},
        'matrices':{'prefix_copy_Q':Q,'image_constraints_C':C,'macro_K':K,
                    'invariant_role_embedding_H':H,'input_role_embedding_J4':J4,
                    'mode_role_frame_Z':Z,'synchronized_mode_frame':Vsync,
                    'source_input_mode_frame_J':J,'glued_primitive_endpoint_defect':native_defect,
                    'micro_P':P,'one_step_boundary_A':A,'internal_exit_B':B,'internal_entry_D':D},
        'boundary':{'dictionary_selection_derived_from_primitive_dynamics':False,
                    'synchronized_mode_preparation_derived':False,'independent_photons_constructed':False,
                    'physical_metric_or_faces_transported':False,'physical_clock_identified':False,
                    'physical_annihilation_derived':False,'ratio_372_derived':False,'formal_outcome_admitted':False},
        'next_gate':'Derive or reject the pair/segment boundary controller and synchronized preparation from native source operations; the graded event-level construction does not supply them.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();report=audit();text=json.dumps(report,indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:
            raise SystemExit('FAIL: missing or stale segmented-copy receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: actual unchanged-copy extension; maximal invariant image dimension 4; synchronized reference mode plane dimension 2.')
    print('PASS: 18-state segmented primitive automaton; exact first-return identity; unrestricted primitive same-step mismatch retained.')
    print('Boundary: conditional dictionary/controller and preparation, not independently emitted photons.')


if __name__=='__main__':main()
