"""General fan identity, native character sewing, and full-source role descent.
No native producer entrypoint or pure producer function is executed.
"""
import sys
import json
from itertools import product as tuples
from pathlib import Path
from check_packet_handoff_naturality_09 import (ROOT,A,F,ZERO,ONE,CI,S3,OMEGA,product,plus,scaled,encode,
    identity,invert,sub,adj,trace,rank,closure,key,vec,norm,xyz,val,digest,read,load,representations,
    native_geometries,independent_encoders,block,conj,qmode,stack,diag,projector,witness,geometry_action,native_from_geometry)

CONTRACT=ROOT/'research/strominger/contracts/packet-handoff-naturality-10.v1.json'
PRIOR=ROOT/'research/strominger/results/packet-handoff-naturality-09-v1.json'
OUT=ROOT/'research/strominger/results/packet-handoff-naturality-10-v1.json'
CORRECTION=ROOT/'research/strominger/contracts/packet-handoff-naturality-10-scope-correction.v1.json'


def mm(*ms):
    out=ms[0]
    for m in ms[1:]:out=product(out,m)
    return out
def bilinear(v,H):return trace(mm(adj(conj(v)),H,v))
def irank(P):
    t=trace(P);assert not any(t.c[1:]) and t.c[0].denominator==1
    return int(t.c[0])
def branch_scalar(N,J):return trace(mm(N,J,conj(N),invert(J,len({i for i,j in J}))))/A(irank(N))
def branch_map(n,name):return identity(n) if name!='electron' else {(2*f+i,2*f+j):x for f in range(4) for i,j,x in ((0,1,ONE),(1,0,-ONE))}
def signature(v):return [v['n']]+[irank(v['ops'][s]) for s in 'LGN']
def original(name,o,data):
    return {'name':name,'kind':'native','n':o['n'],'D':diag([A(x) for x in o['metric']]),'ops':o['ops'],
            'K':data[name]['K'],'E':data[name]['E'],'frames':{s:(o['f'][s]['K'],o['f'][s]['D']) for s in 'LG'},'J':branch_map(o['n'],name)}
def twist(base,T,label):
    Ti=invert(T,base['n']);ops={s:mm(T,p,Ti) for s,p in base['ops'].items()}
    return base|{'kind':label,'ops':ops,'K':product(T,base['K']),
                 'frames':{s:(product(T,K),product(D,Ti)) for s,(K,D) in base['frames'].items()}}
def check_protocol(v,reps):
    ops=v['ops'];n=v['n'];D=v['D']
    assert mm(ops['L'],ops['G'])==mm(ops['G'],ops['L'])==ops['N']
    for p in ops.values():
        assert product(p,p)==p and product(adj(p),D)==product(D,p)
        assert product(p,v['K'])==v['K']
        assert all(product(W,p)==product(p,W) for W in reps['raw'])
    assert rank(v['K'],n,irank(ops['N']))==irank(ops['N'])


def fan_identity(geometry,raw):
    # q_j = coefficient[0]*a + coefficient[1]*b, c=-a-b.
    w=OMEGA;w2=w*w;coeff=((w,w2),(-w2,w-w2),(w2-w,-w))
    B=(sum((a*a for a,b in coeff),ZERO),sum((A(2)*a*b for a,b in coeff),ZERO),sum((b*b for a,b in coeff),ZERO))
    H=(sum((a.flip(8)*a for a,b in coeff),ZERO),sum((a.flip(8)*b+b.flip(8)*a for a,b in coeff),ZERO),sum((b.flip(8)*b for a,b in coeff),ZERO))
    assert B==(A(-4),)*3 and H==(A(5),)*3
    rows={}
    for name in ('proton','neutron'):
        g=geometry[name];fans={}
        for t,c in enumerate(g['base']['faces']):fans.setdefault(c[0],[]).append((t,c))
        entries=[]
        for center,records in fans.items():
            assert len(records)==3
            edges={(c[1],c[2]) for t,c in records};vertices=sorted({k for e in edges for k in e})
            assert len(vertices)==3 and all(sum(a==k for a,b in edges)==sum(b==k for a,b in edges)==1 for k in vertices)
            mean=scaled(A(F(1,3)),plus(*(vec(g['points'][k]) for k in vertices)))
            assert mean==vec(g['points'][center])
            S=sum((norm(sub(vec(g['points'][k]),mean)) for k in vertices),ZERO)
            qs=[qmode([g['points'][k] for k in c]) for t,c in records]
            rho=sum((norm(q) for q in qs),ZERO);beta=sum((bilinear(q,identity(3)) for q in qs),ZERO)
            assert rho==A(F(5,2))*S and beta==-A(2)*S and S!=ZERO
            entries.append({'face_center':center,'ports':[t for t,c in records],'norm':rho.record(),'bilinear':beta.record()})
        u=raw[name]['u'];rho=trace(mm(adj(u),raw[name]['D'],u));beta=bilinear(u,raw[name]['D'])
        assert beta==-A(F(4,5))*rho and branch_scalar(raw[name]['N'],identity(36))==A(F(16,25))
        rows[name]={'fans':entries,'native_bilinear_over_norm':(beta/rho).record(),'native_overlap':{'0':'16/25'}}
    return {'symbolic_Gram_variables':['a.a','a.b','b.b'],'bilinear_coefficients':[x.record() for x in B],
        'Hermitian_coefficients':[x.record() for x in H],
        'general_formula':'sum q_j^T q_j=-2 S; sum q_j* q_j=5 S/2; chi=16/25 for S=sum ||vertex-centroid||^2>0',
        'scope':'Any complete coherent directed centroid-edge fan in a real positive metric, and orthogonal sums with real weights/common global phase. Not arbitrary relative complex sewing.',
        'native_comparisons':rows}


def neutron_face_phases(base,reps,g,raw):
    group=closure(reps['V'],3,3);centers=sorted({c[0] for c in g['base']['faces']})
    chosen={geometry_action(g,R)[2][centers[0]] for R in group};assert len(chosen)==3 and len(centers)==6
    part={k:x for k,x in raw['q'].items() if g['base']['faces'][k[0]//3][0] in chosen};other=sub(raw['q'],part)
    rho=norm(part);assert rho==norm(other) and not product(adj(part),other)
    assert bilinear(part,identity(54))==bilinear(other,identity(54))==-A(F(4,5))*rho
    variants=[];reports=[]
    for label,z,expected in (('face_phase_one',ONE,A(F(16,25))),('face_phase_minus_one',-ONE,A(F(16,25))),
                              ('face_phase_i',CI,ZERO),('face_phase_omega',OMEGA,A(F(4,25)))):
        phases=[z if c[0] in chosen else ONE for c in g['base']['faces']]
        Tw=diag([x for x in phases for _ in range(3)]);T=mm(raw['Eleft'],Tw,raw['E'])
        assert mm(adj(T),base['D'],T)==base['D'] and all(product(T,W)==product(W,T) for W in reps['raw'])
        v=twist(base,T,label);check_protocol(v,reps)
        assert v['ops']['G']==base['ops']['G'] and signature(v)==signature(base)
        assert all(len(v['ops'][s])==len(base['ops'][s]) for s in 'LGN')
        q=product(Tw,raw['q'])
        assert all(projector(block(q,3*t,3),identity(3))==projector(block(raw['q'],3*t,3),identity(3)) for t in range(18))
        scalar=branch_scalar(v['ops']['N'],v['J'])
        predicted=A(F(16,25))*(ONE+z*z)*(ONE+z.flip(8)*z.flip(8))/A(4)
        assert scalar==predicted==expected
        delta={s:rank(sub(v['ops'][s],base['ops'][s]),36,36) for s in 'LGN'}
        if z!=ONE:assert delta=={'L':6,'G':0,'N':2}
        if z==CI:
            assert not product(v['ops']['N'],conj(v['ops']['N']))
            assert not product(v['ops']['L'],conj(v['ops']['L']))
        reports.append({'variant':label,'phase':z.record(),'overlap':scalar.record(),'reader_residual_ranks':delta,
            'N_reader_witness':witness(base['ops']['N'],v['ops']['N'],36) if z!=ONE else None})
        if z!=ONE:variants.append(v)
    return variants,{'selected_C3_face_orbit':sorted(chosen),'equal_two_orbit_norm':rho.record(),
        'general_phase_formula':'chi(z)=16/25*|1+z^2|^2/4=(16/25)cos(theta)^2 for z=exp(i theta)',
        'same_native_G_actions_metric_local_lines_and_stage_supports':True,'variants':reports}


def characters(group):
    # Actual groups here are C3 or A4. Their involutions form the commutator kernel.
    I=identity(3);H=[g for g in group if product(g,g)==I]
    assert len(group) in (3,12) and len(H)*3==len(group)
    keysH={key(h) for h in H};a=next(g for g in group if key(g) not in keysH)
    powers=[I,a,product(a,a)];coset={key(product(p,h)):j for j,p in enumerate(powers) for h in H}
    assert len(coset)==len(group)
    for g,h in tuples(group,repeat=2):assert coset[key(product(g,h))]==(coset[key(g)]+coset[key(h)])%3
    chars=[{k:(ONE,OMEGA,OMEGA*OMEGA)[(j*power)%3] for k,j in coset.items()} for power in range(3)]
    # Certify that no other one-dimensional character is missed.
    comm={key(mm(g,h,adj(g),adj(h))):mm(g,h,adj(g),adj(h)) for g,h in tuples(group,repeat=2)}
    generated=closure(list(comm.values()),3,len(H));assert {key(h) for h in generated}==keysH
    return chars


def scalar_character_sewing(bases,reps,geometry,raw):
    report={};variants=[]
    for name,g in geometry.items():
        G=closure(reps[name]['V'],3,12 if name!='neutron' else 3) if name!='electron' else list({key(R):R for R in reps[name]['V']}.values())
        chars=characters(G);perms=[geometry_action(g,R)[0] for R in G]
        unseen=set(range(len(g['base']['faces'])));orbits=[]
        while unseen:
            t=min(unseen);orbit=sorted({p[t] for p in perms});unseen-=set(orbit);orbits.append(orbit)
        allowed=[];obstructions=[];branch_readers=[]
        for k,chi in enumerate(chars):
            phase={};bad=[]
            for orbit in orbits:
                t=orbit[0]
                for R,perm in zip(G,perms):
                    target=perm[t];z=chi[key(R)].flip(8)
                    if target in phase and phase[target]!=z:bad.append((t,target,key(R)))
                    phase[target]=z
            stabilizer_bad=[(t,key(R)) for orbit in orbits for t in (orbit[0],) for R,perm in zip(G,perms) if perm[t]==t and chi[key(R)]!=ONE]
            assert bool(bad)==bool(stabilizer_bad)
            if bad:obstructions.append({'character':k,'fixed_port':stabilizer_bad[0][0],'stabilizer_character':chi[stabilizer_bad[0][1]].record()});continue
            assert all(phase[p[t]]==chi[key(R)].flip(8)*phase[t] for R,p in zip(G,perms) for t in phase)
            allowed.append(k)
            if k and name!='electron':
                d=raw[name];Tw=diag([phase[t] for t in range(len(phase)) for _ in range(3)]);T=mm(d['Eleft'],Tw,d['E'])
                v=twist(bases[name],T,'global_character_'+str(k));check_protocol(v,reps[name])
                for R,W in zip(reps[name]['V'],reps[name]['raw']):
                    assert product(W,v['K'])==scaled(chi[key(R)],v['K'])
                    assert product(W,T)==scaled(chi[key(R)],product(T,W))
                if name=='proton':assert v['ops']['L']==bases[name]['ops']['L']
                assert not product(v['ops']['G'],bases[name]['ops']['G'])
                assert not product(v['ops']['N'],conj(v['ops']['N'])) and branch_scalar(v['ops']['N'],v['J'])==ZERO
                assert signature(v)==signature(bases[name]) and all(len(v['ops'][s])==len(bases[name]['ops'][s]) for s in 'LGN')
                branch_readers.append({'character':k,'reader_residual_ranks':{s:rank(sub(v['ops'][s],bases[name]['ops'][s]),v['n'],v['n']) for s in 'LGN'},'overlap':branch_scalar(v['ops']['N'],v['J']).record()})
                variants.append(v)
        report[name]={'branch_reader_residuals':branch_readers,'spatial_group_order':len(G),'all_spatial_linear_characters':3,'allowed_scalar_port_character_branches':allowed,
            'independent_unit_phases_per_allowed_character':len(orbits),'stabilizer_obstructions':obstructions}
    assert [len(report[n]['allowed_scalar_port_character_branches']) for n in ('proton','neutron','electron')]==[3,3,1]
    assert [report[n]['independent_unit_phases_per_allowed_character'] for n in ('proton','neutron','electron')]==[1,6,1]
    logical=reps['electron']['logical'];minus=scaled(-ONE,identity(2))
    assert len(logical)==24 and any(mm(u,v,adj(u),adj(v))==minus for u,v in tuples(logical,repeat=2))
    report['electron']['central_minus_is_an_actual_commutator']=True
    report['electron']['all_linear_spin_characters_factor_through_spatial_A4']=True
    return variants,report


def source_coordinate_transport(bases,reps):
    rows={}
    for name,v in bases.items():
        n=v['n'];phase=diag([CI]+[ONE]*(n-1));S=product(plus(identity(n),{(0,1):A(F(1,2))}),phase);Si=invert(S,n)
        assert any(sum(i==r for i,j in S)>1 for r in range(n))
        D=mm(adj(Si),v['D'],Si);E=product(v['E'],Si);J=mm(S,v['J'],conj(Si));Ji=invert(J,n)
        assert mm(adj(J),D,J)==conj(D)
        sign=-ONE if name=='electron' else ONE;assert product(J,conj(J))==scaled(sign,identity(n))
        changed={s:mm(S,p,Si) for s,p in v['ops'].items()}
        for s,p in changed.items():
            assert product(p,p)==p and product(adj(p),D)==product(D,p)
            assert mm(E,p,S)==product(v['E'],v['ops'][s])
        for W in reps[name]['raw']:
            Wnew=mm(S,W,Si);assert mm(E,Wnew,S)==product(v['E'],W)
            assert all(product(Wnew,p)==product(p,Wnew) for p in changed.values())
        before=branch_scalar(v['ops']['N'],v['J']);after=trace(mm(changed['N'],J,conj(changed['N']),Ji))/A(irank(changed['N']))
        naive=branch_scalar(changed['N'],v['J'])
        assert before==after
        rows[name]={'coordinate_map':encode(S),'transported_branch_map':encode(J),'full_raw_geometric_reader_and_native_action_squares':True,
            'branch_scalar_before':before.record(),'correctly_transported_scalar':after.record(),'untransported_branch_scalar':naive.record(),
            'naive_untransported_comparison_is_equal':naive==before}
    assert rows['proton']['naive_untransported_comparison_is_equal'] is False
    return rows


def role_descent(variants,reps):
    rows=[];partitions=[(0,0,0),(0,0,1),(0,1,0),(0,1,1),(0,1,2)]
    for v in variants:
        n=v['n'];ops=v['ops'];K=[identity(n)]+[v['frames'][s][0] for s in 'LG'];D=[identity(n)]+[v['frames'][s][1] for s in 'LG']
        dims=[n,irank(ops['L']),irank(ops['G'])];r=irank(ops['N'])
        roles=['M' if dims[1]<dims[2] else 'C']*2+['C' if dims[1]<dims[2] else 'M']
        T=[mm(D[(s+1)%3],ops['LGN'[s]],K[s]) for s in range(3)]
        for s in range(3):
            assert mm(K[(s+1)%3],T[s])==product(ops['LGN'[s]],K[s])
            active=product(D[s],v['K']);assert mm(K[s],active)==v['K']
            assert product(T[s],active)==product(D[(s+1)%3],v['K'])
        for W in reps[v['name']]['raw']:
            action=[mm(d,W,k) for d,k in zip(D,K)]
            assert all(product(W,k)==product(k,a) for k,a in zip(K,action))
            assert all(product(action[(s+1)%3],T[s])==product(T[s],action[s]) for s in range(3))
        windows=[]
        for start in range(3):
            phases=[start,(start+1)%3,(start+2)%3];s,t=phases[:2]
            assert mm(K[phases[-1]],T[t],T[s])==mm(ops['LGN'[t]],ops['LGN'[s]],K[start])
            windows.append({'initial_phase':start,'commands':['LGN'[s],'LGN'[t]],'roles':[roles[p] for p in phases],'dimensions':[dims[p] for p in phases]})
            cycle=identity(dims[start])
            for j in range(3):cycle=product(T[(start+j)%3],cycle)
            assert cycle==mm(D[start],ops['N'],K[start]) and irank(cycle)==r
            strobe=[(start+2*j)%3 for j in range(7)]
            assert all(any(roles[strobe[i]]!=roles[strobe[i+p]] for i in range(7-p)) for p in (1,2))
        valid=[q for q in partitions if all(q[a]!=q[b] or (roles[a]==roles[b] and q[(a+1)%3]==q[(b+1)%3]) for a,b in tuples(range(3),repeat=2))]
        assert valid==[(0,1,2)]
        # Classifier uses only frame-invariant ranks, never a species name.
        cls=1 if dims[1]<dims[2] else (2 if dims[2]==r else 0)
        rows.append({'source':v['name'],'variant':v['kind'],'joint_rank_signature':signature(v),'source_neutral_rank_class':cls,
            'all_native_action_and_full_reader_squares':True,'windows':windows,'minimal_primitive_phase_contexts':3,
            'two_atomic_arrow_strobe_role_period':3,'primitive_N_target_is_raw_dimension':n})
    policies=list(tuples(range(3),repeat=3));assert len(policies)==27
    desired={0:['C','M','C'],1:['M','C','M'],2:['M','C','C']}
    matches=[p for p in policies if all(r['windows'][p[r['source_neutral_rank_class']]]['roles']==desired[r['source_neutral_rank_class']] for r in rows)]
    assert matches==[(1,1,2)]
    return {'source_family_rectangular_protocols':rows,'source_neutral_origin_policies':[list(p) for p in policies],
        'all27_policies_preserve_frame_naturality_and_primitive_guards_when_origin_is_retained':True,
        'policy_matching_requested_words_if_those_words_are_imposed':[1,1,2],
        'naturality_selects_that_policy':False,'character_branch_selects_primitive_origin':False,
        'M_C_scope':'Source-neutral smaller/larger stage-image capacity convention and raw/local base-family role; not physical codimension or one fixed full state space.'}


def main():
    contract=read(CONTRACT);prior=read(PRIOR);correction=read(CORRECTION)
    assert digest(ROOT/correction['first_frozen_checker'])==correction['first_frozen_checker_sha256']
    assert prior['status']=='pass' and all(prior['checks'].values())
    assert all(digest(ROOT/p)==h for p,h in prior['source_sha256'].items())
    objects,binding,pins=load();reps=representations(objects,binding);geometry,placements=native_geometries(objects)
    data=independent_encoders(objects,geometry,placements);reconstruction,raw,vectors,Q,aux=native_from_geometry(objects,reps,geometry,placements,data)
    bases={n:original(n,o,data) for n,o in objects.items()}
    fan=fan_identity(geometry,raw)
    nvariants,nphase=neutron_face_phases(bases['neutron'],reps['neutron'],geometry['neutron'],raw['neutron'])
    cvariants,characters_report=scalar_character_sewing(bases,reps,geometry,raw)
    e=bases['electron'];J=e['J'];Ji=invert(J,8)
    eplus=e|{'kind':'opposite_Pauli_polarity','ops':{s:mm(J,conj(p),Ji) for s,p in e['ops'].items()},'K':product(J,conj(e['K'])),
        'frames':{s:(product(J,conj(K)),product(conj(D),Ji)) for s,(K,D) in e['frames'].items()}}
    variants=list(bases.values())+nvariants+cvariants+[eplus]
    for v in variants:check_protocol(v,reps[v['name']])
    transports=source_coordinate_transport(bases,reps);roles=role_descent(variants,reps)
    checks={k:True for k in (
        'fresh_iteration9_receipt_and_all_source_pins','general_zero_sum_face_bilinear_coefficient_identity',
        'general_zero_sum_face_Hermitian_coefficient_identity','complete_fan_positive_metric_ratio_minus_four_fifths',
        'all_actual_four_proton_and_six_neutron_fans_match_general_identity','native_raw_metric_return_overlap_sixteen_twentyfifths',
        'real_weighted_orthogonal_fan_sum_has_the_same_ratio','two_disjoint_face_orbits_give_exact_general_complex_phase_formula',
        'actual_neutron_two_C3_face_orbits_have_equal_norm','neutron_i_phase_return_and_its_conjugate_are_orthogonal',
        'neutron_face_phase_preserves_original_metric_native_G_and_all_native_actions','every_local_projector_and_stage_support_is_preserved',
        'phases_one_minus_one_i_omega_have_predicted_overlaps','same_overlap_minus_one_rival_still_has_changed_full_raw_reader',
        'all_actual_C3_and_A4_character_tables_multiply_exactly','commutator_quotients_and_spin_central_commutator_make_character_list_exhaustive',
        'port_stabilizer_criterion_constructs_or_refutes_each_character_phase','allowable_character_branches_three_three_one',
        'nontrivial_proton_global_characters_are_constructed_without_changing_local_L','twisted_baryon_returns_are_conjugate_orthogonal_and_G_orthogonal_to_native_G',
        'all_character_twists_keep_native_ranks_and_stage_supports','all_declared_rivals_commute_with_original_native_geometry_actions',
        'local_corner_character_global_spatial_character_and_primitive_occurrence_remain_distinct',
        'explicit_nonmonomial_complex_source_coordinate_adapters','metric_and_antilinear_branch_map_transport_with_correct_square',
        'full_raw_preparation_geometric_reader_squares_under_coordinate_transport','all_native_action_attachment_transport_squares',
        'correct_branch_scalar_is_coordinate_invariant','untransported_conjugation_counterexample_is_retained',
        'all_native_and_rival_rectangular_primitive_maps_constructed','all_two_arrow_windows_keep_full_raw_N_target',
        'all_rectangular_native_action_squares','capacity_role_windows_survive_character_phase_and_polarity_rivals',
        'all_five_phase_partitions_reject_nontrivial_role_successor_quotient','all_twentyseven_rank_defined_origin_policies_are_source_natural',
        'requested_origins_one_one_two_are_conditional_not_selected_by_naturality')}
    pins.update(prior['source_sha256'])
    for p in (CONTRACT,PRIOR,CORRECTION,ROOT/correction['first_frozen_checker'],ROOT/correction['failed_freeze'],Path(__file__).resolve()):pins[p.relative_to(ROOT).as_posix()]=digest(p)
    for module in tuple(sys.modules.values()):
        path=getattr(module,'__file__',None)
        if path:
            p=Path(path).resolve()
            if p.suffix=='.py' and p.is_relative_to(ROOT/'research'):
                rel=p.relative_to(ROOT).as_posix();assert rel not in pins or pins[rel]==digest(p);pins[rel]=digest(p)
    assert all(digest(ROOT/p)==h for p,h in pins.items())
    report={'schema':'marici.packet-handoff-naturality-iteration-check.v1','iteration':10,'status':'pass','checks':checks,
        'scope_correction':correction,'general_centroid_fan_coefficient_certificate':fan,'neutron_native_covariant_face_phase_family':nphase,
        'scalar_port_character_and_stabilizer_classification':characters_report,'full_source_coordinate_naturality':transports,
        'source_branch_and_primitive_role_descent':roles,
        'general_coherent_centroid_fan_identity_constructed':True,'zero_overlap_uniquely_selects_electron_like_role':False,
        'branch_scalar_alone_determines_full_preparation_task':False,'full_source_metric_reader_and_antilinear_transport_constructed':True,
        'projective_character_twists_are_original_native_protocol':False,'conditional_capacity_role_windows_are_natural_with_retained_origin':True,
        'source_naturality_selects_proposed_indexed_origins':False,'stationary_two_atomic_arrow_law_constructed':False,
        'physical_M_C_grading_constructed':False,'source_native_handoff_constructed':False,'physical_particle_assignment_verified':False,
        'native_producer_entrypoints_executed':False,'pure_proton_assembler_executed_in_memory':False,'formal_proof_recompiled':False,
        'scope_disposition':'General geometric fan identity and full-source naturality constructed; scalar/character selection of indexed roots rejected. Current primitive-source role investigation is disposed, not a physical particle identification.',
        'reopening_gate':['Independent source-supported physical carrier-relative M/C grading','Independent observation/reset/event-boundary policy or changed native primitive source'],
        'source_sha256':pins}
    OUT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','iteration':10,'check_groups':len(checks),'general_fan_identity':'16/25',
        'neutron_face_phase_overlaps':{r['variant']:r['overlap'] for r in nphase['variants']},
        'character_branches':{n:r['allowed_scalar_port_character_branches'] for n,r in characters_report.items()},
        'rectangular_source_protocols':len(roles['source_family_rectangular_protocols']),'natural_origin_policies':27},indent=2))

if __name__=='__main__':main()
