"""Actual triangle-cycle metric versus fixed native preparation readers.
Dependency-free exact arithmetic. No producer entrypoint or shared write.
"""
from itertools import permutations
from pathlib import Path
import sys
import json
from check_packet_handoff_naturality_07 import (ROOT,A,F,ZERO,ONE,CI,S3,product,plus,scaled,encode,
    identity,invert,sub,adj,trace,rank,closure,key,vec,norm,xyz,val,digest,read,
    load,representations,native_geometries,independent_encoders,block,point_key,
    cartan_projector)

CONTRACT=ROOT/'research/strominger/contracts/packet-handoff-naturality-08.v1.json'
PRIOR=ROOT/'research/strominger/results/packet-handoff-naturality-07-v1.json'
OUT=ROOT/'research/strominger/results/packet-handoff-naturality-08-v1.json'
OMEGA=(-ONE+CI*S3)/A(2)
C2={(0,0):-ONE,(0,1):-ONE,(1,0):ONE}
M2={(0,0):A(2),(0,1):ONE,(1,0):ONE,(1,1):A(2)}


def conj(m):return {k:x.flip(8) for k,x in m.items()}
def det3(m):
    return sum((A((-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3)))*
        m.get((0,p[0]),ZERO)*m.get((1,p[1]),ZERO)*m.get((2,p[2]),ZERO) for p in permutations(range(3))),ZERO)
def diagonal_blocks(blocks):
    return {(3*t+i,3*t+j):x for t,b in enumerate(blocks) for (i,j),x in b.items()}
def metric_projector(K,H,r):
    gram=product(adj(K),product(H,K))
    return product(K,product(invert(gram,r),product(adj(K),H))),gram


def triangle(points):
    B={(i,j):p[i]-points[0][i] for j,p in enumerate(points[1:]) for i in range(3) if p[i]!=points[0][i]}
    S=product(adj(B),B);X=product(invert(S,2),adj(B));P=product(B,X);normal=sub(identity(3),P)
    C=plus(product(B,product(C2,X)),normal);Cpow=product(C,C)
    assert product(Cpow,C)==identity(3) and product(C,normal)==normal
    center=scaled(A(F(1,3)),plus(*(vec(p) for p in points)))
    for i in range(3):assert product(C,sub(vec(points[i]),center))==sub(vec(points[(i+1)%3]),center)
    q=vec(sum((p[i]*z for p,z in zip(points,(ONE,OMEGA,OMEGA*OMEGA))),ZERO) for i in range(3))
    assert product(C,q)==scaled(OMEGA*OMEGA,q)
    E=scaled(A(F(1,3)),plus(identity(3),scaled(OMEGA,C),scaled(OMEGA*OMEGA,Cpow)))
    Ebar=conj(E);assert product(E,E)==E and product(E,Ebar)=={} and plus(E,Ebar)==P
    Q=scaled(ONE/norm(q),product(q,adj(q)))
    EE=product(E,adj(E));assert scaled(ONE/trace(EE),EE)==Q
    H=scaled(A(F(1,3)),plus(identity(3),product(adj(C),C),product(adj(Cpow),Cpow)))
    # Positivity is exact: x*Hx=(||x||^2+||Cx||^2+||C^2x||^2)/3.
    assert H==adj(H) and H==conj(H) and product(adj(C),product(H,C))==H
    assert product(adj(q),product(H,q))=={(0,0):norm(q)}
    assert product(adj(conj(q)),product(H,q))=={}
    assert E==scaled(ONE/norm(q),product(q,product(adj(q),H)))
    J=scaled(ONE/S3,product(plus(scaled(A(2),C),identity(3)),P))
    assert product(J,J)==scaled(-ONE,P) and product(adj(J),H)==scaled(-ONE,product(H,J))
    aa=S[0,0];cc=S[1,1];bb=aa+cc-A(2)*S.get((0,1),ZERO)
    assert product(adj(B),product(H,B))==scaled((aa+bb+cc)/A(6),M2)
    bilinear=trace(product(adj(conj(q)),q));chi=bilinear*bilinear.flip(8)/(norm(q)*norm(q))
    assert det3(H)==ONE/(ONE-chi) and trace(product(P,H))==A(2)/(ONE-chi)
    return {'C':C,'H':H,'P':P,'E':E,'Q':Q,'q':q,'J':J,'chi':chi}


def invariant_ray():
    basis=({(0,0):ONE},{(0,1):ONE,(1,0):ONE},{(1,1):ONE})
    residuals=[sub(product(adj(C2),product(h,C2)),h) for h in basis]
    constraints={(2*i+j,k):x for k,r in enumerate(residuals) for (i,j),x in r.items()}
    assert rank(constraints,4,3)==2 and product(adj(C2),product(M2,C2))==M2
    return {'dimension':1,'positive_ray_generator':encode(M2),'coefficient_constraint_rank':2}


def geometric_tests(objects,reps,geometry,data):
    all_triangles={};results={};permutation_checks=0;spatial_squares=0
    for name,g in geometry.items():
        rows=[];triangles=[]
        for t,cell in enumerate(g['base']['faces']):
            points=[g['points'][a] for a in cell];d=triangle(points);triangles.append(d)
            for p in permutations(range(3)):
                other=triangle([points[i] for i in p]);odd=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2
                assert other['H']==d['H'] and other['E']==(conj(d['E']) if odd else d['E'])
                permutation_checks+=1
            if name!='electron':
                v=block(data[name]['Kgeo'],3*t,3)
                assert d['Q']==scaled(ONE/norm(v),product(v,adj(v)))
                assert d['chi']!=ZERO and d['E']!=d['Q'] and d['E']!=adj(d['E'])
                assert product(adj(d['C']),d['C'])!=identity(3) and adj(d['J'])!=scaled(-ONE,d['J'])
            else:
                assert d['chi']==ZERO and d['H']==identity(3) and d['E']==d['Q']
                assert key(d['C']) in {key(R) for R in reps['electron']['V']}
            rows.append({'port':t,'corner_cycle':encode(d['C']),'cycle_metric':encode(d['H']),
                'character_idempotent':encode(d['E']),'complex_structure':encode(d['J']),
                'cycle_metric_determinant':det3(d['H']).record(),'native_circularity_defect':d['chi'].record(),
                'selected_line_norm_preserved':True,'selected_line_null_in_cycle_metric':True,
                'cycle_is_native_Euclidean_spatial_isometry':name=='electron'})
        group=closure(reps[name]['V'],3,12 if name=='proton' else 3) if name!='electron' else reps[name]['V']
        lookup={point_key(p):k for k,p in g['points'].items()};faces={frozenset(c):t for t,c in enumerate(g['base']['faces'])}
        for R in group:
            rename={k:lookup[point_key(xyz(product(R,vec(p))))] for k,p in g['points'].items()}
            for t,cell in enumerate(g['base']['faces']):
                target=faces[frozenset(rename[a] for a in cell)]
                assert triangles[target]['H']==product(R,product(triangles[t]['H'],adj(R)))
                spatial_squares+=1
        all_triangles[name]=triangles;results[name]={'ports':rows,'native_spatial_operations_checked':len(group)}
    return results,all_triangles,permutation_checks,spatial_squares


def native_reader_tests(objects,reps,data,triangles):
    result={}
    for name in ('proton','neutron'):
        o=objects[name];n=o['n'];d=data[name];E=d['E'];D={(i,i):A(x) for i,x in enumerate(o['metric'])}
        Dinv={(i,i):ONE/A(x) for i,x in enumerate(o['metric'])};Eleft=product(Dinv,adj(E))
        assert product(Eleft,E)==identity(n)
        Hworld=diagonal_blocks([x['H'] for x in triangles[name]])
        Cworld=diagonal_blocks([x['C'] for x in triangles[name]])
        H=product(adj(E),product(Hworld,E));C=product(Eleft,product(Cworld,E));Cpow=product(C,C)
        assert product(Cworld,E)==product(E,C) and product(Cpow,C)==identity(n)
        assert H==scaled(A(F(1,3)),plus(D,product(adj(C),product(D,C)),product(adj(Cpow),product(D,Cpow))))
        assert H!=D and product(adj(C),product(D,C))!=D
        assert product(adj(C),product(H,C))==H
        operators={};grams={}
        for s in 'LGN':
            f=o['f'][s];operators[s],grams[s]=metric_projector(f['K'],H,f['rank'])
            assert product(operators[s],operators[s])==operators[s]
            assert product(adj(operators[s]),H)==product(H,operators[s])
        assert grams['L']==o['f']['L']['gram']
        assert operators['G']==o['ops']['G']
        assert product(operators['G'],operators['L'])==product(operators['L'],operators['G'])==operators['N']
        assert operators['L']!=o['ops']['L'] and operators['N']!=o['ops']['N']
        assert product(adj(d['K']),product(H,d['K']))==d['gram']
        assert product(operators['N'],d['K'])==d['K'] and product(o['ops']['N'],d['K'])==d['K']
        assert product(C,o['ops']['L'])!=product(o['ops']['L'],C)
        assert product(C,operators['L'])==product(operators['L'],C)
        assert product(C,operators['N'])==product(operators['N'],C)
        for W in reps[name]['raw']:
            assert product(adj(W),product(H,W))==H
            for s in 'LGN':assert product(W,operators[s])==product(operators[s],W)
        witnesses=[]
        for t in range(len(triangles[name])):
            v=conj(block(d['Kgeo'],3*t,3));z={(3*t+i,0):x for (i,j),x in v.items()};raw=product(Eleft,z)
            assert product(E,raw)==z
            old=product(o['ops']['N'],raw);new=product(operators['N'],raw)
            assert old and not new and product(o['ops']['L'],raw) and not product(operators['L'],raw)
            scalar=trace(product(d['Dgeo'],z));assert old==scaled(scalar,d['K']) and scalar!=ZERO
            witnesses.append({'port':t,'valid_native_raw_input':encode(raw),'native_return_decoded_scalar':scalar.record(),
                'cycle_metric_return_decoded_scalar':ZERO.record(),'native_L_output_nonzero':True,'cycle_metric_L_output_zero':True})
        result[name]={'native_cycle_metric':encode(H),'native_corner_cycle':encode(C),
            'reader_residual_ranks':{s:rank(sub(operators[s],o['ops'][s]),n,n) for s in 'LGN'},
            'native_geometry_action_squares_checked':len(reps[name]['raw']),
            'all_conjugate_port_preparation_witnesses':witnesses,
            'original_G_preserved':True,'original_L_and_N_preserved_on_all_raw_inputs':False,
            'native_active_image_and_its_metric_preserved':True,'new_projectors_commute_with_derived_corner_cycle':True,
            'original_L_commutes_with_derived_corner_cycle':False,
            'fixed_geometric_preparation_adapter_forces_identity':True,
            'metric_change_is_only_coordinate_gauge_with_fixed_preparations':False}
    return result


def electron_branch(data,triangles):
    K=data['electron']['K'];rows=[]
    for f,t in enumerate(triangles['electron']):
        P=block(K,2*f,2);negative=cartan_projector(P);positive=cartan_projector(sub(identity(2),P))
        matches=[label for label,Q in (('native_negative_Pauli_square',negative),('opposite_positive_Pauli_square',positive)) if t['Q']==Q]
        assert len(matches)==1 and conj(t['Q'])==(positive if matches[0]=='native_negative_Pauli_square' else negative)
        rows.append({'face':f,'outward_ordered_triangle_character_matches':matches[0],
            'inverse_character_matches':('opposite_positive_Pauli_square' if matches[0]=='native_negative_Pauli_square' else 'native_negative_Pauli_square')})
    assert len({r['outward_ordered_triangle_character_matches'] for r in rows})==1
    return rows


def main():
    contract=read(CONTRACT);prior=read(PRIOR)
    assert prior['status']=='pass' and all(prior['checks'].values())
    assert all(digest(ROOT/p)==h for p,h in prior['source_sha256'].items())
    objects,binding,pins=load();reps=representations(objects,binding);geometry,placements=native_geometries(objects)
    data=independent_encoders(objects,geometry,placements)
    ray=invariant_ray();geom,triangles,np,ns=geometric_tests(objects,reps,geometry,data)
    readers=native_reader_tests(objects,reps,data,triangles);branches=electron_branch(data,triangles)
    checks={k:True for k in (
      'fresh_iteration7_source_pins','all30_native_baryon_triangles_nondegenerate',
      'real_affine_corner_cycles_have_order3_and_fix_normal','actual_Fourier_lines_have_omega_squared_character',
      'character_idempotents_and_conjugate_complement_close','baryon_character_idempotents_not_native_Euclidean_orthogonal_projectors',
      'Euclidean_support_of_character_idempotent_recovers_selected_line','cycle_averaged_metric_positive_as_sum_of_squares',
      'corner_cycle_preserves_averaged_metric','selected_modes_null_and_complex_structure_metric_skew',
      'selected_mode_norm_unchanged_by_metric_average','complex_structure_squares_to_minus_plane_identity',
      'baryon_cycle_complex_structure_not_Euclidean_skew','unique_real_invariant_plane_metric_ray',
      'invariant_plane_Gram_has_source_squared_edge_normalization','metric_determinant_and_trace_derive_from_circularity_defect',
      'all_S3_relabellings_preserve_metric_and_swap_character_exactly_by_parity','all_native_spatial_metric_transport_squares',
      'cycle_metric_and_cycle_operator_pull_back_to_native_intrinsic_preparations','native_local_image_Gram_preserved',
      'native_G_preserved_and_reprojected_L_G_commute','reprojected_N_equals_G_L_on_all_raw_inputs',
      'native_active_image_and_its_norm_both_preserved','all30_conjugate_port_preparations_have_unequal_native_L_N_readers',
      'electron_equilateral_control_needs_no_metric_change','both_electron_Pauli_Cartan_character_branches_compared_without_orientation_flip',
      'derived_baryon_corner_cycle_not_native_metric_unitary_and_original_L_not_cycle_equivariant',
      'changed_metric_protocol_still_intertwines_actual_native_geometry_actions')}
    pins.update(prior['source_sha256'])
    for p in (CONTRACT,PRIOR,Path(__file__).resolve()):pins[p.relative_to(ROOT).as_posix()]=digest(p)
    for module in tuple(sys.modules.values()):
        path=getattr(module,'__file__',None)
        if path:
            p=Path(path).resolve()
            if p.suffix=='.py' and p.is_relative_to(ROOT/'research'):
                rel=p.relative_to(ROOT).as_posix();assert rel not in pins or pins[rel]==digest(p);pins[rel]=digest(p)
    assert all(digest(ROOT/p)==h for p,h in pins.items())
    report={'schema':'marici.packet-handoff-naturality-iteration-check.v1','iteration':8,'status':'pass','checks':checks,
      'invariant_plane_metric_ray':ray,'actual_triangle_cycle_geometry':geom,'S3_relabelling_checks':np,'native_spatial_metric_squares':ns,
      'cycle_metric_full_native_reader_comparison':readers,'electron_oriented_character_branches':branches,
      'source_derived_cycle_complex_structures_and_metric_rays_constructed':True,
      'circularization_preserves_native_active_image_and_norm':True,
      'circularization_preserves_full_native_preparation_task':False,
      'native_baryon_corner_cycles_are_original_metric_isometries':False,
      'cycle_metric_change_is_only_coordinate_gauge_with_fixed_geometric_preparations':False,
      'character_idempotent_is_native_baryon_local_preparation':False,
      'full_protocol_equivalence_bold_conjecture_rejected':True,
      'derived_corner_cycle_is_given_native_primitive':False,'source_native_handoff_constructed':False,
      'physical_particle_assignment_verified':False,'native_producers_executed':False,'formal_proof_recompiled':False,
      'next_executable_scope':contract['next_executable_scope'],'source_sha256':pins}
    OUT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','iteration':8,'check_groups':len(checks),'relabellings':np,'native_metric_squares':ns,
      'reader_residual_ranks':{n:r['reader_residual_ranks'] for n,r in readers.items()},'electron_branches':branches,
      'full_native_task_preserved':False},indent=2))

if __name__=='__main__':main()
