"""Explicit spinor-fiber/rim attachment and scalar contact, not weak physics."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
import sys

from check_neutrino_triangle_cap_boundary import ROOT,select,generator,apply
from check_neutrino_three_port_boundary import (
    A,ZERO,ONE,S2,S3,CI,I2,identity,plus,scaled,product,transpose,
    from_spin,stack,subtract,dot,det3,encode,source_electron_factors,ACTIONS,STORE)

CONTRACT=ROOT/'research/strominger/contracts/neutrino-spinor-rim-contact.v1.json'
OUT=ROOT/'research/strominger/results/neutrino-spinor-rim-contact-v1.json'
RIM=ROOT/'research/strominger/results/neutrino-rim-attachment-v1.json'
COHERENT=ROOT/'research/strominger/results/neutrino-three-port-boundary-v1.json'
NSOURCE=ROOT/'research/voevodsky/inputs/mode-neutron.json'


def digest(p):return sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def column(v):return {(i,0):x for i,x in enumerate(v) if x!=ZERO}
def vector(m,n=3):return tuple(m.get((i,0),ZERO) for i in range(n))
def fields(M):return {(i,j):A(F(x)) for i,row in enumerate(M) for j,x in enumerate(row) if F(x)}
def kron(a,b,rows_b,cols_b):return {(i*rows_b+k,j*cols_b+l):x*y for (i,j),x in a.items() for (k,l),y in b.items() if x*y!=ZERO}
def scalar(m):return m.get((0,0),ZERO)
def norm(v):return scalar(product(transpose(v,True),v))
def serial(x):
    if isinstance(x,A):return x.record()
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [serial(v) for v in x]
    return x


def main():
    contract=read(CONTRACT);pins={}
    for path in (RIM,COHERENT):
        previous=read(path)
        assert previous['status']=='pass' and all(previous['checks'].values())
        assert all(digest(ROOT/p)==h for p,h in previous['source_sha256'].items()),'stale prerequisite'
        pins.update(previous['source_sha256']);pins[path.relative_to(ROOT).as_posix()]=digest(path)
    store=read(STORE);nsource=read(NSOURCE);neutron,_=select(nsource)
    nv=[tuple(map(F,p)) for p in neutron['vertices']]
    hg=generator(nsource['generators'][0]);lookup={p:i for i,p in enumerate(nv)}
    host_perm=[lookup[apply(hg,p)] for p in nv]
    GN=fields(nsource['metric']);AN=fields(nsource['generators'][0]['matrix'])
    assert not any(F(x) for x in nsource['generators'][0]['translation'])
    powers=[identity(3),AN,product(AN,AN)]
    K,D=source_electron_factors();E=scaled(ONE/S2,K);ED=transpose(E,True)
    assert product(ED,E)==I2 and product(D,K)==I2
    P=[{(i,j):K[2*f+i,j] for i in range(2) for j in range(2) if (2*f+i,j) in K} for f in range(4)]
    normals=[tuple(A(F(x[0]))+S3*F(x[1]) for x in n) for n in store['normals']]
    U=[from_spin(u) for u in ACTIONS];perms=[];rotations=[]
    for u in U:
        perm=tuple(next(i for i,q in enumerate(P) if product(u,product(p,transpose(u,True)))==q) for p in P)
        perms.append(perm)
        rotations.append({(a,b):sum((normals[perm[f]][a]*normals[f][b]*F(3,4) for f in range(4)),ZERO)
            for a in range(3) for b in range(3)})
    epsilon={(1,0):ONE/S2,(2,0):-ONE/S2}
    assert norm(epsilon)==ONE
    I3=identity(3);minus_index=next(i for i,u in enumerate(U) if u==scaled(-ONE,I2))
    charts=[];variants={};transport_checks=0
    for omitted in range(4):
        kept=tuple(f for f in range(4) if f!=omitted)
        tangent={f:tuple(normals[f][a]+normals[omitted][a]*F(1,3) for a in range(3)) for f in kept}
        projected={f:tuple(x*A(F(3,2))/S2 for x in tangent[f]) for f in kept}
        assert all(dot(projected[f],projected[f])==ONE and dot(projected[f],normals[omitted])==ZERO for f in kept)
        assert all(sum((projected[f][a] for f in kept),ZERO)==ZERO for a in range(3))
        for f in kept:
            for g in kept:
                delta=tuple(x-y for x,y in zip(projected[f],projected[g]))
                assert dot(delta,delta)==(ZERO if f==g else A(3))
            # Negative Pauli-line tangential polarization points out of the edge
            # opposite r_f; no physical momentum/helicity is attached here.
            assert tuple(-x for x in tangent[f])==tuple(-x*A(F(2,3))*S2 for x in projected[f])
        B={(a,b):projected[kept[b+1]][a]-projected[kept[0]][a] for a in range(3) for b in range(2)}
        H=fields([[F(4,9),F(-2,9)],[F(-2,9),F(4,9)]])
        assert product(H,product(transpose(B),B))==I2
        Rnorm=plus(P[omitted],scaled(ONE/S2,subtract(I2,P[omitted])))
        V=stack([product(P[f],Rnorm) for f in kept]);VD=transpose(V,True)
        assert product(VD,V)==I2
        pair_encoder=kron(E,V,6,2);pair_decoder=kron(ED,VD,2,6)
        psi=product(pair_encoder,epsilon)
        assert norm(psi)==ONE and product(pair_decoder,psi)==epsilon
        assert product(pair_decoder,pair_encoder)==identity(4)
        branches=[{(i,j):x for (i,j),x in psi.items() if i%6 in (2*k,2*k+1)} for k in range(3)]
        assert all(norm(branch)==A(F(1,3)) for branch in branches)
        fidelity=sum((scalar(product(transpose(psi,True),branch))*scalar(product(transpose(branch,True),psi)) for branch in branches),ZERO)
        assert fidelity==A(F(1,3))!=ONE
        stabilizer=[i for i,p in enumerate(perms) if p[omitted]==omitted]
        assert len(stabilizer)==6 and minus_index in stabilizer
        variants[str(omitted)]={'kept_faces':kept,'projected_triangle_vertices':projected,
            'logical_to_edge_spinor_encoder':encode(V),'normalized_electron_encoder':encode(E),
            'raw48_contact_vector':encode(psi),'logical_singlet':encode(epsilon),
            'edge_flag_probabilities':['1/3']*3,'coherent_projector_overlap_after_dephasing':'1/3'}
        for cap in neutron['external_interfaces']:
            p0=nv[min(cap)];orbit=[p0,apply(hg,p0),apply(hg,apply(hg,p0))]
            center=tuple(sum(p[a] for p in orbit)/3 for a in range(3))
            for shift in range(3):
                host_points=[orbit[(shift+k)%3] for k in range(3)]
                BN=fields([[host_points[b+1][a]-host_points[0][a] for b in range(2)] for a in range(3)])
                plane=product(BN,product(H,transpose(B)))
                candidates=[]
                for axis_sign in (-1,1):
                    frame=plus(plane,{(1,b):axis_sign*normals[omitted][b] for b in range(3)})
                    determinant=det3({(a,b):frame.get((a,b),ZERO) for a in range(3) for b in range(3)})
                    if determinant==S3/F(3):candidates.append((axis_sign,frame))
                assert len(candidates)==1
                axis_sign,frame=candidates[0]
                assert product(transpose(frame),product(GN,frame))==I3
                ids={}
                for f,p in zip(kept,host_points):
                    image=vector(product(frame,column(projected[f])))
                    assert image==tuple(A(x-y) for x,y in zip(p,center))
                    ids[f]=lookup[p]
                edges={f:tuple(sorted(ids[g] for g in kept if g!=f)) for f in kept}
                checks_here=[]
                for ui in stabilizer:
                    perm=perms[ui];u=U[ui]
                    k=kept.index(perm[kept[0]])
                    assert all(perm[f]==kept[(j+k)%3] for j,f in enumerate(kept))
                    assert product(frame,rotations[ui])==product(powers[k],frame)
                    for f in kept:
                        mapped=list(edges[f])
                        for _ in range(k):mapped=[host_perm[v] for v in mapped]
                        assert tuple(sorted(mapped))==edges[perm[f]]
                    W={}
                    for j,f in enumerate(kept):
                        target=kept.index(perm[f])
                        W.update({(2*target+a,2*j+b):x for (a,b),x in u.items()})
                    assert product(W,V)==product(V,u)
                    raw_electron_action=product(K,product(u,D))
                    joint=kron(raw_electron_action,W,6,6)
                    assert product(joint,psi)==psi
                    # Covariance alone allows both zero and nonzero couplings.
                    for strength in (ZERO,ONE):assert product(joint,scaled(strength,psi))==scaled(strength,psi)
                    if ui==minus_index:
                        assert k==0 and W==scaled(-ONE,identity(6))
                        assert product(VD,product(W,V))==scaled(-ONE,I2)
                    checks_here.append({'native_spin_index':ui,'base_cycle_power':k})
                    transport_checks+=1
                assert len([x for x in checks_here if x['base_cycle_power']==0])==2
                charts.append({'omitted_face':omitted,'neutron_cap':cap,'cycle_shift_word':[0]*shift,
                    'proper_metric_frame':encode(frame),'normal_axis_sign':axis_sign,
                    'cap_center':center,'face_to_cap_vertex':ids,'face_to_actual_rim_edge':edges,
                    'native_stabilizer_lifts':checks_here})
    assert len(charts)==24 and transport_checks==144
    checks={name:True for name in (
        'fresh_geometric_attachment_and_coherent_source_prerequisites',
        'four_projected_normal_triangles_are_unit_radius_with_metric_three',
        'twenty_four_proper_isometric_frames_to_actual_neutron_caps',
        'actual_edge_indices_and_outward_tangential_polarization_relation',
        'four_marked_coherent_doublets_keep_full_two_coordinate_recovery',
        'one_hundred_forty_four_joint_geometric_spin_edge_transport_squares',
        'both_lifts_retained_central_spin_sign_does_not_descend_to_base',
        'raw48_scalar_contact_normalized_and_logical_singlet_recovered',
        'source_common_spin_transport_fixes_each_encoded_contact',
        'edge_dephasing_changes_coherent_contact_overlap_to_one_third',
        'zero_and_nonzero_contact_strengths_both_covariant',
        'spinor_fiber_is_explicitly_supplied_not_derived_from_bare_arrows')}
    for p in (CONTRACT,STORE,NSOURCE,Path(__file__).resolve()):pins[p.relative_to(ROOT).as_posix()]=digest(p)
    for module in tuple(sys.modules.values()):
        file=getattr(module,'__file__',None)
        if file:
            p=Path(file).resolve()
            if p.is_relative_to(ROOT/'research') and p.suffix=='.py':pins[p.relative_to(ROOT).as_posix()]=digest(p)
    assert all(digest(ROOT/p)==h for p,h in pins.items()),'source changed during check'
    report={'schema':'marici.neutrino-spinor-rim-contact-check.v1','status':'pass','checks':checks,
        'variants':variants,'geometric_frame_charts':charts,'chart_count':24,'joint_transport_square_count':144,
        'explicit_new_inputs':contract['explicit_new_inputs'],
        'actual_rim_edge_spinor_ports_constructed':True,'spin_compatible_scalar_contact_constructed':True,
        'spinor_fiber_derived_from_bare_arrows':False,'physical_weak_vertex_constructed':False,
        'physical_neutrino_identified':False,'charge_mass_momentum_chirality_or_weak_rate_derived':False,
        'formal_proof_recompiled':False,'source_sha256':pins}
    OUT.write_text(json.dumps(serial(report),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','check_groups':len(checks),'proper_frame_charts':24,
        'joint_transport_squares':transport_checks,'raw_contact_coordinates':48,
        'coherent_overlap_after_edge_dephasing':'1/3','spin_compatible_contact_constructed':True,
        'physical_weak_vertex_constructed':False,'physical_neutrino_identified':False},indent=2))


if __name__=='__main__':main()
