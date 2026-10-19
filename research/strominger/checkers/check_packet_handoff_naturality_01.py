"""Iteration1: actual source-pair structure and limits of intrinsic handoff.
Exact projector algebra, native automorphisms and a full-reader countermodel.
"""
from fractions import Fraction as F
from itertools import product as cartesian
from pathlib import Path
from hashlib import sha256
import json
import sys

from assemble_metric_coefficient_protocol import ROOT,A,ZERO,ONE,read_operator,plus,scaled,product,sharp,integer_trace,encode
from check_port_incidence_conjectures import identity,transpose,factor
from check_neutrino_three_port_boundary import S2,CI,from_spin,source_electron_factors,ACTIONS,STORE
from check_neutrino_arrow_seed_science import rank
from assemble_relative_geometry import assemble as geo_assemble,apply
from electron_packet_interface import gmm,I as SPIN_I

CONTRACT=ROOT/'research/strominger/contracts/packet-handoff-naturality-01.v1.json'
OUT=ROOT/'research/strominger/results/packet-handoff-naturality-01-v1.json'
PRIOR=ROOT/'research/strominger/results/indexed-cycle-handoff-v1.json'
GEO_PATHS={'proton':ROOT/'research/voevodsky/inputs/relative-proton.json',
    'neutron':ROOT/'research/voevodsky/inputs/mode-neutron.json'}


def digest(p):return sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def minus(a,b):return plus(a,scaled(-ONE,b))
def witness(p):
    if not p:return {}
    j=min(j for i,j in p)
    return {(i,0):x for (i,k),x in p.items() if k==j}
def joint(L,G,N,n):return [N,minus(L,N),minus(G,N),plus(identity(n),scaled(-ONE,L),scaled(-ONE,G),N)]
def signature(q):return list(map(integer_trace,q))
def classifier(L,G,N):return {'nested_alignment':int(G==N),'return_multiplet':int(integer_trace(N)>1)}
def encode_joint(q):return [encode(x) for x in q]


def frame_control(L,G,N,n,metric):
    scales=[F(i+2,i+1) for i in range(n)]
    def change(m):return {(i,j):x*scales[i]/scales[j] for (i,j),x in m.items()}
    metric2=[metric[i]/scales[i]**2 for i in range(n)]
    changed=[change(m) for m in (L,G,N)]
    for p in changed:assert sharp(p,metric2)==p
    assert signature(joint(*changed,n))==signature(joint(L,G,N,n))
    assert classifier(*changed)==classifier(L,G,N)
    return {'scales':list(map(str,scales)),'changed_metric':list(map(str,metric2)),
        'joint_signature_and_classifiers_preserved':True}


def geometric_group(path):
    source=read(path);geometry=geo_assemble(source)
    points=[tuple(map(F,p)) for p in geometry['vertices']];lookup={p:i for i,p in enumerate(points)}
    gens=[]
    for raw in source['generators']:
        g=(tuple(tuple(map(F,row)) for row in raw['matrix']),tuple(map(F,raw['translation'])))
        gens.append(tuple(lookup[apply(g,p)] for p in points))
    unit=tuple(range(len(points)));found={unit};front=[unit]
    while front:
        p=front.pop()
        for g in gens:
            q=tuple(g[p[i]] for i in range(len(points)))
            if q not in found:found.add(q);front.append(q)
        assert len(found)<=24
    return {'vertex_count':len(points),'source_generator_permutations':gens,'generated_group_size':len(found)}


def source_pairs():
    previous=read(PRIOR)
    assert previous['status']=='pass' and all(previous['checks'].values())
    pins=dict(previous['source_sha256'])
    assert all(digest(ROOT/p)==h for p,h in pins.items()),'stale source comparison'
    pins[PRIOR.relative_to(ROOT).as_posix()]=digest(PRIOR)
    expected={'proton':[1,11,2,22],'neutron':[1,2,11,22],'electron':[2,2,0,4]}
    rows={};objects={}
    # Truth-table certificate for the four joint projections in the quotient
    # algebra L^2=L,G^2=G,LG=GL, whose actual source relations are checked below.
    for l,g in cartesian((0,1),repeat=2):
        q=[l*g,l*(1-g),(1-l)*g,(1-l)*(1-g)]
        assert sum(q)==1 and all(q[i]*q[j]==(q[i] if i==j else 0) for i,j in cartesian(range(4),repeat=2))
    for name in expected:
        path=ROOT/f'research/strominger/results/common-three-carrier-protocol/{name}.json'
        source=read(path);pins[path.relative_to(ROOT).as_posix()]=digest(path)
        n=len(source['source']['metric']);metric=tuple(map(F,source['source']['metric']))
        L,G,N=[read_operator(source['operators'][s],n) for s in 'LGN']
        assert product(L,L)==L and product(G,G)==G
        assert product(L,G)==product(G,L)==N
        for p in (L,G,N):assert sharp(p,metric)==p
        q=joint(L,G,N,n)
        assert plus(*q)==identity(n) and signature(q)==expected[name]
        eigs=[(1,1),(1,0),(0,1),(0,0)];examples=[]
        for p,(ell,gee) in zip(q,eigs):
            assert sharp(p,metric)==p
            v=witness(p)
            if v:
                assert product(L,v)==scaled(A(ell),v) and product(G,v)==scaled(A(gee),v)
            examples.append(encode(v))
        f=factor(N,n,metric);K=f['K']
        # Entire generated algebra span: I,L,G,N all act identically here.
        assert all(product(p,K)==K for p in (identity(n),L,G,N))
        flags=classifier(L,G,N)
        assert flags=={'nested_alignment':int(name=='electron'),'return_multiplet':int(name=='electron')}
        for index,stage in ((1,L),(2,G)):
            v=witness(q[index])
            if v:assert product(stage,v)==v and not product(N,v)
        rows[name]={'source':path.relative_to(ROOT).as_posix(),
            'joint_order':['both','local_only','alignment_only','neither'],
            'joint_dimensions':signature(q),'joint_sector_witnesses':examples,
            'alignment_alone_equals_return':G==N,'local_alone_equals_return':L==N,
            'two_frame_natural_mode_predicates':flags,
            'coefficient_frame_control':frame_control(L,G,N,n,metric)}
        objects[name]=(L,G,N,n,metric,q,f)
    p=rows['proton']['joint_dimensions'];n=rows['neutron']['joint_dimensions']
    assert p==[n[0],n[2],n[1],n[3]]
    geometry={name:geometric_group(path) for name,path in GEO_PATHS.items()}
    assert geometry['proton']['generated_group_size']==12 and geometry['neutron']['generated_group_size']==3
    for path in GEO_PATHS.values():pins[path.relative_to(ROOT).as_posix()]=digest(path)
    return rows,objects,geometry,pins


def automorphism_control(obj):
    L,G,N,n,metric,q,f=obj
    assert n==8 and metric==(F(1),)*8
    K,D=source_electron_factors();E=scaled(ONE/S2,K)
    assert product(transpose(E,True),E)==identity(2)
    assert product(E,transpose(E,True))==N
    X={(0,1):ONE,(1,0):ONE};Z={(0,0):ONE,(1,1):-ONE}
    native=[from_spin(u) for u in ACTIONS]
    P=[{(i,j):K[2*f+i,j] for i in range(2) for j in range(2) if (2*f+i,j) in K} for f in range(4)]
    rotations=[];selected=(scaled(-CI,X),scaled(-CI,Z))
    assert all(u in native for u in selected)
    full_dormant_alignment=plus(G,q[3])
    assert product(L,full_dormant_alignment)==N
    for u in native:
        perm=[next(i for i,p in enumerate(P) if product(u,product(p0,transpose(u,True)))==p) for p0 in P]
        W={}
        for source,target in enumerate(perm):
            W.update({(2*target+a,2*source+b):x for (a,b),x in u.items()})
        assert product(transpose(W,True),W)==identity(8)
        assert product(W,E)==product(E,u)
        for p in (L,G,N,full_dormant_alignment):assert product(W,p)==product(p,W)
        if u in selected:rotations.append({'logical':encode(u),'face_permutation':perm,'raw':encode(W)})
    assert len(rotations)==2
    assert product(scaled(-CI,X),scaled(-CI,Z))==scaled(-ONE,product(scaled(-CI,Z),scaled(-CI,X)))
    # Commutator constraints for a general2x2 matrix with X and Z; scalar
    # factors -i do not change their commutants. Rank3 leaves only span(I).
    commutator=[]
    for B in (((0,1),(1,0)),((1,0),(0,-1))):
        for i,j in cartesian(range(2),repeat=2):
            commutator.append([F((int(i==a)*B[b][j])-(B[i][a]*int(b==j))) for a,b in cartesian(range(2),repeat=2)])
    assert rank(commutator)==3
    half=scaled(A(F(1,2)),identity(2))
    assert integer_trace(half)==1 and product(half,half)!=half
    # There is no rescue by letting the full native group permute two labels:
    # all order-three elements map trivially to S2, and they generate all24.
    order_three=[i for i,u in enumerate(ACTIONS) if gmm(gmm(u,u),u)==SPIN_I and u!=SPIN_I]
    unit=ACTIONS.index(SPIN_I);generated={unit};front=[unit]
    while front:
        p=front.pop()
        for g in order_three:
            j=ACTIONS.index(gmm(ACTIONS[g],ACTIONS[p]))
            if j not in generated:generated.add(j);front.append(j)
    assert len(generated)==24
    return {'native_noncommuting_automorphisms':rotations,'logical_commutator_constraint':commutator,
        'commutant_dimension':1,'nontrivial_natural_rank_one_sector_projector_exists':False,
        'order_three_native_elements':order_three,'group_generated_by_order_three_elements':len(generated),
        'nontrivial_full_native_group_action_on_two_labels_exists':False,
        'whole_dormant_alignment_extension_preserves_all_native_actions':24,
        'scope':'Pair-only natural endomorphisms, and labelled/unlabelled rank-one payload sector partitions equivariant under the full retained electron group. Not a ban on additional source context or geometric ports.'}


def dormant_control(obj):
    L,G,N,n,metric,q,f=obj
    v=witness(q[3]);assert v and not product(L,v) and not product(G,v)
    row={(0,i):x.flip(8)*metric[i] for (i,j),x in v.items()}
    length=product(row,v)[0,0];assert length!=ZERO
    P=scaled(ONE/length,product(v,row))
    assert product(P,P)==P and sharp(P,metric)==P and integer_trace(P)==1
    assert not product(L,P) and not product(G,P)
    G2=plus(G,P)
    assert product(G2,G2)==G2 and sharp(G2,metric)==G2
    assert product(L,G2)==product(G2,L)==N
    assert signature(joint(L,G2,N,n))==[2,2,1,3]
    assert classifier(L,G,N)=={'nested_alignment':1,'return_multiplet':1}
    assert classifier(L,G2,N)=={'nested_alignment':0,'return_multiplet':1}
    assert product(G2,v)==v and not product(G,v)
    assert not product(N,v)
    assert product(G2,f['K'])==product(G,f['K'])==f['K']
    Gall=plus(G,q[3])
    assert product(Gall,Gall)==Gall and sharp(Gall,metric)==Gall
    assert product(L,Gall)==product(Gall,L)==N
    assert signature(joint(L,Gall,N,n))==[2,2,4,0]
    assert classifier(L,Gall,N)=={'nested_alignment':0,'return_multiplet':1}
    return {'dormant_input':encode(v),'added_rank_one_alignment_projection':encode(P),
        'changed_alignment':encode(G2),'changed_joint_dimensions':[2,2,1,3],
        'original_mode_predicates':classifier(L,G,N),'changed_mode_predicates':classifier(L,G2,N),
        'same_active_return_operator':True,'same_active_metric_and_stage_action':True,
        'same_full_preparation_readers':False,
        'original_G_reader_on_witness':'0','changed_G_reader_on_witness':'v',
        'changed_source_is_native_original':False,
        'whole_dormant_extension':{'alignment':encode(Gall),'joint_dimensions':[2,2,4,0],
            'same_active_return':True,'all24_original_native_spin_face_actions_preserved':True,
            'same_full_preparation_readers':False}}


def generic_relation_controls():
    examples={}
    for sizes in cartesian(range(4),repeat=4):
        a,b,c,d=sizes;n=sum(sizes)
        if a==0 or n>6:continue
        L={};G={};offset=0
        for label,count in enumerate(sizes):
            for i in range(offset,offset+count):
                if label in (0,1):L[i,i]=ONE
                if label in (0,2):G[i,i]=ONE
            offset+=count
        N=product(L,G)
        assert product(G,L)==N and signature(joint(L,G,N,n))==list(sizes)
        relation=('equal' if not b and not c else 'alignment_inside_local' if not c else 'local_inside_alignment' if not b else 'incomparable')
        examples.setdefault(relation,{'joint_dimensions':sizes,'local':encode(L),'alignment':encode(G)})
    assert set(examples)=={'equal','alignment_inside_local','local_inside_alignment','incomparable'}
    return examples


def serial(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [serial(v) for v in x]
    return x


def main():
    contract=read(CONTRACT)
    rows,objects,geometry,pins=source_pairs()
    auto=automorphism_control(objects['electron'])
    dormant=dormant_control(objects['electron'])
    alternatives=generic_relation_controls()
    checks={name:True for name in (
        'fresh_actual_source_projection_and_metric_relations',
        'four_joint_sectors_certified_by_boolean_projector_algebra_and_witnesses',
        'exact_joint_dimensions_one_eleven_two_and_dual_plus_nested_doublet',
        'baryon_ordered_pair_duality_without_full_source_group_identification',
        'electron_alignment_alone_equals_return_baryons_need_both_constraints',
        'all_pair_generated_operators_are_scalar_on_active_return',
        'actual_native_electron_noncommuting_pair_automorphisms',
        'scalar_commutant_excludes_intrinsic_rank_one_payload_sector_split',
        'native_order_three_generation_excludes_two_label_permutation_rescue',
        'two_distinct_frame_natural_predicates_fit_all_three_handoff_modes',
        'actual_dormant_rank_one_alignment_extension_keeps_return_fixed',
        'predicates_disagree_without_changing_active_payload_metric_or_action',
        'whole_dormant_extension_preserves_full_native_group_but_changes_preparation',
        'active_reader_equivalence_is_not_full_preparation_task_equivalence',
        'transported_source_metrics_preserve_joint_structure_and_predicates',
        'generic_projection_axioms_admit_four_relation_types_not_three_species',
        'pair_only_limits_do_not_settle_richer_source_naturality')}
    for path in (CONTRACT,STORE,Path(__file__).resolve()):pins[path.relative_to(ROOT).as_posix()]=digest(path)
    for module in tuple(sys.modules.values()):
        file=getattr(module,'__file__',None)
        if file:
            p=Path(file).resolve()
            if p.is_relative_to(ROOT/'research') and p.suffix=='.py':pins[p.relative_to(ROOT).as_posix()]=digest(p)
    assert all(digest(ROOT/p)==h for p,h in pins.items()),'source changed during check'
    report={'schema':'marici.packet-handoff-naturality-iteration-check.v1','status':'pass',
        'iteration':1,'checks':checks,'source_pair_census':rows,'actual_baryon_geometric_groups':geometry,
        'electron_automorphism_obstruction':auto,'dormant_alignment_countermodel':dormant,
        'other_projection_pair_relations':alternatives,
        'source_intrinsic_preparation_redundancy_distinction_constructed':True,
        'unique_handoff_mode_selected_by_projection_pair':False,
        'intrinsic_active_payload_M_C_partition_constructed':False,
        'full_source_geometry_identified_by_joint_signature':False,
        'physical_particle_assignment_verified':False,'source_native_handoff_constructed':False,
        'next_executable_scope':contract['next_executable_scope'],
        'formal_proof_recompiled':False,'source_sha256':pins}
    OUT.write_text(json.dumps(serial(report),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','iteration':1,'check_groups':len(checks),
        'joint_dimensions':{name:row['joint_dimensions'] for name,row in rows.items()},
        'alignment_alone_equals_return':{name:row['alignment_alone_equals_return'] for name,row in rows.items()},
        'electron_native_equivariant_payload_split':False,'unique_source_selected_handoff':False,
        'dormant_extension_preserves_active_return':True,'full_source_continuation_executable':True},indent=2))


if __name__=='__main__':main()
