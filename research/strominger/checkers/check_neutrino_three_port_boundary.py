"""Conditional source-normal1-to3 boundary instrument, not a neutrino identification.
Exact standard-library field arithmetic. No native producer or proof source runs.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product as cartesian
from pathlib import Path
import json
import sys

from assemble_metric_coefficient_protocol import (
    ROOT, A, ZERO, ONE, plus, scaled, product, integer_trace, encode, assemble)
from check_packet_stage_cost_comparison import source_electron_factors
from check_port_incidence_conjectures import transpose, identity, pivot_columns
from electron_packet_interface import ACTIONS, I as SPIN_I, gmm

CONTRACT=ROOT/'research/strominger/contracts/neutrino-three-port-boundary-construction.v1.json'
OUT=ROOT/'research/strominger/results/neutrino-three-port-boundary-v1.json'
STORE=ROOT/'research/voevodsky/results/electron_tetrahedral_spinor_store.json'
S2=A(tuple(F(i==1) for i in range(16)))
S3=A(tuple(F(i==2) for i in range(16)))
CI=A(tuple(F(i==8) for i in range(16)))
I2=identity(2)


def digest(p):return sha256(p.read_bytes()).hexdigest()

def subtract(a,b):return plus(a,scaled(-ONE,b))

def trace(a):return sum((v for (i,j),v in a.items() if i==j),ZERO)

def from_spin(U):
    return {(i,j):A(U[i][j][0])+CI*U[i][j][1]
            for i in range(2) for j in range(2) if U[i][j]!=(F(0),F(0))}


def stack(blocks):
    return {(2*k+i,j):x for k,b in enumerate(blocks) for (i,j),x in b.items()}


def block_diagonal(blocks):
    return {(2*k+i,2*k+j):x for k,b in enumerate(blocks) for (i,j),x in b.items()}


def channel(Aj,rho):return product(Aj,product(rho,transpose(Aj,True)))


def dot(a,b):return sum((x*y for x,y in zip(a,b)),ZERO)


def det3(R):
    return sum((R[0,p[0]]*R[1,p[1]]*R[2,p[2]]*s for p,s in
        (((0,1,2),1),((1,2,0),1),((2,0,1),1),((0,2,1),-1),((1,0,2),-1),((2,1,0),-1))),ZERO)


def reject(f,text):
    try:f()
    except ValueError as e:assert text in str(e)
    else:raise AssertionError('accepted hostile '+text)


def main():
    contract=json.loads(CONTRACT.read_text(encoding='utf-8'))
    prior_path=ROOT/'research/strominger/results/electron-packet-extraction-v1.json'
    prior=json.loads(prior_path.read_text(encoding='utf-8'))
    assert prior['status']=='pass' and all(prior['checks'].values())
    pins=dict(prior['source_sha256'])
    assert all(digest(ROOT/p)==h for p,h in pins.items()),'stale source'
    pins[prior_path.relative_to(ROOT).as_posix()]=digest(prior_path)
    for module in tuple(sys.modules.values()):
        file=getattr(module,'__file__',None)
        if file:
            p=Path(file).resolve()
            if p.is_relative_to(ROOT/'research') and p.suffix=='.py':
                key=p.relative_to(ROOT).as_posix()
                assert key not in pins or pins[key]==digest(p)
                pins[key]=digest(p)
    for p in (CONTRACT,STORE,Path(__file__).resolve()):
        pins[p.relative_to(ROOT).as_posix()]=digest(p)
    store=json.loads(STORE.read_text(encoding='utf-8'))
    K4,D4=source_electron_factors()
    assert product(D4,K4)==I2
    oldN=product(K4,D4)
    P=[{(i,j):K4[2*f+i,j] for i in range(2) for j in range(2) if (2*f+i,j) in K4} for f in range(4)]
    normals=[tuple(A(F(x[0]))+S3*F(x[1]) for x in n) for n in store['normals']]
    vertices=[tuple(-3*x for x in n) for n in normals]
    sigma=({(0,1):ONE,(1,0):ONE},{(0,1):-CI,(1,0):CI},{(0,0):ONE,(1,1):-ONE})
    for f in range(4):
        assert product(P[f],P[f])==P[f]==transpose(P[f],True)
        assert integer_trace(P[f])==1 and dot(normals[f],normals[f])==ONE
        H=plus(*(scaled(normals[f][a],sigma[a]) for a in range(3)))
        assert P[f]==scaled(A(F(1,2)),subtract(I2,H))
        assert product(H,P[f])==scaled(-ONE,P[f])
        for j in range(4):
            assert trace(product(P[f],P[j]))==(ONE if f==j else A(F(1,3)))
            assert dot(normals[f],vertices[j])==(A(-3) if f==j else ONE)
    assert plus(*P)==scaled(A(2),I2)
    assert product(transpose(K4,True),K4)==scaled(A(2),I2)

    U=[from_spin(u) for u in ACTIONS]
    permutations=[];rotations=[]
    for u in U:
        perm=[]
        for p in P:
            image=product(u,product(p,transpose(u,True)))
            perm.append(next(i for i,q in enumerate(P) if q==image))
        assert sorted(perm)==list(range(4))
        permutations.append(tuple(perm))
        R={(a,b):sum((normals[perm[f]][a]*normals[f][b]*F(3,4) for f in range(4)),ZERO)
           for a in range(3) for b in range(3)}
        R={k:x for k,x in R.items() if x!=ZERO}
        assert product(transpose(R),R)==identity(3) and det3({(a,b):R.get((a,b),ZERO) for a in range(3) for b in range(3)})==ONE
        for f in range(4):
            assert tuple(sum((R.get((a,b),ZERO)*normals[f][b] for b in range(3)),ZERO) for a in range(3))==normals[perm[f]]
        rotations.append(R)
    assert len(set(permutations))==12

    variants={};objects={}
    for omitted in range(4):
        kept=tuple(f for f in range(4) if f!=omitted)
        P0=P[omitted];Q0=subtract(I2,P0)
        S=subtract(scaled(A(2),I2),P0)
        R=plus(P0,scaled(ONE/S2,Q0))
        assert product(R,product(S,R))==I2 and transpose(R,True)==R
        maps=[product(P[f],R) for f in kept]
        V=stack(maps);D=transpose(V,True);N=product(V,D)
        assert product(D,V)==I2
        assert product(N,N)==N==transpose(N,True) and integer_trace(N)==2
        for f,a in zip(kept,maps):
            assert product(P[f],a)==a and len(pivot_columns(a,2,2))==1
        compression=product(V,D4);recovery=product(K4,D)
        assert product(recovery,compression)==oldN
        assert product(compression,recovery)==N
        assert product(recovery,V)==K4
        L=block_diagonal([P[f] for f in kept])
        source={'schema':'marici.metric-coefficient-source.v1',
            'coordinates':[f'face{f}:spin{j}' for f in kept for j in range(2)],
            'metric':['1']*6,'local':encode(L),'alignment':encode(N),
            'provenance':{'native_store':STORE.relative_to(ROOT).as_posix(),
                'omitted_face':omitted,'normalizer':'P_o+(I-P_o)/sqrt(2)',
                'status':'conditional derived protocol, not physical particle selection'}}
        assembly=assemble(source)
        assert [assembly['measures'][k] for k in ('local_rank','alignment_rank','return_rank')]==[3,2,2]
        assert assembly['measures']['stage_transfer_supports']==[12,36,36]
        assert assembly['measures']['protocol_transfer_count']==84
        raw=stack([P[f] for f in kept])
        assert product(transpose(raw,True),raw)==S!=I2
        assert trace(product(P0,S))==ONE and trace(product(Q0,S))==A(2)
        dephased=[]
        for f,a in zip(kept,maps):
            output0=channel(a,P0);output1=channel(a,Q0)
            assert output0==output1==scaled(A(F(1,3)),P[f])
            assert trace(output0)==A(F(1,3))
            dephased.append(encode(output0))
        coherent0=channel(V,P0);coherent1=channel(V,Q0)
        assert coherent0!=coherent1
        assert channel(D,coherent0)==P0 and channel(D,coherent1)==Q0
        assert trace(product(P0,P0))==ONE and not product(P0,Q0)
        assert trace(P0)==trace(Q0)==ONE and product(P0,Q0)=={}
        stabilizer=[i for i,p in enumerate(permutations) if p[omitted]==omitted]
        assert len(stabilizer)==6 and len({permutations[i] for i in stabilizer})==3
        assert {p[omitted] for p in permutations}==set(range(4))
        for i in stabilizer:
            p=permutations[i]
            assert all(p[p[p[f]]]==f for f in kept)
        # Same ports permit different scalar coupling characters; these are
        # supplied rivals, not actual neutrino/electron charge measurements.
        for q in (0,-1):
            assert product(V,scaled(A(q),I2))==product(scaled(A(q),identity(6)),V)
        objects[omitted]={'V':V,'D':D,'N':N,'kept':kept,'R':R,'maps':maps}
        variants[str(omitted)]={'kept_faces':kept,'source_input_ports':1,'output_face_ports':3,
            'logical_complex_dimension':2,'raw_output_coordinates':6,'return_rank':2,
            'output_line_complex_codimension':1,'facet_real_codimension':1,
            'encoder':encode(V),'decoder':encode(D),'return_projector':encode(N),
            'old_raw8_compression':encode(compression),'old_raw8_recovery':encode(recovery),
            'normalizer':encode(R),'port_maps':[encode(a) for a in maps],
            'new_protocol':assembly,'fixed_mark_spin_stabilizer_indices':stabilizer,
            'source_omission_orbit':[0,1,2,3],
            'dephasing_hostile':{'input_densities':[encode(P0),encode(Q0)],
                'identical_three_flagged_output_blocks':dephased,
                'identical_port_probabilities':['1/3']*3,
                'omitted_face_reader_values':['1','0'],
                'coherent_states_distinct_and_recoverable':True},
            'omitted_normalizer_hostile':{'two_input_norm_weights':['1','2']}}

    transports={}
    for omitted in range(4):
        source=objects[omitted]
        for ui,u in enumerate(U):
            perm=permutations[ui];target_omitted=perm[omitted]
            target=objects[target_omitted]
            W={}
            for j,f in enumerate(source['kept']):
                k=target['kept'].index(perm[f])
                W.update({(2*k+a,2*j+b):x for (a,b),x in u.items()})
            assert product(transpose(W,True),W)==identity(6)
            assert product(W,source['V'])==product(target['V'],u)
            assert product(W,product(source['N'],transpose(W,True)))==target['N']
            old_action=product(K4,product(u,D4))
            assert product(W,product(source['V'],D4))==product(product(target['V'],D4),old_action)
            transports[omitted,ui]=(target_omitted,W)
    for omitted in range(4):
        for vi,ui in cartesian(range(24),repeat=2):
            middle,A1=transports[omitted,ui]
            target,A2=transports[middle,vi]
            composed_index=ACTIONS.index(gmm(ACTIONS[vi],ACTIONS[ui]))
            end,B=transports[omitted,composed_index]
            assert target==end and product(A2,A1)==B

    def fixed_mark_step(omitted,index):
        if permutations[index][omitted]!=omitted:
            raise ValueError('fixed mark not preserved')
        return transports[omitted,index]
    wrong=next(i for i,p in enumerate(permutations) if p[0]!=0)
    reject(lambda:fixed_mark_step(0,wrong),'fixed mark not preserved')
    minus=next(i for i,u in enumerate(U) if u==scaled(-ONE,I2))
    one=ACTIONS.index(SPIN_I)
    for omitted in range(4):
        assert permutations[minus]==permutations[one]
        assert transports[omitted,minus][1]==scaled(-ONE,identity(6))
        assert product(objects[omitted]['D'],product(transports[omitted,minus][1],objects[omitted]['V']))==scaled(-ONE,I2)
    # Retaining endpoint matrices is not a quotient of source execution words.
    u=wrong;v=ACTIONS.index(gmm(ACTIONS[u],ACTIONS[u]))
    endpoint=gmm(ACTIONS[v],ACTIONS[u])
    direct_word=(ACTIONS.index(endpoint),)
    composed_word=(u,v)
    assert direct_word!=composed_word
    assert gmm(ACTIONS[composed_word[1]],ACTIONS[composed_word[0]])==ACTIONS[direct_word[0]]

    checks={k:True for k in (
        'frozen_source_pins_and_actual_four_projectors',
        'source_normals_clifford_lines_and_dual_tetrahedron_facets',
        'four_positive_source_normalizers_and_three_rank_one_output_ports',
        'coherent_encoder_decoder_and_old_raw8_return_image_recovery',
        'four_changed_metric_protocols_ranks3_2_2_and_supports12_36_36',
        'all96_family_source_spin_and_raw_transport_squares',
        'all2304_family_compositions_preserve_source_words',
        'exactly_six_native_spin_actions_preserve_each_fixed_mark',
        'transitive_four_mark_orbit_forbids_invariant_single_omission',
        'wrong_fixed_mark_and_central_sign_erasure_hostiles',
        'omitting_tightening_breaks_norm_by_exact_one_vs_two',
        'orthogonal_inputs_have_identical_dephased_flagged_outputs',
        'coherent_output_recovers_the_distinct_omitted_face_reader',
        'same_port_maps_admit_neutral_and_charged_scalar_rivals')}
    assert all(digest(ROOT/p)==h for p,h in pins.items()),'source changed during check'
    report={'schema':'marici.neutrino-three-port-boundary-check.v1','status':'pass',
        'checks':checks,'variants':variants,'source_normal_geometry':{
            'normals':[[x.record() for x in n] for n in normals],
            'dual_vertices':[[x.record() for x in v] for v in vertices],
            'facet_vertex_incidence':[[j for j in range(4) if j!=f] for f in range(4)],
            'unit_plane_offset_is_reference_scale_not_physical':True},
        'spin_action_permutations':permutations,
        'transport_family':[{'source_omission':o,'spin_index':i,'target_omission':t,'matrix':encode(W)} for (o,i),(t,W) in sorted(transports.items())],
        'scope':'Conditional logical/source-facet1-to3 construction on an explicitly changed electron spinor fixture. Not a physical neutrino source.',
        'new_nonunitary_port_maps_are_supplied_derived_capabilities':True,
        'native24_fixed_interface_preserved':False,'coherent_full_image_recovery':True,
        'dephased_full_image_recovery':False,'source_invariant_omitted_face_selected':False,
        'neutral_charge_or_chirality_selected':False,'physical_neutrino_identified':False,
        'physical_spacetime_codimension_map_constructed':False,
        'native_producers_executed':False,'formal_proof_recompiled':False,
        'source_sha256':pins}
    OUT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','check_groups':len(checks),'omission_variants':4,
        'source_ports':[1,3],'new_stage_supports':[12,36,36],'new_protocol_total':84,
        'fixed_mark_native_spin_actions':6,'family_source_squares':96,'composition_equations':2304,
        'coherent_recovery':True,'dephased_recovery':False,'physical_neutrino_identified':False},indent=2))


if __name__=='__main__':main()
