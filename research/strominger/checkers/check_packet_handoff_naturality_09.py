"""Directed-character reconstruction and full-reader erasure hostiles.
Exact retained-source arithmetic; only a pure proton function runs in memory.
"""
import sys
import json
from pathlib import Path
from check_packet_handoff_naturality_08 import (ROOT,A,F,ZERO,ONE,CI,S3,OMEGA,product,plus,scaled,encode,
    identity,invert,sub,adj,trace,rank,closure,key,vec,norm,xyz,val,digest,read,load,representations,
    native_geometries,independent_encoders,block,point_key,conj,triangle)
from check_packet_handoff_naturality_03 import pure_proton,PINPUT,PHASES,complex_weight
from check_packet_handoff_naturality_05 import GEOMETRY
import assemble_triangle_arrow_source as proton_source

CONTRACT=ROOT/'research/strominger/contracts/packet-handoff-naturality-09.v1.json'
PRIOR=ROOT/'research/strominger/results/packet-handoff-naturality-08-v1.json'
OUT=ROOT/'research/strominger/results/packet-handoff-naturality-09-v1.json'


def stack(vs):return {(3*t+i,0):x for t,v in enumerate(vs) for (i,j),x in v.items()}
def projector(v,H):return scaled(ONE/trace(product(adj(v),product(H,v))),product(v,product(adj(v),H)))
def diag(values):return {(i,i):x for i,x in enumerate(values) if x!=ZERO}
def qmode(points):return vec(sum((p[i]*z for p,z in zip(points,(ONE,OMEGA,OMEGA*OMEGA))),ZERO) for i in range(3))
def frame_matrix(points):return {(i,j):p[i] for j,p in enumerate(points) for i in range(3) if p[i]!=ZERO}
def witness(old,new,n):
    difference=sub(old,new);j=next(j for i,j in difference);v={(j,0):ONE}
    assert product(old,v)!=product(new,v)
    return {'raw_input':encode(v),'old_output':encode(product(old,v)),'new_output':encode(product(new,v)),'difference_rank':rank(difference,n,n)}
def geometry_action(g,R):
    lookup={point_key(p):k for k,p in g['points'].items()};faces={frozenset(c):i for i,c in enumerate(g['base']['faces'])}
    rename={k:lookup[point_key(xyz(product(R,vec(p))))] for k,p in g['points'].items()}
    perm=[faces[frozenset(rename[k] for k in c)] for c in g['base']['faces']]
    W={(3*t+i,3*s+j):x for s,t in enumerate(perm) for (i,j),x in R.items()}
    return perm,W,rename


def native_from_geometry(objects,reps,geometry,placements,data):
    Q={};vectors={};raw={};result={};aux={}
    for name in ('proton','neutron'):
        g=geometry[name];qs=[qmode([g['points'][k] for k in c]) for c in g['base']['faces']]
        vectors[name]=qs;Q[name]=[projector(q,identity(3)) for q in qs]
        o=objects[name];E=data[name]['E'];D=diag([A(x) for x in o['metric']]);Eleft=product(diag([ONE/A(x) for x in o['metric']]),adj(E))
        q=stack(qs);u=product(Eleft,q);assert product(E,u)==q
        native=data[name]['Kgeo'];i=next(i for i,j in q);alpha=val(native,i)/val(q,i)
        assert native==scaled(alpha,q)
        if name=='proton':
            X=[frame_matrix([g['points'][k] for k in c]) for c in g['base']['faces']];Xi=invert(X[0],3)
            rotations=[product(x,Xi) for x in X]
            Rsrc=[{(i,j):A(F(x)) for i,row in enumerate(p['rotation']) for j,x in enumerate(row) if F(x)} for p in placements]
            assert all(R==product(S,adj(Rsrc[0])) for R,S in zip(rotations,Rsrc))
            assert all(product(adj(R),R)==identity(3) and product(R,qs[0])==v for R,v in zip(rotations,qs))
            L={(3*t+i,3*t+j):x for t,p in enumerate(Q[name]) for (i,j),x in p.items()}
            G={(3*t+i,3*s+j):x/A(12) for t,R in enumerate(rotations) for s,S in enumerate(rotations) for (i,j),x in product(R,adj(S)).items()}
            corner={(i,j):A(x) for i,row in enumerate(proton_source.C) for j,x in enumerate(row) if x}
            extension=[]
            for t,x in enumerate(X):
                C=product(x,product(corner,invert(x,3)));center=scaled(A(F(1,3)),plus(*(vec(g['points'][k]) for k in g['base']['faces'][t])))
                centered=triangle([g['points'][k] for k in g['base']['faces'][t]])
                delta=sub(C,product(centered['C'],centered['C']))
                assert product(C,qs[t])==scaled(OMEGA,qs[t]) and product(C,center)==center
                assert not product(delta,centered['P']) and rank(delta,3,3)==1
                extension.append({'port':t,'homogeneous_minus_centered_inverse':encode(delta),'rank':1})
            aux['proton_extension']=extension
        else:
            geo=read(GEOMETRY);panels=geo['belt_faces'];centers=['F_'+'_'.join(sorted(f)) for f in panels]
            owners=[centers.index(c[0]) for c in g['base']['faces']]
            R={(0,2):ONE,(1,0):ONE,(2,1):ONE};perm,W,rename=geometry_action(g,R)
            assert key(R) in {key(r) for r in closure(reps[name]['V'],3,3)}
            faceperm=[next(j for j,f in enumerate(panels) if set(f)=={rename[k] for k in panel}) for panel in panels]
            adjacent=[j for j in range(1,6) if len(set(panels[0])&set(panels[j]))==2]
            assert len(adjacent)==2;matchings=[]
            for j in adjacent:
                pair=(0,j);matching=[]
                for _ in range(3):matching.append(pair);pair=tuple(faceperm[k] for k in pair)
                assert sorted(k for p in matching for k in p)==list(range(6));matchings.append(matching)
            reference=[t for t,a in enumerate(owners) if a in matchings[0][0]]
            order=reference+[perm[t] for t in reference]+[perm[perm[t]] for t in reference]
            assert len(reference)==6 and sorted(order)==list(range(18))
            Enew={};dnew=[];unew={}
            for slot,t in enumerate(order):
                real=scaled(A(F(1,2)),plus(qs[t],conj(qs[t])));imag=scaled(ONE/(A(2)*CI*S3),sub(qs[t],conj(qs[t])))
                aa=norm(imag);bb=trace(product(adj(real),imag));v=sub(real,scaled(bb/aa,imag));beta=norm(v)
                assert all(x.c[0]>0 and all(c==0 for c in x.c[1:]) for x in (aa,beta))
                assert not product(adj(v),imag)
                for axis,(column,d) in enumerate(((imag,aa),(v,beta))):
                    dnew.append(d);Enew.update({(3*t+i,2*slot+axis):x/d for (i,j),x in column.items()})
                unew[2*slot,0]=bb+CI*S3*aa;unew[2*slot+1,0]=beta
            assert Enew==E and diag([ONE/x for x in dnew])==D and unew==u==data[name]['K']
            Araw=product(Eleft,product(W,E));assert product(E,Araw)==product(W,E)
            G=scaled(A(F(1,3)),plus(identity(o['n']),Araw,product(Araw,Araw)))
            alternatives=[]
            for matching in matchings:
                patch_fields=[];patches=[]
                for pair in matching:
                    ids=[t for t,a in enumerate(owners) if a in pair];patches.append(ids)
                    field={k:x for k,x in q.items() if k[0]//3 in ids};patch_fields.append(product(Eleft,field))
                PL=plus(*(projector(k,D) for k in patch_fields))
                assert product(G,PL)==product(PL,G)==projector(u,D)
                alternatives.append({'patches':patches,'L':PL})
            L=alternatives[0]['L'];other=alternatives[1]['L']
            assert L!=other and rank(sub(L,other),o['n'],o['n'])==4
            assert len(L)==len(other)==432
            aux['neutron_matching']={'matchings':matchings,'patches':[r['patches'] for r in alternatives],
                'same_G_and_N':True,'same_original_metric_and_geometry':True,'L_reader_witness':witness(L,other,o['n'])}
        N=projector(u,D)
        assert [L,G,N]==[o['ops'][s] for s in 'LGN'] and product(L,G)==product(G,L)==N
        raw[name]={'L':L,'G':G,'N':N,'q':q,'u':u,'D':D,'E':E,'Eleft':Eleft}
        result[name]={'native_vector_to_geometric_Fourier_global_scale':alpha.record(),
            'all_L_G_N_reconstructed_on_all_raw_inputs':True,'no_per_port_phase_fit':True,
            'stage_supports':{s:len(m) for s,m in zip('LGN',(L,G,N))}}
    return result,raw,vectors,Q,aux


def reverse_proton(o):
    source=read(PINPUT);original,rows=pure_proton(source)
    inverted=json.loads(json.dumps(source));inverted['arrows']=[list(reversed(e)) for e in source['arrows']]
    reversed_report,reversed_rows=pure_proton(inverted);labels=o['source']['source']['coordinates']
    def restore(records,reverse):
        maps=[{} for _ in range(3)]
        for a in records:
            s=a['source'];t=a['target'];edge_s=s[1][::-1] if reverse else s[1];edge_t=t[1][::-1] if reverse else t[1]
            j=labels.index(edge_s+':'+s[2]);i=labels.index(edge_t+':'+t[2]);k=PHASES.index(s[0])
            assert t[0]==PHASES[(k+1)%3]
            maps[k][i,j]=complex_weight(a['weight_real'],a['weight_imag_sqrt3'])
        return maps
    assert restore(rows,False)==[o['ops'][s] for s in 'LGN']
    assert restore(reversed_rows,True)==[conj(o['ops'][s]) for s in 'LGN']
    assert len(rows)==len(reversed_rows)==1836
    return {'original_typed_transfers':len(rows),'reversed_typed_transfers':len(reversed_rows),
        'reversed_outer_edge_port_adapter':'new edge ba is compared with original ab',
        'entire_reversed_protocol_equals_conjugate_after_port_adapter':True,
        'source_arrow_reversal_is_not_the_same_directed_input':True}


def orbit_phase_tests(objects,reps,geometry,data,raw):
    census={};permutations_by_name={}
    for name,g in geometry.items():
        group=closure(reps[name]['V'],3,12 if name=='proton' else 3) if name!='electron' else reps[name]['V']
        perms=[geometry_action(g,R)[0] for R in group];permutations_by_name[name]=perms
        unseen=set(range(len(g['base']['faces'])));orbits=[]
        while unseen:
            t=min(unseen);orbit=sorted({p[t] for p in perms});unseen-=set(orbit);orbits.append(orbit)
        census[name]={'port_orbits':orbits,'scalar_equivariant_phase_parameters':len(orbits),'relative_phase_parameters_mod_global':len(orbits)-1}
    assert [len(census[n]['port_orbits']) for n in ('proton','neutron','electron')]==[1,6,1]
    d=raw['neutron'];n=objects['neutron']['n'];orbit=census['neutron']['port_orbits'][0]
    phases=[OMEGA if t in orbit else ONE for t in range(18)];Tworld=diag([z for z in phases for _ in range(3)])
    T=product(d['Eleft'],product(Tworld,d['E']));Ti=conj(T)
    assert product(T,Ti)==identity(n) and product(adj(T),product(d['D'],T))==d['D']
    assert product(T,d['G'])==product(d['G'],T)
    assert all(product(T,W)==product(W,T) for W in reps['neutron']['raw'])
    L=product(T,product(d['L'],Ti));N=product(T,product(d['N'],Ti))
    assert product(L,d['G'])==product(d['G'],L)==N
    assert len(L)==len(d['L']) and len(N)==len(d['N'])
    assert rank(sub(L,d['L']),n,n)==6 and rank(sub(N,d['N']),n,n)==2
    changed_q=product(Tworld,d['q']);assert changed_q!=d['q']
    assert all(projector(block(changed_q,3*t,3),identity(3))==projector(block(d['q'],3*t,3),identity(3)) for t in range(18))
    return {'native_port_phase_orbit_census':census,'neutron_nonconstant_orbit_phase':{'changed_triangle_orbit':orbit,
        'phase':OMEGA.record(),'source_metric_G_and_native_actions_preserved':True,'all_local_selected_projectors_preserved':True,
        'stage_supports_preserved':True,'L_difference_rank':6,'N_difference_rank':2,
        'fixed_geometric_Fourier_representatives_preserved':False,'N_reader_witness':witness(d['N'],N,n)}}


def inverse_characters(objects,reps,data):
    result={}
    for name in ('proton','neutron'):
        o=objects[name];D=diag([A(x) for x in o['metric']]);ops={s:conj(o['ops'][s]) for s in 'LGN'}
        assert product(ops['L'],ops['G'])==product(ops['G'],ops['L'])==ops['N']
        for s,p in ops.items():
            assert product(p,p)==p and product(adj(p),D)==product(D,p)
            assert all(conj(W)==W and product(W,p)==product(p,W) for W in reps[name]['raw'])
        assert ops['G']==o['ops']['G']
        ranks={s:rank(sub(ops[s],o['ops'][s]),o['n'],o['n']) for s in 'LGN'}
        assert ranks==({'L':24,'G':0,'N':2} if name=='proton' else {'L':6,'G':0,'N':2})
        result[name]={'inverse_character_residual_ranks':ranks,'conjugate_return_overlap':trace(product(ops['N'],o['ops']['N'])).record(),
            'native_metric_and_geometry_actions_preserved':True,'branch_reversal_antilinear_square':'+I',
            'not_an_original_fixed_reader_equivalence':True}
    o=objects['electron'];K=data['electron']['K'];P=[block(K,2*f,2) for f in range(4)];Pplus=[sub(identity(2),p) for p in P]
    assert plus(*Pplus)==scaled(A(2),identity(2))
    Kplus={(2*f+i,j):x for f,p in enumerate(Pplus) for (i,j),x in p.items()}
    Lplus={(2*f+i,2*f+j):x for f,p in enumerate(Pplus) for (i,j),x in p.items()};Nplus=scaled(A(F(1,2)),product(Kplus,adj(Kplus)))
    assert product(Nplus,Nplus)==Nplus and trace(Nplus)==A(2) and not product(o['ops']['N'],Nplus)
    assert rank(sub(Lplus,o['ops']['L']),8,8)==8 and rank(sub(Nplus,o['ops']['N']),8,8)==4
    eps={(0,1):ONE,(1,0):-ONE};T={(2*f+i,2*f+j):x for f in range(4) for (i,j),x in eps.items()}
    assert product(T,conj(T))==scaled(-ONE,identity(8)) and product(adj(T),T)==identity(8)
    for s,positive in (('L',Lplus),('G',Nplus),('N',Nplus)):
        assert positive==product(T,product(conj(o['ops'][s]),adj(T)))
        for W in reps['electron']['raw']:
            assert product(T,conj(W))==product(W,T) and product(W,positive)==product(positive,W)
    H=sub(identity(8),scaled(A(2),o['ops']['L']))
    assert product(H,o['ops']['N'])==scaled(-ONE,o['ops']['N']) and product(H,Nplus)==Nplus
    result['electron']={'opposite_Pauli_polarity_residual_ranks':{'L':8,'G':4,'N':4},'opposite_rank2_returns_are_orthogonal':True,
        'all24_native_geometry_action_squares':True,'branch_reversal_antilinear_square':'-I',
        'native_negative_vs_positive_polarization_eigenvalues':[-1,1],'branch_reversal_is_a_given_complex_linear_primitive':False}
    return result


def seam_tests(geometry,vectors,raw):
    rows={}
    for name in ('proton','neutron'):
        qs=vectors[name];total=sum((norm(v) for v in qs),ZERO);g=geometry[name];pairs=[]
        worldN=projector(stack(qs),identity(3*len(qs)))
        assert worldN==product(raw[name]['E'],product(raw[name]['N'],raw[name]['Eleft']))
        for i,c in enumerate(g['base']['faces']):
            for j,d in enumerate(g['base']['faces']):
                if i==j or len(set(c)&set(d))!=2:continue
                tau=scaled(ONE/norm(qs[j]),product(qs[i],adj(qs[j])))
                Nblock={(a-3*i,b-3*j):x for (a,b),x in worldN.items() if 3*i<=a<3*i+3 and 3*j<=b<3*j+3}
                assert tau==scaled(total/norm(qs[j]),Nblock) and product(tau,qs[j])==qs[i]
                pairs.append([i,j])
        rows[name]={'source_derived_directed_seam_comparisons':len(pairs),'no_phase_fitting_or_native_N_factorization_used':True}
    return rows


def main():
    contract=read(CONTRACT);prior=read(PRIOR)
    assert prior['status']=='pass' and all(prior['checks'].values())
    assert all(digest(ROOT/p)==h for p,h in prior['source_sha256'].items())
    assert complex_weight(*proton_source.OMEGA)==OMEGA
    objects,binding,pins=load();reps=representations(objects,binding);geometry,placements=native_geometries(objects)
    data=independent_encoders(objects,geometry,placements)
    reconstruction,raw,vectors,Q,aux=native_from_geometry(objects,reps,geometry,placements,data)
    reversal=reverse_proton(objects['proton']);phase=orbit_phase_tests(objects,reps,geometry,data,raw)
    inverse=inverse_characters(objects,reps,data);seams=seam_tests(geometry,vectors,raw)
    checks={k:True for k in (
      'fresh_iteration8_source_pins','positive_complex_character_matches_actual_source_constant',
      'all30_geometric_Fourier_vectors_fix_native_sewing_without_per_port_phase_fit',
      'proton_alignment_frames_derived_from_marked_vertex_matrices','complete_native_baryon_L_G_N_reconstructed_on_all_raw_inputs',
      'neutron_intrinsic_plane_embedding_reconstructed_from_real_imaginary_modes','neutron_native_denominators_and_raw_mode_numerators_recovered',
      'neutron_G_is_actual_C3_geometry_Reynolds_projector','both_geometric_adjacent_pair_matchings_cover_all_triangles',
      'neutron_matching_rival_same_G_N_metric_but_L_difference_rank4','explicit_matching_raw_L_reader_witness',
      'actual_proton_homogeneous_source_corner_character_omega',
      'homogeneous_source_cycle_equals_centered_inverse_on_tangent_plane','ambient_extension_difference_rank1_retained_at_all12_proton_ports',
      'original_pure_proton_constructor_recovers_every_typed_transfer','reversed_seed_arrows_give_conjugate_protocol_after_explicit_port_reversal',
      'inverse_character_baryon_protocols_are_metric_projectors','inverse_character_protocols_preserve_actual_native_geometry_actions',
      'inverse_character_full_native_L_N_residuals_are_nonzero','native_equivariant_port_phase_parameter_counts_one_six_one',
      'nonconstant_neutron_orbit_phase_is_metric_unitary_and_commutes_with_native_G_and_actions',
      'orbit_phase_preserves_every_local_line_and_stage_support','orbit_phase_changes_full_L_N_with_exact_ranks_six_two',
      'explicit_orbit_phase_raw_N_reader_witness','fixed_directed_geometric_mode_representatives_exclude_nonconstant_phase_rival',
      'both_electron_Pauli_polarities_give_tight_rank2_codes','opposite_electron_codes_are_orthogonal_with_rank4_return_difference',
      'electron_branch_reversal_is_equivariant_antiunitary_squaring_to_minus_identity',
      'retained_Pauli_polarization_reader_distinguishes_both_branches',
      'geometric_mode_seams_reproduce_normalized_native_N_blocks_without_phase_fit')}
    pins.update(prior['source_sha256'])
    for p in (CONTRACT,PRIOR,PINPUT,Path(__file__).resolve()):pins[p.relative_to(ROOT).as_posix()]=digest(p)
    for module in tuple(sys.modules.values()):
        path=getattr(module,'__file__',None)
        if path:
            p=Path(path).resolve()
            if p.suffix=='.py' and p.is_relative_to(ROOT/'research'):
                rel=p.relative_to(ROOT).as_posix();assert rel not in pins or pins[rel]==digest(p);pins[rel]=digest(p)
    assert all(digest(ROOT/p)==h for p,h in pins.items())
    report={'schema':'marici.packet-handoff-naturality-iteration-check.v1','iteration':9,'status':'pass','checks':checks,
      'full_native_geometric_reconstruction':reconstruction,'proton_directed_seed_reversal':reversal,
      'proton_homogeneous_versus_centered_corner_extensions':aux['proton_extension'],
      'neutron_geometric_matching_rival':aux['neutron_matching'],'native_phase_sewing_and_rival':phase,
      'inverse_character_and_Pauli_polarity_rivals':inverse,'source_derived_geometric_seam_comparisons':seams,
      'native_directed_geometric_full_stage_reconstruction_constructed':True,
      'native_sewing_requires_fitted_per_port_phases':False,'native_symmetry_and_local_lines_uniquely_determine_full_protocol':False,
      'neutron_geometric_pair_matching_is_unique':False,'opposite_electron_polarity_is_same_fixed_reader_task':False,
      'character_polarity_selects_primitive_phase_origin':False,'branch_reversal_antiunitary_is_given_complex_linear_primitive':False,
      'source_native_handoff_constructed':False,'physical_particle_assignment_verified':False,
      'pure_proton_assembler_executed_in_memory':True,'native_producer_entrypoints_executed':False,'formal_proof_recompiled':False,
      'next_executable_scope':contract['next_executable_scope'],'source_sha256':pins}
    OUT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','iteration':9,'check_groups':len(checks),'reconstruction':reconstruction,
      'port_phase_orbit_counts':{n:r['scalar_equivariant_phase_parameters'] for n,r in phase['native_port_phase_orbit_census'].items()},
      'neutron_matching_L_difference_rank':aux['neutron_matching']['L_reader_witness']['difference_rank'],
      'inverse_branch_residuals':inverse},indent=2))

if __name__=='__main__':main()
