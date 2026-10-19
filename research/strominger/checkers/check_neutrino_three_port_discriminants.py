"""Source complement and rotation/flavor discriminants; no physical identification."""
from itertools import product as cartesian, permutations as all_permutations
from pathlib import Path
import json
from check_neutrino_three_port_boundary import (
    ROOT,A,F,ZERO,ONE,S2,CI,I2,ACTIONS,from_spin,product,transpose,
    plus,scaled,subtract,stack,block_diagonal,identity,trace,assemble,
    source_electron_factors,digest,encode,pivot_columns)

CONTRACT=ROOT/'research/strominger/contracts/neutrino-three-port-discriminants.v1.json'
OUT=ROOT/'research/strominger/results/neutrino-three-port-discriminants-v1.json'


def main():
    contract=json.loads(CONTRACT.read_text(encoding='utf-8'))
    path=ROOT/contract['prerequisite']
    prior=json.loads(path.read_text(encoding='utf-8'))
    assert prior['status']=='pass' and len(prior['checks'])==14 and all(prior['checks'].values())
    pins=dict(prior['source_sha256'])
    assert all(digest(ROOT/p)==h for p,h in pins.items()),'stale source'
    for p in (CONTRACT,path,Path(__file__).resolve()):pins[p.relative_to(ROOT).as_posix()]=digest(p)
    K4,D4=source_electron_factors()
    P=[{(i,j):K4[2*f+i,j] for i in range(2) for j in range(2) if (2*f+i,j) in K4} for f in range(4)]
    Q=[subtract(I2,p) for p in P]
    U=[from_spin(u) for u in ACTIONS]
    perms=prior['spin_action_permutations']
    assert plus(*Q)==scaled(A(2),I2)
    for f in range(4):
        H=subtract(I2,scaled(A(2),P[f]))
        assert product(H,P[f])==scaled(-ONE,P[f])
        assert product(H,Q[f])==Q[f]
        assert product(Q[f],Q[f])==Q[f]==transpose(Q[f],True)
        assert trace(Q[f])==ONE and not product(P[f],Q[f])
        for g in range(4):assert trace(product(Q[f],Q[g]))==(ONE if f==g else A(F(1,3)))
    objects={};rows={}
    for omitted in range(4):
        kept=tuple(f for f in range(4) if f!=omitted)
        R=plus(Q[omitted],scaled(ONE/S2,P[omitted]))
        maps=[product(Q[f],R) for f in kept]
        V=stack(maps);D=transpose(V,True);N=product(V,D)
        assert product(D,V)==I2
        assert product(product(K4,D),product(V,D4))==product(K4,D4)
        L=block_diagonal([Q[f] for f in kept])
        source={'schema':'marici.metric-coefficient-source.v1',
            'coordinates':[f'complement_face{f}:spin{j}' for f in kept for j in range(2)],
            'metric':['1']*6,'local':encode(L),'alignment':encode(N),
            'provenance':{'source':'canonical complements I-P_f of retained projectors','omitted':omitted}}
        assembly=assemble(source)
        assert assembly['measures']['stage_transfer_supports']==[12,36,36]
        assert [assembly['measures'][k] for k in ('local_rank','alignment_rank','return_rank')]==[3,2,2]
        objects[omitted]={'kept':kept,'V':V}
        rows[str(omitted)]={'encoder':encode(V),'decoder':encode(D),'normalizer':encode(R),
            'opposite_normal_eigenvalue':1,'source_recovery':True,'new_protocol':assembly}
    for omitted in range(4):
        for ui,u in enumerate(U):
            target=perms[ui][omitted];source=objects[omitted];dest=objects[target]
            W={}
            for j,f in enumerate(source['kept']):
                k=dest['kept'].index(perms[ui][f])
                W.update({(2*k+a,2*j+b):x for (a,b),x in u.items()})
            assert product(W,source['V'])==product(dest['V'],u)
            for f in range(4):
                assert product(u,product(Q[f],transpose(u,True)))==Q[perms[ui][f]]
    # A source three-cycle cannot intertwine with a trivial three-label action.
    omitted=0;kept=objects[omitted]['kept']
    ui=next(i for i,p in enumerate(perms) if p[omitted]==omitted and all(p[f]!=f for f in kept))
    p=perms[ui];failures=[]
    for labels in all_permutations(range(3)):
        assignment=dict(zip(kept,labels))
        residual=[f for f in kept if assignment[p[f]]!=assignment[f]]
        assert len(residual)==3
        failures.append({'labels_in_kept_order':labels,'nonintertwining_faces':residual})
    # Exact commutant computation over the source field. Two actual quaternion
    # generators suffice, and scalar identity is independently in the kernel.
    from electron_packet_interface import E
    equations={};row=0
    for e in E[:2]:
        e=from_spin(e)
        commutators=[]
        for a,b in cartesian(range(2),repeat=2):
            basis={(a,b):ONE}
            commutators.append(subtract(product(e,basis),product(basis,e)))
        for i,j in cartesian(range(2),repeat=2):
            for col,C in enumerate(commutators):
                if (i,j) in C:equations[row,col]=C[i,j]
            row+=1
    assert len(pivot_columns(equations,8,4))==3
    assert product(equations,{(0,0):ONE,(3,0):ONE})=={}
    assert scaled(A(F(1,4)),I2)!=scaled(A(F(1,2)),I2)
    checks={k:True for k in (
        'canonical_complements_have_opposite_spin_normal_eigenvalue',
        'four_complement_interfaces_recover_actual_old_source_image',
        'opposite_family_has_same_ranks_and84_protocol_occurrences',
        'all96_complement_family_transport_squares',
        'all_six_flavor_label_bijections_fail_rotation_intertwining',
        'native_quaternion_commutant_is_only_scalar_identity')}
    assert all(digest(ROOT/p)==h for p,h in pins.items()),'source changed during check'
    report={'schema':'marici.neutrino-three-port-discriminants-check.v1','status':'pass',
        'checks':checks,'complement_variants':rows,
        'rotation_inert_flavor_label_hostile':{'omitted_face':omitted,'native_spin_index':ui,
            'source_face_permutation':p,'all_six_failed_label_bijections':failures,
            'scope':'Conditional on interpreting the native action as physical spatial rotation; no actual flavor map supplied'},
        'commutant':{'matrix_unknowns':4,'constraint_rank':3,'kernel_dimension':1,
            'kernel':'complex scalar identity','no_rank_one_projector':True,'equations':encode(equations)},
        'physical_chirality_or_antiparticle_interpretation':False,
        'physical_neutrino_identified':False,'formal_proof_recompiled':False,
        'source_sha256':pins}
    OUT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','check_groups':6,'opposite_normal_family_same_total':84,
        'failed_flavor_label_bijections':6,'spin_commutant_dimension':1,'physical_neutrino_identified':False},indent=2))


if __name__=='__main__':main()
