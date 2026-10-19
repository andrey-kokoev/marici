"""Source line holonomy, both Cartan helicities and full sewing tests.
No native producer, proof backend or other-owner write. Exact number field.
"""
from fractions import Fraction as F
from itertools import combinations,product as pairs
from pathlib import Path
from hashlib import sha256
import json
import sys
from assemble_metric_coefficient_protocol import ROOT,A,ZERO,ONE,product,plus,scaled,encode,read_operator
from check_port_incidence_conjectures import identity,invert
from check_packet_handoff_naturality_02 import load,sub,adj,column,trace,kron
from check_packet_handoff_naturality_04 import representations,rank,closure,key,CI,S3
from check_packet_handoff_naturality_05 import native_geometries,point_key,chain_action,vec,dot,cross
from check_packet_handoff_naturality_06 import independent_encoders,block

CONTRACT=ROOT/'research/strominger/contracts/packet-handoff-naturality-07.v1.json'
PRIOR=ROOT/'research/strominger/results/packet-handoff-naturality-06-v1.json'
OUT=ROOT/'research/strominger/results/packet-handoff-naturality-07-v1.json'
J={(0,0):ONE,(0,2):-ONE,(1,0):CI,(1,2):CI,(2,1):A(-2)}


def read(p):return json.loads(p.read_text(encoding='utf-8'))
def digest(p):return sha256(p.read_bytes()).hexdigest()
def val(v,i):return v.get((i,0),ZERO)
def xyz(v):return tuple(val(v,i) for i in range(3))
def norm(v):return trace(product(adj(v),v))
def matrix_block(m,i,j,d):return {(a-i,b-j):x for (a,b),x in m.items() if i<=a<i+d and j<=b<j+d}
def sym2(u):
    a,b,c,d=[u.get(k,ZERO) for k in ((0,0),(0,1),(1,0),(1,1))]
    return {(i,j):x for i,row in enumerate(((a*a,A(2)*a*b,b*b),(a*c,a*d+b*c,b*d),(c*c,A(2)*c*d,d*d))) for j,x in enumerate(row) if x!=ZERO}
def cartan_projector(p):return product(J,product(sym2(p),invert(J,3)))


def dual_cycles(faces):
    edges=[(i,j) for i,j in combinations(range(len(faces)),2) if len(set(faces[i])&set(faces[j]))==2]
    adjacency={i:[] for i in range(len(faces))}
    for a,b in edges:adjacency[a].append(b);adjacency[b].append(a)
    parent={0:None};todo=[0];tree=set()
    while todo:
        a=todo.pop(0)
        for b in adjacency[a]:
            if b not in parent:parent[b]=a;tree.add(tuple(sorted((a,b))));todo.append(b)
    assert len(parent)==len(faces)
    cycles=[]
    for a,b in edges:
        if (a,b) in tree:continue
        pa=[a];pb=[b]
        while parent[pa[-1]] is not None:pa.append(parent[pa[-1]])
        while parent[pb[-1]] is not None:pb.append(parent[pb[-1]])
        common=next(x for x in pa if x in pb)
        cycle=pa[:pa.index(common)+1]+list(reversed(pb[:pb.index(common)]))
        assert cycle[0]==a and cycle[-1]==b and len(set(cycle))==len(cycle)
        cycles.append(cycle)
    assert len(cycles)==len(edges)-len(faces)+1
    return edges,cycles


def projection_loop(Q,cycle):
    op=Q[cycle[0]];modulus=ONE;zero=[]
    for i,j in zip(cycle,cycle[1:]+cycle[:1]):
        gamma=trace(product(Q[i],Q[j]));modulus=modulus*gamma
        if gamma==ZERO:zero.append([i,j])
        op=product(Q[j],op)
    lam=trace(op)
    assert lam*lam.flip(8)==modulus
    return {'raw_loop_scalar':lam.record(),'squared_modulus':modulus.record(),
       'normalized_phase_squared':None if zero else (lam*lam/modulus).record(),
       'zero_overlap_edges':zero},lam,modulus


def line_geometry(objects,geometry,data):
    result={};projectors={};vectors={}
    for name in ('proton','neutron'):
        g=geometry[name];K=data[name]['Kgeo'];Q=[];V=[];rows=[]
        for t,c in enumerate(g['base']['faces']):
            v=block(K,3*t,3);s=norm(v);assert s!=ZERO
            q=scaled(ONE/s,product(v,adj(v)));assert product(q,q)==q and trace(q)==ONE
            w=xyz(v);bilinear=dot(w,w);chi=bilinear*bilinear.flip(8)/(s*s)
            angular=tuple(-CI*x/s for x in cross(tuple(x.flip(8) for x in w),w))
            assert all(x.flip(8)==x for x in angular) and dot(angular,angular)==ONE-chi
            points=[g['points'][x] for x in c]
            normal=cross(tuple(b-a for a,b in zip(points[0],points[1])),tuple(b-a for a,b in zip(points[0],points[2])))
            assert dot(normal,w)==ZERO
            m=product(invert(J,3),v)
            det=val(m,0)*val(m,2)-val(m,1)*val(m,1)
            assert bilinear==-A(4)*det
            quadratic={(0,0):val(m,0),(0,1):val(m,1),(1,0):val(m,1),(1,1):val(m,2)}
            quadratic={k:x for k,x in quadratic.items() if x!=ZERO}
            assert rank(quadratic,2,2)==(1 if det==ZERO else 2)
            if name=='proton':assert chi==ZERO and q==matrix_block(objects[name]['ops']['L'],3*t,3*t,3)
            Q.append(q);V.append(v)
            rows.append({'triangle':t,'null_bilinear':bilinear.record(),'circularity_defect':chi.record(),
                         'Cartan_symmetric_matrix_rank':1 if det==ZERO else 2,'tangent_to_actual_geometric_triangle':True})
        if name=='neutron':assert any(r['Cartan_symmetric_matrix_rank']==2 for r in rows)
        classes={}
        for row in rows:classes.setdefault(str(row['circularity_defect']),{'value':row['circularity_defect'],'triangles':[]})['triangles'].append(row['triangle'])
        result[name]={'lines':rows,'circularity_classes':list(classes.values()),
          'pure_Cartan_square_count':sum(r['Cartan_symmetric_matrix_rank']==1 for r in rows),
          'nondecomposable_symmetric_matrix_count':sum(r['Cartan_symmetric_matrix_rank']==2 for r in rows)}
        projectors[name]=Q;vectors[name]=V
    return result,projectors,vectors


def local_square_and_global_sewing(objects,reps,geometry,placements,data,Q):
    K=data['electron']['K'];P=[block(K,2*f,2) for f in range(4)]
    points=geometry['electron']['points'];normals=[tuple(-x/A(3) for x in points[f'E{f}']) for f in range(4)]
    Qminus=[cartan_projector(p) for p in P];Qplus=[cartan_projector(sub(identity(2),p)) for p in P]
    assert all(q==adj(q) and product(q,q)==q and trace(q)==ONE for q in Qminus+Qplus)
    assert all(product(a,b)=={} for a,b in zip(Qminus,Qplus))
    labels=[]
    for triangle in geometry['proton']['base']['faces']:
        pp=[geometry['proton']['points'][k] for k in triangle]
        f=next(f for f,n in enumerate(normals) if dot(n,pp[0])==dot(n,pp[1])==dot(n,pp[2]))
        labels.append(f)
    assert [labels.count(f) for f in range(4)]==[3]*4
    matches=[name for name,candidate in (('native_negative_Pauli_line',Qminus),('opposite_positive_Pauli_line',Qplus)) if all(q==candidate[f] for q,f in zip(Q['proton'],labels))]
    assert len(matches)==1
    sign=matches[0];chosen=Qminus if sign=='native_negative_Pauli_line' else Qplus
    adapters=[]
    for name,candidate in (('native_negative_Pauli_line',Qminus),('opposite_positive_Pauli_line',Qplus)):
        Fmap={(3*t+i,j):x for t,f in enumerate(labels) for (i,j),x in candidate[f].items()}
        assert product(adj(Fmap),Fmap)==scaled(A(4),identity(3))
        LF=product(objects['proton']['ops']['L'],Fmap)
        assert LF==(Fmap if name==sign else {})
        assert not product(objects['proton']['ops']['G'],Fmap)
        assert not product(objects['proton']['ops']['N'],Fmap)
        adapters.append({'helicity':name,'local_L_preserves_adapter':name==sign,
                         'adapter':encode(Fmap),'source_G_and_N_annihilate_entire_quadratic_module':True})
    pgroup=closure(reps['proton']['V'],3,12);pkeys={key(R) for R in pgroup}
    g=geometry['proton'];lookup={point_key(p):k for k,p in g['points'].items()}
    for U,R,perm in zip(reps['electron']['logical'],reps['electron']['V'],reps['electron']['permutations']):
        assert key(R) in pkeys and product(J,sym2(U))==product(R,J)
        for f,p in enumerate(P):
            assert product(U,product(p,adj(U)))==P[perm[f]]
            assert product(R,product(Qminus[f],adj(R)))==Qminus[perm[f]]
            assert product(R,product(Qplus[f],adj(R)))==Qplus[perm[f]]
        rename={k:lookup[point_key(tuple(product(R,vec(p)).get((i,0),ZERO) for i in range(3)))] for k,p in g['points'].items()}
        W=kron(chain_action(g['base']['faces'],rename),R,3)
        for candidate in (Qminus,Qplus):
            Fmap={(3*t+i,j):x for t,f in enumerate(labels) for (i,j),x in candidate[f].items()}
            assert product(W,Fmap)==product(Fmap,R)
    representatives=[labels.index(f) for f in range(4)]
    rotations=[{(i,j):A(F(x)) for i,row in enumerate(p['rotation']) for j,x in enumerate(row) if F(x)} for p in placements]
    phase_rows=[]
    for f in range(4):
        ids=[t for t,x in enumerate(labels) if x==f];v0=data['proton']['Kgeo'];base=block(v0,3*ids[0],3);s=norm(base);phases=[]
        for t in ids:
            v=block(v0,3*t,3);phase=trace(product(adj(base),v))/s
            assert scaled(phase,base)==v and phase*phase*phase==ONE
            phases.append(phase)
        assert len({x.c for x in phases})==3
        phase_rows.append({'face':f,'ports':ids,'native_relative_phases':[x.record() for x in phases]})
    return {'matched_helicity':sign,'same_normal_mapping':labels,'both_helicity_sewing_adapters':adapters,
        'all24_native_quadratic_spatial_and_port_adapter_squares':True,
        'four_face_projectors_erase_three_distinct_native_port_phases':phase_rows,
        'local_square_relation_is_global_native_packet_equivalence':False},P,chosen,representatives,rotations,pgroup


def tetrahedral_loops(objects,reps,geometry,P,Q,representatives,rotations,pgroup):
    cycles=[[int(v[1:]) for v in c] for c in geometry['electron']['base']['faces']]
    e_rows=[];p_rows=[]
    for cycle in cycles:
        eop=P[cycle[0]];pop=Q[cycle[0]];body=Q[cycle[0]]
        for i,j in zip(cycle,cycle[1:]+cycle[:1]):
            assert trace(product(P[i],P[j]))==A(F(1,3))
            assert trace(product(Q[i],Q[j]))==A(F(1,9))
            Te=scaled(S3,product(P[j],P[i]));Tp=scaled(A(3),product(Q[j],Q[i]))
            assert product(adj(Te),Te)==P[i] and product(adj(Tp),Tp)==Q[i]
            assert Te==scaled(A(2)*S3,matrix_block(objects['electron']['ops']['N'],2*j,2*i,2))
            native=product(rotations[representatives[j]],adj(rotations[representatives[i]]))
            assert product(native,product(Q[i],adj(native)))==Q[j]
            body=product(native,body);eop=product(Te,eop);pop=product(Tp,pop)
        eh=trace(eop);ph=trace(pop)
        assert eh in (CI,-CI) and product(eop,eop)==scaled(-ONE,P[cycle[0]])
        assert ph==-ONE and pop==scaled(-ONE,Q[cycle[0]]) and body==Q[cycle[0]]
        e_rows.append({'oriented_face_cycle':cycle,'normalized_phase':eh.record(),'native_N_blocks_up_to_common_positive_normalizer':True})
        p_rows.append({'normal_face_cycle':cycle,'projection_phase':ph.record(),'supplied_body_phase':ONE.record(),
                        'projection_minus_body':encode(sub(pop,body))})
    assert len({str(x['normalized_phase']) for x in e_rows})==1
    e_misses=[];p_misses=[]
    for i,j in pairs(range(4),repeat=2):
        if i==j:continue
        Te=scaled(S3,product(P[j],P[i]));Tp=scaled(A(3),product(Q[j],Q[i]))
        available_e=[k for k,U in enumerate(reps['electron']['logical']) if product(U,P[i])==Te]
        available_p=[k for k,R in enumerate(pgroup) if product(R,Q[i])==Tp]
        assert not available_e and not available_p
        e_misses.append([i,j]);p_misses.append([i,j])
    fixed=[]
    for f in range(4):
        k=next(k for k,(U,perm) in enumerate(zip(reps['electron']['logical'],reps['electron']['permutations'])) if perm[f]==f and product(U,product(U,U))==scaled(-ONE,identity(2)) and U!=scaled(-ONE,identity(2)))
        U=reps['electron']['logical'][k];R=reps['electron']['V'][k];phase=trace(product(P[f],U))
        assert product(U,P[f])==scaled(phase,P[f]) and phase*phase*phase==-ONE
        for q,p in ((cartan_projector(P[f]),P[f]),(cartan_projector(sub(identity(2),P[f])),sub(identity(2),P[f]))):
            lam=trace(product(p,U));assert product(R,q)==scaled(lam*lam,q)
        fixed.append({'face':f,'native_operation_index':k,'native_spin_line_phase':phase.record(),
                       'native_squared_line_phase':(phase*phase).record()})
    return {'electron_oriented_loops':e_rows,'proton_projection_vs_supplied_body_loops':p_rows,
       'electron_projection_moves_not_native_spin_unitary_restrictions':e_misses,
       'proton_projection_moves_not_native_spatial_unitary_restrictions':p_misses,
       'native_face_stabilizer_spin_to_squared_line_characters':fixed,
       'projection_connection_gauge_equivalent_to_supplied_flat_body_connection':False,
       'finite_loop_phases_assert_a_physical_Chern_number':False}


def baryon_native_block_transport(objects,geometry,data,projectors,vectors):
    results={}
    for name in ('proton','neutron'):
        d=data[name];K=d['Kgeo'];rho=d['gram'][0,0]
        # The geometric coefficient extension uses the source-plane metric
        # left inverse; only its pullback to native coefficients is licensed.
        Hinv={(i,i):ONE/A(x) for i,x in enumerate(objects[name]['metric'])}
        Eleft=product(Hinv,adj(d['E']))
        assert product(Eleft,d['E'])==identity(objects[name]['n'])
        native=product(d['E'],product(objects[name]['ops']['N'],Eleft))
        assert native==scaled(ONE/rho,product(K,adj(K)))
        edges,cycles=dual_cycles(geometry[name]['base']['faces']);T={}
        for i,j in edges+[(j,i) for i,j in edges]:
            si=norm(vectors[name][i]);T[j,i]=scaled(ONE/si,product(vectors[name][j],adj(vectors[name][i])))
            assert T[j,i]==scaled(rho/si,matrix_block(native,3*j,3*i,3))
            assert product(T[j,i],vectors[name][i])==vectors[name][j]
        records=[]
        for cycle in cycles:
            out=projectors[name][cycle[0]]
            for i,j in zip(cycle,cycle[1:]+cycle[:1]):out=product(T[j,i],out)
            assert out==projectors[name][cycle[0]]
            projection,lam,mod=projection_loop(projectors[name],cycle)
            records.append({'triangle_cycle':cycle,'native_code_phase':ONE.record(),'projection_comparison':projection})
        results[name]={'dual_graph_edges':len(edges),'fundamental_cycles':records,
          'native_N_block_induced_code_transport_flat':True,
          'ambient_extension_is_new_full_preparation_task':False,
          'neutron_ambient_scope':'Native intrinsic-plane embedding and its metric left inverse, not free ambient preparation.' if name=='neutron' else None}
    assert len(results['proton']['fundamental_cycles'])==len(results['neutron']['fundamental_cycles'])==7
    return results


def main():
    contract=read(CONTRACT);prior=read(PRIOR)
    assert prior['status']=='pass' and all(prior['checks'].values())
    assert all(digest(ROOT/p)==h for p,h in prior['source_sha256'].items())
    retained=read(ROOT/'research/strominger/results/packet-handoff-naturality-04-v1.json')
    assert J==read_operator(retained['electron_quadratic_spatial_bridges']['Cartan_symmetric_square_to_spatial'],3)
    objects,binding,pins=load();reps=representations(objects,binding)
    geometry,placements=native_geometries(objects);data=independent_encoders(objects,geometry,placements)
    lines,Q,vectors=line_geometry(objects,geometry,data)
    square,P,Qface,reps_ports,rotations,pgroup=local_square_and_global_sewing(objects,reps,geometry,placements,data,Q)
    loops=tetrahedral_loops(objects,reps,geometry,P,Qface,reps_ports,rotations,pgroup)
    blocks=baryon_native_block_transport(objects,geometry,data,Q,vectors)
    checks={k:True for k in (
       'fresh_iteration6_source_pins',
       'selected_geometric_line_encoders_independent_of_return_factorization',
       'all_baryon_mode_lines_tangent_to_actual_source_triangles',
       'source_norm_nullity_and_angular_circularity_identity',
       'proton_all12_local_lines_are_null_Cartan_square_type',
       'neutron_contains_nondecomposable_symmetric_quadratic_modes',
       'binary_symmetric_matrix_determinant_equals_minus_null_form_over_four',
       'both_explicit_Pauli_helicities_compared_without_silent_sign_flip',
       'same_actual_tetrahedral_normals_match_four_proton_local_lines',
       'all24_native_symmetric_square_spatial_and_port_adapter_squares',
       'both_quadratic_face_adapters_have_Gram_four_I',
       'only_matching_helicity_survives_actual_proton_L',
       'actual_proton_G_and_N_annihilate_entire_facewise_quadratic_modules',
       'local_spinorial_square_is_not_global_coherent_packet_equivalence',
       'all_four_oriented_electron_line_loops_have_exact_imaginary_unit_phase',
       'squared_proton_line_loops_have_phase_minus_one',
       'actual_proton_supplied_body_loops_have_phase_plus_one',
       'projection_and_body_holonomy_mismatch_is_not_a_scalar_frame_gauge',
       'electron_line_projection_transports_are_normalized_actual_N_blocks',
       'all12_electron_projection_moves_not_restrictions_of_native_spin_unitaries',
       'all12_proton_projection_moves_not_restrictions_of_native_spatial_unitaries',
       'native_order_six_face_stabilizer_character_squares_to_order_three',
       'same_proton_face_projector_hides_three_actual_source_port_phases',
       'baryon_native_N_block_to_flat_code_transport_squares',
       'all_seven_fundamental_dual_cycles_each_baryon_native_code_flat',
       'neutron_projection_loop_moduli_and_zero_overlap_scope_retained',
       'flat_code_atlas_native_unitary_and_lossy_line_blocks_not_identified')}
    pins.update(prior['source_sha256'])
    for p in (PRIOR,CONTRACT,Path(__file__).resolve()):pins[p.relative_to(ROOT).as_posix()]=digest(p)
    for module in tuple(sys.modules.values()):
        path=getattr(module,'__file__',None)
        if path:
            p=Path(path).resolve()
            if p.suffix=='.py' and p.is_relative_to(ROOT/'research'):
                rel=p.relative_to(ROOT).as_posix();assert rel not in pins or pins[rel]==digest(p);pins[rel]=digest(p)
    assert all(digest(ROOT/p)==h for p,h in pins.items())
    report={'schema':'marici.packet-handoff-naturality-iteration-check.v1','iteration':7,'status':'pass','checks':checks,
       'geometric_mode_line_types':lines,'local_spinorial_square_and_global_sewing':square,
       'tetrahedral_line_holonomy_and_native_word_comparison':loops,'baryon_native_block_and_projection_transport':blocks,
       'local_source_spinorial_square_relation_constructed':True,
       'native_proton_packet_identified_with_electron_spinorial_square':False,
       'flat_code_transport_equals_projection_line_transport':False,
       'normalized_projection_move_is_existing_native_unitary':False,
       'all_neutron_selected_modes_are_pure_Cartan_squares':False,
       'finite_line_holonomy_selects_physical_spin_or_clock':False,
       'source_native_handoff_constructed':False,'physical_particle_assignment_verified':False,
       'native_producers_executed':False,'formal_proof_recompiled':False,
       'next_executable_scope':contract['next_executable_scope'],'source_sha256':pins}
    OUT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','iteration':7,'check_groups':len(checks),
       'proton_matched_helicity':square['matched_helicity'],
       'neutron_nondecomposable_modes':lines['neutron']['nondecomposable_symmetric_matrix_count'],
       'native_global_square_sewing':False},indent=2))


if __name__=='__main__':main()
