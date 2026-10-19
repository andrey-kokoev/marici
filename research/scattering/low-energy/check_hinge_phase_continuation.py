"""Finite-source hinge obstruction and a resource-explicit conditional spin lift."""
import argparse
import ast
import copy
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from pathlib import Path
import pentachoron_exact as x
import check_edge_face_hinge as hinge

ROOT=hinge.ROOT;HOME=hinge.HOME;BASE=hinge.BASE
CONTRACT=HOME/'contracts/hinge-phase-continuation.v1.json'
PROOF=HOME/'HINGE-PHASE-CONTINUATION.md'
RESULT=HOME/'results/hinge-phase-continuation.v1.json'
PRODUCER=BASE/'checkers/check_electron_tetrahedral_spinor.py'
ALGEBRA=BASE/'checkers/check_electron_charge_spin_frontier.py'
STORE=BASE/'results/electron_tetrahedral_spinor_store.json'
OWNER=BASE/'results/electron_tetrahedral_spinor.json'
F,mm,adj,eye,add=x.F,x.mm,x.adjoint,x.eye,x.add


def root(mask):return F(tuple(Q(int(i==mask)) for i in range(16)))
SQ2,SQ3,SQ6,IM=root(1),root(2),root(3),root(8)
def scale(c,A):return [[c*v for v in row] for row in A]
def blockdiag(blocks):
    size=sum(len(b) for b in blocks);out=[[F() for _ in range(size)] for _ in range(size)];k=0
    for B in blocks:
        for i,row in enumerate(B):
            for j,v in enumerate(row):out[k+i][k+j]=v
        k+=len(B)
    return out

def tensor(A,B):return [[a*b for a in rowA for b in rowB] for rowA in A for rowB in B]
def decode(z):
    (a,b),(c,d)=z
    return F(Q(a))+F(Q(b))*SQ3+IM*(F(Q(c))+F(Q(d))*SQ3)

def source_group():
    # Execute only the producer's three group-declaration statements and its
    # two standalone arithmetic functions. Never call a producer entrypoint.
    tree=ast.parse(PRODUCER.read_text(encoding='utf-8'))
    main=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='main')
    start=next(i for i,n in enumerate(main.body) if isinstance(n,ast.Assign)
               and any(isinstance(t,ast.Name) and t.id=='quats' for t in n.targets))
    nodes=main.body[start:start+3]
    assert isinstance(nodes[1],ast.For) and isinstance(nodes[2],ast.Expr)
    assert isinstance(nodes[2].value,ast.Call) and isinstance(nodes[2].value.func,ast.Attribute)
    assert nodes[2].value.func.attr=='update' and nodes[2].value.func.value.id=='quats'
    arithmetic=ast.parse(ALGEBRA.read_text(encoding='utf-8'))
    funcs=[n for n in arithmetic.body if isinstance(n,ast.FunctionDef) and n.name in ('qm','spin')]
    assert len(funcs)==2
    env={'F':Q,'product':product}
    exec(compile(ast.Module(body=nodes+funcs,type_ignores=[]),str(PRODUCER),'exec'),env)
    return env['quats'],env['qm'],env['spin']

def from_spin(spin,q):return [[F(a)+IM*F(b) for a,b in row] for row in spin(q)]
def pauli(v):
    a,b,c=v
    return [[c,a-IM*b],[a+IM*b,-c]]
SIGMA=[pauli([F(int(i==j)) for i in range(3)]) for j in range(3)]
def spatial(U):
    R=[[F() for _ in range(3)] for _ in range(3)]
    for j,S in enumerate(SIGMA):
        V=mm(mm(U,S),adj(U))
        coords=[(V[0][1]+V[1][0])/2,(V[1][0]-V[0][1])/(2*IM),V[0][0]]
        assert pauli(coords)==V
        for i in range(3):R[i][j]=coords[i]
    return R

def validate_contract(c):
    assert c['schema']=='marici.scattering.hinge-phase-continuation.v1'
    assert c['finite_word_class']==['L','G=N','N','24_binary_tetrahedral_actions']
    assert c['herald_success_probability']=='3/8'
    for key in ('all_source_implementations_excluded','continuous_generator_native_licensed',
                'controller_preparation_native_licensed','controlled_selector_native_licensed',
                'moving_face_adapter_native_licensed','herald_probability_is_annihilation_probability',
                'capture_release_law_derived','outgoing_photon_factorization_constructed',
                'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=hinge.build();assert parent==json.loads(hinge.RESULT.read_text(encoding='utf-8')),'stale EF1 geometry'
    owner_before={path:path.read_bytes() for path in (STORE,OWNER)}
    raw=json.loads(owner_before[STORE]);P=[[[decode(z) for z in row] for row in B] for B in raw['face_projectors']]
    I=eye(2);K=[row for B in P for row in B]
    assert len(P)==4 and mm(adj(K),K)==scale(F(2),I)
    assert all(mm(B,B)==B and adj(B)==B for B in P)
    N=scale(F(Q(1,2)),mm(K,adj(K)));L=blockdiag(P)
    stages={name:[[F() for _ in range(8)] for _ in range(8)] for name in ('L','G','N')};seen=set()
    for arrow in raw['arrows']:
        name,i,j=arrow['stage'],arrow['target'],arrow['source'];key=(name,i,j)
        assert key not in seen and name in stages and 0<=i<8 and 0<=j<8
        seen.add(key);stages[name][i][j]=decode(arrow['weight'])
    assert stages=={'L':L,'G':N,'N':N} and len(seen)==144
    assert mm(L,K)==mm(N,K)==K and mm(N,N)==N
    quats,qm,spin=source_group();assert len(quats)==24
    assert all(qm(q,r) in quats for q in quats for r in quats)
    rotations=[];raw_actions={}
    for q in sorted(quats):
        assert sum(t*t for t in q)==1
        U=from_spin(spin,q);assert mm(adj(U),U)==I
        images=[mm(mm(U,B),adj(U)) for B in P];perm=[P.index(B) for B in images]
        T=[[U[i%2][j%2] if i//2==perm[j//2] else F() for j in range(8)] for i in range(8)]
        assert mm(T,K)==mm(K,U) and mm(adj(T),T)==eye(8)
        raw_actions[q]=T
        R=spatial(U)
        if R not in rotations:rotations.append(R)
    assert len(rotations)==12
    traces={sum(R[i][i] for i in range(3)) for R in rotations}
    assert traces=={F(-1),F(),F(3)}
    points={k:[F(v) for v in p] for k,p in hinge.POINTS.items()}
    for R in rotations:
        assert {tuple(row[0] for row in mm(R,[[v] for v in p])) for p in points.values()}=={tuple(p) for p in points.values()}
    stabilizer=[R for R in rotations if all(mm(R,[[v] for v in points[k]])==[[v] for v in points[k]] for k in 'AB')]
    assert stabilizer==[eye(3)]
    E1=from_spin(spin,(Q(),Q(1),Q(),Q()));E2=from_spin(spin,(Q(),Q(),Q(1),Q()))
    A=scale(F(-1),add(E1,E2));Un=add(scale(F(2),I),A);U=scale(F(1)/SQ6,Un)
    assert adj(A)==scale(F(-1),A) and mm(A,A)==scale(F(-2),I)
    assert mm(adj(U),U)==I and U==scale(F(1)/SQ6,from_spin(spin,(Q(2),Q(-1),Q(-1),Q())))
    R=spatial(U);expected=[[Q(1,3),Q(-2,3),Q(2,3)],[Q(2,3),Q(2,3),Q(1,3)],[Q(-2,3),Q(1,3),Q(2,3)]]
    assert R==[[F(v) for v in row] for row in expected]
    assert sum(R[i][i] for i in range(3))==F(Q(5,3)) and R not in rotations
    # Same affine hinge as EF1, using the actual Pauli/source convention.
    M=hinge.mean([tuple(points['A']),tuple(points['B'])])
    def moved(point):return tuple(row[0]+m for row,m in zip(mm(R,[[v-m] for v,m in zip(point,M)]),M))
    assert moved(points['A'])==tuple(points['A']) and moved(points['B'])==tuple(points['B'])
    assert moved(points['C'])==tuple(points['D'])
    Pnew=[mm(mm(U,B),adj(U)) for B in P];Knew=[row for B in Pnew for row in B]
    V=blockdiag([U]*4);Nnew=scale(F(Q(1,2)),mm(Knew,adj(Knew)))
    assert mm(adj(Knew),Knew)==scale(F(2),I)
    assert mm(Knew,U)==mm(V,K) and mm(mm(V,N),adj(V))==Nnew and Nnew!=N
    # Explicit additional coherent controller. Payload gates themselves are native.
    prep=[[F(1)/SQ2,F(1)/SQ2,F()],[F(Q(1,2)),F(Q(-1,2)),F(1)/SQ2],
          [F(Q(1,2)),F(Q(-1,2)),-F(1)/SQ2]]
    assert mm(adj(prep),prep)==eye(3)
    select=blockdiag([I,scale(F(-1),E1),scale(F(-1),E2)])
    W=mm(mm(tensor(adj(prep),I),select),tensor(prep,I));assert mm(adj(W),W)==eye(6)
    payloads=[(Q(1),Q(),Q(),Q()),(Q(),Q(-1),Q(),Q()),(Q(),Q(),Q(-1),Q())]
    raw_select=blockdiag([raw_actions[q] for q in payloads])
    Wraw=mm(mm(tensor(adj(prep),eye(8)),raw_select),tensor(prep,eye(8)))
    assert mm(adj(Wraw),Wraw)==eye(24)
    code=tensor(eye(3),K);assert mm(Wraw,code)==mm(code,W)
    kraus=[[row[:2] for row in W[2*j:2*j+2]] for j in range(3)]
    assert kraus[0]==scale(F(Q(1,4)),Un) and kraus[1]==scale(F(Q(1,4)),adj(Un))
    assert kraus[2]==scale(F(1)/(2*SQ2),add(E2,scale(F(-1),E1)))
    probs=[Q(3,8),Q(3,8),Q(1,4)]
    assert all(mm(adj(B),B)==scale(F(prob),I) for B,prob in zip(kraus,probs))
    # Countermodels for a separate face-contact mixer; no photon identity given.
    capture_examples={}
    for t in (Q(),Q(1,2),Q(1)):
        a,b=(1-t*t)/(1+t*t),2*t/(1+t*t);C=[[F(a),F(-b)],[F(b),F(a)]]
        assert mm(adj(C),C)==I
        assert mm(tensor(U,I),tensor(I,C))==mm(tensor(I,C),tensor(U,I))
        capture_examples[str(t)]=str(b*b)
    refused=[]
    for key in ('all_source_implementations_excluded','controller_preparation_native_licensed',
                'moving_face_adapter_native_licensed','herald_probability_is_annihilation_probability',
                'capture_release_law_derived','physical_outcomes_admitted'):
        bad=copy.deepcopy(c);bad[key]=True
        try:validate_contract(bad)
        except AssertionError:refused.append(key)
        else:raise AssertionError('unsupported phase-continuation promotion: '+key)
    assert all(path.read_bytes()==data for path,data in owner_before.items())
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((hinge.RESULT,PRODUCER,ALGEBRA,STORE,OWNER,CONTRACT,PROOF,Path(__file__),Path(x.__file__),
                  HOME/'test_hinge_phase_continuation.py'))
    old=json.loads(owner_before[OWNER])
    return {'schema':'marici.scattering.hinge-phase-continuation-receipt.v1','status':'pass',
        'scope_verdict':'finite_word_obstruction_and_conditional_phase_lift_not_native_capture',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'actual_stored_stage_entries_verified':144,
        'source_group_order':24,'projected_group_order':12,'projected_trace_values':['-1','0','3'],
        'pointwise_AB_stabilizer_order':1,'hinge_spatial_trace':'5/3','finite_protocol_word_hinge_excluded':True,
        'hinge_spinor':x.encoded(U),'hinge_spatial_rotation':[[str(v) for v in row] for row in expected],
        'source_convention_quaternion_numerator':['2','-1','-1','0'],'quaternion_denominator':'sqrt(6)',
        'moving_frame_intertwining_verified':True,'moving_frame_changes_native_projector':True,
        'full_raw_controller_unitary_dimension':24,'raw_logical_controller_intertwining_verified':True,
        'conditional_controller_preparation':x.encoded(prep),'conditional_herald_kraus':[x.encoded(B) for B in kraus],
        'conditional_herald_probabilities':[str(v) for v in probs],
        'all_failure_records_retained':True,'conditional_logical_hinge_gate_constructed':True,
        'face_mixer_capture_counterexamples':capture_examples,
        'native_producer_called':False,'owner_files_unchanged':True,
        'owner_producer_hash_matches_current':old['checker_sha256']==hashlib.sha256(PRODUCER.read_bytes()).hexdigest(),
        'historical_ancestor_freshness_claimed':False,'all_source_implementations_excluded':False,
        'continuous_generator_native_licensed':False,'controller_preparation_native_licensed':False,
        'controlled_selector_native_licensed':False,'moving_face_adapter_native_licensed':False,
        'herald_probability_is_annihilation_probability':False,'capture_release_law_derived':False,
        'outgoing_photon_factorization_constructed':False,'analytic_argument_machine_formalized':False,
        'new_live_proposition_admitted':False,'C12_protocol_renewed':False,'high_energy_protocol_executed':False,
        'physical_outcomes_admitted':False,'unsupported_promotions_refused':refused}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale hinge phase continuation'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','finite_protocol_word_hinge_excluded',
        'moving_frame_intertwining_verified','conditional_herald_probabilities','face_mixer_capture_counterexamples',
        'owner_producer_hash_matches_current','capture_release_law_derived')}))


if __name__=='__main__':main()
