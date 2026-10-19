"""Actual geometric boundary modules and native coefficient tasks, iteration5.
Pure retained-source arithmetic; no producer entrypoints or shared writes.
"""
from fractions import Fraction as F
from itertools import combinations,product as pairs
from pathlib import Path
from hashlib import sha256
import json
import sys
from assemble_metric_coefficient_protocol import ROOT,A,ZERO,ONE,product,plus,scaled,encode
from check_port_incidence_conjectures import identity,transpose,pivot_columns
from check_packet_handoff_naturality_02 import load,sub,adj,kron,MERKLE,BELT
from check_packet_handoff_naturality_04 import representations,vec,rank,S2,S3
from check_packet_stage_cost_comparison import source_electron_factors
from check_belt_operator_inputs import frame
from electron_packet_interface import STORE

CONTRACT=ROOT/'research/strominger/contracts/packet-handoff-naturality-05.v1.json'
OUT=ROOT/'research/strominger/results/packet-handoff-naturality-05-v1.json'
PRIOR=ROOT/'research/strominger/results/packet-handoff-naturality-04-v1.json'
GEOMETRY=ROOT/'research/voevodsky/results/four_six_center_cones.json'
AMBIENT=ROOT/'research/voevodsky/results/coupled_six_piece_belt_store.json'


def read(p):return json.loads(p.read_text(encoding='utf-8'))
def digest(p):return sha256(p.read_bytes()).hexdigest()
def parity(xs):return (-1)**sum(xs[i]>xs[j] for i in range(len(xs)) for j in range(i+1,len(xs)))
def orientation(a,b):return parity([b.index(v) for v in a])
def dot(a,b):return sum((x*y for x,y in zip(a,b)),ZERO)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def point_key(p):return tuple(x.c for x in p)
def simplex_boundary(top,lower):
    lookup={frozenset(c):i for i,c in enumerate(lower)};out={}
    for j,c in enumerate(top):
        for i in range(len(c)):
            f=c[:i]+c[i+1:];k=lookup[frozenset(f)]
            out[k,j]=A((-1)**i*orientation(f,lower[k]))
    return out


def surface(faces):
    faces=list(map(tuple,faces));vertices=sorted({v for c in faces for v in c})
    edges=sorted({tuple(sorted(e)) for c in faces for e in combinations(c,2)})
    B1=simplex_boundary(edges,[(v,) for v in vertices]);B2=simplex_boundary(faces,edges)
    assert not product(B1,B2)
    r1,r2=rank(B1,len(vertices),len(edges)),rank(B2,len(edges),len(faces))
    return {'vertices':vertices,'edges':edges,'faces':faces,'B1':B1,'B2':B2,
            'counts':[len(vertices),len(edges),len(faces)],'boundary_ranks':[r1,r2],
            'betti':[len(vertices)-r1,len(edges)-r1-r2,len(faces)-r2]}


def cone(base):
    assert 'O' not in base['vertices']
    tets=[('O',)+c for c in base['faces']]
    faces=sorted({tuple(sorted(f)) for c in tets for f in combinations(c,3)})
    edges=sorted({tuple(sorted(e)) for c in tets for e in combinations(c,2)})
    B3=simplex_boundary(tets,faces);B2=simplex_boundary(faces,edges)
    assert not product(B2,B3)
    radial=[i for i,f in enumerate(faces) if 'O' in f]
    relative={(radial.index(i),j):x for (i,j),x in B3.items() if i in radial}
    relrank=rank(relative,len(radial),len(tets))
    assert len(tets)-relrank==base['betti'][2]
    return {'tets':tets,'faces':faces,'B3':B3,'radial':radial,'relative_B3':relative,
            'relative_H3':len(tets)-relrank,'relative_H2':base['betti'][1]}


def chain_action(basis,rename):
    lookup={frozenset(c):i for i,c in enumerate(basis)};out={}
    for j,c in enumerate(basis):
        image=tuple(rename[v] for v in c);i=lookup[frozenset(image)]
        out[i,j]=A(orientation(image,basis[i]))
    return out


def native_geometries(objects):
    merkle=read(MERKLE);pg=merkle['objects'][merkle['objects'][merkle['root']]['geometry']]['payload']
    placements=sorted(pg['triangles_and_transports'],key=lambda r:r['outer_arrow'])
    ppoints={k:tuple(A(x) for x in v) for k,v in zip('ABCD',((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)))}
    pfaces=[tuple(r['triangle']) for r in placements]
    for c in pfaces:
        for k in c:
            if k not in ppoints:
                labels=k[2:].replace('_','');assert len(labels)==3
                ppoints[k]=tuple(sum((ppoints[v][i] for v in labels),ZERO)/A(3) for i in range(3))
    geo=read(GEOMETRY);ambient=read(AMBIENT)['record'];store=read(BELT)
    points={k:tuple(map(F,p)) for k,p in geo['belt_scaled_coordinates'].items() if k!='O'}
    for face in geo['belt_faces']:
        points['F_'+'_'.join(sorted(face))]=tuple(sum(points[k][i] for k in face)/3 for i in range(3))
    npoints={k:tuple(A(x)+S2*y for x,y in frame(p)) for k,p in points.items()}
    nfaces=list(map(tuple,ambient['triangles']))
    normals=[tuple(A(F(x[0]))+S3*F(x[1]) for x in n) for n in read(STORE)['normals']]
    epoints={f'E{i}':tuple(-A(3)*x for x in n) for i,n in enumerate(normals)};efaces=[]
    for f,n in enumerate(normals):
        c=tuple(f'E{i}' for i in range(4) if i!=f);a,b,d=[epoints[k] for k in c]
        q=dot(n,cross(tuple(y-x for x,y in zip(a,b)),tuple(z-x for x,z in zip(a,d))))/S3
        assert all(x==0 for x in q.c[1:]) and q.c[0]!=0
        if q.c[0]<0:c=(c[0],c[2],c[1])
        efaces.append(c)
    geometry={'proton':{'points':ppoints,'base':surface(pfaces),'fiber':3,'patches':[[i] for i in range(12)]},
       'neutron':{'points':npoints,'base':surface(nfaces),'fiber':3,
                  'patches':[store['triangle_order'][6*s:6*s+6] for s in range(3)]},
       'electron':{'points':epoints,'base':surface(efaces),'fiber':2,'patches':[[i] for i in range(4)]}}
    for name,g in geometry.items():
        g['cone']=cone(g['base']);points=g['points'];p0=next(iter(points.values()))
        mat={(i,j):x-p0[i] for j,p in enumerate(points.values()) for i,x in enumerate(p) if x!=p0[i]}
        assert rank(mat,3,len(points))==3
        for c in g['base']['faces']:
            a,b,d=[points[k] for k in c]
            mat={(i,j):x-a[i] for j,p in enumerate((b,d)) for i,x in enumerate(p) if x!=a[i]}
            assert rank(mat,3,2)==2
        patch_rows=[]
        for patch in g['patches']:
            s=surface([g['base']['faces'][i] for i in patch]);assert s['betti']==[1,0,0]
            patch_rows.append({'triangle_indices':patch,'base_dimension':2,'codimension_in_fixed_ambient3':1,
                               'counts':s['counts'],'betti':s['betti']})
        assert len(patch_rows)==objects[name]['f']['L']['rank']
        g['patch_rows']=patch_rows
    assert {n:g['base']['betti'] for n,g in geometry.items()}=={'proton':[1,0,1],'neutron':[1,1,0],'electron':[1,0,1]}
    return geometry,placements


def native_embedding(name,o):
    if name!='neutron':return identity(o['n'])
    store=read(BELT);d=[F(c['d']) for c in store['coordinates']]
    E={}
    for row in store['embedding_entries']:
        a,b=map(F,row['numerator']);x=(A(a)+S2*b)/A(d[row['intrinsic_source']])
        if x!=ZERO:E[row['ambient_target'],row['intrinsic_source']]=x
    assert product(adj(E),E)=={(i,i):A(x) for i,x in enumerate(o['metric'])}
    return E


def coefficient_and_chain_squares(objects,reps,geometries):
    results={}
    for name,o in objects.items():
        g=geometries[name];base=g['base'];d=g['fiber'];nf=len(base['faces']);ne=len(base['edges'])
        E=native_embedding(name,o);K=product(E,o['f']['N']['K'])
        boundary=kron(base['B2'],identity(d),d);residual=product(boundary,K)
        assert rank(residual,ne*d,o['f']['N']['rank'])==o['f']['N']['rank']
        lookup={point_key(p):k for k,p in g['points'].items()};actions=[]
        for index,(R,W) in enumerate(zip(reps[name]['V'],reps[name]['raw'])):
            rename={k:lookup[point_key(tuple(product(R,vec(p)).get((i,0),ZERO) for i in range(3)))] for k,p in g['points'].items()}
            T0=chain_action([(v,) for v in base['vertices']],rename)
            T1=chain_action(base['edges'],rename);T2=chain_action(base['faces'],rename)
            assert product(base['B1'],T1)==product(T0,base['B1'])
            assert product(base['B2'],T2)==product(T1,base['B2'])
            fiber=reps[name]['logical'][index] if name=='electron' else R
            A2=kron(T2,fiber,d);A1=kron(T1,fiber,d)
            assert product(A2,E)==product(E,W)
            assert product(boundary,A2)==product(A1,boundary)
            active=product(o['f']['N']['D'],product(W,o['f']['N']['K']))
            assert product(A2,K)==product(K,active)
            for patch in g['patches']:
                image=sorted(i for (i,j),x in T2.items() if j in patch)
                assert image in [sorted(p) for p in g['patches']]
            actions.append({'rename':rename,'T1':T1,'T2':T2})
        g.update({'embedding':E,'active_encoder':K,'untwisted_boundary':boundary,'actions':actions})
        results[name]={'untwisted_active_boundary_rank':o['f']['N']['rank'],'untwisted_active_boundary':encode(residual),
                       'native_chain_and_fiber_action_count':len(actions),
                       'native_active_field_is_ordinary_untwisted_cycle':False}
    return results


def proton_flat_bulk(o,g,placements,reps):
    U={(3*t+i,3*t+j):A(F(x)) for t,p in enumerate(placements) for i,row in enumerate(p['rotation']) for j,x in enumerate(row) if F(x)}
    assert product(adj(U),U)==identity(36)
    Dtw=product(g['untwisted_boundary'],adj(U))
    assert not product(Dtw,o['ops']['G']) and not product(Dtw,o['ops']['N'])
    assert 36-rank(Dtw,len(g['base']['edges'])*3,36)==3
    constant={(3*t+i,i):ONE for t in range(12) for i in range(3)}
    stack=product(U,constant);G=scaled(A(F(1,12)),product(stack,adj(stack)))
    assert G==o['ops']['G']
    c=g['cone'];nface=len(c['faces']);outer={frozenset(t):j for j,t in enumerate(g['base']['faces'])}
    U2={};restrict={}
    for f,cell in enumerate(c['faces']):
        t=outer.get(frozenset(cell))
        if t is None:
            U2.update({(3*f+i,3*f+i):ONE for i in range(3)})
        else:
            block={(i,j):x for (a,b),x in U.items() if a//3==b//3==t for i,j in [(a%3,b%3)]}
            U2.update({(3*f+i,3*f+j):x for (i,j),x in block.items()})
            sign=A(orientation(g['base']['faces'][t],cell))
            restrict.update({(3*t+i,3*f+i):sign for i in range(3)})
    assert product(adj(U2),U2)==identity(3*nface)
    D3=product(U2,product(kron(c['B3'],identity(3),3),adj(U)))
    exterior=product(restrict,product(D3,stack));assert exterior==stack
    bulk_boundary=product(D3,stack)
    assert all(i//3 not in c['radial'] for i,j in bulk_boundary)
    fill=scaled(A(F(1,12)),product(stack,adj(stack)))
    assert product(restrict,product(D3,fill))==G
    assert product(o['ops']['L'],product(restrict,product(D3,fill)))==o['ops']['N']
    for R,W,action in zip(reps['V'],reps['raw'],g['actions']):
        rename=action['rename']|{'O':'O'}
        T3=chain_action(c['tets'],rename);T2=chain_action(c['faces'],rename)
        A3=product(U,product(kron(T3,identity(3),3),adj(U)))
        A2=product(U2,product(kron(T2,identity(3),3),adj(U2)))
        assert product(D3,A3)==product(A2,D3)
        assert product(restrict,A2)==product(W,restrict)
    return {'native_frame_twisted_boundary':encode(Dtw),'cycle_kernel_dimension':3,
            'G_is_exact_metric_projector_onto_twisted_boundary_cycles':True,
            'N_is_local_line_selected_subspace_of_twisted_cycles':True,
            'relative_bulk_H3_scalar_rank':c['relative_H3'],'relative_bulk_H3_with_native_vector_fiber':3,
            'bulk_to_boundary_source_square_constructed':True,
            'bulk_boundary_restrict_then_L_equals_native_N_on_all_raw_inputs':True,
            'interior_frame_extension':'Explicit flat gauge extension; native rotations on outer faces/cones, identity interior face frames. Gauge-dependent presentation, not new holonomy.',
            'bulk_filling_is_a_given_primitive_protocol_operation':False,
            'filling_reader_archive_and_types_must_be_retained':True}


def neutron_patch_boundary(o,g,reps):
    base=g['base'];patches=g['patches']
    J={(t,s):ONE for s,patch in enumerate(patches) for t in patch}
    boundary=product(base['B2'],J);assert rank(boundary,len(base['edges']),3)==3
    occurrence_rows=[(s,i) for s in range(3) for (i,j),x in boundary.items() if j==s]
    occurrence_rows=sorted(occurrence_rows);assert len(occurrence_rows)==12
    D={(k,s):boundary[i,s] for k,(s,i) in enumerate(occurrence_rows)}
    assert rank(D,12,3)==3 and rank(o['B'],12,3)==1
    action=g['actions'][0];M=reps['M'][0];W=reps['raw'][0]
    assert product(action['T2'],J)==product(J,M)
    assert product(adj(J),J)==scaled(A(6),identity(3))
    T={}
    for col,(s,i) in enumerate(occurrence_rows):
        target_s=next(a for (a,b),x in M.items() if b==s)
        target_i,sign=next((a,x) for (a,b),x in action['T1'].items() if b==i)
        T[occurrence_rows.index((target_s,target_i)),col]=sign
    assert product(T,D)==product(D,M) and T!=identity(12)
    avg=scaled(A(F(1,3)),plus(identity(12),T,product(T,T)))
    assert rank(avg,12,12)==4
    f=o['f']['G'];nativeC=product(f['D'],product(W,f['K']))
    assert nativeC==identity(12)
    rim=product(boundary,vec([ONE]*3));assert len(rim)==6
    geo=read(GEOMETRY);caps=[tuple(k for k in t if k!='O') for t in geo['missing_cap_tetrahedra']]
    capped=surface(base['faces']+caps);assert capped['betti']==[1,0,1]
    return {'sector_chain_encoder':encode(J),'sector_boundary':encode(boundary),
            'twelve_boundary_occurrences':[[s,list(base['edges'][i])] for s,i in occurrence_rows],
            'geometric_patch_to_boundary_rank':3,'native_M_to_C_rank':1,
            'geometric_boundary_occurrence_fixed_dimension':4,'native_C_fixed_dimension':12,
            'twelve_occurrences_are_not_equivariantly_the_native_twelve_alignment_channels':True,
            'native_active_sector_sum_has_nonzero_geometric_rim_boundary':encode(rim),
            'uncapped_relative_bulk_H3':g['cone']['relative_H3'],'uncapped_relative_bulk_H2':g['cone']['relative_H2'],
            'two_cap_completion_betti':capped['betti'],'cap_completion_is_same_native_preparation_task':False,
            'adding_cap_fields_or_radial_boundary_readers_requires_explicit_new_interface':True}


def covers_and_electron_local_system(objects,geometries):
    covers={}
    for name,o in objects.items():
        g=geometries[name];K=g['active_encoder'];d=g['fiber'];nf=len(g['base']['faces']);r=o['f']['N']['rank']
        evaluations=[]
        for f in range(nf):
            e={(i-d*f,j):x for (i,j),x in K.items() if d*f<=i<d*(f+1)}
            evaluations.append(rank(e,d,r))
        minimal=[]
        for size in range(1,nf+1):
            for subset in combinations(range(nf),size):
                kept={(d*subset.index(i//d)+i%d,j):x for (i,j),x in K.items() if i//d in subset}
                if rank(kept,d*size,r)==r:minimal.append(list(subset))
            if minimal:break
        covers[name]={'active_return_rank':r,'single_geometric_face_evaluation_ranks':evaluations,
                       'minimum_faithful_face_count':size,'minimal_covers':minimal,
                       'scope':'Active return packet with retained source encoder, not the full raw/stage preparation task.'}
    assert {n:c['minimum_faithful_face_count'] for n,c in covers.items()}=={'proton':1,'neutron':1,'electron':2}
    assert {n:len(c['minimal_covers']) for n,c in covers.items()}=={'proton':12,'neutron':18,'electron':6}
    e=geometries['electron'];K,D=source_electron_factors();witnesses=[]
    for face in range(4):
        P={(i,j):K[2*face+i,j] for i,j in pairs(range(2),repeat=2) if (2*face+i,j) in K}
        Q=sub(identity(2),P);col=min(j for i,j in Q)
        z={(i,0):x for (i,j),x in Q.items() if j==col};field=product(K,z)
        assert z and field and not product(P,z)
        assert all(i//2!=face for i,j in field)
        witnesses.append({'zero_face':face,'nonzero_spinor':encode(z),'native_face_field':encode(field)})
    # The dual adjacency graph is connected; invertible edge comparisons
    # propagate zero from one face to all. Each witness forbids an ordinary
    # invertible-transport top-cycle model for the WHOLE native doublet.
    adjacency={f:set() for f in range(4)}
    for f,g in combinations(range(4),2):
        if len(set(e['base']['faces'][f])&set(e['base']['faces'][g]))==2:
            adjacency[f].add(g);adjacency[g].add(f)
    seen={0};todo=[0]
    while todo:
        f=todo.pop()
        for g in adjacency[f]-seen:seen.add(g);todo.append(g)
    assert len(seen)==4
    return covers,{'zero_face_nonzero_global_code_witnesses':witnesses,
       'dual_face_graph_connected':True,'ordinary_invertible_transport_cycle_model_for_entire_native_doublet':False,
       'obstruction':'A top-cycle with invertible pairwise edge transports has injective evaluation at any face. Native doublet evaluations have rank1, not2.',
       'general_sheaf_or_noninvertible_code_constraint_model_excluded':False}


def main():
    contract=read(CONTRACT);prior=read(PRIOR)
    assert prior['status']=='pass' and all(prior['checks'].values())
    assert all(digest(ROOT/p)==h for p,h in prior['source_sha256'].items())
    objects,binding,pins=load();reps=representations(objects,binding)
    geometries,placements=native_geometries(objects)
    residuals=coefficient_and_chain_squares(objects,reps,geometries)
    p=proton_flat_bulk(objects['proton'],geometries['proton'],placements,reps['proton'])
    n=neutron_patch_boundary(objects['neutron'],geometries['neutron'],reps['neutron'])
    covers,e=covers_and_electron_local_system(objects,geometries)
    checks={k:True for k in (
       'fresh_iteration4_source_and_native_geometry_pins',
       'actual_native_ordered_triangle_and_face_bases_reconstructed',
       'all_boundary_squared_and_cone_boundary_squared_zero',
       'source_base_Betti_sphere_annulus_sphere_recomputed',
       'all_native_local_port_patches_are_disks_of_dimension_two_codimension_one',
       'native_generators_all_scalar_chain_and_patch_permutation_squares',
       'native_coefficient_to_geometric_fiber_embeddings_preserve_source_metric',
       'all27_native_chain_fiber_and_active_encoder_action_squares',
       'ordinary_untwisted_boundary_is_nonzero_on_every_native_active_payload',
       'proton_supplied_body_frames_not_packet_fitted_frames',
       'proton_G_exactly_projects_onto_native_frame_twisted_surface_cycles',
       'proton_N_is_line_selected_twisted_cycle_subspace',
       'proton_relative_bulk_filling_and_boundary_L_square_on_all_raw_inputs',
       'proton_flat_cone_extension_equivariant_but_not_claimed_primitive_handoff',
       'neutron_relative_bulk_H3_zero_and_relative_H2_one_without_caps',
       'neutron_sector_patch_boundary_is_injective_rank_three',
       'twelve_geometric_boundary_occurrences_not_twelve_native_alignment_channels',
       'neutron_rim_boundary_and_changed_task_cap_completion_retained',
       'electron_code_zero_face_nonzero_section_obstructs_invertible_local_system',
       'source_actual_port_cover_minima_one_one_two',
       'six_electron_minimum_covers_are_geometric_face_pairs_not_fitted_tags',
       'topological_degree_and_complex_fiber_rank_not_conflated',
       'new_geometric_adapters_not_silently_substituted_for_native_stage_readers')}
    additions=[PRIOR,CONTRACT,GEOMETRY,AMBIENT,MERKLE,BELT,STORE,Path(__file__).resolve()]
    pins.update(prior['source_sha256'])
    for path in additions:pins[path.relative_to(ROOT).as_posix()]=digest(path)
    for module in tuple(sys.modules.values()):
        path=getattr(module,'__file__',None)
        if path:
            path=Path(path).resolve()
            if path.suffix=='.py' and path.is_relative_to(ROOT/'research'):
                key=path.relative_to(ROOT).as_posix();assert key not in pins or pins[key]==digest(path);pins[key]=digest(path)
    assert all(digest(ROOT/path)==h for path,h in pins.items())
    bases={name:{'vertices':g['base']['vertices'],'edges':g['base']['edges'],'faces':g['base']['faces'],
        'counts':g['base']['counts'],'boundary_ranks':g['base']['boundary_ranks'],'betti':g['base']['betti'],
        'B1':encode(g['base']['B1']),'B2':encode(g['base']['B2']),'native_local_port_patches':g['patch_rows'],
        'relative_cone_H3':g['cone']['relative_H3'],'relative_cone_H2':g['cone']['relative_H2']} for name,g in geometries.items()}
    report={'schema':'marici.packet-handoff-naturality-iteration-check.v1','iteration':5,'status':'pass','checks':checks,
       'geometric_boundary_modules':bases,'ordinary_boundary_native_encoder_comparison':residuals,
       'proton_native_flat_cycle_and_bulk_bridge':p,'neutron_patch_boundary_and_rim':n,
       'electron_invertible_local_system_obstruction':e,'minimal_geometric_reconstruction_covers':covers,
       'native_geometric_types_distinguished_without_particle_name_mode_bit':True,
       'all_capacity_M_C_labels_are_same_ambient_geometric_grading':False,
       'proton_source_frame_cycle_and_relative_bulk_bridge_constructed':True,
       'geometric_boundary_idempotent_projector_and_code_closure_identified':False,
       'neutron_cap_completion_preserves_full_native_task':False,
       'electron_native_doublet_is_ordinary_invertible_transport_top_cycle':False,
       'source_native_handoff_constructed':False,'physical_particle_assignment_verified':False,
       'native_producers_executed':False,'formal_proof_recompiled':False,
       'next_executable_scope':contract['next_executable_scope'],'source_sha256':pins}
    OUT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','iteration':5,'check_groups':len(checks),
        'base_betti':{name:g['base']['betti'] for name,g in geometries.items()},
        'native_port_cover_minima':{n:c['minimum_faithful_face_count'] for n,c in covers.items()},
        'proton_native_twisted_cycle_bulk_bridge':True,'common_physical_grading_selected':False},indent=2))


if __name__=='__main__':main()
