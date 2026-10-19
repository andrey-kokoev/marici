"""Native faithful-cover gluing, six-edge atlas and marked-handoff tests.
Exact retained-source arithmetic only; no native producer entrypoint runs.
"""
from fractions import Fraction as F
from itertools import combinations,product as pairs
from math import factorial
from pathlib import Path
from hashlib import sha256
import json
import sys
from assemble_metric_coefficient_protocol import ROOT,A,ZERO,ONE,product,plus,scaled,encode
from check_port_incidence_conjectures import identity,invert
from check_packet_handoff_naturality_02 import load,sub,adj,column,trace,MERKLE,BELT
from check_packet_handoff_naturality_03 import History,replay,digest_source
from check_packet_handoff_naturality_04 import representations,rank,hom,key,SIGMA,S3
from check_packet_handoff_naturality_05 import native_geometries,native_embedding,point_key,chain_action,vec
from check_packet_stage_cost_comparison import source_electron_factors
from electron_packet_interface import STORE

CONTRACT=ROOT/'research/strominger/contracts/packet-handoff-naturality-06.v1.json'
PRIOR=ROOT/'research/strominger/results/packet-handoff-naturality-05-v1.json'
OUT=ROOT/'research/strominger/results/packet-handoff-naturality-06-v1.json'


def read(p):return json.loads(p.read_text(encoding='utf-8'))
def digest(p):return sha256(p.read_bytes()).hexdigest()
def restrict(cover,d):return {(d*t+i,d*f+i):ONE for t,f in enumerate(cover) for i in range(d)}
def block(m,start,d):return {(i-start,j):x for (i,j),x in m.items() if start<=i<start+d}
def scalar(row):
    c=[F(0)]*16
    for mask,x in zip((0,1,10,11),row):c[mask]=F(x)
    return A(tuple(c))


def independent_encoders(objects,geometries,placements):
    rotations=[{(i,j):A(F(x)) for i,row in enumerate(p['rotation']) for j,x in enumerate(row) if F(x)} for p in placements]
    L0={(i,j):x for (i,j),x in objects['proton']['ops']['L'].items() if i<3 and j<3}
    local=product(adj(rotations[0]),product(L0,rotations[0]));v=column(local)
    pK={(3*t+i,0):x for t,R in enumerate(rotations) for (i,j),x in product(R,v).items()}
    nK=vec([scalar(c['selected_numerator']) for c in read(BELT)['coordinates']])
    eK={}
    for f,n in enumerate(read(STORE)['normals']):
        normal=[A(F(x[0]))+S3*F(x[1]) for x in n]
        P=scaled(A(F(1,2)),sub(identity(2),plus(*(scaled(x,s) for x,s in zip(normal,SIGMA)))))
        assert product(P,P)==P and trace(P)==ONE
        eK.update({(2*f+i,j):x for (i,j),x in P.items()})
    assert eK==source_electron_factors()[0]
    data={}
    for name,K in (('proton',pK),('neutron',nK),('electron',eK)):
        o=objects[name];E=native_embedding(name,o);Kgeo=product(E,K);r=1 if name!='electron' else 2
        gram=product(adj(Kgeo),Kgeo);Dgeo=product(invert(gram,r),adj(Kgeo))
        # N enters ONLY this comparison, not the independent encoder construction.
        assert product(K,product(Dgeo,E))==o['ops']['N']
        data[name]={'K':K,'E':E,'Kgeo':Kgeo,'r':r,'gram':gram,'Dgeo':Dgeo}
    return data


def metric_gluing(objects,geometries,data,prior):
    results={}
    for name,g in geometries.items():
        d=g['fiber'];K=data[name]['Kgeo'];r=data[name]['r'];covers=prior['minimal_geometric_reconstruction_covers'][name]['minimal_covers']
        charts=[]
        for cover in covers:
            R=restrict(cover,d);E=product(R,K);S=product(adj(E),E);D=product(invert(S,r),adj(E))
            assert product(D,E)==identity(r)
            charts.append({'cover':cover,'R':R,'E':E,'S':S,'D':D,'reader':product(D,R)})
        multiplicities=[sum(f in c for c in covers) for f in range(len(g['base']['faces']))]
        assert len(set(multiplicities))==1
        total=plus(*(c['S'] for c in charts));assert total==scaled(A(multiplicities[0]),data[name]['gram'])
        totalinv=invert(total,r)
        weighted=plus(*(product(totalinv,product(c['S'],c['reader'])) for c in charts))
        uniform=scaled(A(F(1,len(charts))),plus(*(c['reader'] for c in charts)))
        assert weighted==data[name]['Dgeo']
        raw_decoder=product(weighted,data[name]['E']);N=product(data[name]['K'],raw_decoder)
        assert N==objects[name]['ops']['N']
        uniform_return=product(data[name]['K'],product(uniform,data[name]['E']))
        if name=='neutron':assert uniform_return!=N
        else:assert uniform_return==N
        for c in charts:
            for stage in 'LGN':
                assert product(c['R'],product(data[name]['E'],product(objects[name]['ops'][stage],data[name]['K'])))==c['E']
        results[name]={'cover_multiplicity':multiplicities[0],'native_return_reconstructed_on_all_raw_inputs':True,
            'encoder_provenance':{'proton':'supplied body frames and native local mode, not N','neutron':'actual selected geometric numerators, not N','electron':'native negative Pauli normal lines, not N'}[name],
            'source_gram':encode(data[name]['gram']),'chart_grams':[encode(c['S']) for c in charts],
            'metric_weights':[encode(product(totalinv,c['S'])) for c in charts],
            'uniform_average_is_native_return':uniform_return==N,
            'uniform_return_minus_native':encode(sub(uniform_return,N)),
            'all_stage_actions_on_active_chart_values_are_identity':True}
    return results


def electron_atlas(o,reps,geometry):
    K,Dglobal=source_electron_factors();I=identity(2);I4=identity(4);pairlist=list(combinations(range(4),2));charts=[]
    for p in pairlist:
        R=restrict(p,2);E=product(R,K);S=product(adj(E),E)
        det=S.get((0,0),ZERO)*S.get((1,1),ZERO)-S.get((0,1),ZERO)*S.get((1,0),ZERO)
        assert trace(S)==A(2) and det==A(F(2,3))
        Si=invert(S,2);assert Si==scaled(A(F(3,2)),sub(scaled(A(2),I),S))
        D=product(Si,adj(E));P=product(E,D);H=product(adj(D),D)
        local={}
        for t,f in enumerate(p):
            Pf=block(K,2*f,2);local.update({(2*t+i,2*t+j):x for (i,j),x in Pf.items()})
        assert P==local and product(D,E)==I and product(adj(E),product(H,E))==I
        assert S!=I and S!=scaled(A(2),I)
        Q=plus(I4,{(0,1):A(F(2,3)),(1,2):A(F(len(charts)+1,5)),(2,3):ONE});Qi=invert(Q,4)
        charts.append({'pair':p,'R':R,'E':E,'S':S,'D':D,'P':P,'H':H,'Q':Q,'Qi':Qi})
    T={(q,p):product(charts[q]['E'],charts[p]['D']) for p,q in pairs(range(6),repeat=2)}
    changed={(q,p):product(charts[q]['Q'],product(t,charts[p]['Qi'])) for (q,p),t in T.items()}
    for p,q in pairs(range(6),repeat=2):
        c,b=charts[p],charts[q];t=T[q,p]
        assert product(adj(t),product(b['H'],t))==c['H']
        if p!=q:assert product(adj(c['E']),product(adj(t),product(t,c['E'])))!=c['S']
        Hq=product(adj(b['Qi']),product(b['H'],b['Qi']));Hp=product(adj(c['Qi']),product(c['H'],c['Qi']))
        assert product(adj(changed[q,p]),product(Hq,changed[q,p]))==Hp
    for p,q,r in pairs(range(6),repeat=3):
        assert product(T[r,q],T[q,p])==T[r,p]
        assert product(changed[r,q],changed[q,p])==changed[r,p]
    pairactions=[];native=[]
    for u,perm in zip(reps['logical'],reps['permutations']):
        targets=[];blocks=[]
        for p,c in enumerate(charts):
            target=tuple(sorted(perm[f] for f in c['pair']));q=pairlist.index(target);b=charts[q]
            B={(2*target.index(perm[f])+i,2*t+j):x for t,f in enumerate(c['pair']) for (i,j),x in u.items()}
            assert product(B,c['E'])==product(b['E'],u)
            assert product(b['D'],B)==product(u,c['D'])
            assert product(adj(B),product(b['H'],B))==c['H']
            assert product(B,c['P'])==product(b['E'],product(u,c['D']))
            Bnew=product(b['Q'],product(B,c['Qi']))
            assert product(Bnew,product(c['Q'],c['E']))==product(b['Q'],product(b['E'],u))
            targets.append(q);blocks.append(B)
        pairactions.append(tuple(targets));native.append(blocks)
    lookup={key(u):i for i,u in enumerate(reps['logical'])}
    for a,b in pairs(range(24),repeat=2):
        c=lookup[key(product(reps['logical'][a],reps['logical'][b]))]
        assert pairactions[c]==tuple(pairactions[a][pairactions[b][p]] for p in range(6))
        assert reps['permutations'][c]==[reps['permutations'][a][reps['permutations'][b][f]] for f in range(4)]
    minus=next(i for i,u in enumerate(reps['logical']) if u==scaled(-ONE,I))
    assert pairactions[minus]==tuple(range(6)) and all(B==scaled(-ONE,I4) for B in native[minus])
    average=scaled(A(F(1,6)),plus(*(product(c['D'],c['R']) for c in charts)))
    assert average==Dglobal and product(K,average)==o['ops']['G']==o['ops']['N']
    hom_result,_=hom([product(o['f']['L']['D'],product(W,o['f']['L']['K'])) for W in reps['raw']],reps['logical'],4,2)
    assert hom_result['dimension']==1
    witnesses=[]
    for c in charts:
        omitted=next(f for f in range(4) if f not in c['pair']);Pf=block(K,2*omitted,2);v=column(Pf)
        raw={(2*omitted+i,0):x for (i,j),x in v.items()}
        assert product(o['ops']['L'],raw)==raw and not product(c['R'],raw)
        assert product(Dglobal,raw) and product(o['ops']['G'],raw)
        pairdecoder=product(c['D'],c['R'])
        assert rank(product(sub(pairdecoder,Dglobal),o['f']['L']['K']),2,4)==2
        witnesses.append({'pair':list(c['pair']),'omitted_face':omitted,'input':encode(raw),'native_global_decoded':encode(product(Dglobal,raw))})
    # Face density fixes an order3 rotation, but its edge-pair action fixes no chart.
    Pf=block(K,0,2)
    stabilizer=next(i for i,(u,perm) in enumerate(zip(reps['logical'],reps['permutations'])) if perm[0]==0 and perm!=list(range(4)))
    u=reps['logical'][stabilizer]
    assert product(u,product(Pf,adj(u)))==Pf and all(pairactions[stabilizer][p]!=p for p in range(6))
    return {'charts':[{'faces':list(c['pair']),'shared_geometric_edge':sorted(set(geometry['base']['faces'][c['pair'][0]])&set(geometry['base']['faces'][c['pair'][1]])),
        'encoder':encode(c['E']),'decoder':encode(c['D']),'Gram':encode(c['S']),'transported_metric':encode(c['H'])} for c in charts],
        'coordinate_cocycles_checked':216,'nonmonomial_gauge_cocycles_checked':216,'native_chart_action_squares':144,
        'native_group_multiplication_and_base_action_checks':576,'central_minus_retained_at_every_chart':True,
        'pair_Gram_trace':'2','pair_Gram_determinant':'2/3','raw_Euclidean_chart_transitions_are_isometries':False,
        'uniform_six_pair_decoder_average_equals_native_decoder_on_all_raw_inputs':True,
        'full_C_to_logical_Hom':hom_result,'equivariant_retraction_unique_at_actual_native_module_scope':True,
        'pair_raw_decoder_full_C_counterexamples':witnesses,'pair_chart_is_full_native_C_preparation_equivalence':False,
        'density_only_equivariant_edge_selector_obstruction':{'fixed_face':0,'native_operation_index':stabilizer,'no_fixed_pair':True}},charts,pairactions,native


def permutation_group(gens,n):
    unit=tuple(range(n));seen={unit};todo=[unit]
    while todo:
        a=todo.pop()
        for g in gens:
            b=tuple(g[a[i]] for i in range(n))
            if b not in seen:seen.add(b);todo.append(b)
    return sorted(seen)


def base_policy_and_native_lifts(geometries,reps,pairactions,native,charts):
    rows={}
    for name in ('proton','neutron'):
        g=geometries[name];base=g['base'];lookup={point_key(p):k for k,p in g['points'].items()};gens=[]
        for R in reps[name]['V']:
            rename={k:lookup[point_key(tuple(product(R,vec(p)).get((i,0),ZERO) for i in range(3)))] for k,p in g['points'].items()}
            T=chain_action(base['faces'],rename)
            assert all(x==ONE for x in T.values())
            gens.append(tuple(next(i for i,j in T if j==f) for f in range(len(base['faces']))))
        group=permutation_group(gens,len(base['faces']));remaining=set(range(len(base['faces'])));orbits=[]
        while remaining:
            p=min(remaining);orbit={g[p] for g in group};orbits.append(sorted(orbit));remaining-=orbit
        assert all(len(orbit)==len(group) for orbit in orbits)
        count=len(group)**len(orbits)*factorial(len(orbits))
        rows[name]={'native_geometric_group_order':len(group),'primitive_faithful_chart_orbits':orbits,
                    'equivariant_bijective_base_successor_count':count,'source_selected_successor':False}
    assert rows['proton']['equivariant_bijective_base_successor_count']==12
    assert rows['neutron']['equivariant_bijective_base_successor_count']==524880
    complement=tuple(next(q for q,c in enumerate(charts) if set(c['pair']).isdisjoint(charts[p]['pair'])) for p in range(6))
    stabilizer=[i for i,g in enumerate(pairactions) if g[0]==0]
    fixed=[p for p in range(6) if all(pairactions[i][p]==p for i in stabilizer)]
    assert fixed==sorted([0,complement[0]]) and len(stabilizer)==4
    assert all(complement[complement[p]]==p for p in range(6))
    assert all(g[complement[p]]==complement[g[p]] for g in pairactions for p in range(6))
    I=identity(2);candidate=[i for i,g in enumerate(pairactions) if g[0]==complement[0]]
    assert len(candidate)==4
    h=next(i for i in stabilizer if product(reps['electron']['logical'][i],reps['electron']['logical'][i])==scaled(-ONE,I))
    assert product(native[h][0],native[h][0])==scaled(-ONE,identity(4))
    assert all(product(reps['electron']['logical'][h],product(reps['electron']['logical'][i],adj(reps['electron']['logical'][h])))==scaled(-ONE,reps['electron']['logical'][i]) for i in candidate)
    assert not [i for i in candidate if all(product(reps['electron']['logical'][i],reps['electron']['logical'][j])==product(reps['electron']['logical'][j],reps['electron']['logical'][i]) for j in stabilizer)]
    for p,c in enumerate(charts):
        q=complement[p];T=product(charts[q]['E'],c['D']);back=product(c['E'],charts[q]['D'])
        assert product(back,T)==c['P'] and product(charts[q]['D'],product(T,c['E']))==I
    rows['electron']={'native_geometric_group_order':12,'native_spin_group_order':24,
       'equivariant_base_endomorphisms':[list(range(6)),list(complement)],
       'unique_nonidentity_base_policy_is_complement':True,'native_commands_select_nonidentity_policy':False,
       'complement_coordinate_return_order':2,'stabilizer_native_spin_order':4,
       'chart0_native_stabilizer_indices':stabilizer,'native_complement_move_indices':candidate,
       'native_stabilizer_conjugates_every_complement_move_to_its_negative':True,
       'conjugation_equivariant_native_spin_lift_of_complement_exists':False,
       'coordinate_complement_is_given_primitive_command':False}
    return rows


def main():
    contract=read(CONTRACT);prior=read(PRIOR)
    assert prior['status']=='pass' and all(prior['checks'].values())
    assert all(digest(ROOT/p)==h for p,h in prior['source_sha256'].items())
    objects,binding,pins=load();reps=representations(objects,binding)
    geometries,placements=native_geometries(objects)
    data=independent_encoders(objects,geometries,placements)
    glue=metric_gluing(objects,geometries,data,prior)
    atlas,charts,pairactions,native=electron_atlas(objects['electron'],reps['electron'],geometries['electron'])
    policies=base_policy_and_native_lifts(geometries,reps,pairactions,native,charts)
    phase={}
    for name,o in objects.items():
        source=digest_source(o);a=History(source,0);b=History(source,2)
        assert a!=b and replay(a,source)[0]!=replay(b,source)[0]
        phase[name]={'same_all_active_chart_values_in_distinct_marked_phases':True,
                     'indistinguishable_phases':[0,2],'different_enabled_primitive_commands':['L','N'],
                     'all_chart_values_are_still_insufficient_for_phase_origin':True}
    checks={k:True for k in (
       'fresh_prior_source_pins',
       'independent_supplied_mode_frame_normal_encoders_not_derived_from_N',
       'one_metric_weighted_minimal_cover_gluing_recovers_all_native_returns_on_all_raw_inputs',
       'proton_uniform_singleton_gluing_matches_native_return',
       'neutron_uniform_singleton_gluing_fails_with_exact_retained_residual',
       'electron_six_actual_face_pair_edge_charts_are_faithful',
       'pair_Grams_trace_two_determinant_two_thirds_and_explicit_inverse',
       'transported_logical_metric_not_silent_raw_port_isometry',
       'all216_chart_coordinate_cocycles',
       'all216_nonmonomial_gauge_coordinate_cocycles',
       'all144_native_chart_action_reader_metric_squares',
       'all576_native_group_word_and_chart_base_compositions',
       'actual_central_minus_retained_not_erased_by_geometric_chart_marks',
       'uniform_six_pair_decoder_average_is_native_global_decoder_on_all_raw_inputs',
       'full_native_C_to_doublet_Hom_dimension_one_with_left_inverse_normalization',
       'all_six_pair_decoders_have_full_C_preparation_counterexamples',
       'phase_blind_density_edge_selector_obstructed_by_actual_face_stabilizer',
       'baryon_source_equivariant_chart_successor_counts_twelve_and_524880',
       'electron_only_equivariant_chart_base_maps_identity_and_complement',
       'opposite_edge_code_coordinate_involution_is_exact_but_not_source_selected',
       'native_order_four_stabilizer_keeps_spin_sign_on_fixed_chart',
       'every_native_complement_move_sign_flipped_by_chart_stabilizer',
       'no_conjugation_equivariant_native_spin_lift_of_complement',
       'all_source_stage_actions_fix_active_chart_values',
       'same_chart_packet_different_primitive_marked_phase_and_enabled_command')}
    pins.update(prior['source_sha256'])
    for p in (PRIOR,CONTRACT,Path(__file__).resolve()):pins[p.relative_to(ROOT).as_posix()]=digest(p)
    for module in tuple(sys.modules.values()):
        path=getattr(module,'__file__',None)
        if path:
            p=Path(path).resolve()
            if p.suffix=='.py' and p.is_relative_to(ROOT/'research'):
                rel=p.relative_to(ROOT).as_posix();assert rel not in pins or pins[rel]==digest(p);pins[rel]=digest(p)
    assert all(digest(ROOT/p)==h for p,h in pins.items())
    report={'schema':'marici.packet-handoff-naturality-iteration-check.v1','iteration':6,'status':'pass','checks':checks,
       'metric_minimal_cover_gluing':glue,'electron_native_edge_chart_atlas':atlas,
       'source_equivariant_chart_successors_and_native_lift':policies,'chart_reader_phase_obstruction':phase,
       'common_metric_minimal_cover_gluing_reconstructs_native_N':True,
       'electron_native_G_from_uniform_six_pair_reconstruction':True,
       'electron_natural_nonidentity_chart_base_involution_constructed':True,
       'opposite_edge_chart_involution_selected_by_native_stage_commands':False,
       'opposite_edge_chart_involution_is_natively_lifted_without_new_sign_choice':False,
       'pair_chart_is_full_native_C_preparation_equivalence':False,
       'active_chart_atlas_selects_primitive_phase_origin':False,
       'source_native_handoff_constructed':False,'physical_particle_assignment_verified':False,
       'native_producers_executed':False,'formal_proof_recompiled':False,
       'next_executable_scope':contract['next_executable_scope'],'source_sha256':pins}
    OUT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','iteration':6,'check_groups':len(checks),'electron_charts':6,
      'native_chart_squares':144,'unique_nonidentity_base_policy':'opposite_edge',
      'source_selected_native_handoff':False},indent=2))


if __name__=='__main__':main()
